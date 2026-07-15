# Visualization Roadmap

## Planned Visualizations

### 1. All-Time Franchise Win-Loss Bar Chart
- **Data Source**: `nl_all_time_records.csv`
- **Type**: Horizontal bar chart ordered by win percentage
- **Insight**: Compare franchise durability and winning % across the century-plus landscape

### 2. Championship Timeline (Gantt-style)
- **Data Source**: `nl_championship_trends.csv`
- **Type**: Timeline/Gantt chart showing championship runs across eras
- **Insight**: Visualize eras of dominance (Braves 1991-2005, Dodgers 2017-2025)

### 3. Heatmap: Head-to-Head Records
- **Data Source**: Baseball Almanac team-vs-team matrix
- **Type**: Matrix heatmap (NL team vs NL team)
- **Insight**: Identify historical rivalries and dominance patterns

### 4. Season-by-Season Win-Loss Trends
- **Data Source**: SABR Lahman + season records
- **Type**: Line chart overlaying multiple franchises
- **Insight**: Track franchise trajectories through winning and losing cycles

### 5. Pennant/Championship Flow Diagram
- **Data Source**: `nl_championship_trends.csv` + `nl_key_seasons.csv`
- **Type**: Sankey/flow diagram showing pennant flows to WS outcomes
- **Insight**: Which pennant winners won the World Series vs. fell short

### 6. Division Dominance Over Time
- **Data Source**: `nl_recent_standings.csv` + historical divisions
- **Type**: Small multiples by division, showing which team led each decade
- **Insight**: How competitive balance has shifted across NL East/West/Central

## Tools Suggestions

- **Python**: matplotlib, seaborn, plotly
- **R**: ggplot2, plotly
- **JavaScript**: D3.js, Chart.js
- **Dashboard**: Streamlit or Dash for interactive exploration
