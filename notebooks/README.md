# NL Team Trends — Analysis Notebooks

This directory contains Jupyter Notebooks for exploring and visualizing National League team performance data.

## Available Notebooks

| Notebook | Description |
|----------|-------------|
| `01_eda_nl_standings.ipynb` | Exploratory data analysis of NL season-by-season standings |
| `02_championship_trends.ipynb` | Championship and dynasty analysis by era |
| `03_h2h_rivalries.ipynb` | Head-to-head rivalry heatmaps and trend lines |
| `04_franchise_comparison.ipynb` | Franchise win-loss comparison across eras |
| `05_win_pct_evolution.ipynb` | Win percentage evolution over time by division |

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r ../requirements.txt
   ```

2. Launch Jupyter:
   ```bash
   jupyter notebook
   ```

3. Open a notebook and follow the guided analysis steps.

## Data Files Used

All notebooks use CSV files from the `data/` directory:
- `nl_historical_performance.csv` — Season-by-season standings
- `nl_all_time_records.csv` — Franchise records
- `nl_championship_trends.csv` — Era highlights
- `nl_team_vs_team_summary.csv` — H2H matrices
- `nl_recent_standings.csv` — Recent divisional data

## Suggested Workflow

1. **Load & clean** → Read CSV, handle era-specific schedule lengths
2. **Explore** → Summary stats, distributions, missing data
3. **Visualize** → Line charts (trends), heatmaps (H2H), bar charts (comparisons)
4. **Analyze** → Dynasty detection, drought analysis, era comparisons
5. **Conclude** → Key takeaways and hypotheses for further research
