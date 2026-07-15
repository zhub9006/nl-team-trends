# Visualization Roadmap

## Planned Visualizations

### 1. Win-Loss Trend Lines Per Franchise (1876–2025)
- **Type**: Line chart (multi-line, one per franchise)
- **X-axis**: Season (1876–2025)
- **Y-axis**: Cumulative or rolling win percentage
- **Tool**: Matplotlib / Seaborn / Plotly
- **Insight**: Identify dynasty cycles, drought periods, and franchise trajectories
- **Status**: Not started

### 2. Pennant/Win Heatmap by Era
- **Type**: Heatmap (rows = teams, columns = decades or eras)
- **Color scale**: Win% or pennant count
- **Tool**: Seaborn / Plotly
- **Insight**: Spot dominant dynasties and competitive balance shifts
- **Status**: Not started

### 3. Head-to-Head Matchup Matrix Heatmap
- **Type**: Square heatmap (15×15 for current 15 NL teams)
- **Values**: Win% in head-to-head matchups (from Baseball Almanac W-L matrix)
- **Tool**: Plotly / Seaborn
- **Insight**: See inter-league rivalries and historical advantages
- **Status**: Not started

### 4. Championship Drought Duration Chart
- **Type**: Bar chart or horizontal bar chart
- **Metric**: Years since last championship per franchise
- **Tool**: Matplotlib
- **Insight**: Highlight historic droughts (e.g., Cubs 108 years) and recent dominance
- **Status**: Not started

### 5. Win% Distribution by Decade (Box Plot)
- **Type**: Box plot or violin plot (one box per decade)
- **X-axis**: Decade (1880s, 1890s, ..., 2020s)
- **Y-axis**: Win% (162-game adjusted)
- **Tool**: Seaborn / Plotly
- **Insight**: Show competitive balance changes over time
- **Status**: Not started

### 6. Interactive Dashboard (Future)
- **Type**: Streamlit or Dash web app
- **Features**:
  - Interactive team selector
  - Adjustable time range slider
  - Toggle between raw and rolling averages
  - Hover tooltips for detailed stats
  - Download data as CSV button
- **Tool**: Streamlit + Plotly
- **Status**: Planned

## Recommended Tool Stack

| Tool | Purpose |
|------|---------|
| Python | Core analysis language |
| Pandas | Data manipulation and CSV handling |
| Matplotlib / Seaborn | Static charts |
| Plotly | Interactive charts |
| Streamlit | Interactive dashboard |
| Jupyter Notebooks | Exploratory analysis (planned in `notebooks/`) |

## Data Source Priority

1. `data/nl_all_time_records.csv` — All-time franchise totals
2. `data/nl_championship_trends.csv` — Era-level championship highlights
3. `data/nl_notable_records.csv` — Single-season and franchise records
4. `data/source_references.md` — How to access deeper data for each era
