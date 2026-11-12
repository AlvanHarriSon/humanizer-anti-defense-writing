"""Meaningful mutation tests for notebook preservation boundaries."""

import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "humanizer-anti-defense-writing/scripts/check_notebook_prose.py"
spec = importlib.util.spec_from_file_location("notebook_guard", SCRIPT)
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)


def notebook():
    return {
        "nbformat": 4, "nbformat_minor": 5,
        "metadata": {"kernelspec": {"name": "python3", "display_name": "Python 3"}},
        "cells": [
            {"cell_type": "markdown", "id": "results", "metadata": {"tags": ["results"]},
             "attachments": {"tiny.txt": {"text/plain": "synthetic"}},
             "source": ["## Results\n", "It is important to note that `score(X)` uses $t=0.5$.\n",
                        "See [methods](methods.md#thresholds).\n",
                        "```python\nthreshold = 0.5\n```\n"]},
            {"cell_type": "code", "id": "compute", "metadata": {},
             "execution_count": 1, "source": ["print(0.82)\n"],
             "outputs": [{"output_type": "stream", "name": "stdout", "text": ["0.82\n"]}]},
            {"cell_type": "raw", "id": "raw", "metadata": {}, "source": "raw content"},
        ],
    }


class GuardTests(unittest.TestCase):
    def assert_rejected(self, mutate):
        before = notebook()
        after = copy.deepcopy(before)
        mutate(after)
        self.assertTrue(guard.compare_notebooks(before, after))

    def test_prose_edit_passes(self):
        before = notebook()
        after = copy.deepcopy(before)
        after["cells"][0]["source"][1] = "The baseline uses `score(X)` with $t=0.5$.\n"
        self.assertEqual([], guard.compare_notebooks(before, after))

    def test_code_change_rejected(self):
        self.assert_rejected(lambda n: n["cells"][1].update(source=["print(0.99)\n"]))

    def test_output_change_rejected(self):
        self.assert_rejected(lambda n: n["cells"][1].update(outputs=[]))

    def test_execution_count_change_rejected(self):
        self.assert_rejected(lambda n: n["cells"][1].update(execution_count=None))

    def test_kernel_change_rejected(self):
        self.assert_rejected(lambda n: n["metadata"].update(kernelspec={"name": "other"}))

    def test_cell_metadata_change_rejected(self):
        self.assert_rejected(lambda n: n["cells"][0].update(metadata={}))

    def test_attachment_change_rejected(self):
        self.assert_rejected(lambda n: n["cells"][0].update(attachments={}))

    def test_source_type_change_rejected(self):
        self.assert_rejected(lambda n: n["cells"][0].update(source="".join(n["cells"][0]["source"])))

    def test_cell_deletion_rejected(self):
        self.assert_rejected(lambda n: n["cells"].pop())

    def test_cell_reordering_rejected(self):
        self.assert_rejected(lambda n: n["cells"].reverse())

    def test_raw_edit_rejected(self):
        self.assert_rejected(lambda n: n["cells"][2].update(source="edited"))

    def test_inline_code_math_link_and_fence_changes_rejected(self):
        for old, new in [("score(X)", "score(Y)"), ("$t=0.5$", "$t=0.7$"),
                         ("methods.md#thresholds", "other.md"), ("threshold = 0.5", "threshold = 0.8")]:
            with self.subTest(change=old):
                self.assert_rejected(lambda n: n["cells"][0].update(
                    source=[line.replace(old, new) for line in n["cells"][0]["source"]]))

    def test_common_extended_spans(self):
        before = "$$a+b$$ and \\(x=2\\)\n~~~r\nx <- 1\n~~~\n``a`b``\n[ref]: methods.md\n"
        for old, new in [("a+b", "a-b"), ("x=2", "x=3"), ("x <- 1", "x <- 2"),
                         ("a`b", "a`c"), ("methods.md", "other.md")]:
            with self.subTest(change=old):
                self.assertNotEqual(guard.protected_spans(before), guard.protected_spans(before.replace(old, new)))

    def test_link_label_edit_passes(self):
        self.assertEqual(guard.protected_spans("[old](methods.md)"), guard.protected_spans("[new](methods.md)"))

    def test_cli_pass_and_reject_without_modifying_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            original = Path(temporary) / "original.ipynb"
            edited = Path(temporary) / "edited.ipynb"
            original.write_text(json.dumps(notebook()), encoding="utf-8")
            edited.write_bytes(original.read_bytes())
            original_bytes = original.read_bytes()
            passed = subprocess.run([sys.executable, "-B", str(SCRIPT), str(original), str(edited)], capture_output=True)
            self.assertEqual(0, passed.returncode, passed.stdout)
            bad = notebook()
            bad["cells"][1]["outputs"] = []
            edited.write_text(json.dumps(bad), encoding="utf-8")
            edited_bytes = edited.read_bytes()
            failed = subprocess.run([sys.executable, "-B", str(SCRIPT), str(original), str(edited)], capture_output=True)
            self.assertEqual(1, failed.returncode)
            self.assertEqual(original_bytes, original.read_bytes())
            self.assertEqual(edited_bytes, edited.read_bytes())

    def test_cli_malformed_json_returns_two(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "invalid.ipynb"
            path.write_text("{broken", encoding="utf-8")
            result = subprocess.run([sys.executable, "-B", str(SCRIPT), str(path), str(path)], capture_output=True)
            self.assertEqual(2, result.returncode)


if __name__ == "__main__":
    unittest.main()
