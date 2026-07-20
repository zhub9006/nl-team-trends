# Visualizations Roadmap — nl-team-trends

## Planned Visualization Projects

### 1. Win-Loss Trends Over Time
- **Type**: Line chart
- **Data Source**: `data/nl_historical_performance.csv`
- **Description**: Plot each NL team's cumulative win% over the decades (1876–present)
- **Tools**: matplotlib, seaborn, or plotly for interactive version
- **Insight**: See how franchise trajectories diverge and converge over time

### 2. World Series Titles by Team
- **Type**: Bar chart
- **Data Source**: `data/nl_all_time_records.csv`
- **Description**: Horizontal bar chart of WS titles for each NL team
- **Tools**: matplotlib or plotly
- **Insight**: Cardinals (11) vs Dodgers (9) vs Giants (8) dominance

### 3. Head-to-Head Rivalry Heatmap
- **Type**: Heatmap / matrix
- **Data Source**: `data/nl_h2h_rivalries_detailed.csv`
- **Description**: 15×15 matrix of H2H win% for all NL team vs NL team matchups
- **Tools**: seaborn heatmap or plotly
- **Insight**: Color-coded view of who dominates whom (Cardinals vs Pirates 60.6% is most lopsided)

### 4. Championship Timeline by Era
- **Type**: Timeline / Sankey diagram
- **Data Source**: `data/nl_championship_trends.csv`
- **Description**: Visual flow of pennant winners + WS champions by decade
- **Tools**: plotly or matplotlib
- **Insight**: See dynasty periods (1942-46 Cardinals, 1991-2005 Braves, 2018-2025 Dodgers)

### 5. Pitching vs Hitting Performance Over Time
- **Type**: Dual-axis line chart
- **Data Source**: SABR Lahman Database (separate from this repo)
- **Description**: NL ERA and run scoring trends by era (Dead-Ball, Live-Ball, Integration, Steroids)
- **Tools**: matplotlib or plotly
- **Insight**: Correlation between pitching dominance eras and low-scoring games

### 6. Breakeven Chart
- **Type**: Scatter plot with varying point sizes
- **Data Source**: `data/nl_all_time_records.csv`
- **Description**: Win% over time with number of games as point size (shows "more data = more stability")
- **Tools**: matplotlib or plotly
- **Insight**: Small franchises (Marlins) can't win titles despite shorter history

### 7. Win Probability by Decade Flywheel
- **Type**: Box plot or violin plot
- **Data Source**: `data/nl_historical_performance.csv` (season-by-season)
- **Description**: Distribution of team win% within each decade
- **Tools**: seaborn
- **Insight**: How competitive the NL was in each era (1990s flattened by Braves monopoly)

### 8. Draft: Interleague Era Comparison (1876-1902 vs 1903-Present)
- **Type**: Overlapping histograms
- **Data Source**: `data/nl_historical_performance.csv`
- **Description**: Compare NL-only pennant winners with NL teams in World Series era
- **Tools**: matplotlib
- **Insight**: How much the WS changed NL competitive dynamics post-1903

## Suggested Tools

| Tool | Use Case | Installation |
|------|----------|--------------|
| matplotlib | Static charts | `pip install matplotlib` |
| seaborn | Statistical viz | `pip install seaborn` |
| plotly | Interactive HTML charts | `pip install plotly` |
| streamlit | Web dashboard | `pip install streamlit` |
| pandas | Data manipulation | `pip install pandas` |
| jupyter | Notebook environment | `pip install jupyter` |

## Quick Start (Jupyter Notebook)
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
all_time = pd.read_csv('data/nl_all_time_records.csv')
h2h = pd.read_csv('data/nl_h2h_rivalries_detailed.csv')
seasonal = pd.read_csv('data/nl_historical_performance.csv')

# Bar chart: WS titles by team
ax = all_time.sort_values('WS_Titles', ascending=True).plot(
    x='Team', y='WS_Titles', kind='barh', figsize=(10, 6),
    color='steelblue', edgecolor='white')
plt.title('NL World Series Titles by Team')
plt.xlabel('Number of WS Titles')
plt.tight_layout()
plt.savefig('charts/ws_titles_by_team.png', dpi=150)
plt.show()

# H2H heatmap
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
fig, ax = plt.subplots(figsize=(14, 10))
heat_data = ... # pivot h2h data
sns.heatmap(heat_data, annot=True, fmt='.1%', cmap='RdYlGn_r', ax=ax)
plt.title('NL Team vs Team Win% H2H (1876-2026)')
plt.tight_layout()
plt.savefig('charts/h2h_heatmap.png', dpi=150)
plt.show()
```