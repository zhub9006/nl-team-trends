# Visualization Roadmap

Planned charts and visualization outputs for the NL Team Trends project.

## Planned Visualizations
- NL Wins by Season (multi-line time series)
- Win % Heatmap (decade × team)
- Pennant Winners Timeline (Gantt-style)
- Team-vs-Team H2H W-L Matrix (interactive 15×15 heatmap)
- Championship Frequency Bar Chart
- Championship Drought Visualization
- Era Comparison (grouped bar/line)
- Run Differential Over Time
- Division Dominance Stacked Area

## Tools
- matplotlib, seaborn, plotly (Python)
- ggplot2, dplyr (R)
- D3.js, Chart.js (JavaScript)

## Chart Naming
`charts/<year>-<chart_type>_<descriptor>.png`

## Quick Start
```bash
pip install -r requirements.txt
jupyter notebook notebooks/explore_nl_data.ipynb
python scripts/data_loader.py
```