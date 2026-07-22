# NL Team Trends — Visualization Roadmap

## Overview

This document outlines the planned visualizations for the NL Team Trends project, along with recommended tools and data sources.

## Visualization Projects

### 1. NL Win-Loss Trends Over Time
- **Type**: Multi-line time series chart
- **Description**: Plot win percentage for each NL franchise from 1876 to present, grouped by era
- **Data Source**: `data/nl_historical_performance.csv`
- **Tools**: matplotlib, seaborn, plotly
- **Insights**: Identify dynasties, droughts, and franchise trajectories

### 2. NL Team vs Team H2H Heatmap
- **Type**: Heatmap / matrix visualization
- **Description**: 15×15 matrix showing win-loss records for every NL team vs every other NL team
- **Data Source**: `data/nl_team_vs_team_summary.csv`
- **Tools**: seaborn (heatmap), plotly (interactive)
- **Insights**: Identify geographic and historical rivalries

### 3. World Series Titles by Franchise
- **Type**: Horizontal bar chart
- **Description**: Bar chart showing WS titles per NL franchise, sorted by count
- **Data Source**: `data/nl_all_time_records.csv`
- **Tools**: matplotlib, plotly
- **Insights**: Visualize dynasty franchises

### 4. Championship Era Comparison
- **Type**: Grouped bar chart or stacked area chart
- **Description**: Compare NL WS winners across eras (Founding through Modern)
- **Data Source**: `data/nl_pennant_winners.csv`, `data/nl_championship_trends.csv`
- **Tools**: matplotlib, seaborn
- **Insights**: Identify era-specific dominance patterns

### 5. Pennant Winners by Year (Timeline)
- **Type**: Timeline / Gantt-style chart
- **Description**: Show pennant winners from 1876–2025 with color coding by team
- **Data Source**: `data/nl_pennant_winners.csv`
- **Tools**: plotly, altair
- **Insights**: Visualize franchise sustained success

### 6. Franchise Win% Distribution
- **Type**: Box plot or violin plot
- **Description**: Show distribution of seasonal win percentages by franchise
- **Data Source**: `data/nl_historical_performance.csv`
- **Tools**: seaborn, plotly
- **Insights**: Identify consistency vs. volatility patterns

### 7. NL Division Dominance Map
- **Type**: Stacked area chart
- **Description**: Show which NL division dominated each era
- **Data Source**: `data/nl_recent_standings.csv`
- **Tools**: matplotlib, plotly
- **Insights**: Track shift of competitive balance across divisions

### 8. Interactive Dashboard
- **Type**: Plotly Dash or Streamlit web app
- **Description**: Interactive dashboard combining multiple views
- **Data Source**: All CSV files
- **Tools**: Streamlit, Plotly Dash, voila
- **Features**: Team selector, era slider, H2H lookup, record comparison

## Tool Recommendations

### Python Libraries
- **pandas**: Data manipulation and analysis
- **matplotlib**: Static publication-quality figures
- **seaborn**: Statistical visualizations
- **plotly**: Interactive web-based charts
- **altair**: Declarative statistical visualization
- **jupyter**: Notebook environment for exploration

### Quick Start
```bash
pip install -r requirements.txt
jupyter notebook
```

## File Organization

```
visualizations/
├── README.md                  ← This file
├── v1_win_loss_trends.py      ← Time series of W% by team
├── v2_h2h_heatmap.py          ← H2H rivalry heatmap
├── v3_ws_titles_bar.py        ← WS titles by franchise
├── v4_era_comparison.py       ← Championship by era
├── v5_timeline.py             ← Pennant winners timeline
├── v6_distribution.py         ← Win% distribution
├── v7_division_dominance.py   ← Division comparison
└── dashboard_app.py           ← Interactive dashboard
```
