# Visualization Roadmap

## Planned Visualizations

### 1. All-Time Franchise Win-Loss Bar Chart
- **Data Source**: `data/nl_all_time_records.csv`
- **Type**: Horizontal bar chart ordered by win percentage
- **Color**: Team primary colors
- **Insight**: Compare franchise durability and winning percentage across the century-plus landscape

### 2. Championship Timeline (Gantt-style)
- **Data Source**: `data/nl_championship_trends.csv`
- **Type**: Timeline/Gantt chart showing championship runs across eras
- **Insight**: Visualize eras of dominance (Braves 1991-2005, Dodgers 2017-2025)

### 3. Heatmap: Head-to-Head Records
- **Data Source**: `https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml`
- **Type**: Matrix heatmap (NL team vs NL team)
- **Insight**: Identify historical rivalries and dominance patterns

### 4. Season-by-Season Win-Loss Trends
- **Data Source**: SABR Lahman `Teams.csv` + season records
- **Type**: Line chart overlaying multiple franchises
- **Insight**: Track franchise trajectories through winning and losing cycles

### 5. Pennant/Championship Wind roses or Sankey diagrams
- **Data Source**: `data/nl_championship_trends.csv` + `nl_key_seasons.csv`
- **Type**: Flow diagram showing pennant flows to World Series outcomes
- **Insight**: Which pennant winners won the World Series vs. fell short

### 6. Division Dominance Over Time
- **Data Source**: `data/nl_recent_standings.csv` + historical divisions
- **Type**: Small multiples by division, showing which team led each decade
- **Insight**: How competitive balance has shifted across the NL East/West/Central

## Tools Suggestions

- **Python**: matplotlib, seaborn, plotly
- **R**: ggplot2, plotly
- **JavaScript**: D3.js, Chart.js
- **Dashboard**: Streamlit or Dash for interactive exploration

## Data File Inventory

| File | Description |
|------|-------------|
| `data/nl_all_time_records.csv` | All-time franchise W-L totals |
| `data/nl_key_seasons.csv` | Key individual season records & championships |
| `data/nl_recent_standings.csv` | Full recent standings (2020-2025) |
| `data/nl_championship_trends.csv` | Championship highlights organized by era |
| `data/nl_notable_records.csv` | Notable single-season and franchise records |
| `data/source_references.md` | Detailed source attribution |
