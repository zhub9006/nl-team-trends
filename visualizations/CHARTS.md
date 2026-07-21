# NL Team Trends — Visualization Guide

This directory contains documentation for all planned visualizations in the NL Team Trends project.

## Completed Visualizations

| Chart | Description | 
|-------|-------------|
| `ws_titles_by_team.png` | Horizontal bar chart of WS titles per NL franchise |
| `win_pct_vs_differential.png` | Scatter plot: Win% vs Win Differential (bubble = games played) |
| `ws_titles_by_era.png` | Bar chart: WS titles distributed across NL eras |
| `top_h2h_rivalries.png` | Grouped bar chart: Top 10 NL rivalries by total games |

## Planned Visualizations

| Chart | Description | Tool | Status |
|-------|-------------|------|--------|
| Franchise Win% Timeline | Line chart showing win% trends by team over decades | Matplotlib | Planned |
| Dynasty Gantt | Horizontal bars for sustained success spans | Matplotlib | Planned |
| Era Win Distribution | Box plot of win% by era | Seaborn | Planned |
| H2H Heatmap | 15×15 correlation-based heatmap | Seaborn/Plotly | Planned |
| Interactive Dashboard | Full web app with filters by team/era | Streamlit/Plotly | Planned |
| Franchise Wins by Decade | Grouped bar chart of franchise wins per decade | Matplotlib | Planned |
| Championship Drought Map | Timeline showing championship droughts per team | Plotly | Planned |

## Adding New Charts

1. Create your chart script in `scripts/build_visualizations.py`
2. Save output to `charts/` directory
3. Document in this README
4. Update `DATA_INDEX.md` with the new chart file

## Quick Start

```bash
python scripts/get_nl_data.py  # Extract data from Lahman DB
python -m jupyter notebook notebooks/01_eda_nl_standings.ipynb  # Run EDA
```

## Recommended Tools

| Tool | Use Case |
|------|----------|
| Matplotlib | Static, publication-quality charts |
| Seaborn | Statistical heatmaps, distribution plots |
| Plotly | Interactive dashboards with hover info |
| Streamlit | Web-app dashboards for exploration |
| Plotly Express | Quick interactive chart creation |
