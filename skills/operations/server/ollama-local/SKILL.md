---
name: server-ollama-local
description: Local LLM execution via Ollama (Qwen, Llama, DeepSeek, Mistral).
metadata:
  hermes:
    tags: [server, ollama, local-llm, ai, qwen]
    category: server
---

# Ollama Local LLM

Integration and API reference for local LLMs running via Ollama.

## Quick CLI Reference
```bash
# List local models
ollama list

# Run interactive model
ollama run qwen2.5-coder:7b

# Pull a new model
ollama pull deepseek-r1:8b

# View running models & VRAM
ollama ps
```

## Basic REST API Request
```bash
curl http://localhost:11434/api/generate \
  -d '{
    "model": "qwen2.5-coder:7b",
    "prompt": "Write a python health check script",
    "stream": false
  }'
```

## Chat API (OpenAI Compatible)
Endpoint: `http://localhost:11434/v1/chat/completions`

```python
import openai

client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

response = client.chat.completions.create(
    model="qwen2.5-coder:7b",
    messages=[{"role": "user", "content": "Hello"}]
)
```

## GPU & Performance Optimization
- Set `OLLAMA_NUM_PARALLEL=2` or higher for concurrent requests.
- Set `OLLAMA_KEEP_ALIVE=24h` to prevent unloading models from VRAM.
- Check GPU utilization with `nvidia-smi` or `rocm-smi`.
