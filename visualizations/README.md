# NL Visualizations Roadmap

This directory contains visualization plans, Python code, and Jupyter notebooks for exploring National League team trends.

## Planned Visualizations

### 1. Timeline of NL Pennant Winners
- **Type**: Timeline / Bar chart
- **Data**: `nl_pennant_winners.csv`
- **Tools**: Matplotlib / Plotly
- **Insights**: Shows franchise dominance cycles across eras

### 2. H2H Win-Loss Heatmap
- **Type**: Heatmap (15×15 matrix)
- **Data**: `nl_team_vs_team_summary.csv`
- **Tools**: Seaborn / Plotly
- **Insights**: Highlights lopsided rivalries like Cardinals vs. Pirates

### 3. Win% Trajectory by Franchise
- **Type**: Rolling 10-year win% line chart
- **Data**: `nl_historical_performance.csv`
- **Tools**: Pandas + Matplotlib
- **Insights**: Shows dynasty arcs and rebuild patterns

### 4. Era Comparison: Win% by Schedule Era
- **Type**: Box plot / Violin plot
- **Data**: `nl_historical_performance.csv` (categorized by era)
- **Tools**: Seaborn
- **Insights**: Compares team performance across 60/154/162-game eras

### 5. Championship Drought Chart
- **Type**: Horizontal bar chart
- **Data**: `nl_all_time_records.csv`
- **Tools**: Matplotlib
- **Insights**: Shows cumulative drought lengths by franchise

### 6. Division Dominance Stacked Area
- **Type**: Stacked area chart
- **Data**: `nl_pennant_winners.csv`, `nl_all_time_records.csv`
- **Tools**: Plotly
- **Insights**: Tracks NL division title concentration over time

### 7. 23-Year Sliding Window Win%
- **Type**: Line chart with slider
- **Data**: `nl_recent_trends_2000_2024.csv`
- **Tools**: Plotly (interactive)
- **Insights**: Shows sliding window win% for all 15 NL franchises

### 8. Rebuild vs. Dynasty Patterns
- **Type**: Scatter plot (games played vs. win%)
- **Data**: `nl_all_time_records.csv`
- **Tools**: ggplot2 / Python
- **Insights**: Identifies franchises with sustained success vs. short peaks

## Notebook Ideas

| Notebook | Description |
|----------|-------------|
| `01_all_time_records.ipynb` | All-time W-L analysis by franchise |
| `02_championship_cycles.ipynb` | NL championship patterns over eras |
| `03_h2h_rivalries.ipynb` | Team-vs-team win analysis |
| `04_era_comparison.ipynb` | Performance across schedule eras |
| `05_division_dominance.ipynb` | NL division title trends |
| `06_drought_analysis.ipynb` | Championship drought modeling |
| `07_sliding_window.ipynb` | 23-year sliding window win% |
| `08_rebuild_vs_dynasty.ipynb` | Franchise trajectory classification |

## Setup

```bash
pip install pandas numpy matplotlib seaborn plotly jupyter
```

## Quick Start

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load all-time records
df = pd.read_csv('data/nl_all_time_records.csv')

# Top 5 NL franchises by all-time wins
top5 = df[df['team'].isin([
    'San Francisco Giants', 'Los Angeles Dodgers', 'Chicago Cubs',
    'Atlanta Braves', 'St. Louis Cardinals'
])].sort_values('wins', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(data=top5, x='team', y='wins', palette='viridis')
plt.title('All-Time NL Franchise Win Totals')
plt.ylabel('Wins')
plt.xlabel('Franchise')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/nl_all_time_wins.png', dpi=150)
plt.show()
```