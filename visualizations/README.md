# Visualization Roadmap

## Planned Visualizations

### 1. All-Time Franchise Win-Loss Bar Chart
- **Type**: Horizontal bar chart
- **X-axis**: Win percentage
- **Y-axis**: Franchise name
- **Insight**: Clear visual of which franchises have been most successful over time
- **Tool**: Plotly or Altair

### 2. Seasonal Standings Heatmap
- **Type**: Heatmap
- **Rows**: Seasons (years)
- **Columns**: NL teams
- **Color**: Win percentage (green = high, red = low)
- **Insight**: See competitive balance shift over decades; identify dynasties

### 3. Pennant Winners Timeline
- **Type**: Timeline / Gantt chart
- **Details**: Show which team won pennants each year, colored by team
- **Insight**: Visualize dominant eras and drought periods

### 4. Championship Drought Chart
- **Type**: Vertical bar chart
- **X-axis**: Years since last championship
- **Insight**: Highlight long-suffering franchises (Cubs, Phillies, Brewers)

### 5. Division Dominance Over Time
- **Type**: Stacked area chart
- **X-axis**: Years
- **Y-axis**: Win percentage by division
- **Insight**: See which divisions have been most competitive

### 6. Eras Comparison Radar Chart
- **Type**: Radar/spider chart
- **Axes**: Pennants, WS titles, win%, division titles, championship frequency
- **Insight**: Compare franchise profiles across eras

## Recommended Libraries
| Library | Use Case |
|---------|----------|
| Plotly | Interactive, web-ready charts |
| Altair | Declarative statistical visualization in Python |
| Matplotlib | Static publication-quality charts |
| Seaborn | Statistical heatmaps and distributions |
| Bokeh | Interactive dashboards |

## Data Flow
```
data/*.csv → notebooks/analysis.ipynb → visualizations/*.html
```

## Source Integration
- Download [Lahman Database](https://sabr.org/lahman-database/) for raw season-level data
- Cross-reference with `source_references.md` for attribution
