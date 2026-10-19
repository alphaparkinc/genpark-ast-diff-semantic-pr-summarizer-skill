"""MCP Server wrapper for AST Diff Semantic PR Summarizer."""
import json
import sys
from client import AstDiffSemanticPrSummarizer

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [
                {
                    "name": "summarize_ast_diff",
                    "description": "Analyze unified git diff for AST structural changes and breaking signature alterations",
                    "inputSchema": {
                        "type": "object",
                        "properties": {"unified_diff": {"type": "string"}},
                        "required": ["unified_diff"]
                    }
                }
            ]
        }
    elif method == "tools/call":
        args = req.get("params", {}).get("arguments", {})
        res = AstDiffSemanticPrSummarizer.summarize_diff(args.get("unified_diff", ""))
        return {
            "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
        }
    return {}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            try:
                r = json.loads(line)
                out = handle_request(r)
                print(json.dumps(out), flush=True)
            except Exception as e:
                print(json.dumps({"error": str(e)}), flush=True)
