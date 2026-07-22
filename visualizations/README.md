# NL Team Trends — Visualization Roadmap & Notebooks

## Purpose

This directory contains planned data visualizations and analysis notebooks for the NL team trends research project. Visualizations are designed to reveal team performance patterns, era-specific trends, franchise trajectories, and rivalry dynamics across the full history of the National League from 1876 to present. **Updated with comprehensive research data and Python code examples.**

## Dependencies

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
```

## Data Files Used

| File | Purpose | Rows |
|------|---------|------|
| `data/nl_all_time_records.csv` | All-time franchise records | 15 teams |
| `data/nl_pennant_winners.csv` | Season-by-season pennant winners | ~150 seasons |
| `data/nl_championship_trends.csv` | Championship results by era | ~150 seasons |
| `data/nl_historical_performance.csv` | Season-by-season team standings | ~500+ key seasons |
| `data/nl_notable_records.csv` | Single-season & franchise records | ~22 records |
| `data/nl_recent_standings.csv` | Divisional standings 2014-2025 | ~12 years × 15 teams |
| `data/nl_team_vs_team_summary.csv` | H2H W-L summary matrix | 11 key rivalries |
| `data/nl_season_by_year.json` | Complete season-by-season data | 150 seasons |
| `data/research_data_supplement.json` | Extra research data (H2H, division titles, records) | Multiple sections |

---

## Planned Visualizations

### 1. NL All-Time Franchise Win-Loss Comparison

```python
def plot_all_time_win_pct():
    """Horizontal bar chart comparing all-time NL franchise winning percentages."""
    import pandas as pd
    df = pd.read_csv('data/nl_all_time_records.csv')
    df = df.sort_values('win_pct', ascending=True)

    fig, ax = plt.subplots(figsize=(12, 8))
    colors = ['#c0392b' if ws >= 5 else '#2980b9' if ws >= 2 else '#7f8c8d' for ws in df['ws_titles']]
    ax.barh(df['team'], df['win_pct'], color=colors, edgecolor='white')
    ax.set_xlabel('All-Time Winning Percentage')
    ax.set_title('NL All-Time Franchise Win % (color-coded by World Series titles)')
    ax.axvline(x=0.500, color='black', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig('visualizations/nl_all_time_win_pct.png', dpi=150)
    plt.show()
```

### 2. NL Pennant Winners Timeline / Heatmap

```python
def plot_pennant_timeline():
    """Heatmap showing NL pennant winners by year, grouped by decade."""
    import pandas as pd
    df = pd.read_csv('data/nl_pennant_winners.csv')

    # Create decade columns
    df['decade'] = (df['year'] // 10) * 10
    pivot = df.groupby(['decade', 'NL_champion']).size().unstack(fill_value=0)

    fig, ax = plt.subplots(figsize=(16, 10))
    sns.heatmap(pivot, annot=True, fmt='d', cmap='YlOrRd', ax=ax)
    ax.set_title('NL Pennant Winners by Decade')
    ax.set_xlabel('Winning Team')
    ax.set_ylabel('Decade')
    plt.tight_layout()
    plt.savefig('visualizations/nl_pennant_timeline.png', dpi=150)
    plt.show()
```

### 3. Team Win-Loss Trends Over Time (Small Multiples)

```python
def plot_team_win_trends():
    """Faceted small-multiple line charts by team showing winning percentage."""
    import pandas as pd
    df = pd.read_csv('data/nl_historical_performance.csv')

    # Only top franchises
    top_teams = ['St. Louis Cardinals', 'LA Dodgers', 'SF Giants',
                 'Cincinnati Reds', 'Pittsburgh Pirates', 'Atlanta Braves',
                 'Chicago Cubs', 'NY Mets', 'Philadelphia Phillies']
    df = df[df['team'].isin(top_teams)]

    g = sns.FacetGrid(df, col='team', col_wrap=3, height=4, sharey=False)
    g.map(sns.lineplot, 'year', 'win_pct', marker='o', markersize=4, linewidth=1.5)
    g.set_titles("{col_name}")
    g.set_axis_labels("Season", "Win %")
    g.add_legend()
    plt.tight_layout()
    plt.savefig('visualizations/nl_team_win_trends.png', dpi=150)
    plt.show()
```

### 4. Championship Era Dominance Heatmap

```python
def plot_era_dominance():
    """Heatmap showing era-by-era championship landscape."""
    import pandas as pd
    df = pd.read_csv('data/nl_championship_trends.csv')

    # Aggregate by era
    era_counts = df.groupby(['era', 'NL_champion']).size().unstack(fill_value=0)

    fig, ax = plt.subplots(figsize=(14, 8))
    sns.heatmap(era_counts.T, annot=True, fmt='d', cmap='RdPu', ax=ax)
    ax.set_title('NL Championship Landscape by Era')
    ax.set_xlabel('Era')
    ax.set_ylabel('Winning Team')
    plt.tight_layout()
    plt.savefig('visualizations/nl_era_dominance.png', dpi=150)
    plt.show()
```

### 5. H2H Rivalry Comparison

```python
def plot_h2h_rivalries():
    """Diverging bar chart comparing head-to-head winning percentages."""
    import pandas as pd
    df = pd.read_csv('data/nl_team_vs_team_summary.csv')
    df['edge'] = df['t1_wins'] - df['t2_wins']
    df['t1_pct'] = df['t1_wins'] / (df['t1_wins'] + df['t2_wins'])

    df = df.sort_values('t1_pct', ascending=True)

    fig, ax = plt.subplots(figsize=(12, 8))
    colors = ['#e74c3c' if pct < 0.45 else '#2ecc71' if pct > 0.55 else '#3498db'
              for pct in df['t1_pct']]
    labels = [f"{row['team1']} vs {row['team2']}" for _, row in df.iterrows()]

    ax.barh(labels, df['t1_pct'], color=colors, edgecolor='white')
    ax.set_xlabel('Team 1 Winning Percentage')
    ax.set_title('NL Head-to-Head Rivalry Win %')
    ax.axvline(x=0.500, color='black', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('visualizations/nl_h2h_rivalries.png', dpi=150)
    plt.show()
```

### 6. World Series Championships by Team (Donut Chart)

```python
def plot_ws_titles():
    """Donut chart showing NL World Series titles by franchise."""
    import pandas as pd
    df = pd.read_csv('data/nl_all_time_records.csv')
    df = df[df['ws_titles'] > 0].sort_values('ws_titles', ascending=False)

    fig, ax = plt.subplots(figsize=(10, 8))
    colors = ['#c0392b', '#e74c3c', '#f39c12', '#2ecc71', '#2980b9',
              '#8e44ad', '#1abc9c', '#d35400', '#2c3e50', '#7f8c8d',
              '#34495e', '#16a085']

    wedges, texts, autotexts = ax.pie(
        df['ws_titles'],
        labels=df['team'],
        autopct='%1.0f%%',
        colors=colors,
        startangle=90,
        pctdistance=0.85,
        wedgeprops={'width': 0.5}
    )
    ax.set_title('NL World Series Championships by Team')
    centre_circle = plt.Circle((0, 0), 0.40, fc='white')
    fig.gca().add_artist(centre_circle)
    plt.tight_layout()
    plt.savefig('visualizations/nl_ws_titles.png', dpi=150)
    plt.show()
```

### 7. Single-Season Dominance Bar Chart

```python
def plot_best_seasons():
    """Horizontal bar of top NL single-season winning percentages."""
    import pandas as pd, json
    with open('data/nl_season_by_year.json') as f:
        data = json.load(f)

    # Extract NL season records filtered by NL teams
    nl_records = []
    for season in data['seasons']:
        # Filter for NL championships / dominant performances
        if 'win_pct' in season and isinstance(season['win_pct'], (int, float)):
            if season['win_pct'] >= 0.680:  # top 10%
                nl_records.append(season)

    df = pd.DataFrame(nl_records)
    df = df.sort_values('win_pct', ascending=True)

    fig, ax = plt.subplots(figsize=(14, 10))
    ax.barh(df['year'].astype(str) + ' — ' + df.get('champion', ''), df['win_pct'],
            color='#2980b9', edgecolor='white')
    ax.set_xlabel('Win Percentage')
    ax.set_title('Top NL Single-Season Dominance (W-L ≥ .680)')
    ax.axvline(x=0.500, color='black', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig('visualizations/nl_best_seasons.png', dpi=150)
    plt.show()
```

---

## Planned Jupyter Notebooks

| Notebook | Description | Difficulty |
|----------|-------------|------------|
| `notebooks/01_nl_overview.ipynb` | All-time franchise overview & summary stats | Beginner |
| `notebooks/02_nl_pennant_timeline.ipynb` | Pennant winners timeline & era analysis | Beginner |
| `notebooks/03_nl_win_trends.ipynb` | Team win/loss trends over time (small multiples) | Intermediate |
| `notebooks/04_nl_h2h_rivalries.ipynb` | Head-to-head rivalry analysis & visualization | Intermediate |
| `notebooks/05_nl_dynasties_droughts.ipynb` | Dynasty identification & championship drought analysis | Advanced |
| `notebooks/06_nl_championship_model.ipynb` | Statistical modeling of championship predictors | Advanced |
| `notebooks/07_nl_interactive_dashboard.ipynb` | Plotly interactive dashboard with all views | Intermediate |

## Notable Visual Ideas

### Championship Cycle Model
- **Sankey diagram** showing franchise success flow over eras
- **Network graph** of NL pennant winners by decade showing shifts
- **Arrow charts** for seasonal rank changes

### Best Seasons
- **Dot plot** of top NL seasons (1906 Cubs 116-36, 1909 Pirates 110-42, etc.)
- **Season-length adjusted model** differentiating 60-, 154-, and 162-game seasons

### Future Research
- **Win probability added (WPA)** by team per decade
- **WAR win estimates** for pre-1900 NL seasons
- **Pitcher vs hitter era** line graphs tracking league averages

---

## Recommended Tools

| Tool | Use Case | Complexity |
|------|----------|------------|
| Python (pandas + matplotlib/seaborn) | Static charts for papers, docs | Low |
| Python (plotly) | Interactive web charts | Low |
| R (ggplot2) | Statistical approach; academic papers | Medium |
| D3.js | Custom interactive web visualizations | High |
| Tableau / PowerBI | Business intelligence dashboards | Medium |

## Data Source Links

- [Lahman Baseball Database](https://sabr.org/lahman-database/) — free CSV download
- [Baseball-Reference (NL)](https://www.baseball-reference.com/leagues/NL/) — official standings & stats
- [Baseball Data Hub](https://baseballdatahub.com/seasons/) — browsable season-by-season data
- [Baseball Almanac](https://www.baseball-almanac.com/yearmenu.shtml) — historical summaries by year
- [Champs or Chumps](https://champsorchumps.us/mlb) — NL records, streaks, droughts
- [Linger & Look](https://lingerandlook.com/Names/BaseballStandings.php) — Year-by-year standings

## Contribution Guide

To add a new visualization:
1. Create a new file in this directory (e.g., `viz_01_franchise_win_pct.py`)
2. Include the data source, chart type, and key insights in comments
3. Add any output charts as PNG or SVG files in `/charts` subdirectory
4. Update this README with a description of the new visualization
