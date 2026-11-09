---
name: docs-research
description: Focused external documentation and API research. Retrieves official docs, SDK changes, and usage examples while isolating raw web text from the main conversation context.
---

# Docs Research Workflow

Docs Research handles targeted retrieval of official library documentation,
API contracts, migration guides, and dependency references.

## When to Use

- Looking up rapidly changing third-party libraries (e.g. Next.js App Router, LangChain, modern ORMs).
- Verifying exact method signatures, breaking changes, or deprecation notices.
- Finding official code examples for complex configurations (OAuth, database drivers).
- Investigating tricky runtime errors with latest web / issue tracker solutions.

Do not use for:
- Standard language features and stable built-in standard libraries.
- General programming concepts already well understood.

## Core Contract

1. **Context Isolation:** When research is dispatched via subagent (`delegate_task(goal="Research latest X docs...", background=True)`), the subagent reads raw web documents and returns only compressed, structured findings:
   - Specific API signature / configuration block.
   - Exact version constraints.
   - Actionable code snippet.
2. **Authoritative Sources First:** Prioritize official documentation domains and official repository READMEs over unverified blog posts or forums.
3. **Structured Summary:** Return facts and reproducible examples; never dump unformatted HTML or wall-of-text documentation.

## Output Contract

```markdown
### Documentation Research: <Library / Tool>

- **Target Version:** <Version or range>
- **Official Source:** <URL>
- **Key API Contract / Signature:**
  ```typescript/python
  // Verified signature
  ```
- **Gotchas / Breaking Changes:**
  - <Point 1>
- **Minimal Working Example:**
  ```typescript/python
  // Verified example
  ```
```
