# NL Team Trends - Visualization Roadmap

This file outlines planned visualizations and analysis for the NL Team Trends research project.

## Completed
- [x] All-time franchise records bar charts (Python/matplotlib)
- [x] Era-based championship comparison charts
- [x] Historical data CSVs compiled

## Planned
- [ ] Win-loss trend lines per franchise (1876-2025)
- [ ] Pennant/Win Heatmap by Era and Franchise
- [ ] Head-to-Head Matchup Matrix Heatmap
- [ ] Championship Drought Duration Chart
- [ ] Win% Distribution by Decade Histogram
- [ ] Interactive Dashboard (Plotly / Streamlit)
- [ ] Wild Card Era Analysis (1995-present)
- [ ] Divisional Realignment Impact
- [ ] Multi-Season Rolling Win Percentage

## Recommended Tools

| Task | Tool |
|------|------|
| Data Processing | Python pandas, R dplyr |
| Static Charts | matplotlib, seaborn, ggplot2 |
| Interactive | plotly, altair, bokeh |
| Dashboard | Streamlit, Dash |

## Getting Started
```bash
git clone https://github.com/zhub9006/nl-team-trends.git
cd nl-team-trends
pip install pandas matplotlib seaborn plotly
python notebooks/visualization_starter.py
```