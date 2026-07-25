# NL Team Trends — Visualization Roadmap

> A comprehensive guide to visualizing National League team performance data with Python code examples.

## Overview

This directory contains a roadmap for building interactive data visualizations and analysis notebooks for the NL Team Trends project. All code uses open-source Python libraries.

## Required Libraries

```bash
pip install -r ../requirements.txt
```

## Visualization Ideas & Implementation Guide

### 1. NL Pennant Winners Timeline (Choropleth/Timeline)

**What**: A timeline showing NL pennant winners by year, color-coded by franchise.

```python
import pandas as pd
import plotly.express as px

# Load pennant winners data
pennants = pd.read_csv('../data/nl_pennant_winners.csv')

# Create timeline
fig = px.scatter(pennants, x='Year', y='Team', color='Team',
                 size='W_L_Pct', hover_data=['W_L', 'WS_Result'],
                 title='NL Pennant Winners by Year (1876-2025)',
                 color_discrete_sequence=px.colors.qualitative.Set2)
fig.show()
```

### 2. H2H Win-Loss Heatmap

**What**: A 15×15 heatmap showing the H2H win-loss record between all NL teams.

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load H2H data
h2h = pd.read_csv('../data/nl_team_vs_team_summary.csv')

# Build matrix - use the full Baseball Almanac H2H data
# (This is a simplified version; the full 15x15 matrix is in the Baseball Almanac raw data)
 teams = sorted(h2h['Team_1'].unique())
matrix = np.zeros((len(teams), len(teams)))

for _, row in h2h.iterrows():
    i = teams.index(row['Team_1'])
    j = teams.index(row['Team_2'])
    # Team_1 Win% = T1_Wins / (T1_Wins + T2_Wins)
    matrix[i][j] = row['Team_1_Win_Pct'] if row['Team_1_Win_Pct'] != 'N/A' else 0.5

fig, ax = plt.subplots(figsize=(14, 12))
sns.heatmap(matrix, annot=True, fmt='.3f', xticklabels=teams,
            yticklabels=teams, cmap='RdYlGn', ax=ax,
            vmin=0, vmax=1)
ax.set_title('NL Team H2H Win Percentage Matrix (1876-2026)', fontsize=16)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('../charts/h2h_heatmap.png', dpi=150)
plt.show()
```

### 3. Franchise Win% Trajectory (Rolling 10-Year)

**What**: Each franchise's rolling 10-year win% over time to show dynasty cycles.

```python
import pandas as pd
import plotly.graph_objects as go

# Load historical performance
perf = pd.read_csv('../data/nl_historical_performance.csv')

# Add rolling 10-year win% (simulated with champion data)
# For full implementation, load the Lahman Database teams.csv for season-by-season data
fig = go.Figure()

# Sample dynasties to highlight
dynasties = {
    'Chicago Cubs': {'era': '1906-1910', 'color': '#0E3386'},
    'St. Louis Cardinals': {'era': '1926-1934, 1942-1946, 2006-2011', 'color': '#C41E3A'},
    'NY Giants': {'era': '1921-1924', 'color': '#3B2410'},
    'LA Dodgers': {'era': '2017-2025', 'color': '#005A9C'},
    'Atlanta Braves': {'era': '1991-2005', 'color': '#A71930'},
}

for team, info in dynasties.items():
    # Implement with full season-by-season data from Lahman DB
    fig.add_trace(go.Scatter(x=[], y=[], name=team, line=dict(color=info['color'])))

fig.update_layout(title='NL Dynasty Cycles: Rolling Win% by Franchise',
                  xaxis_title='Year', yaxis_title='Win Percentage',
                  template='plotly_white')
fig.show()
```

### 4. Era Comparison: Win% Distributions

**What**: Compare win% distributions across schedule eras (72-game, 154-game, 162-game).

```python
import pandas as pd
import plotly.express as px

# Categorize seasons by era
era_sizes = {
    '72-90G Era': range(1876, 1892),
    '100-130G Era': range(1892, 1901),
    '154G Era': range(1901, 1962),
    '162G Era': range(1962, 2020),
    'Shortened Era': [2020],
    'Full 162G (modern)': range(2021, 2026),
}

# Load and filter performance data
perf = pd.read_csv('../data/nl_historical_performance.csv')
perf['Era'] = perf['Year'].apply(
    lambda y: next((era for era, years in era_sizes.items() if y in years), 'Other')
)

fig = px.box(perf, x='Era', y='Champion_WPct', color='Era',
             title='NL Pennant-Winning Win% by Schedule Era',
             points='all')
fig.update_layout(showlegend=False)
fig.show()
```

### 5. Championship Drought Chart

**What**: Bar chart showing championship drought by franchise.

```python
import pandas as pd
import plotly.express as px

# Load franchise records
records = pd.read_csv('../data/nl_all_time_records.csv')

# Calculate droughts (years since last WS title)
from datetime import datetime
current_year = datetime.now().year
records['Years_Since_Last_WS'] = current_year - records['Last_WS_Title_Year'].fillna(0).astype(int)

fig = px.bar(records.sort_values('Years_Since_Last_WS', ascending=True),
             x='Team', y='Years_Since_Last_WS', color='Team',
             title='NL Championship Droughts (Years Since Last World Series Title)',
             labels={'Years_Since_Last_WS': 'Drought (Years)', 'Team': ''})
fig.add_hline(y=0, line_dash='dash', line_color='green',
              annotation_text='Most recent champions')
