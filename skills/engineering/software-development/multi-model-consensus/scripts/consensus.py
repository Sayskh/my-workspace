#!/usr/bin/env python3
"""Multi-model consensus query runner.

Queries multiple LLMs concurrently via OpenRouter or OpenAI-compatible endpoint
and prints structured responses for consensus synthesis.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any

DEFAULT_MODELS = [
    "anthropic/claude-3.7-sonnet",
    "openai/gpt-4o",
    "deepseek/deepseek-chat",
]


def query_model(
    model: str,
    prompt: str,
    api_key: str,
    base_url: str = "https://openrouter.ai/api/v1",
    timeout: int = 60,
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an expert technical advisor evaluating options. "
                    "Analyze the decision concisely: state your recommendation, "
                    "pros/cons, and primary risks."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.2,
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
            "HTTP-Referer": "https://github.com/NousResearch/hermes-agent",
            "X-Title": "Hermes-Agent-Consensus",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            content = data["choices"][0]["message"]["content"]
            return {"model": model, "content": content, "error": None}
    except Exception as exc:
        return {"model": model, "content": None, "error": str(exc)}


def main() -> int:
    parser = argparse.ArgumentParser(description="Query multiple models concurrently for consensus evaluation.")
    parser.add_argument("prompt", help="The decision prompt or question to evaluate")
    parser.add_argument("--models", nargs="+", default=DEFAULT_MODELS, help="List of model identifiers")
    parser.add_argument("--base-url", default=os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"), help="API base URL")
    parser.add_argument("--timeout", type=int, default=60, help="Per-request timeout in seconds")
    args = parser.parse_args()

    api_key = os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        sys.stderr.write("Error: OPENROUTER_API_KEY or OPENAI_API_KEY environment variable is required.\n")
        return 1

    print(f"Dispatching consensus query across {len(args.models)} models...\n")

    results: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=len(args.models)) as executor:
        futures = {
            executor.submit(query_model, m, args.prompt, api_key, args.base_url, args.timeout): m
            for m in args.models
        }
        for future in as_completed(futures):
            res = future.result()
            results.append(res)

    for item in results:
        print(f"=== Model: {item['model']} ===")
        if item["error"]:
            print(f"Error: {item['error']}\n")
        else:
            print(f"{item['content']}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
