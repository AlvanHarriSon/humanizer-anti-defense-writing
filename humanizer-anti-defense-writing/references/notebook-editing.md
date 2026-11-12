# Editing Jupyter notebook prose

Use for `.ipynb` files. This workflow edits narrative without changing the experiment.

## Scope and preparation

Read relevant Markdown cells, nearby code, and displayed outputs to understand what each claim refers to. Do not execute the notebook merely to polish its prose. If outputs and narrative disagree, identify the inconsistency; do not change numbers or rerun analysis without a separate request.

Keep the original recoverable through version control or an exact backup outside the publication set. Record the input notebook path. Work on the requested notebook, not every notebook in its directory.

## Allowed changes

Edit prose in Markdown cell `source` fields. Preserve cell order, IDs, number, metadata, attachments, headings and section hierarchy, table shape, image references, formulas, fenced code blocks, inline code, paths, URLs, citations, technical labels, and requested spacing. Reflow paragraph text only as allowed by the user's layout requirements. Keep `source` represented as a string or list as originally stored.

Code cells, raw cells, outputs, execution counts, kernelspec, language metadata, and top-level fields stay identical as parsed JSON. Code comments and docstrings are executable-cell content: edit them only when explicitly requested, then use a review specific to that expanded scope. The default guard deliberately rejects such changes.

Avoid “clear all outputs”, notebook execution, format upgrades, automatic cell IDs, or saving through tooling that silently rewrites metadata. Serialize carefully with UTF-8 and preserve the original formatting where practical. Parsed equality does not guarantee identical JSON whitespace or identical visual layout.

## Deterministic guard

After writing the edited copy, run the bundled standard-library checker against the original:

```text
python scripts/check_notebook_prose.py original.ipynb edited.ipynb
```

Resolve the script path relative to the installed skill folder. It reads both files and never writes to them. It checks:

- notebook-level fields, cell count, and per-cell non-prose fields;
- exact parsed equality for code/raw cells, including outputs;
- unchanged Markdown source representation type;
- the ordered Markdown spans for common fenced code, inline code, LaTeX math, and link targets.

The span check covers common Markdown/LaTeX syntax, not every extension. Review uncommon syntax, references, HTML, citations, numeric claims, and table/layout preservation separately. A passing structural check does not establish semantic or statistical correctness.

Run a source-versus-rewrite claim check, especially for negation, data provenance, interval coverage, subgroup trade-offs, and selection optimism. Inspect rendered Markdown when a renderer is available and format preservation was requested. State any visual check that could not be performed.

## Delivery

Summarize the narrative changes and checks actually performed. Keep backups out of a GitHub upload unless the user asked to publish them. Upload only the skill's synthetic examples and test fixtures when distributing this skill.
