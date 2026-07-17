# scripts/ Directory

This directory contains Python scripts for data loading, transformation, and analysis.

## Files

| File | Description |
|------|-------------|
| `data_loader.py` | Main data loader and chart generator (generates charts/ directory) |
| `seasonal_analysis.py` | Seasonal trend analysis: win rates by era, division dominance, championship droughts, expansion impact |

## Usage

```bash
pip install -r requirements.txt

# Generate all charts
python scripts/data_loader.py

# Run seasonal trend analysis
python scripts/seasonal_analysis.py

# Or use the Jupyter notebook
jupyter notebook notebooks/explore_nl_data.ipynb
```

## Analysis Scripts

### data_loader.py
- Loads all CSV data files from `data/`
- Generates visualization charts saved to `charts/`
- Charts include: pennant winners by franchise, win% by team, championship droughts, H2H summary, NL West dominance, era trends, division win counts

### seasonal_analysis.py
- **`analyze_era_win_rates()`** — Compare winning percentages across 154G, 162G, and 60G eras
- **`analyze_division_dominance()`** — Which division has the most/least titles
- **`analyze_championship_droughts()`** — Years since last WS title per franchise
- **`analyze_expansion_impact()`** — Expansion teams vs original franchises
- **`analyze_pennant_wins_by_decade()`** — Pennant winners by franchise across history

## Planned Scripts
- `generate_charts.py` — Generate all visualization charts in batch
- `eda_analysis.py` — Interactive exploration analysis
- `era_comparison.py` — Franchise-era performance comparison
- `pythagorean_analysis.py` — Pythagorean expectation analysis
- `h2h_matrix.py` — Generate full 15×15 H2H W-L heatmap

## Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Run the analysis: `python scripts/data_loader.py`
3. Or use the Jupyter notebook: `jupyter notebook notebooks/explore_nl_data.ipynb`
