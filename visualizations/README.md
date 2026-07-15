# Visualization Roadmap & Guide

## Available Data Files

| File | Description |
|------|-------------|
| `data/nl_all_time_records.csv` | All-time franchise win-loss totals (basic) |
| `data/nl_all_time_records_enriched.csv` | All-time records with era, playoff appearances, last WS, current division |
| `data/nl_historical_comprehensive.csv` | Full historical data: pennant winners, era summary, franchise records, division champions |
| `data/nl_championship_trends.csv` | Championship highlights organized by era |
| `data/nl_notable_records.csv` | Notable single-season and franchise records |
| `data/nl_pennant_winners_recent.csv` | NL pennant winners & WS results (1995-2025) |
| `data/nl_recent_standings.csv` | Division champions (2020-2025) |
| `source_references.md` | Detailed source attribution and data conventions |

## Planned Visualizations

### 1. Win-Loss Trend Lines Per Franchise (1876–2025)
- **Type**: Multi-line chart (one line per franchise, 15 teams)
- **X-axis**: Season (1876–2025)
- **Y-axis**: Cumulative win percentage or rolling 10-year average
- **Color**: Use team color palette
- **Insight**: Identify dynasty cycles (Braves, Dodgers, Cardinals), drought periods (Cubs 108 years), and franchise trajectories
- **Tool**: Python (Pandas + Matplotlib/Seaborn) or Plotly for interactivity
- **Status**: Ready for implementation — data available in `nl_historical_comprehensive.csv`

### 2. Pennant/Win Heatmap by Era
- **Type**: Heatmap (rows = teams, columns = decades: 1880s, 1890s, ..., 2020s)
- **Color scale**: Green (high win%) to Red (low win%)
- **Insight**: Spot dominant dynasties and competitive balance shifts; see how team performance changed after relocations
- **Tool**: Seaborn `heatmap()` or Plotly `go.Heatmap()`
- **Status**: Ready for implementation

### 3. Head-to-Head Matchup Matrix Heatmap
- **Type**: Square heatmap (15×15 for current 15 NL teams, or full historical for all teams that ever existed)
- **Values**: Head-to-head win% from Baseball Almanac's 1876-2026 matchup matrices
- **Insight**: See inter-league rivalries and historical advantages; identify which teams historically dominate others
- **Tool**: Plotly `imshow()` or Seaborn
- **Status**: Data available on [Baseball Almanac](https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml)

### 4. Championship Drought Duration Chart
- **Type**: Horizontal bar chart or dot plot
- **Metric**: Years since last WS title per franchise
- **Insight**: Highlight historic droughts (Cubs 108 years) and recent dominance (Dodgers back-to-back)
- **Tool**: Matplotlib `barh()`
- **Status**: Ready for implementation

### 5. Win% Distribution by Decade (Box Plot / Violin Plot)
- **Type**: Box plot or violin plot (one per decade: 1880s-2020s)
- **X-axis**: Decade
- **Y-axis**: Win% (162-game adjusted)
- **Insight**: Show how competitive balance has changed; 19th century vs modern era variance
- **Tool**: Seaborn `boxplot()` or `violinplot()`
- **Status**: Ready for implementation

### 6. Dividional Shift Tracker
- **Type**: Sankey diagram or stacked bar chart
- **Metric**: Team division changes over time (e.g., Braves: West → Central → East)
- **Insight**: Visualize franchise migrations and division realignments
- **Tool**: Plotly `sankey()` diagram
- **Status**: Preliminary tracking data in `nl_all_time_records_enriched.csv`

### 7. Interactive Dashboard (Streamlit / Dash)
- **Type**: Web app with controls
- **Features**: 
  - Interactive team selector
  - Adjustable time range slider (1876-2025)
  - Toggle raw vs rolling average win%
  - Pennant/win heatmap with hover tooltips
  - Download data as CSV button
  - Comparison mode (select 2+ teams to compare)
- **Tool**: Streamlit + Plotly
- **Status**: Planned

## Recommended Tool Stack

| Tool | Purpose | Install |
|------|---------|---------|
| Python | Core analysis language | python.org |
| Pandas | Data manipulation and CSV handling | `pip install pandas` |
| Matplotlib | Static charts and publication-ready figures | `pip install matplotlib` |
| Seaborn | Statistical visualizations (heatmaps, boxplots) | `pip install seaborn` |
| Plotly | Interactive charts and dashboards | `pip install plotly` |
| Streamlit | Interactive web dashboard | `pip install streamlit` |
| Jupyter | Exploratory analysis and notebooks | `pip install jupyter` |

## Quick Start Template

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the comprehensive data (parse semantically split sections)
data = pd.read_csv('data/nl_historical_comprehensive.csv', comment='#')
all_time = pd.read_csv('data/nl_all_time_records_enriched.csv')
pennants = pd.read_csv('data/nl_historical_comprehensive.csv', comment='#')
# Note: For full parsing, split by '---eof---' markers or process sections

# Quick win-loss bar chart
fig, ax = plt.subplots(figsize=(14, 8))
sorted_teams = all_time.sort_values('wins', ascending=True)
ax.barh(sorted_teams['franchise'], sorted_teams['wins'], color=team_colors)
ax.set_xlabel('All-Time Wins')
ax.set_title('NL Team All-Time Wins (1876-2025)')
plt.tight_layout()
plt.savefig('visualizations/win_totals.png', dpi=150)
plt.show()
```

## Data Source Priority

1. `data/nl_historical_comprehensive.csv` — Full historical data (pennants, records, eras)
2. `data/nl_all_time_records_enriched.csv` — Enriched all-time franchise totals
3. `data/nl_championship_trends.csv` — Era-level championship highlights
4. `data/nl_notable_records.csv` — Single-season and franchise records
5. `source_references.md` — How to access deeper data for each era
6. `docs/data_notes.md` — Methodology, conventions, and caveats
