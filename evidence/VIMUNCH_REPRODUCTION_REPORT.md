# ViMUNCH reproduction and portfolio review

## Scope and ownership boundary

The public repository and thesis are team artifacts and do not contain a formal per-author task-assignment table. The repository was uploaded in one bulk commit, so Git history cannot attribute individual notebook cells or figures reliably.

For portfolio purposes, the safe individual scope is therefore limited to the data work already documented for Nguyen Phi Long: collection/preprocessing, benchmark curation/validation, EDA/rule-based QA, and train/dev/test split validation. The final seven-LLM experiment implementation is treated as teammate-owned and is not claimed as individual implementation.

## Repository inventory and run status

| Artifact | Status | Finding |
|---|---|---|
| `ViMUNCH.json` | Reproduced | Full EDA/QA was rerun from the final 8,501-row JSON. |
| `crawl_data.ipynb` | Not end-to-end reproducible | Depends on Selenium/browser state and Google Drive paths; raw crawled documents are not included. Saved outputs report 27,177 source documents and 628,170 preprocessed candidate sentences. |
| `preprocessed_streamlit.py` | Static check only | Python source is readable, but the repository has no environment lock/requirements. The uploaded file does not contain the poem/prose-specific heuristic described in the thesis, so the thesis preprocessing pipeline cannot be reproduced from this file alone. |
| `AnnotationTool_SourceCode.zip` | Syntax compile passed; runtime not reproduced | Python files compile, but `manage.py check` fails in a clean environment because dependencies are not provided; the app also expects a local MySQL database. |
| `metaphor-identification-classification-llms (1).ipynb` | Prototype only; not final experiment pipeline | Saved execution is interrupted after a small number of samples and relies on gated remote models / Colab-Kaggle paths. It does not contain the final seven-model experiment pipeline used for thesis tables. |
| Thesis Chapter 4 model results | Not reproducible from uploaded code | Final prediction files / evaluation pipeline for all seven LLMs are not present in the repository package. |

## Final dataset audit

- Rows: **8,501**
- Fields: **24** in the final JSON (the thesis describes 23 analysis fields before the final `split` field is added)
- IDs: unique, contiguous `0..8500`
- Exact duplicate rows: **0**
- Duplicate sentence strings: **1**
- Metaphor-positive: **3,182 (37.43%)**
- Non-metaphor: **5,319 (62.57%)**
- Saved split: **5,950 train / 850 dev / 1,701 test**
- Metaphor prevalence by split: **37.43% / 37.41% / 37.45%**

### Internal consistency checks

- `sentence_len` equals Python character length for **100%** of rows.
- `num_metaphor_types` and `num_metaphor_phrases` match the stored list lengths for **100%** of rows.
- `has_interpretation` and `has_scores` match field presence for **100%** of rows.
- Flattened score columns match the nested `scores` object for **100%** of scored rows.
- All **3,765** stored metaphor spans match `sentence[start:end]` exactly using an end-exclusive convention.
- `score_overall` exactly matches its weighted formula; `score_quality` matches its weighted formula after stored rounding.

### Missingness: expected vs reviewable

Most missing interpretation/type/score values are structurally expected because non-metaphor rows do not require those fields. Among 3,182 metaphor-positive rows:

- **50** have no stored metaphor phrase/span.
- **17** have no metaphor type.
- **28** have no interpretation.
- **28** have no scores.

These are review flags, not automatic deletion candidates. Whole-sentence metaphors can legitimately be represented without a local phrase span.

## Reproduced EDA

### Target balance

- Non-metaphor: **5,319 (62.6%)**
- Metaphor: **3,182 (37.4%)**

This reproduces the class distribution reported in Chapter 3.

### Sentence length vs target

`sentence_len` is character count. The share of rows containing metaphors rises across length bands:

| Character length | Metaphor rate |
|---|---:|
| 0–30 | 19.4% |
| 31–60 | 35.3% |
| 61–100 | 39.7% |
| 101–200 | 49.2% |
| >200 | 68.3% |

This is an association, not a causal result. It is relevant to split validation because length drift could become a shortcut/confound.

