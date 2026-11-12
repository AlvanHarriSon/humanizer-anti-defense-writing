# Academic reports and statistical writing

Read for reports, papers, abstracts, results, discussion, captions, and statistical claims. Use supplied evidence and preserve the required scholarly register.

## Present the contribution precisely

Identify what the analysis establishes: a measured improvement, a trade-off, a conditional comparison, a stable pattern, a sensitivity result, or an unresolved difference. Start with that finding where it helps the reader. Explain its practical or methodological meaning only as far as the supplied evidence supports.

Replace a sequence of generic negatives with a specific statement of scope and a reasoned interpretation. “Within the tested grid, ratio 4 had the lowest validation MAE” communicates a result and its selection boundary. Do not append “this demonstrates the value of the method” without explaining what the comparison actually informs.

For a mixed result, present both directions close together. If subgroup error falls while overall error rises, describe the prioritisation and measured aggregate cost. A non-significant comparison can still identify the observed difference and remaining uncertainty; it does not establish equality or superiority.

## What to keep and where

| Information | Editorial treatment |
| --- | --- |
| Effect size, metric, unit, denominator, comparator, evaluation population | Keep with the result or in a clearly identified supplied table. |
| Confidence/credible/bootstrap interval and its type | Preserve signs, bounds, level, and method. Keep interpretations consistent with that interval. |
| Out-of-fold (OOF) predictions, training-only tuning, nesting, selection objective | Keep enough to explain how choices were made. Selected OOF scores remain selection-affected when the same labels selected the configuration. |
| Reused diagnostic/test data or earlier inspection | Keep its status in results and summaries where independence would otherwise be implied. |
| Fixed-model, stratified resampling; omitted retraining or selection variability | State the uncertainty target once in methods, with a compact qualifier near the result as needed. Do not call it total pipeline uncertainty. |
| Subgroup gains and overall deterioration | Keep both, with direction and scale. |
| Sensitivity grid, cutoff, and evaluation population | Distinguish changes to training priority from changes to the population being evaluated. |
| Calibration or probability quality | Keep separate from discrimination, threshold choice, and recall/F1. Brier scores alone do not establish calibration. |
| Costs or deployment utility | Discuss only supplied costs and utility models. Accuracy gains alone do not establish economic benefit. |
| Repeated “not universal”, “not guaranteed”, “not definitive” | Consolidate into the specific evidence boundary already supported by the source. |
| Genuine reviewer criticism | Respond to its exact substance and retain required response structure. |

## Compression without distortion

- In an abstract, keep the data status, main effect, material trade-off, and uncertainty that changes the conclusion. Detailed resampling mechanics can remain in the supplied methods section when the abstract does not overstate their coverage.
- In results, couple effect sizes with their relevant qualification. Explain the comparison before interpreting it.
- In discussion, connect supported findings to the research objective. Report an implication as conditional when the evidence is conditional.
- In limitations, group distinct methodological boundaries and explain their consequence. Avoid repeating them in full after every statistic. Moving a caveat must not detach it from a stronger claim.
- In captions, retain sample definition, units, interval type, and panel/model identifiers needed to read the figure independently.

Do not apply a word blacklist. “Significant” may refer to a defined statistical test, “however” may mark a real trade-off, and “may” may encode genuine uncertainty. Edit for function.

## Bilingual precision

Write in the source language unless asked to translate. Preserve the strength of the claim when translating:

| English | Chinese | Meaning to retain |
| --- | --- | --- |
| associated with | 与……相关 | No established causal direction. |
| may reflect | 可能反映 | A plausible interpretation, not an observed mechanism. |
| lowest among tested settings | 在已测试设置中最低 | Restricted comparison set. |
| interval includes zero | 区间包含零 | The interval does not establish a directional effect at that level. |
| reused diagnostic set | 复用诊断集 | No independent confirmation implied. |
| no clear difference was detected | 未检测到明确差异 | Does not establish equivalence. |

Retain reference style, citation keys, table and figure labels, mathematical notation, spelling convention, and field-specific terminology. Resolve terminology consistently without altering variable names or code.
