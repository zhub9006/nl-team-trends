# Visualization Roadmap

This document outlines planned visualizations and recommended tools for the NL Team Trends project.

## Recommended Visualization Tools

| Tool | Best For | Setup | Link |
|------|----------|-------|------|
| Matplotlib | Static charts (bar, line, scatter) | pip install matplotlib | https://matplotlib.org |
| Seaborn | Statistical heatmaps, distribution plots | pip install seaborn | https://seaborn.pydata.org |
| Plotly | Interactive dashboards & hover tooltips | pip install plotly | https://plotly.com |
| Streamlit | Full web app dashboards | pip install streamlit | https://streamlit.io |
| Foliium | Geographic maps (team locations over time) | pip install folium | https://python-visualization.github.io/foliium |
| WordCloud | Championship word clouds by era | pip install wordcloud | https://amueller.github.io/word_cloud |

## Proposed Visualizations

### 1. NL Win-Loss Trends Over Time (Line Chart)
X-axis: Year (1876-2025), Y-axis: Win % or total wins, one line per team or per division. Highlight dominant eras.

### 2. Championship Hierarchy (Treemap or Sunburst)
Each ring represents a level: League to Division to Championship outcome. Color by WS win vs loss.

### 3. Head-to-Head Heatmap (Seaborn)
15x15 matrix of all NL teams. Values: total H2H wins for team (row) vs opponent (column). Color gradient source: data/nl_team_vs_team_summary.csv.

### 4. Dynasty Timeline (Gantt Chart)
Horizontal bars spanning years of sustained success. Group by franchise. Annotate with WS titles and pennants.

### 5. WS Title Distribution (Bar Chart and Pie)
How many WS titles each NL team holds. Compare NL vs AL. Source data: data/nl_all_time_records.csv.

### 6. Division Dominance Heatmap
Rows: divisions (NL East, NL Central, NL West). Columns: decades. Cells: which team dominated that division in that decade.

### 7. Win % Distribution by Era (Box Plot)
Show spread of win percentages within each era. Identify outlier seasons. Source data: data/nl_historical_performance.csv.

### 8. Interleague H2H Trends (Line Chart)
Track NL vs AL win ratio since 1997. Source data: data/nl_notable_records.csv.

## Getting Started

1. Install dependencies: pip install -r requirements.txt
2. Download Lahman Database: wget https://github.com/chadwickbureau/baseballdatabank/archive/refs/heads/master.zip
3. Load data: python -c "import pandas as pd; df = pd.read_csv('data/nl_all_time_records.csv')"
4. Plot! See notebooks/01_eda_nl_standings.ipynb for a template