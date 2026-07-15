# Visualization Roadmap

## Planned Visualizations

### 1. Franchise Win-Loss Bar Chart
- **Type**: Horizontal bar chart (sorted)
- **Data**: `data/nl_all_time_records.csv`
- **Shows**: All-time wins/losses per franchise
- **Tool**: Matplotlib / Seaborn / Plotly

### 2. Pennant Winners Timeline
- **Type**: Gantt-style timeline or strip plot
- **Data**: `data/nl_championship_trends.csv`
- **Shows**: Pennant winners by year, color-coded by team
- **Highlight**: 8-era color coding for dominance periods

### 3. World Series Wins by Team
- **Type**: Pie chart or treemap
- **Data**: `data/nl_all_time_records.csv` (WS_Titles column)
- **Shows**: NL teams' championship share vs. AL

### 4. Recent Standings Heatmap
- **Type**: Heatmap
- **Data**: `data/nl_recent_standings.csv`
- **Shows**: Division champion win-loss trends 2020–2025

### 5. Franchise Win%-Over-Time Line Chart
- **Type**: Multi-line chart (15 lines, one per franchise)
- **Data**: Season-by-season data (to be compiled)
- **Shows**: team strength trajectories across eras

### 6. Era Dominance Sunburst
- **Type**: Sunburst or nested pie
- **Data**: `data/nl_championship_trends.csv`
- **Shows**: Dominant team per era; sub-segments for key events

## Recommended Tools
| Tool | Use Case | Benefit |
|------|----------|---------|
| Python + Matplotlib | Static charts | Fine-grained control |
| Seaborn | Statistical viz | Beautiful defaults |
| Plotly / Dash | Interactive dashboards | Hover, zoom, filter |
| Streamlit | Web app | Quick to deploy |
| R + ggplot2 | Statistical graphics | Publication-quality |
| D3.js | Custom web viz | Maximum flexibility |

## Getting Started
```bash
# Clone the repo
git clone https://github.com/zhub9006/nl-team-trends.git
cd nl-team-trends

# Install dependencies (example with Python)
pip install matplotlib pandas seaborn plotly

# Run example notebook
jupyter notebook notebooks/01_exploratory_analysis.ipynb
```