# NL Team Trends — Analysis Notebooks

## Overview
This directory is planned for Jupyter notebooks that perform systematic analysis of the NL historical performance data.

## Planned Notebooks

### 1. `01_nl_all_time_analysis.ipynb`
**Goal**: Load and explore the all-time franchise records
**Data**: `data/nl_all_time_records.csv`
**Key Questions**:
- Which franchise has the highest winning percentage with 1500+ games?
- What is the correlation between WS titles and regular-season wins?
- How have franchise sizes (games played) grown over time?

### 2. `02_nl_era_analysis.ipynb`
**Goal**: Analyze NL performance by era
**Data**: `data/nl_team_era_performance.json`, `data/nl_pennant_winners.csv`
**Key Questions**:
- How does era schedule length affect record comparison?
- Which era produced the most dominant single-season records?
- How has competitive balance changed across eras?

### 3. `03_h2h_rivalry_analysis.ipynb`
**Goal**: Analyze head-to-head rivalry data
**Data**: `data/nl_team_vs_team_summary.csv`, `data/nl_research_data_supplement.json`
**Key Questions**:
- Which rivalries are most one-sided historically?
- How have H2H win percentages shifted over time for key matchups?
- What correlations exist between H2H dominance and pennants?

### 4. `04_nl_recent_trends.ipynb`
**Goal**: Analyze NL trends from 2000–2025
**Data**: `data/nl_recent_standings.csv`, `data/nl_recent_championships.csv`
**Key Questions**:
- Has the NL become more or less competitive since 2000?
- Which teams have the longest active postseason droughts?
- How does Dodger dominance compare to historical patterns?

### 5. `05_nl_dynasty_detection.ipynb`
**Goal**: Identify and quantify dynasty periods
**Data**: `data/nl_pennant_winners.csv`, `data/nl_team_era_performance.json`
**Key Questions**:
- What defines a dynasty in the NL context?
- How do the Cardinals, Dodgers, and Braves dynasty periods compare?
- Can we detect dynasty shifts before they become obvious?

## Getting Started

### Setup
```bash
pip install -r ../requirements.txt
pip install jupyterlab ipykernel
```

### Run a Notebook
```bash
jupyter notebook 01_nl_all_time_analysis.ipynb
```

### Data Loading Template
```python
import pandas as pd
import json

# CSV files
records = pd.read_csv('../data/nl_all_time_records.csv')
pennants = pd.read_csv('../data/nl_pennant_winners.csv')
recent = pd.read_csv('../data/nl_recent_standings.csv')

# JSON files
era_data = json.load(open('../data/nl_team_era_performance.json'))
season_data = json.load(open('../data/nl_season_by_year.json'))

# Quick summary
print(f"Total NL franchises (with historical): {len(records)}")
print(f"Earliest season: {pennants['year'].min()}")
print(f"Latest season: {pennants['year'].max()}")
print(f"Total data points (pennant years): {len(pennants)}")
```