# Chinese and English examples

All numeric examples below are synthetic editorial fixtures. They are not research results. Each “after” illustrates a local edit; it is not permission to drop other claims from a larger source.

## 1. English: contribution with an aggregate trade-off

Before:
> It is important to stress that this does not mean weighting is universally better. On the reused diagnostic set, high-region RMSE was $780 for WLS and $1,000 for OLS. Overall RMSE was $1,260 and $1,180, respectively. We should be careful not to claim that every prediction improves.

After:
> On the reused diagnostic set, WLS reduced high-region RMSE from $1,000 to $780, while overall RMSE rose from $1,180 to $1,260. Weighting improved high-region accuracy at a measurable cost to aggregate accuracy.

The original evaluation status and both directions remain explicit. The interpretation names the observed trade-off without adding a deployment cost model.

## 2. 中文：成果、评价范围与代价

修改前：
> 必须强调，这并不意味着加权方法在所有方面都优于基线。在复用诊断集上，WLS 的高价区域 RMSE 为 780 元，OLS 为 1,000 元；整体 RMSE 分别为 1,260 元和 1,180 元。我们不能据此声称每个样本的预测都有改善。

修改后：
> 在复用诊断集上，WLS 将高价区域的 RMSE 从 1,000 元降至 780 元，整体 RMSE 则从 1,180 元升至 1,260 元。加权提高了高价区域的预测精度，同时增加了整体误差。

删除重复自辩，保留数据状态、区域收益和整体代价。

## 3. English: favourable point estimate and an interval containing zero

Before:
> We do not wish to overstate these results. On the reused diagnostic set, baseline F1 was 0.638 and weighted-model F1 was 0.612. Baseline minus weighted F1 was 0.026, with a paired 95% bootstrap interval of [-0.010, 0.061] from 2,000 draws. The bootstrap held fitted models and class counts fixed and omitted retraining and selection variability. Ratios and thresholds were selected using the same training OOF labels used to score them. One should therefore be cautious.

After:
> On the reused diagnostic set, baseline F1 was 0.638 versus 0.612 for the weighted model. The observed difference was 0.026; its paired 95% bootstrap interval of [-0.010, 0.061] includes zero, leaving the direction of the difference unresolved. The 2,000-draw bootstrap conditioned on fitted models and fixed class counts and excluded retraining and selection variability. Ratios and thresholds were selected and scored using the same training OOF labels, so the selected OOF scores are subject to selection optimism.

The revision keeps the uncertainty target and the selection caveat. It does not infer equivalence or established superiority.

## 4. 中文：固定模型区间与选参

修改前：
> 为避免误解，需要说明区间不能涵盖所有不确定性。复用诊断集上的 MAE 差值（A 减 B）为 -120 元，2,000 次区域分层 bootstrap 的 95% 区间为 [-180, -40] 元。重采样固定拟合模型和各区域样本数，未包括重新训练与选参变化。参数由训练 OOF 选择，因此被选择的 OOF 得分存在选择乐观偏差。不能作过于广泛的解释。

修改后：
> 在复用诊断集上，A 的 MAE 比 B 低 120 元。2,000 次区域分层 bootstrap 得到 A 减 B 的 95% 区间为 [-180, -40] 元，支持该诊断集上的误差下降。该区间固定拟合模型和区域样本数，未计入重新训练及选参变动；参数由训练 OOF 选择，被选择的 OOF 得分仍受选择乐观偏差影响。

结论的力度与区间覆盖范围保持一致。

## 5. English: calibration and threshold selection

Before:
> It is not just about F1; the real story is probability quality. Training OOF Brier scores were 0.052 for the baseline and 0.087 for weighting. Threshold selection retained each model's probabilities. No calibration correction was fitted.

After:
> Training OOF Brier scores were 0.052 for the baseline and 0.087 for weighting, favouring the baseline on this probability scoring rule. Threshold selection left each model's probabilities unchanged, and no calibration correction was fitted.

Do not convert the Brier result into proof of calibration or turn threshold tuning into probability recalibration.

## 6. 中文：网格最优与敏感性分析

修改前：
> 本文不是声称比率 4 在任何情况下都最佳。等区域目标在测试网格中选择了比率 4，其 OOF MAE 为 900 元，比率 6 为 904 元。所有截点设置均在同一组 120 个高价 OOF 样本上评价。截点分析只是敏感性检查，不能证明某一截点普遍最好。

修改后：
> 在测试网格内，等区域目标选择比率 4，OOF MAE 为 900 元；比率 6 的结果为 904 元。各截点设置均在同一组 120 个高价 OOF 样本上评价，使敏感性分析能够在固定评价人群下比较不同的训练优先级。该比较支持测试网格内的选择，未确定普遍最优截点。

真实比较和边界应保留；“未确定普遍最优截点”在此仍限制了可能被误读的结论。

## 7. Keep causal uncertainty / 保留因果不确定性

Before: The difference may reflect sample size; the study did not manipulate sample size.

After: The difference may reflect sample size, which was not manipulated in this study.

中文原文：差异可能与样本量有关；研究未操纵样本量。

中文修改：差异可能与样本量有关，本研究未操纵这一因素。

Do not replace “may reflect” with “was caused by”, or “可能有关” with “由……导致”.

## 8. Real criticism and real contrasts / 真实异议与比较

Reviewer: “The thresholds differed, so the weighting comparison is confounded.”

Source: Both models used threshold 0.5. Only the class weights differed.

Response: Both models used threshold 0.5; only the class weights differed.

中文回复：两个模型的阈值均为 0.5，差异仅在类别权重。

Preserve this correction. The objection is actually present, and the comparison carries information.

## 9. Null findings / 零结果

Before: We must acknowledge that the treatment was not significantly different from control (p = 0.41). This does not mean the two are equivalent.

After: The test did not detect a treatment-control difference (p = 0.41); this does not establish equivalence.

中文修改：检验未检测到处理组与对照组的明确差异（p = 0.41），该结果不能证明两组等效。

Do not replace the qualification with “equivalence was not assessed” unless the source establishes that methodological fact.

## 10. Notebook prose with protected technical spans

Before:
> It is important to note that `predict_proba(X)[:, 1]` returns the scores. We used $t=0.5$ for the baseline; the observed recall was 0.82. See [methods](methods.md#thresholds).

After:
> The baseline used scores from `predict_proba(X)[:, 1]` with $t=0.5$ and achieved an observed recall of 0.82. See [methods](methods.md#thresholds).

Keep inline code, formula, value, link target, and notebook structure. Preserve displayed outputs even when a prose rewrite would look neater with them removed.

## 11. Deliberate rhythm and voice / 作者声音

A real list of three distinct mechanisms remains a list of three. A writer sample using dashes, parentheses, or mixed feelings can keep those features. Do not introduce personal opinions into a factual report to make it sound human.

原文：这个结果让我有些犹豫：平均误差下降了，但最难的那组样本没有改善。

修改：这个结果让我有些犹豫：平均误差下降了，但最难的那组样本没有改善。

No change is needed when the sentence is already clear and the reservation carries meaning.
