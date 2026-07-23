# NL Team Trends — Visualization Roadmap

## Overview
This directory contains visualization plans, Python scripts, and output for all NL historical data visualizations.

## Planned Visualizations

### 1. NL Championship Timeline
- **Type**: Interactive horizontal bar chart / timeline
- **Description**: Shows which team won the NL pennant each year from 1876–2025, color-coded by franchise
- **Key Insight**: Reveals dynasty periods and competitive shifts across eras
- **Tools**: Plotly or Matplotlib

### 2. Win-Loss Parity Chart
- **Type**: Scatter plot (Wins vs Losses)
- **Description**: All 15 NL teams plotted with their all-time W-L records
- **Key Insight**: Shows the competitive balance/imbalance across the league

### 3. Era Dominance Heatmap
- **Type**: Heatmap (Years × Teams)
- **Description**: Each cell colored by which team won the NL pennant in that year
- **Key Insight**: Visual dynasty identification and era transitions

### 4. H2H Rivalry Network Graph
- **Type**: Network/force-directed graph
- **Description**: Nodes are NL teams, edges are H2H matchups weighted by game count
- **Key Insight**: Reveals the most intense rivalries and lopsided matchups

### 5. Division Title Winners Bar Chart
- **Type**: Horizontal grouped bar chart
- **Description**: Division titles per team, grouped by division
- **Key Insight**: Shows which divisions have been most shared vs. dominated

### 6. Franchise Trajectory Sparklines
- **Type**: Small multiples of winning % over time
- **Description**: One small line chart per team showing seasonal winning %
- **Key Insight**: Franchise trajectories from founding to present

### 7. Single-Season Dominance Chart
- **Type**: Bar chart (Top 15 single-season records)
- **Description**: Top 15 single-season win totals in NL history
- **Key Insight**: Statistically impossible seasons vs. realistic records

### 8. WS Title Timeline
- **Type**: Gantt-style timeline
- **Description**: Shows WS title droughts and clusters for each franchise
- **Key Insight**: Cubs' 108-year drought, Dodgers' current run, etc.

### 9. H2H Pairwise Matrix Heatmap
- **Type**: 15×15 heatmap (reordered by rivalry intensity)
- **Description**: Full H2H W-L win percentage matrix
- **Key Insight**: Visual identification of the most and least competitive rivalries

### 10. NL West Competitiveness Over Time
- **Type**: Line chart (NL West parity over years)
- **Description**: Shows spread in division standings width per year
- **Key Insight**: NL West is the most competitive division (Dodgers-Giants-Padres)

## Quick Start (Matplotlib Example)

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load data
records = pd.read_csv('data/nl_all_time_records.csv')
records = records.sort_values('ws_titles', ascending=False)

# WS Titles chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(records['team'], records['ws_titles'], color='steelblue')
ax.set_xlabel('World Series Titles')
ax.set_title('NL Teams by World Series Titles (1876–2025)')
plt.tight_layout()
plt.savefig('charts/ws_titles_by_team.png', dpi=150)
plt.show()

# Winning percentage chart
fig, ax = plt.subplots(figsize=(10, 6))
records_sorted = records.sort_values('win_pct', ascending=True)
ax.barh(records_sorted['team'], records_sorted['win_pct'], color='coral')
ax.set_xlabel('All-Time Win Percentage')
ax.set_title('NL Teams by All-Time Winning Percentage')
ax.axvline(x=0.500, color='gray', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('charts/win_pct_by_team.png', dpi=150)
plt.show()
```

## Required Python Packages
See `requirements.txt` at root level:
- pandas>=1.5.0
- matplotlib>=3.6.0
- seaborn>=0.12.0
- plotly>=5.0.0
- numpy>=1.23.0
- requests>=2.28.0

## Output Directory
Save chart PNGs to `charts/` directory:
- `charts/ws_titles_by_team.png`
- `charts/win_pct_by_team.png`
- `charts/era_heatmap.png`
- `charts/rivalry_network.png`
- `charts/division_titles.png`
- `charts/seasonal_trajectories.png`
- `charts/single_season_dominance.png`
- `charts/h2h_matrix.png`
- `charts/nlwest_competitiveness.png`