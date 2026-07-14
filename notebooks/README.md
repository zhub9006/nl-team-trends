# NL Team Trends - Analysis Notebooks

Jupyter notebooks for NL historical performance analysis.

## Purpose

Notebooks in this directory will contain:
1. Data exploration & cleaning
2. Visualization scripts
3. Statistical modeling (regression, Elo, Pythagorean expectation)
4. Era-specific deep dives

## Setup

```bash
pip install jupyter pandas matplotlib numpy seaborn
jupyter notebook
```

## Planned Notebooks

| Notebook | Description |
|----------|-------------|
| 01_explore_all_time_records.ipynb | Explore franchise win-loss patterns |
| 02_pennant_timeline.ipynb | Pennant winners by decade visualization |
| 03_seasonal_trends.ipynb | Year-by-year performance trajectory analysis |
| 04_division_impact.ipynb | Divisional realignment effect analysis |
| 05_era_comparison.ipynb | Dead Ball vs Live Ball vs Modern era comparison |
| 06_forecasting.ipynb | Simple win% forecasting model |

## Data Location

Notebooks read from `../data/*.csv` and write outputs to `../visualizations/output/`
