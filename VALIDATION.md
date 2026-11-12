# Validation record

Date: 2026-11-12 (Asia/Shanghai). Skill version: 1.0.0.

## Checks completed

| Check | Actual result |
| --- | --- |
| Bundled skill-creator `quick_validate.py` | Passed: `Skill is valid!` |
| YAML/UI metadata, matching directory/name, prompt invocation, default discovery | Passed |
| Local documentation links and referenced resources | Passed; example-only `methods.md#thresholds` is deliberately illustrative |
| Notebook guard regression suite | 16 tests passed |
| Independent prose generation | 10 of 10 requests completed in a separate agent context |
| Source/output semantic review by the primary agent | All 10 preserve substantive meaning and necessary qualifications |
| Unique numeric-value comparison | Passed for all 10 pairs; repeated mentions can be consolidated, and meaning still requires review |
| Protected Markdown spans | Passed for the inline-code/math/link/fence case |
| Synthetic notebook before/after guard | Passed; only Markdown prose changed |

Deterministic checks ran with Python 3.14.6. The installed skill and guard require no third-party packages. PyYAML 6.0.3 was installed only into an ignored local validation directory for the external skill-creator validator.

The first sandboxed regression run encountered temporary-directory access errors. The same suite passed with access to its temporary files; no test assertion was weakened.

## Behavioral run

The independent evaluator received SKILL.md, relevant academic/notebook references, and raw requests in [cases.json](evals/cases.json). It generated actual final prose in [outputs.json](evals/outputs.json) before reading the review rubric or prior conclusions. The primary agent then compared outputs with sources and rubric.

| Case | Observed behavior |
| --- | --- |
| en_tradeoff | Keeps reused-data status, model comparators, subgroup gain, and aggregate deterioration. |
| zh_interval | Keeps the zero-crossing interval, conditional bootstrap coverage, and OOF selection optimism. |
| en_probability | Keeps Brier values and unchanged probabilities without claiming proven calibration. |
| zh_causality | Preserves causal uncertainty and the equal-threshold comparison. |
| en_reviewer | Answers the real threshold objection using supplied evidence. |
| zh_null | Preserves the null finding; infers neither equivalence nor an unperformed test. |
| en_grid | Keeps tested-grid scope, all MAEs, and the fixed evaluation population. |
| en_protected | Keeps inline code, math, link target, code fence, and recall. |
| zh_voice | Leaves clear personal prose unchanged. |
| en_missing | Uses explicit placeholders for missing MAEs; invents no result. |

These observations on synthetic cases do not establish performance on all future writing or predict grades.

## Reproduce notebook checks

From the repository root:

```text
python -B -m unittest discover -s tests -v
python -B humanizer-anti-defense-writing/scripts/check_notebook_prose.py evals/notebook-before.ipynb evals/notebook-after.ipynb
```

The notebook pair was created and edited during independent forward-testing. It contains Markdown represented as both a list and a string, cell IDs and metadata, inline code and math, a link, fenced code, a code cell with a saved output and execution count, and a raw cell. Contents and saved output are synthetic; notebook cells were not executed.

## Verification scope

No notebook or document rendering was performed. The guard checks common Markdown/LaTeX patterns and parsed JSON integrity, not every Markdown extension, semantic validity, numeric meaning, or pagination. Statistical meaning and prose quality were reviewed against synthetic sources. No real coursework, research artifact, or private chat transcript is included in the distributed evaluation set.
