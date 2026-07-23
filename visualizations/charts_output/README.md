# NL Team Trends - Data Visualization Output

This directory stores generated charts and visual assets.

## Generated Chart Descriptions

### nl_franchise_wins_losses.png
Grouped horizontal bar chart showing all-time NL franchise wins (blue) and losses (gray), sorted by total wins.

### nl_era_win_pct_boxplot.png
Box plot showing the distribution of NL championship-winning season win percentages across eras. Highlights how dominant eras produce extreme win% champions.

### nl_h2h_rivalry_pct.png
Horizontal bar chart of H2H rivalry win percentages. Red bars (Dominant), Blue bars (Underdog), Gray (Even). Reveals the most one-sided NL rivalries.

### nl_win_pct_heatmap.png
Heatmap of NL division winners' win percentages by year. Shows the concentration of Dodger dominance in recent years.

### nl_ws_timeline.png
Scatter chart tracking NL champion season win percentage over time, with NL WS winners (diamonds) and AL WS winners (squares).

## Generate Charts

```bash
cd charts/
python nl_viz.py
```

## Planned Visualizations

- Interactive Plotly dashboard (with team selection dropdowns)
- NL pennant winners timeline chart
- Franchise era transition analysis
- Individual team career win% trajectories
- Longest drought/streak analysis charts
- Division crossover championship analysis
- Cycles and dynasty identification
---

## Supporting Data

See `../README.md` for the complete data file index.