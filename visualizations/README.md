# Visualization Roadmap

Planned charts and visualization outputs for the NL Team Trends project.

## Planned Visualizations

### Core Charts
- **NL Wins by Season** (multi-line time series) — Track franchise performance across eras
- **Win% Heatmap** (decade × team) — Identify dominant periods for each franchise
- **Pennant Winners Timeline** (Gantt-style) — Visualize championship streaks and gaps
- **Team-vs-Team H2H W-L Matrix** (interactive 15×15 heatmap) — Rivalry intensity mapping
- **Championship Frequency Bar Chart** — Pennant counts and WS titles per team
- **Championship Drought Visualization** — Length of droughts (108-year Cubs drought, etc.)
- **Era Comparison** (grouped bar/line) — Compare team performance across decades
- **Run Differential Over Time** — Year-by-year NL run differential trends
- **Division Dominance** (stacked area chart) — Visualize division control over time

### Advanced Charts
- **Shortened-Season vs Full-Season Win%** (bar chart) — 2020 COVID season comparison
- **H2H Head-to-Head Heatmap** (matrix) — Dodgers vs Cubs (.695), Cardinals vs Cubs, etc.
- **NL West Dominance** (timeline) — 8 straight NL West titles (2018-2025 Dodgers)
- **Franchise Relocation Impact** (before/after) — Brooklyn → LA, NY Giants → SF
- **Expansion Team Trajectory** — Marlins, Rockies, D-backs, Marlins win curves
- **Championship Drought Bar Chart** — Years since last WS title
- **Pythagorean Win Expectation vs Actual** — Scoring efficiency vs results
- **Divisional W-L Trend** — East/Central/West win% over time
- **Manager Tenure Impact** — Win% by manager decade overlap

### Interactive Dashboards (Plotly/Dash)
- Full NL Standings Explorer (1876-2026)
- H2H W-L Matrix (15×15 interactive heatmap)
- Championship Drought Tracker
- Seasonal Win% Comparison Tool

## Tools
- **matplotlib, seaborn, plotly** (Python) — Static and interactive charts
- **ggplot2, dplyr** (R) — Statistical visualization
- **D3.js, Chart.js** (JavaScript) — Web-based interactive dashboards
- **Pandas** (Python) — Data manipulation and aggregation

## Chart Naming Convention
`charts/<year>-<chart_type>_<descriptor>.png`

Example: `charts/2025-win_pct_by_franchise.png`

## Quick Start
```bash
pip install -r requirements.txt
jupyter notebook notebooks/explore_nl_data.ipynb
python scripts/data_loader.py
```

## Key Metrics for Visualization
1. **Win% by Decade** — Grouped bar chart of NL team winning percentages by decade
2. **Pennant Timeline** — Horizontal bar chart showing pennant wins per team over time
3. **H2H Heatmap** — 15×15 heatmap of head-to-head win totals (all 105 pairs)
4. **Era Dominance** — Stacked/ annotation chart showing championship cycles
5. **Trend Lines** — Multi-line chart of team winning % over time (1876-2026)
6. **Drought Map** — Time since last WS title per team, sorted
7. **Division Hierarchy** — Heatmap of division winners by year
8. **Relocation Impact** — Before/after franchise relocation performance
9. **Expansion Trajectory** — Win% trajectory for 1993+ expansion teams
10. **Pythagorean W-L** — Exp. W-L vs Actual W-L across seasons