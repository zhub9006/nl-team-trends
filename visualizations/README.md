# NL Team Trends - Visualization Roadmap

## Completed
- [x] Era-based championship comparison charts
- [x] All-time franchise records bar charts
- [x] WW2 era pentant heatmap
- [x] NL pennant winners by year (1876-2025)

## Planned Visualizations

### 1. Win-Loss Trend Lines Per Franchise (1876-2025)
- **Type**: Line chart (multi-line; one per franchise)
- **X-axis**: Season rolling 5-year average
- **Y-axis**: Rolling win%
- **Tool**: Matplotlib / Seaborn
- **Insight**: Identify dynasty cycles, drought periods, franchise trajectories

### 2. Pennant/Win Heatmap by Era
- **Type**: Heatmap (rows=teams, columns=eras or decades)
- **Color scale**: Win% or pennant count
- **Tool**: Seaborn / Plotly
- **Insight**: Spot dominant dynasties and competitive balance shifts

### 3. Head-to-Head Matchup Matrix Heatmap
- **Type**: Square heatmap (15x15 for current NL teams)
- **Values**: Win% in head-to-head matchups
- **Tool**: Plotly
- **Insight**: See inter-league rivalries and historical advantages

### 4. Championship Drought Duration Chart
- **Type**: Horizontal bar chart
- **Metric**: Years since last championship per franchise
- **Tool**: Matplotlib
- **Insight**: Highlight historic droughts (Cubs 108yr, Mets 18yr?)

### 5. Win% Distribution by Decade (Box Plot)
- **Type**: Violin/box plot (decades x Win%)
- **X-axis**: Decade (1880s, 90s, ..., 2020s)
- **Y-axis**: Win% (162-game adjusted)
- **Tool**: Seaborn
- **Insight**: Show competitive balance changes over time

### 6. Interactive Dashboard (Streamlit)
- **Type**: Streamlit web app
- **Features**: Team selector, time range slider, rolling averages toggle, download button
- **Tool**: Streamlit + Plotly
- **Status**: Future

## Recommended Tool Stack
| Tool | Purpose |
|------|--------|
| Python | Core language |
| Pandas | Data manipulation |
| Matplotlib/Seaborn | Static charts |
| Plotly | Interactive charts |
| Streamlit | Web dashboard |
| Jupyter | Exploration |

## Data Source Priority
1. `data/nl_all_time_records.csv` - All-time franchise totals
2. `data/nl_championship_by_decade.csv` - Era-level trends
3. `data/nl_pennant_winners_1876_2025.csv` - Annual champion detail
4. `data/nl_recent_standings_2020_2025.csv` - Recent divisional data
5. `docs/source_references.md` - How to access deeper data