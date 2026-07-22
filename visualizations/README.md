# NL Team Trends — Visualization Roadmap

## Purpose

This directory contains planned data visualizations for the NL team trends research project. All visualizations are designed to reveal team performance patterns, era-specific trends, franchise trajectories, and rivalry dynamics across the full history of the National League.

## Planned Visualizations

### 1. NL All-Time Franchise Win-Loss Bar Chart
- **Type**: Horizontal bar chart
- **Data**: `nl_all_time_records.csv`
- **X-axis**: Win percentage (all-time)
- **Y-axis**: Franchise name (sorted by win%)
- **Color**: By division or era of founding
- **Notable**: Highlight Cardinals (11 WS), Dodgers (9 WS), Giants (8 WS)

### 2. NL Pennant Winners by Era (Timeline/Heatmap)
- **Type**: Timeline or heatmap
- **Data**: `nl_pennant_winners.csv`
- **X-axis**: Year (chronological)
- **Y-axis**: Team
- **Color**: Win % or pennant count per era
- **Notable**: Show Cardinals/Dodgers/Giants dominance periods

### 3. Team Win-Loss Trends Over Time (Small Multiples)
- **Type**: Small multiple line charts (faceted by team)
- **Data**: `nl_historical_performance.csv`
- **X-axis**: Year
- **Y-axis**: Win %
- **Notable**: Show championship droughts (Cubs 1908–2016), Braves dynasty, etc.

### 4. Championship Response Surface (W-L by Season Type)
- **Type**: Heatmap or contour plot
- **Data**: Combined from `nl_championship_trends.csv` + `nl_historical_performance.csv`
- **X-axis**: Season year
- **Y-axis**: Team
- **Color**: W-L record differential (W - L)
- **Notable**: Highlight peak dominance periods (1906 Cubs, 1907–08 Cubs, 2020 Dodgers)

### 5. H2H Rivalry Win-Loss Comparison
- **Type**: Diverging bar chart or slope graph
- **Data**: `nl_team_vs_team_summary.csv`
- **X-axis**: Win % differential
- **Y-axis**: Pair of teams
- **Color**: Which team has the edge
- **Notable**: Cardinals vs Pirates (60.6%), Dodgers vs Cubs (69.5%), Mets vs Phillies (50-50)

### 6. Draft Era Comparison Box Plot
- **Type**: Box plot per era
- **Data**: `nl_historical_performance.csv`
- **X-axis**: Era
- **Y-axis**: Win %
- **Notable**: Compare competitive balance across eras

### 7. World Series Winners by Team (Treemap or Sunburst)
- **Type**: Treemap or sunburst chart
- **Data**: `nl_championship_trends.csv`
- **Notable**: Cardinals 11, Dodgers 9, Giants 8 — all other NL teams with 5 or fewer fall below

### 8. NL Team Expansion Timeline
- **Type**: Horizontal timeline or Gantt chart
- **Data**: Derived from `nl_all_time_records.csv` (first_season field)
- **Notable**: Mark expansion years (1962, 1969, 1993, 1998) and relocations (1958, 2005)

## Recommended Tools

| Tool | Use Case | Complexity |
|------|----------|------------|
| Python (pandas + matplotlib/seaborn) | Static charts for papers, docs | Low |
| Python (plotly) | Interactive web charts | Low |
| R (ggplot2) | Statistical approach; academic papers | Medium |
| D3.js | Custom interactive web visualizations | High |
| Tableau / PowerBI | Business intelligence dashboards | Medium |

## Data Source Links

- [Lahman Baseball Database](https://sabr.org/lahman-database/) — free CSV download
- [Baseball-Reference (NL)](https://www.baseball-reference.com/leagues/NL/) — official standings & stats
- [Baseball Data Hub](https://baseballdatahub.com/seasons/) — browsable season-by-season data
- [Baseball Almanac](https://www.baseball-almanac.com/yearmenu.shtml) — historical summaries by year

## Contribution Guide

To add a new visualization:
1. Create a new file in this directory (e.g., `viz_01_franchise_win_pct.py`)
2. Include the data source, chart type, and key insights in comments
3. Add any output charts as PNG or SVG files in `/charts` subdirectory
4. Update this README with a description of the new visualization
