# Visualizations Roadmap — nl-team-trends

## Planned Visualization Projects

1. **Win-Loss Trends Over Time** (line chart) — Cumulative win% over decades
2. **World Series Titles by Team** (bar chart) — Cardinals (11) vs Dodgers (9) vs Giants (8)
3. **H2H Rivalry Heatmap** (15x15 matrix) — All NL team vs NL team matchups
4. **Championship Timeline by Era** (Sankey) — Pennant flow by decade
5. **NL ERA & Run Scoring Trends** (dual-axis) — Dead-Ball, Live-Ball, Integration eras
6. **Division Dominance Tracker** — Las Vegas-style division control by decade

## Suggested Tools
- matplotlib: Static charts
- seaborn: Statistical visualizations
- plotly: Interactive HTML charts
- streamlit: Web dashboard

## Quick Start
```python
import pandas as pd
all_time = pd.read_csv('data/nl_all_time_records.csv')
seasonal = pd.read_csv('data/nl_historical_performance.csv')
h2h = pd.read_csv('data/nl_h2h_rivalries_detailed.csv')

# WS titles bar chart
ax = all_time.sort_values('WS_Titles', ascending=True).plot(
    x='Team', y='WS_Titles', kind='barh', figsize=(10, 6),
    color='steelblue', edgecolor='white')
plt.title('NL WS Titles by Team')
plt.savefig('charts/ws_titles_by_team.png', dpi=150)
```