# NL Team Trends — Visualization Roadmap

This directory contains Python scripts, Jupyter notebooks, and configuration for building interactive data visualizations from the National League historical performance data.

## Planned Visualizations

### 1. Vanishing Win% — Franchise Win% Trajectory (Line Chart)
- **Description**: Rolling 10-year win% for each NL franchise over time
- **Data Source**: `data/nl_historical_performance.csv`
- **Library**: Plotly or Matplotlib
- **Insight**: Shows which franchises have sustained dominance vs. those with cyclical performance

### 2. H2H Heatmap (Correlation Matrix)
- **Description**: 15×15 heatmap of NL team head-to-head win percentages
- **Data Source**: `data/nl_team_vs_team_summary.csv` and Baseball Almanac full matrix
- **Library**: Seaborn or Plotly
- **Insight**: Reveals the most one-sided and most competitive rivalries

### 3. Championship Timeline (Timeline Chart)
- **Description**: NL pennant winners and WS champions by year, color-coded by franchise
- **Data Source**: `data/nl_pennant_winners.csv`
- **Library**: Plotly
- **Insight**: Shows championship clusters, droughts, and dynasty periods

### 4. Era Comparison (Box Plot)
- **Description**: Win% distributions across different schedule eras (60-game, 154-game, 162-game)
- **Data Source**: `data/nl_historical_performance.csv`
- **Library**: Matplotlib/Seaborn
- **Insight**: Highlights how scheduling affects competitive balance and record comparability

### 5. Dynasty Cycles (Stacked Area Chart)
- **Description**: Decade-by-decade championship concentration by franchise
- **Data Source**: `data/nl_pennant_winners.csv`
- **Library**: Plotly
- **Insight**: Shows which eras saw the most concentrated NL dominance

### 6. Championship Drought Bar Chart
- **Description**: Bar chart of years since last WS title for each NL franchise
- **Data Source**: `data/nl_all_time_records.csv`
- **Library**: Plotly
- **Insight**: Visualizes the Cubs' famous 108-year drought and current pending droughts

### 7. Division Dominance (Stacked Area Chart)
- **Description**: Stacked area of division titles over time by team within each division
- **Data Source**: `README.md` (division title leaders section)
- **Library**: Plotly
- **Insight**: Shows the Braves' NL East dominance and Dodgers' NL West run

### 8. 23-Year Sliding Window (Small Multiples)
- **Description**: Side-by-side win% rankings for 23-year spans, showing how rankings shift
- **Data Source**: `data/nl_recent_trends_2000_2024.csv`
- **Library**: Plotly
- **Insight**: Demonstrates how franchise performance varies over extended periods

## Getting Started

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Load the data:
```python
import pandas as pd
import json

# Load all-time records
records = pd.read_csv('data/nl_all_time_records.csv')

# Load pennant winners
pennants = pd.read_csv('data/nl_pennant_winners.csv')

# Load recent standings
standings = pd.read_csv('data/nl_recent_standings.csv')
```

3. Run visualization scripts (TBD — will be added as notebooks are created)