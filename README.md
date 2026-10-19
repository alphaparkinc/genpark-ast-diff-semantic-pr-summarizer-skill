# genpark-ast-diff-semantic-pr-summarizer-skill

[![Verified by Smithery](https://smithery.ai/badge/@alphaparkinc/genpark-ast-diff-semantic-pr-summarizer-skill)](https://smithery.ai/servers/@alphaparkinc/genpark-ast-diff-semantic-pr-summarizer-skill)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![Website](https://img.shields.io/badge/Website-GenPark.ai-green)](https://www.genpark.ai)

> Synthesize semantic AST delta trees across git diffs, classify breaking signature changes, and output structured PR summaries

## Quick Installation & MCP Integration
Add to your Claude Desktop or Cursor configuration:
```json
{
  "mcpServers": {
    "genpark-ast-diff-semantic-pr-summarizer-skill": {
      "command": "python",
      "args": ["mcp_server.py"]
    }
  }
}
```

## Zero Dependencies
Implemented entirely in Python 3 standard library.
