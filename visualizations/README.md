# NL Team Trends Visualization Guide

A practical guide for building data visualizations from the datasets in this repository.

---

## Available Datasets

| File | Description | Estimated Rows |
|------|------------|:--------------:|
| `data/nl_all_time_records.csv` | All-time franchise W-L records for all 15 NL teams | 15 |
| `data/nl_h2h_rivalries.csv` | Key H2H rivalry matchups (11 highest-profile rivalries) | 11 |
| `data/nl_pennant_and_ws_champions.csv` | NL pennant winners + WS champions from 1970 onward | ~56 |
| `data/nl_historical_seasons.csv` | Key historical seasons with context from 1876-2025 | 150+ |

---

## Chart Types to Build

| Chart | Description | Recommended Tool |
|-------|------------|:-----------------:|
| Franchise Win% Comparison | Horizontal bars showing all-time win% by team (min 5K games) | matplotlib / plotly |
| Era-Adjusted Win% | Grouped bar chart normalizing for different schedule lengths (154 vs 162 games) | pandas / matplotlib |
| Championship Drought Chart | Horizontal bars showing years since last WS title | matplotlib |
| NL World Series Winners | Heatmap/calendar showing NL winners by decade | matplotlib / seaborn / plotly |
| H2H Rivalry Network | Networkx/graph showing all NL team-vs-team rivalries | networkx + matplotlib |
| Division Title Stacked Bar | Which team dominates each division | matplotlib |
| Losing/ Winning Streak Histogram | Distribution of winning streaks per team | matplotlib |
| Franchise Relocation Map | Sankey diagram showing city changes | plotly |
| Pennant Race Timeline | Gantt-style timeline of division leads through each season | matplotlib / plotly |
| Competitive Era Streamgraph | Streamgraph showing NL competitive balance over time | matplotlib / bokeh |

---

## Quick-Start Examples

### 1. All-Time Wins Bar Chart

```python
import pandas as pd
import matplotlib.pyplot as plt

teams_df = pd.read_csv('data/nl_all_time_records.csv')
teams_df['wins_int'] = teams_df['wins'].astype(int)
teams_df = teams_df.sort_values('wins_int', ascending=True)

fig, ax = plt.subplots(figsize=(12, 7))
colors = ['#2c7bb6' if w > 10000 else '#fc8d59' for w in teams_df['wins_int']]
ax.barh(teams_df['team'], teams_df['wins_int'], color=colors)
ax.set_xlabel('All-Time Regular Season Wins')
ax.set_title('NL All-Time Regular Season Wins')
plt.tight_layout()
plt.savefig('nl_all_time_wins.png', dpi=150)
plt.show()
```

### 2. World Series Winners by Year

```python
import pandas as pd
import matplotlib.pyplot as plt

ws_df = pd.read_csv('data/nl_pennant_and_ws_champions.csv')
fig, ax = plt.subplots(figsize=(14, 5))
ws_df['is_nl_champ_ws'] = ws_df.apply(lambda r: r['ws_champion'] == r['nl_champion'] if pd.notna(r['ws_champion']) else False, axis=1)
ws_df['for_plot'] = ws_df['year'].astype(int)
ws_df['bar_color'] = ws_df['is_nl_champ_ws'].map({True: '#2c7bb6', False: '#d7191c'})
ws_df = ws_df.dropna(subset=['year'])

ax.bar(ws_df['for_plot'], [1]*len(ws_df), color=ws_df['bar_color'])
ax.set_xlabel('Year')
ax.set_ylabel('NL pennant-won World Series? NL-blue / AL-red')
ax.set_title('NL World Series Champion by Year')
ax.set_xticks(range(1970, 2030, 2))
plt.tight_layout()
plt.savefig('nl_ws_winners.png', dpi=150)
plt.show()
```

### 3. H2H Network Graph

```python
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

rival_df = pd.read_csv('data/nl_h2h_rivalries.csv')
G = nx.Graph()
for _, row in rival_df.iterrows():
    G.add_edge(row['team_1'], row['team_2'],
               weight=row['total_games'],
               win_pct=row['team_1_win_pct'])

pos = nx.spring_layout(G, k=2)
plt.figure(figsize=(12, 8))
nx.draw_networkx(G, pos, with_labels=True, node_size=800,
                 node_color='steelblue', font_size=8)
edges = nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.4)
plt.title('NL Rivalry Network')
plt.axis('off')
plt.tight_layout()
plt.savefig('nl_h2h_network.png', dpi=150)
plt.show()
```

### 4. Era-Adjusted Win%

```python
import pandas as pd
import matplotlib.pyplot as plt

teams = pd.read_csv('data/nl_all_time_records.csv')
teams['wins_int'] = teams['wins'].astype(int)
teams['games_int'] = teams['games'].astype(int)
teams['genuine_w_pct'] = teams['wins_int'] / teams['games_int']
teams = teams.sort_values('genuine_w_pct', ascending=True)

fig, ax = plt.subplots(figsize=(12, 7))
labels = ['red' if x<.50 else 'orange' if x<.515 else 'green' for x in teams['genuine_w_pct']]
ax.barh(teams['team'], teams['genuine_w_pct'], color=labels)
ax.axvline(x=0.50, color='black', linestyle='--')
ax.set_xlabel('Genuine all-time win% (regardless of schedule length)')
ax.set_title('NL All-Time Win% by Franchise')
plt.tight_layout()
plt.savefig('nl_consistency.png', dpi=150)
plt.show()
```

---

## Recommended Python Libraries

- **matplotlib** — Core plotting, highest quality output
- **seaborn** — Statistical visualization with nicer defaults
- **plotly / dash** — Interactive web-based visualization
- **bokeh** — Interactive browser-based charts
- **networkx** — Rivalry graph network visualizations
- **pandas** — Data manipulation, analysis and preparation for charting
- **numpy** — Numerical array operations
- **statsmodels** — Statistical tests and significance
- **scipy** — Additional statistical routines

---

## Output Folders

The recommended structure for the `visualizations/` directory:

```
visualizations/
├── outputs/          ← Generated static image files (.png, .svg, .html)
├── templates/        ← Reusable visualization functions/templates
└── README.md         ← This file
```

---

## Additional Product Ideas

1. **NL Pennant Race Flow Diagram** — Sankey-style visualization of division lead changes in key seasons.
2. **Franchise Relocation Map** — Interactive map showing team city changes over time.
3. **H2H Win% Matrix Heatmap** — 15x15 heatmap of all NL team-vs-team win percentages.
4. **NL Competitive Balance Over Time** — Line chart of win% standard deviation by year.
5. **Dynasty Identification** — Automated detection of periods where one team wins multiple titles.

---

> **This visualization guide is part of the NL Team Trends research project.** For discussion, see the GitHub issues page. Last updated: July 2026.
