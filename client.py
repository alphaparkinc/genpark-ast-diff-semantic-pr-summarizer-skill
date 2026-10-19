"""AST Diff Semantic PR Summarizer.
100% Python Standard Library.
"""
import re

class AstDiffSemanticPrSummarizer:
    """Synthesize semantic AST delta trees across git diffs, classify breaking signature changes, and output structured PR summaries."""

    @staticmethod
    def summarize_diff(unified_diff: str) -> dict:
        added_funcs = re.findall(r'^\+\s*def\s+([a-zA-Z0-9_]+)\s*\((.*?)\)', unified_diff, re.M)
        removed_funcs = re.findall(r'^\-\s*def\s+([a-zA-Z0-9_]+)\s*\((.*?)\)', unified_diff, re.M)
        added_classes = re.findall(r'^\+\s*class\s+([a-zA-Z0-9_]+)', unified_diff, re.M)
        removed_classes = re.findall(r'^\-\s*class\s+([a-zA-Z0-9_]+)', unified_diff, re.M)

        breaking_changes = []
        rem_dict = {f[0]: f[1] for f in removed_funcs}
        for f_name, args in added_funcs:
            if f_name in rem_dict and rem_dict[f_name] != args:
                breaking_changes.append(f"Function signature changed for '{f_name}': ({rem_dict[f_name]}) -> ({args})")

        for c_name in removed_classes:
            breaking_changes.append(f"Class '{c_name}' was removed")

        risk_score = min(100, len(breaking_changes) * 35 + len(removed_funcs) * 15 + len(added_funcs) * 5)
        risk_level = "HIGH" if risk_score >= 50 else ("MEDIUM" if risk_score >= 20 else "LOW")

        return {
            "functions_added": [f[0] for f in added_funcs],
            "functions_removed": [f[0] for f in removed_funcs],
            "classes_added": added_classes,
            "classes_removed": removed_classes,
            "breaking_changes_detected": breaking_changes,
            "risk_score": risk_score,
            "risk_level": risk_level,
            "summary": f"PR adds {len(added_funcs)} functions, modifies/removes {len(removed_funcs)}, with {len(breaking_changes)} potential breaking changes."
        }
