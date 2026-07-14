# NL Team Trends Visualizations

Visualizations for NL historical performance analysis. See `../docs/data_notes.md` for methodology.

## Planned Visualizations

| Plot | Description | Tool |
|------|-------------|------|
| franchise_win_trajectory.png | Win% by decade per franchise (line chart) | Python/Matplotlib |
| pennant_frequency_heatmap.png | Pennant per decade grid heatmap (teams × decade) | Python/Seaborn |
| division_balance.png | Win% distribution strip chart by division | R/ggplot2 |
| h2h_network.png | Team-vs-team win-loss network (edge weights = H2H) | NetworkX/Plotly |
| expansion_ramp.png | New franchise adjustment 7-10 year curves | Python |
| run_diff_vs_pennant.png | Run differential vs pennant success | Python/Seaborn |
| elo_ratings_evolution.png | Cumulative Elo ratings across decades | PyElo |
| home_away_splits.png | Home vs Away win% by era (bar chart) | Python/Matplotlib |

## Quick Start

```bash
cd visualizations
pip install matplotlib pandas numpy seaborn
```

Each script reads from `../data/*.csv` and writes to `./output/`.
