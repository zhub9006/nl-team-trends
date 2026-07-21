# Analysis Notebooks

This directory contains Jupyter notebooks for analysis and visualization of NL team trends data.

## Planned / Available Notebooks

| Notebook | Description |
|----------|-------------|
| `01_eda_nl_standings.ipynb` | Exploratory Data Analysis of NL seasonal standings (1876-2025) |
| `02_championship_trends.ipynb` | Championship heatmaps, dynasty timelines, eras analysis |
| `03_h2h_rivalries.ipynb` | Head-to-head rivalry visualizations and matrices |
| `04_win_percentage_trends.ipynb` | Win% distribution by era, team rankings, and cross-era comparisons |
| `05_dynamic_dashboards.ipynb` | Interactive Plotly/Streamlit dashboards |

## Setup

```bash
pip install -r requirements.txt
jupyter notebook
```

## Data Loading Template

```python
import pandas as pd

# Load all-time records
records = pd.read_csv('data/nl_all_time_records.csv')

# Load pennant winners
pennants = pd.read_csv('data/nl_pennant_winners.csv')

# Load seasonal standings
seasonal = pd.read_csv('data/nl_seasonal_standings.csv')

# Load H2H rivalries
h2h = pd.read_csv('data/nl_h2h_rivalries_detailed.csv')

# Load recent standings
recent = pd.read_csv('data/nl_recent_standings.csv')

print(f"Records loaded: {len(records)} teams")
print(f"Pennant data: {len(pennants)} seasons")
print(f"Seasonal data: {len(seasonal)} team-seasons")
```