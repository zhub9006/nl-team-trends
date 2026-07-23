# NL Team Trends - Visualization & Analytics Roadmap

This directory contains the visualization plan and starter code for generating charts and dashboards from the NL historical performance data.

## Purpose

Transform the compiled NL data into insightful visual narratives about team dominance, era transitions, and rivalry patterns in National League baseball (1876–2025).

## Visualization Ideas

### 1. Franchise Win-Loss Bar Chart
Grouped horizontal bar chart of all-time NL franchise wins and losses.

```python
import pandas as pd
import matplotlib.pyplot as plt

records = pd.read_csv('../data/nl_all_time_franchise_records.csv')
records_sorted = records.sort_values('wins', ascending=True)

fig, ax = plt.subplots(figsize=(12, 8))
colors = ['#E31837' if x == 'Los Angeles Dodgers' else '#005A9C' if x == 'San Francisco Giants' else '#C41E3A' if x == 'St. Louis Cardinals' else '#2C2C54' for x in records_sorted['team']]
bars = ax.barh(records_sorted['team'], records_sorted['wins'], color=colors, edgecolor='white')
ax.set_xlabel('Total Wins')
ax.set_title('All-Time NL Regular-Season Franchise Wins (through 2025)')
plt.tight_layout()
plt.savefig('nl_all_time_wins.png', dpi=150)
plt.show()
```

### 2. Win % by Era (Box Plot)
Show NL champion win percentages grouped by era. Highlights how dominant eras produced extreme .700+ champions vs. recent low-.550 champions.

### 3. Championship Drought Timeline
Heatmap or Gantt-style interval chart showing years since each franchise's last World Series title.

### 4. H2H Rivalry Heat Map
Seaborn heatmap of the NL team-vs-team win-loss matrix — reveals which rivalries are most lopsided.

### 5. Division Titles Over Time
Stacked area/bar chart showing division titles won by franchise per decade.

### 6. NL Pennant Winners by Year
Faceted bar chart or chord diagram showing pennant winners by era.

### 7. Single-Season Dominance Scatter
Scatter plot of each NL champion's W-L record by season, highlighting outliers like the 1906 Cubs.

### 8. Interactive Dashboard (Plotly/Dash)
Interactive time-series with dropdown selectors for teams and tooltip hover for season details.

## Data Files Used

| File | Description |
|------|-------------|
| `../data/nl_all_time_franchise_records.csv` | All-time franchise records (15 NL teams) |
| `../data/nl_historical_performance.csv` | Key season performances (27 seasons)\ |
| `../data/nl_team_vs_team_summary.csv` | H2H rivalry summary (20 key matchups) |
| `../data/nl_recent_standings.csv` | Divisional standings 2018–2025 |
| `../data/nl_recent_championships.csv` | Recent championship results 2015–2025 |
| `../data/season_by_year_sample.json` | Comprehensive JSON with era definitions |
| `../data/nl_notable_records.csv` | Key records and milestones |
| `../data/nl_division_title_leaders.csv` | Division title leaders by division |

## Quick Start

```bash
cd ..
pip install -r docs/requirements.txt
python charts/visualize_wins.py
```

## Additional Recommended Data Sources
- SABR Lahman Database (CSV)
- Baseball-Reference API
- StatMuse / ESPN