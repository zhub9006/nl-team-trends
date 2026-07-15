# NL Team Trends — Visualization Roadmap

## Planned Visualizations

### 1. Win-Loss Trend Lines by Franchise (1876–2025)
- **Type**: Multi-line time series
- **X-axis**: Season year
- **Y-axis**: Win % or W-L record
- **Lines**: One per franchise, color-coded
- **Insight**: See competitive shifts across eras

### 2. Pennant Heatmap
- **Type**: Heatmap (team × year)
- **Color**: Intensity by pennant count or win%
- **Insight**: Dominance patterns by era
- **Example**: Atlanta 1991–2005 as a bright stripe

### 3. Championship Drought Chart
- **Type**: Bar chart with annotations
- **X-axis**: Team
- **Y-axis**: Years since last WS title
- **Insight**: Cardinals (1982→2006 gap), Cubs (1908→2016 gap)

### 4. Head-to-Head Matchup Matrix
- **Type**: Square matrix heatmap
- **Cells**: W-L record between each pair of NL teams
- **Insight**: Rivalry intensity and historical balances
- **Source**: Baseball Almanac team-vs-team data

### 5. Win% Distribution by Decade
- **Type**: Box plot or violin plot
- **X-axis**: Decade
- **Y-axis**: Team win%
- **Insight**: Whether the league has become more competitive over time

### 6. Interactive Dashboard
- **Tool**: Streamlit + Plotly
- **Features**:
  - Filter by era, team, division
  - Hover tooltips with detailed season records
  - Download filtered data as CSV
  - Animated timeline of franchise trajectories

## Recommended Tools
| Tool | Use Case | Difficulty |
|------|----------|-----------|
| Matplotlib | Static charts, publications | Easy |
| Seaborn | Statistical heatmaps, distributions | Easy |
| Plotly | Interactive charts, dashboards | Medium |
| Streamlit | Full web dashboard | Medium |
| Altair | Declarative statistical visualization | Easy |

## Data Files Available
- `data/nl_all_time_records.csv` — Franchise-level summary
- `data/nl_historical_performance.csv` — Year-by-year championship data
- `data/nl_pennant_winners_recent.csv` — Pennant winners 1995–2025
- `data/nl_recent_standings.csv` — Full standings 2016–2025
- `data/nl_championship_trends.csv` — Era-level analysis
- `data/nl_notable_records.csv` — Records and milestones
- `docs/data_notes.md` — Methodology & conventions
- `source_references.md` — Source attribution