# Visualization Roadmap

This document outlines the planned visualizations and provides starter code for building interactive NL performance charts.

## Planned Visualizations

### 1. NL Championship Timeline
- Type: Interactive horizontal timeline
- Data: nl_pennant_winners.csv or nl_season_by_year.json
- Tool: Plotly or D3.js
- Description: Color-coded timeline showing each NL pennant winner from 1876 to present

### 2. Win-Loss Parity Chart
- Type: Scatter plot
- Data: nl_all_time_records.csv
- Tool: Matplotlib or Seaborn
- Description: Each dot represents an NL team; x-axis = losses, y-axis = wins

### 3. Era Dominance Heatmap
- Type: Heatmap
- Data: nl_pennant_winners.csv
- Tool: Seaborn or Plotly
- Description: Rows = eras, columns = teams, cell color = intensity of dominance

### 4. H2H Rivalry Network Graph
- Type: Network/force-directed graph
- Data: nl_team_vs_team_summary.csv
- Tool: NetworkX + Matplotlib or Plotly
- Description: Nodes = teams, edges = rivalry matchups, edge thickness = total games

### 5. Division Title Winners Bar Chart
- Type: Horizontal bar chart
- Data: research_data_supplement.json
- Tool: Matplotlib
- Description: Each bar shows total division titles for each team, grouped by division

### 6. Franchise Trajectory Sparklines
- Type: Faceted small multiples
- Data: Lahman Database (full season-by-season)
- Tool: Plotly or Matplotlib
- Description: Each small chart shows one team's season-by-season winning percentage

### 7. Single-Season Dominance
- Type: Bar chart
- Data: nl_notable_records.csv + Lahman Database
- Tool: Matplotlib
- Description: Top 10 NL single-season win totals, with year and team labeled

## Visualization File Structure

```
visualizations/
├── README.md
├── charts/          ← Generated chart images
├── notebooks/       ← Jupyter notebooks
└── scripts/         ← Python scripts
```

## Starter Code Examples

### Championship Timeline (Plotly)
```python
import pandas as pd
import plotly.express as px

pennants = pd.read_csv('data/nl_pennant_winners.csv')
fig = px.timeline(pennants, x_start='year', x_end='year', y='NL_champion',
                  color='NL_champion', title='NL Pennant Winners (1876-2025)')
fig.update_yaxes(categoryorder='total ascending')
fig.show()
```

### Win-Loss Parity Chart (Matplotlib)
```python
import pandas as pd
import matplotlib.pyplot as plt

records = pd.read_csv('data/nl_all_time_records.csv')
fig, ax = plt.subplots(figsize=(10, 7))
ax.scatter(records['losses'], records['wins'], s=records['games']/100, alpha=0.7)
for _, row in records.iterrows():
    ax.annotate(row['team'], (row['losses'], row['wins']), fontsize=8)
ax.set_xlabel('Losses')
ax.set_ylabel('Wins')
ax.set_title('NL Teams: Wins vs Losses (All-Time)')
plt.tight_layout()
plt.savefig('charts/win_loss_parity.png', dpi=150)
```

### Era Heatmap (Seaborn)
```python
import pandas as pd
import seaborn as sns

pennants = pd.read_csv('data/nl_pennant_winners.csv')
pennants['era'] = pd.cut(pennants['year'], 
    bins=[1875, 1900, 1920, 1940, 1960, 1980, 2000, 2015, 2026],
    labels=['1876-1900', '1901-1920', '1921-1940', '1941-1960', '1961-1980', '1981-2000', '2001-2015', '2016-2025'])
ct = pd.crosstab(pennants['era'], pennants['NL_champion'])
sns.heatmap(ct, cmap='YlOrRd', annot=True, fmt='d')
```