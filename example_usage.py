"""Example usage for AST Diff Semantic PR Summarizer."""
from client import AstDiffSemanticPrSummarizer

if __name__ == "__main__":
    diff = """
--- a/core.py
+++ b/core.py
-def execute(query, timeout=5):
+def execute(query, timeout=10, retries=3):
+def health_check():
"""
    res = AstDiffSemanticPrSummarizer.summarize_diff(diff)
    print("Semantic PR Summary:", res)
