# NL Team Trends — Visualization Roadmap

## 📊 Planned Visualizations

### Phase 1: Basic Charts (Quick Wins)
- [x] All-Time Franchise Win-Loss Bar Chart (fig1_alltime_win_pct.png)
- [x] Pennants vs WS Titles Bubble Chart (fig2_pennants_vs_ws.png)
- [x] Modern Era Win% Trend Lines (fig3_modern_win_trends.png)
- [x] Top 10 Teams by Avg Modern Win% (fig4_top10_avg_win.png)
- [x] Era Dominance Timeline (fig5_era_dominance.png)

### Phase 2: Advanced Visualizations
- [ ] Heatmap: Head-to-Head Records (NL team vs NL team)
- [ ] Championship Flow/Sankey Diagram (pennant → WS outcome)
- [ ] Pennant Distribution by Decade (histogram/stacked bar)
- [ ] Win% Distribution Histogram (all teams, all seasons)
- [ ] Linear Regression of Winning % Over Time
- [ ] Run Differential Over Time (if available in Lahman)

### Phase 3: Interactive Dashboards
- [ ] Streamlit App: Filters by team/era/era_label
- [ ] Plotly Dash: Interactive NL competitive balance chart
- [ ] D3.js: Custom head-to-head matrix heatmap
- [ ] Tableau Public: Export-friendly dashboard

### Phase 4: Advanced Research
- [ ] Cluster Analysis: Group similar franchise trajectories
- [ ] Autocorrelation: Is there momentum from year to year?
- [ ] Payroll vs Win% (if MLB salary data is integrated)
- [ ] Impact of division realignment on competitive balance
- [ ] Pre-emptive: NL East vs West vs Central — win% gap over time
- [ ] Wild Card era effect: Does winning the division increase WS odds?

## 🛠 Recommended Tools

| Tool | Use Case | Learning Curve |
|------|----------|----------------|
| Python + matplotlib | Publication-quality charts | Medium |
| Python + seaborn | Statistical visualizations | Medium |
| Python + plotly | Interactive web charts | Medium |
| Python + streamlit | Full dashboard app | Low-Medium |
| R + ggplot2 | Elegant statistical graphics | Medium |
| D3.js | Custom interactive web visualizations | High |
| Tableau Public | Quick exploratory dashboards | Low |
| Jupyter Notebooks | Iterative analysis & exploration | Low-Medium |

## 📐 Design Guidelines

1. **Color scheme**: Use MLB team colors where possible; otherwise, use a blues/red grayscale
2. **Axis scaling**: Always use equal scaling when comparing across eras (normalize by games played)
3. **Annotate special seasons**: Mark strike years, COVID, etc. with vertical lines
4. **Save high-res**: Always save at 300 DPI for papers, 150 DPI for web
5. **Paper format**: 16:9 for presentations, 4:3 for papers, 1:1 for square social posts

## 📂 Output Structure

```
visualizations/
├── fig1_alltime_win_pct.png          ← All-time bar chart
├── fig2_pennants_vs_ws.png           ← Bubble chart
├── fig3_modern_win_trends.png        ← Trend lines
├── fig4_top10_avg_win.png            ← Top 10 avg win%
├── fig5_era_dominance.png            ← Era Gantt chart
├── heatmap_head_to_head.png          ← Team-vs-team matrix
├── sankey_championship_flow.png      ← Pennant → WS
└── interactive_dashboard/            ← Streamlit/Dash app
```