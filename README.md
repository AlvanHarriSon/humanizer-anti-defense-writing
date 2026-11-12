# Humanizer-Anti-Defense Writing

Polish Chinese and English academic reports and Jupyter notebook prose so supported findings are easy to see. Preserve statistical meaning, technical content, and the writer's voice.

用于中英文学术报告与 Jupyter notebook 的写作润色：突出有证据支持的成果与分析价值，精简重复自辩，保留必要的统计说明和作者语气。

## What it does / 功能

- Removes redundant defensive framing, empty emphasis, and mechanical AI prose.
- Preserves evaluation status, selection effects, interval coverage, null findings, and aggregate/subgroup trade-offs.
- Keeps report structure and notebook code, outputs, metadata, formulas, citations, and links intact.
- Uses bilingual examples, including cases where cautious language must remain.

The skill is self-contained. It does not require the original humanizer skill or any third-party Python package. The notebook guard uses Python's standard library and reads files without modifying them.

## Install / 安装

Copy the complete `humanizer-anti-defense-writing` folder into your agent's skills directory. For Codex, current project skills live in `.agents/skills/`; user skills live in `~/.agents/skills/`. See [official OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills). Installation is separate from keeping this source repository on disk.

将完整的 `humanizer-anti-defense-writing` 目录复制到技能目录。项目级 Codex 安装后的结构为：

```text
.agents/skills/humanizer-anti-defense-writing/SKILL.md
```

This repository creates source files only; it does not alter your agent configuration.

## Use / 使用

```text
Use $humanizer-anti-defense-writing to polish the results and discussion below.
Lead with supported findings and retain essential statistical qualifications.
```

```text
使用 $humanizer-anti-defense-writing 润色这份报告和 Q2.ipynb 的 Markdown 正文。
突出实验发现与方法取舍，保留统计边界、公式、代码、输出、引用和原有结构。
```

Supply an author sample when matching a specific voice. The default output is final prose. Ask for review mode to receive issue locations and concise explanations. Notebook execution or analysis changes require a separate request.

## Example / 示例

All examples and evaluation fixtures are synthetic.

Before:
> We must stress that weighting is not universally better. On the reused diagnostic set, high-region RMSE was $780 for WLS and $1,000 for OLS. Overall RMSE was $1,260 and $1,180, respectively.

After:
> On the reused diagnostic set, WLS reduced high-region RMSE from $1,000 to $780, while overall RMSE rose from $1,180 to $1,260.

中文：
> 在复用诊断集上，WLS 将高价区域的 RMSE 从 1,000 元降至 780 元，整体 RMSE 则从 1,180 元升至 1,260 元。

More examples: [Chinese and English transformations](humanizer-anti-defense-writing/references/examples.md).

## Notebook integrity check / Notebook 完整性检查

From the skill directory:

```text
python scripts/check_notebook_prose.py original.ipynb edited.ipynb
```

The guard checks JSON structure and common protected Markdown spans. It does not assess statistical correctness, all Markdown extensions, or rendered layout. Review claims and formatting separately.

## Validation / 验证

From the repository root:

```text
python -B -m unittest discover -s tests -v
```

See [evals/README.md](evals/README.md) for natural-language evaluation tasks and [VALIDATION.md](VALIDATION.md) for the actual validation record. Deterministic checks and behavioral review address different properties; neither predicts grades.

## Repository contents / 目录

```text
humanizer-anti-defense-writing/
  SKILL.md
  agents/openai.yaml
  references/academic-writing.md
  references/notebook-editing.md
  references/examples.md
  scripts/check_notebook_prose.py
evals/              Synthetic behavioral tasks and review rubric
tests/              Notebook guard regression tests
VALIDATION.md       Checks actually completed
LICENSE
THIRD_PARTY_NOTICES.md
```

## Sources and license / 来源与许可

Adapted from [blader/humanizer](https://github.com/blader/humanizer), locally available version 3.1.0, and the user's requested contribution-focused editorial approach. Upstream notices are preserved in [LICENSE](LICENSE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). No private chat transcript, coursework, or original research notebook is included. MIT licensed.
