# DA Portfolio 2026 — Updated deployment package

This package is designed to be overlaid on the existing GitHub repository:
`philonguit-blip/DA-portfolio`.

## Replace / add

1. Replace the deployed page with:
   - `index.html`
   - `index-datathon-redesign.html` (same content; kept as a compatibility copy)

2. Add these new DATATHON assets to `assets/`:
   - `datathon_traffic_vs_orders_index.png`
   - `datathon_promotion_aov_comparison.png`
   - `datathon_replenishment_vs_sales.png`
   - `datathon_inventory_risk_by_category.png`

## Keep these existing repository files unchanged

The updated HTML still references the existing APAOMA assets already in your old repo:
- `assets/apaoma_campaign_efficiency.png`
- `assets/apaoma_promo_efficiency.png`
- `assets/apaoma_finance_margin.png`
- `assets/apaoma_inventory_flow.png`

It also references the existing CV:
- `Nguyen-Phi-Long-Data-Analyst-CV-Rebuilt.docx`

Do not delete those files when applying this update.

## What changed in DATATHON

The public project story now follows:
Problem / Context → My Role → EDA → Key Insights → Business Actions → Team Forecast Extension.

Portfolio-ready reproduced results:
- Sessions +62.7% from 2013 to 2022 while orders −53.1%; conversion 1.13% → 0.33%.
- Promoted net AOV 31.5% lower: 18,895 vs 27,565 VND; gross AOV was also lower before discount.
- Monthly receipts vs sales in 2020–2022: r = 0.9999; receipts averaged 14.7% above units sold.
- Outdoor in 2020–2022: 84.3% overstock and 9.43% sell-through.

Ownership is explicit:
- User-owned: business EDA, grain-aware joins, KPI construction, visualization, interpretation, recommendations.
- Teammate-owned: final LightGBM/XGBoost forecasting implementation.
- User contribution to forecasting: review / interpretation of team output.

## Evidence folder

`evidence/` contains the reproduced metrics and technical review notes used to validate the public portfolio claims.
These files do not need to be published with GitHub Pages.

## Quick deployment

If GitHub Pages is configured to serve the repository root:
1. Copy `index.html` to the repository root.
2. Copy the four DATATHON PNGs into `assets/`.
3. Keep the four existing APAOMA PNGs and CV file.
4. Commit and push.


## ViMUNCH update

The latest update expands ViMUNCH from a text-only project card into a reproduced EDA / data-quality case study.

Add / keep these ViMUNCH assets under `assets/`:
- `vimunch_metaphor_rate_by_length.png`
- `vimunch_metaphor_type_distribution.png`
- `vimunch_data_quality_flags.png`
- `vimunch_split_validation.png`

The portfolio now states the ownership boundary explicitly: Nguyen Phi Long's evidence is the data pipeline, curation, EDA, QA and split validation; the final seven-LLM experiment implementation is a teammate contribution.

The updated CV is included as `Nguyen-Phi-Long-Data-Analyst-CV-Rebuilt.docx`.

Supporting reproduction files are under `evidence/` and do not need to be deployed publicly.
