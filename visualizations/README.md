# NL Team Trends Visualizations

Visualizations for NL historical performance analysis. See `../docs/data_notes.md` for methodology.

## Available Data Files

| Data File | Description | Rows |
|-----------|-------------|------|
| `../data/nl_all_time_records.csv` | All-time franchise W-L records by team | 16 |
| `../data/nl_key_seasons.csv` | Key individual season standings | 204+ |
| `../data/nl_pennant_winners_recent.csv` | NL pennant winners 1995–2025 | 32 |
| `../data/nl_recent_standings.csv` | Full standings 2020–2025 | 64+ |
| `../data/nl_championship_trends.csv` | Championship highlights by era | 30+ |
| `../data/nl_notable_records.csv` | Aggregated records & milestones | 25+ |

## Planned Visualizations

| Plot | Description | Data Source | Tool |
|------|-------------|-------------|------|
| franchise_win_trajectory.png | Win% by decade per franchise (line chart) | nl_all_time_records.csv + nl_recent_standings.csv | Python/Matplotlib |
| pennant_frequency_heatmap.png | Pennant per decade grid (teams × decade) | nl_pennant_winners_recent.csv | Python/Seaborn |
| division_balance.png | Win% distribution strip chart by division | nl_recent_standings.csv | R/ggplot2 |
| h2h_network.png | Team-vs-team W-L network (edge weights = H2H) | From Baseball Almanac | NetworkX/Plotly |
| expansion_ramp.png | New franchise adjustment 7-10 year curves | nl_all_time_records.csv | Python/Matplotlib |
| run_diff_vs_pennant.png | Run differential vs pennant success | nl_key_seasons.csv | Python/Seaborn |
| elo_ratings_evolution.png | Cumulative Elo ratings across decades | nl_championship_trends.csv | PyElo/Matplotlib |
| home_away_splits.png | Home vs Away win% by era (bar chart) | nl_recent_standings.csv | Python/Matplotlib |
| championship_timeline.png | NL WS winners timeline 1876-2025 | nl_championship_trends.csv | Python/Plotly |
| era_comparison.png | Win% & pennants by era (grouped bar) | nl_championship_trends.csv | Python/Seaborn |
| record_breakdown.png | Single-season records by franchise (horizontal bar) | nl_notable_records.csv | Python/Matplotlib |

## Quick Start

```bash
cd visualizations
pip install matplotlib pandas numpy seaborn plotly
python franchise_win_trajectory.py
```

Each script reads from `../data/*.csv` and writes to `./output/`.

## Sample Analysis Script

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load key data
records = pd.read_csv('../data/nl_all_time_records.csv')
trends = pd.read_csv('../data/nl_championship_trends.csv')

# Top 5 franchises by win percentage
top5 = records.nlargest(5, 'Win_Pct')
print(top5[['Franchise', 'Win_Pct', 'Wins', 'Losses', 'WS_Titles']])
```