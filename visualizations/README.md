# Visualization Roadmap

## Planned Visualizations for NL Team Trends

This directory will house all analysis notebooKS, scripts, and output visualizations.

---

## 1. Win-Loss Trend Lines by Franchise (1876–2025)
- **Type:** Multi-line chart
- **Data Source:** nl_historical_performance_detailed.csv, nl_all_time_records.csv
- **Tool:** matplotlib / plotly
- **Goal:** Show franchise power curves; highlight dominant eras

## 2. Pennant Count Bar Chart by Franchise
- **Type:** Horizontal bar chart
- **Data Source:** nl_all_time_records.csv
- **Tool:** matplotlib / seaborn
- **Goal:** Compare pennant totals across all 15 NL franchises

## 3. World Series Timeline Heatmap
- **Type:** Heatmap (teams × years)
- **Data Source:** nl_historical_performance_detailed.csv, nl_pennant_winners_recent.csv
- **Tool:** plotly
- **Goal:** Visualize WS appearances and results by franchise

## 4. Championship Drought Duration Chart
- **Type:** Bar chart + timeline
- **Data Source:** nl_historical_performance_detailed.csv
- **Tool:** matplotlib
- **Goal:** Compare championship droughts (Cubs 108 years vs others)

## 5. Era-Based Win% Distribution
- **Type:** Histogram + KDE
- **Data Source:** nl_historical_performance_detailed.csv
- **Tool:** matplotlib / seaborn
- **Goal:** Show how winning margins have changed across eras

## 6. Head-to-Head Matchup Matrix Heatmap
- **Type:** Matrix heatmap
- **Data Source:** nl_team_v_team_wl.csv (future)
- **Tool:** seaborn
- **Goal:** Visualize NL team-vs-team historical dominance

## 7. Division Championship Timeline
- **Type:** Sankey diagram or alluvial chart
- **Data Source:** nl_historical_performance_detailed.csv
- **Tool:** plotly
- **Goal:** Show how pennant power shifted between teams and divisions

## 8. Run Differential Analysis by Era
- **Type:** Scatter plot / box plot
- **Data Source:** nl_historical_performance_detailed.csv (future)
- **Tool:** matplotlib
- **Goal:** Correlate run differential with championships

## 9. Interactive Dashboard
- **Type:** Web dashboard
- **Data Source:** All CSVs
- **Tool:** Plotly Dash or Streamlit
- **Goal:** Interactive exploration of NL trends

## 10. Machine Learning: Pennant Prediction
- **Type:** Classification / regression model
- **Data Source:** Future expanded dataset with batting/pitching stats
- **Tool:** scikit-learn
- **Goal:** Predict pennant winners based on seasonal statistics

---

## Recommended Tools

| Tool | Use Case |
|------|----------|
| matplotlib | Static charts, publication-ready figures |
| seaborn | Statistical visualizations, heatmaps, distributions |
| plotly | Interactive charts, dashboards, 3D plots |
| pandas | Data loading, wrangling, aggregation |
| numpy | Numerical computations |
| jupyter | Interactive notebook environment |

## File Naming Convention
- `viz_{name}.py` — Python script for a specific visualization
- `viz_{name}.html` — HTML output from plotly (if interactive)
- `viz_{name}.png` / `.svg` — Static image output
- `notebooks/{name}.ipynb` — Jupyter notebook with analysis

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/zhub9006/nl-team-trends.git
cd nl-team-trends

# Install dependencies
pip install -r requirements.txt

# Run a visualization script
python viz_pennant_bars.py

# Launch interactive dashboard
streamlit run dashboards/main_dashboard.py
```