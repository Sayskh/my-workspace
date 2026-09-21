---
name: server-grok-api
description: xAI Grok API integration and OpenAI-compatible endpoint usage.
metadata:
  hermes:
    tags: [server, api, grok, xai, llm]
    category: server
---

# Grok API (xAI)

Client configuration and tool calling patterns for xAI Grok models.

## Available Models
- `grok-2-latest`: General reasoning and coding
- `grok-2-vision-latest`: Multimodal image processing
- `grok-beta`: Fast inference

## Basic Request (OpenAI SDK)
```python
import openai
import os

client = openai.OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

response = client.chat.completions.create(
    model="grok-2-latest",
    messages=[
        {"role": "system", "content": "You are a server automation assistant."},
        {"role": "user", "content": "Diagnose server health."}
    ]
)
```