### Multi-label type distribution

Label assignments:

- Emotional: **1,730**
- Ontological: **1,558**
- Structural: **932**
- Cultural / folklore: **381**
- Orientational: **288**
- Other: **23**

Because rows can have multiple labels, these counts sum to more than the number of metaphor-positive rows.

A notable data-contract issue is that the task specification describes five named metaphor types, while the final JSON contains **23 `other` assignments**. This should be explicitly mapped or excluded by a documented rule before model evaluation.

### Rule-based QA flags

The thesis anomaly table can be reproduced from the final JSON:

- Metaphor-positive but no phrase/span: **50**
- Sentence length >80 words: **37**
- Very low evaluation score (`score_overall < 1.5` or `score_quality < 1.5`): **14**

The reproduction also found **1 exact duplicate sentence string**.

### Score relationships

The thesis correlation heatmap is reproducible from scored rows. Key Pearson correlations:

- Accuracy vs Clarity: **0.20**
- Accuracy vs Quality: **0.98**
- Accuracy vs Overall: **0.87**
- Overall vs Quality: **0.89**

This is useful as supporting project analysis, but it is not selected as a primary portfolio chart because the QA and split visuals communicate stronger Data Analyst evidence faster.

### Exact span lexical diversity

Among **3,724** unique normalized exact metaphor spans:

- **3,687 (99.0%)** appear only once.
- **33** appear twice.
- **4** appear three times.

This suggests high surface-form diversity and is useful as project-only evidence; it is not required in the main portfolio story.

## Existing thesis EDA and reproduction status

| Existing analysis | Reproduction status | Portfolio decision |
|---|---|---|
| Metaphor vs non-metaphor distribution | Reproduced | Supporting / folded into split chart |
| Sentence-length distribution by target | Reproduced | Replace with more decision-oriented metaphor-rate-by-length chart |
| Metaphor-type distribution | Reproduced | Keep, redesigned |
| Poetry vs prose distribution | Not reproducible from final JSON | Do not claim / do not publish as individual evidence |
| Metaphor rate by genre | Not reproducible from final JSON | Do not claim / do not publish as individual evidence |
| Top metaphor phrases | Reproducible, but exact phrase recurrence is extremely sparse | Project-only |
| Interpretation-score correlation | Reproduced | Project-only |
| QA anomaly table | Reproduced | Keep, redesigned as QA chart |
| Train/dev/test target balance | Reproduced | Keep |
| Train/dev/test length distribution | Reproduced | Supporting evidence |
| Train/dev/test type distribution | Reproduced | Supporting evidence |

## Important discrepancies / code-quality issues

1. **Final model experiment code is missing.** The public LLM notebook is an early prototype and cannot reproduce Chapter 4 tables.
2. **Credential exposure:** the public notebook/settings include hardcoded credentials. Rotate/revoke exposed credentials and replace them with environment variables before further public sharing.
3. **Task taxonomy mismatch:** final data contains 23 `other` type assignments although the task definition and prototype prompt describe five types.
4. **Preprocessing implementation mismatch:** the thesis describes poem/prose-aware sentence segmentation, but the uploaded Streamlit preprocessing file contains a simpler punctuation-based splitter; the exact thesis preprocessing version is not present.
5. **Thesis count inconsistency:** Chapter 3 and the final JSON use 8,501 rows, while the conclusion text refers to 8,500.
6. **Task 3 narrative/table mismatch:** the thesis discussion cites fine-tuned ROUGE-L/chrF values that do not match the values in the preceding result table. These model metrics should not be surfaced in the individual portfolio.

## Portfolio chart selection

Primary portfolio charts:

1. `vimunch_metaphor_rate_by_length.png`
2. `vimunch_metaphor_type_distribution.png`
3. `vimunch_data_quality_flags.png`
4. `vimunch_split_validation.png`

Project-only supporting charts:

- `vimunch_span_recurrence_project_only.png`
- `vimunch_score_correlation_project_only.png`

The selected story is:

**Problem / Context → My Data Role → Target Relationship → Label Imbalance → QA Review → Split Validation → Evaluation Implications → Team Modeling Boundary**