fig.show()
```

### 6. Division Dominance Stacked Area Chart

**What**: Stacked area chart showing division titles accumulated over time by franchise.

```python
import pandas as pd
import plotly.graph_objects as go

# This requires year-by-year division title data from Baseball-Reference
# Sample framework:
fig = go.Figure()

# NL East division title accumulation
division_data = {
    'NL East - Braves': [(1995, 1), (2000, 1), ..., (2025, 1)],  # 18 total
    'NL East - Phillies': [(1980, 1), ..., (2025, 1)],  # 13 total
    'NL Central - Cardinals': [...],  # 12 total
    'NL West - Dodgers': [...],  # 23 total
}

for team, data in division_data.items():
    cum_sum = 0
    xs, ys = [], []
    for year, increment in sorted(data):
        cum_sum += increment
        xs.append(year)
        ys.append(cum_sum)
    fig.add_trace(go.Scatter(x=xs, y=ys, name=team, fill='tozeroy'))

fig.update_layout(title='NL Division Titles Accumulated Over Time',
                  xaxis_title='Year', yaxis_title='Cumulative Division Titles',
                  template='plotly_white')
fig.show()
```

### 7. 23-Year Sliding Window Win% Comparison

**What**: Interactive bar chart comparing NL team win% over sliding 23-year windows.

```python
import pandas as pd
import plotly.express as px

# Load 23-year trend data
trends = pd.read_csv('../data/nl_recent_trends_2000_2024.csv')

fig = px.bar(trends.sort_values('Win_Pct', ascending=True),
             x='Team', y='Win_Pct', color='Team',
             title='NL Teams: 2000-2024 Win% (23-Year Window)',
             text='Wins'-'-'Losses',
             color_continuous_scale='RdYlGn')
fig.update_traces(textposition='outside')
fig.update_layout(showlegend=False)
fig.show()
```

### 8. H2H Rivalry Network Graph

**What**: A network graph showing the intensity and direction of H2H rivalries.

```python
import pandas as pd
import networkx as nx
import plotly.graph_objects as go

# Load H2H data
h2h = pd.read_csv('../data/nl_team_vs_team_summary.csv')

G = nx.DiGraph()

for _, row in h2h.iterrows():
    if row['Team_1_Win_Pct'] == 'N/A':
        continue
    t1, t2 = row['Team_1'], row['Team_2']
    wp = float(row['Team_1_Win_Pct'])
    G.add_edge(t1, t2, weight=abs(wp - 0.5) * 10)  # stronger edge = more lopsided

# Layout with spring algorithm
pos = nx.spring_layout(G, k=3, iterations=50)

edge_x, edge_y, edge_colors, edge_widths = [], [], [], []
for edge in G.edges(data=True):
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])
    edge_colors.append(abs(float(edge[2]['weight']) - 5))
    edge_widths.append(abs(float(row['Team_1_Win_Pct']) - 0.5) * 10 if row['Team_1_Win_Pct'] != 'N/A' else 1)

fig = go.Figure()
fig.add_trace(go.Scatter(x=edge_x, y=edge_y, mode='lines',
                         line=dict(width=edge_widths, color='lightgray'),
                         hoverinfo='none'))

for node in G.nodes():
    x, y = pos[node]
    fig.add_trace(go.Scatter(x=[x], y=[y], mode='markers+text',
                             marker=dict(size=20, color='#C41E3A'),
                             text=[node], textposition='top center',
                             hoverinfo='text'))

fig.update_layout(title='NL Team H2H Rivalry Network',
                  showlegend=False, template='plotly_white',
                  xaxis_showgrid=False, yaxis_showgrid=False)
fig.show()
```

## Recommended Visualization Stack

| Tool | Use Case | Install |
|------|----------|---------|
| **Plotly** | Interactive HTML charts, dashboards | `pip install plotly` |
| **Seaborn** | Static statistical charts | `pip install seaborn` |
| **Matplotlib** | Publication-quality static charts | `pip install matplotlib` |
| **NetworkX** | Rivalry network graphs | `pip install networkx` |
| **Streamlit** | Web dashboards | `pip install streamlit` |
| **D3.js** | Custom web visualizations | NPM |

## Notebook Structure (Planned)

```
notebooks/
├── 01_data_exploration.ipynb    — Load & explore all NL data files
├── 02_era_comparison.ipynb      — Compare performance across eras
├── 03_dynasty_analysis.ipynb    — Identify dynasty cycles & streaks
├── 04_rivalry_analysis.ipynb    — H2H rivalry deep dives
├── 05_visualization_dashboard.ipynb    — Interactive Plotly dashboard
└── 06_prediction_model.ipynb           — Simple predictive models for team performance
```

## Data Sources for Visualization

All chart data is sourced from the `data/` directory:
- `nl_all_time_records.csv` — Franchise-level records
- `nl_historical_performance.csv` — Year-by-year champion data
- `nl_pennant_winners.csv` — Complete pennant winners with WS results
- `nl_team_vs_team_summary.csv` — H2H rivalry summary
- `nl_recent_trends_2000_2024.csv` — 23-year window trends
- `nl_notable_records.csv` — Key single-season & franchise milestones
- `nl_championship_trends.csv` — Championship highlights by era
- `nl_recent_standings.csv` — Divisional standings 2020-2025
- `nl_season_standings_2025_2026.csv` — Latest season data

## Contributing Visualizations

To add a new visualization:
1. Create a new file in `visualizations/` following the naming pattern `viz_01_title.md`
2. Include: description, Python code, required data files, output description
3. Update this README with the new visualization entry
4. Run the notebook and verify outputs
5. Save static chart images to `../charts/` directory