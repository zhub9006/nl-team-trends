# Visualizations 📊

This directory contains planned and in-progress data visualizations for NL Team Trends research.

## Visualization Projects

### 1. All-Time Franchise Win-Loss Bar Chart
- **Data Source**: `data/nl_all_time_records.csv`
- **Type**: Horizontal bar chart ordered by win percentage
- **Insight**: Compare franchise durability and winning % across the century-plus landscape
- **Status**: 🔲 Planned
- **Tools**: Python (matplotlib/seaborn), Plotly

### 2. Championship Timeline (Gantt-style)
- **Data Source**: `data/nl_championship_trends.csv`
- **Type**: Timeline/Gantt chart showing championship runs across eras
- **Insight**: Visualize eras of dominance (Braves 1991-2005, Dodgers 2017-2025)
- **Status**: 🔲 Planned
- **Tools**: Python (plotly), D3.js

### 3. Heatmap: Head-to-Head Records
- **Data Source**: Baseball Almanac team-vs-team matrix (see source_references.md)
- **Type**: Matrix heatmap (NL team vs NL team)
- **Insight**: Identify historical rivalries and dominance patterns
- **Status**: 🔲 Planned
- **Tools**: Python (seaborn), Plotly

### 4. Season-by-Season Win-Loss Trends
- **Data Source**: SABR Lahman + season records
- **Type**: Line chart overlaying multiple franchises with rolling averages
- **Insight**: Track franchise trajectories through winning and losing cycles
- **Status**: 🔲 Planned
- **Tools**: Python (pandas + matplotlib)

### 5. Pennant/Championship Flow Diagram
- **Data Source**: `data/nl_championship_trends.csv` + `data/nl_historical_performance_detailed.csv`
- **Type**: Sankey/flow diagram showing pennant flows to WS outcomes
- **Insight**: Which pennant winners won the World Series vs. fell short
- **Status**: 🔲 Planned
- **Tools**: Plotly, D3.js

### 6. Division Dominance Over Time
- **Data Source**: `data/nl_recent_standings.csv` + historical division data
- **Type**: Small multiples by division, showing which team led each decade
- **Insight**: How competitive balance has shifted across NL East/West/Central
- **Status**: 🔲 Planned
- **Tools**: Python (seaborn), R (ggplot2)

### 7. Championship Drought Duration Chart
- **Data Source**: `data/nl_historical_performance_detailed.csv`
- **Type**: Bar chart showing years between championships for each franchise
- **Insight**: Visualize droughts (Cubs 108 years, Indians 68 years) and recent runs (Dodgers 8 titles in 7 years)
- **Status**: 🔲 Planned
- **Tools**: Python (plotly)

### 8. Win% Distribution by Decade
- **Data Source**: SABR Lahman dataset
- **Type**: Box plots per decade showing competitive balance evolution
- **Insight**: Has the NL become more or less competitive over time?
- **Status**: 🔲 Planned
- **Tools**: Python (seaborn), R (ggplot2)

### 9. Interactive Dashboard
- **Data Sources**: All CSV files
- **Type**: Streamlit/Dash web app with filters by era, team, stat
- **Insight**: Allow users to explore NL team trends interactively
- **Status**: 🔲 Planned
- **Tools**: Streamlit or Dash (Python)

## Suggested Tool Stack

| Tool | Use Case |
|------|----------|
| `pandas` | Data loading, cleaning, aggregation |
| `matplotlib` | Static chart publication quality |
| `seaborn` | Statistical visualizations, heatmaps |
| `plotly` | Interactive charts, hover tooltips |
| `streamlit` | Web dashboard framework |
| `d3.js` | Custom JavaScript visualizations |
| `numpy` | Numerical operations and calculations |
| `jupyter` | Notebook-based exploration |

## Quick Start for Visualization Projects

```python
# Example: Load and plot all-time NL records
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/nl_all_time_records.csv')
df = df.sort_values('WinPct', ascending=True)

fig, ax = plt.subplots(figsize=(14, 8))
sns.barplot(data=df, y='Team', x='WinPct', palette='Blues_r', ax=ax)
ax.set_title('NL All-Time Franchise Winning Percentage (1876-2025)', fontsize=16)
ax.set_xlabel('Win Percentage')
ax.set_ylabel('Franchise')
plt.tight_layout()
plt.savefig('charts/all_time_wins_by_team.png', dpi=300)
```

## Visualization Roadmap Status

| # | Chart | Priority | Status |
|---|-------|----------|--------|
| 1 | All-Time W-L Bar Chart | 🔴 High | 🔲 Planned |
| 2 | Championship Timeline | 🔴 High | 🔲 Planned |
| 3 | Head-to-Head Heatmap | 🔴 High | 🔲 Planned |
| 4 | Season-by-Season Trends | 🟠 Medium | 🔲 Planned |
| 5 | Championship Flow Diagram | 🟠 Medium | 🔲 Planned |
| 6 | Division Dominance | 🟡 Lower | 🔲 Planned |
| 7 | Championship Droughts | 🔴 High | 🔲 Planned |
| 8 | Win% Distribution by Decade | 🟡 Lower | 🔲 Planned |
| 9 | Interactive Dashboard | 🟠 Medium | 🔲 Planned |

All charts are designed to be reproducible from the CSV data files in `../data/`.