#!/usr/bin/env python3
"""Read-only guard for prose edits to Jupyter notebooks (standard library only)."""

import argparse
import json
from pathlib import Path
import re
import sys

# Common Markdown/LaTeX forms. This is a preservation check, not a full parser.
_PROTECTED = re.compile(
    r"(?P<fence>^[ \t]{0,3}(?P<marker>`{3,}|~{3,})[^\n]*\n.*?"
    r"^[ \t]{0,3}(?P=marker)[ \t]*(?:\n|$))"
    r"|(?P<code>(?P<ticks>`+)(?!`).*?(?<!`)(?P=ticks)(?!`))"
    r"|(?P<display>\$\$.*?\$\$)"
    r"|(?P<latex>\\\(.*?\\\)|\\\[.*?\\\])"
    r"|(?P<math>(?<!\\)\$(?!\$)(?=\S)(?:\\.|[^$\\\n])*?"
    r"(?<=\S)(?<!\\)\$(?!\$))"
    r"|(?P<link>!?\[[^\]\n]*\]\((?P<target>[^)\n]*)\))"
    r"|(?P<reference>^[ \t]{0,3}\[[^\]\n]+\]:[^\n]*)"
    r"|(?P<url>https?://[^\s<>\]\)]+)",
    re.MULTILINE | re.DOTALL,
)


def protected_spans(source):
    """Return ordered technical spans; allow prose in link labels to change."""
    if isinstance(source, list):
        if not all(isinstance(line, str) for line in source):
            raise ValueError("Markdown source list must contain strings")
        source = "".join(source)
    if not isinstance(source, str):
        raise ValueError("Markdown source must be a string or list of strings")
    spans = []
    for match in _PROTECTED.finditer(source):
        if match.group("link") is not None:
            spans.append(("target", match.group("target")))
        else:
            spans.append((match.lastgroup, match.group(0)))
    return spans


def compare_notebooks(before, after):
    """Return violations. Only Markdown source text may differ."""
    if not isinstance(before, dict) or not isinstance(after, dict):
        return ["Notebook root must be an object"]
    issues = []
    if {k: v for k, v in before.items() if k != "cells"} != {
        k: v for k, v in after.items() if k != "cells"
    }:
        issues.append("Notebook-level fields changed")
    old_cells, new_cells = before.get("cells"), after.get("cells")
    if not isinstance(old_cells, list) or not isinstance(new_cells, list):
        return issues + ["Notebook cells must be lists"]
    if len(old_cells) != len(new_cells):
        return issues + ["Cell count changed"]
    for index, (old, new) in enumerate(zip(old_cells, new_cells)):
        prefix = f"Cell {index}"
        if not isinstance(old, dict) or not isinstance(new, dict):
            issues.append(f"{prefix}: cell must be an object")
            continue
        if old.get("cell_type") != "markdown":
            if old != new:
                issues.append(f"{prefix}: code/raw cell or cell order changed")
            continue
        if {k: v for k, v in old.items() if k != "source"} != {
            k: v for k, v in new.items() if k != "source"
        }:
            issues.append(f"{prefix}: non-prose fields changed")
        if type(old.get("source")) is not type(new.get("source")):
            issues.append(f"{prefix}: Markdown source representation changed")
            continue
        try:
            if protected_spans(old.get("source")) != protected_spans(new.get("source")):
                issues.append(f"{prefix}: protected Markdown spans changed")
        except ValueError as error:
            issues.append(f"{prefix}: {error}")
    return issues


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("original", type=Path)
    parser.add_argument("edited", type=Path)
    args = parser.parse_args(argv)
    try:
        before = json.loads(args.original.read_text(encoding="utf-8-sig"))
        after = json.loads(args.edited.read_text(encoding="utf-8-sig"))
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    issues = compare_notebooks(before, after)
    if issues:
        for issue in issues:
            print(f"FAIL: {issue}")
        return 1
    print("PASS: only Markdown prose changed; checked technical spans are intact.")
    print("Semantic, statistical, uncommon-syntax, and visual review remain separate.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
