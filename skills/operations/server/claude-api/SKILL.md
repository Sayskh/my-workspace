---
name: server-claude-api
description: Anthropic Claude API integration, tool use definitions, and system prompts.
metadata:
  hermes:
    tags: [server, api, claude, anthropic, llm]
    category: server
---

# Claude API

Anthropic Claude API client patterns, tool use schemas, and configurations.

## Available Models
- `claude-3-7-sonnet-latest` / `claude-sonnet-4-6`: Primary balanced reasoning model
- `claude-3-5-haiku-latest` / `claude-haiku-4-5`: Fast and cost-efficient
- `claude-opus-4-6`: Maximum capability for complex reasoning tasks

## Basic Request
```python
import anthropic
import os

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
response = client.messages.create(
    model="claude-3-7-sonnet-latest",
    max_tokens=8096,
    system="System instructions here...",
    messages=[{"role": "user", "content": "User prompt here..."}]
)
```

## Tool Use Definition
```python
tools = [{
    "name": "execute_command",
    "description": "Execute a shell command on the host",
    "input_schema": {
        "type": "object",
        "properties": {
            "command": {"type": "string", "description": "Shell command to run"}
        },
        "required": ["command"]
    }
}]
```

## Defer Loading
- `defer_loading: false`: Tool is always loaded in the context window.
- `defer_loading: true`: Tool loaded on-demand via search tool (reduces token usage).

## Stop Reasons
- `end_turn`: Natural complete response.
- `tool_use`: Model requested tool execution.
- `max_tokens`: Generation exceeded token budget.

## Critical Gotchas
- `examples` inside JSON Schema properties are not permitted (triggers HTTP 400).
- `max_tokens` parameter is mandatory.
- System prompt must be passed as `system`, not inside `messages`.
- `tool_result` must always be sent back as a `user` role message.
