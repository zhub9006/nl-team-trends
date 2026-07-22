# NL Team Trends — Quick Start Guide

## Overview

Welcome to the NL Team Trends research hub! This repository contains comprehensive historical National League (NL) team performance data, win-loss records, pennant winners, division champions, World Series championships, and era-specific trends — from the NL's founding in 1876 through today. This guide will get you started.

## Quick Stats at a Glance

| Metric | Leader | Value |
|--------|--------|-------|
| NL Pennants | LA Dodgers | 26 |
| NL World Series Titles | St. Louis Cardinals | 11 |
| Most NL Regular-Season Wins | San Francisco Giants | 11,663 |
| Highest NL Win % (1500+ games) | LA Dodgers / SF Giants | .532-.535 |
| Biggest Single-Season Dominance | 1906 Chicago Cubs | 116–36 (.763) |
| Longest NL Championship Drought | Chicago Cubs | 108 years (1908–2016) |
| Longest NL Dynasty | Atlanta Braves | 14 straight division titles (1991–2005) |
| Most NL Consecutive Pennants | Boston Braves | 7 (1891–1898 - Original) |
| NL Franchise with Most Games | Chicago Cubs | 22,513 |

## Repository Structure

```
nl-team-trends/
├── README.md                          ← Overview & research summary
├── DATA_INDEX.md                      ← Data file descriptions & column definitions
├── source_references.md               ← Detailed source attribution
├── requirements.txt                   ← Python dependencies
├── data/
│   ├── nl_all_time_records.csv        ← All-time franchise records (W/L, pennants, WS)
│   ├── nl_pennant_winners.csv         ← Complete NL pennant winners 1876-2025
│   ├── nl_championship_trends.csv     ← Championship highlights by era
│   ├── nl_historical_performance.csv  ← Season-by-season standings (key seasons)
│   ├── nl_notable_records.csv         ← Key single-season & franchise records
│   ├── nl_recent_standings.csv        ← Divisional standings 2014-2025
│   ├── nl_team_vs_team_summary.csv    ← H2H W-L summary for key rivalries
│   ├── nl_season_by_year.json         ← Comprehensive season-by-season data (1876-2025)
│   └── research_data_supplement.json  ← Extra research data (H2H, division titles, records)
├── docs/
│   └── data_notes.md                  ← Methodology, conventions & caveats
└── visualizations/
    └── README.md                      ← Visualization roadmap, code & notebooks
```

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/zhub9006/nl-team-trends.git
cd nl-team-trends
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Download the Lahman Database (Recommended for deeper analysis)
The SABR Lahman Database is the industry-standard free CSV dataset for all MLB team data:
```bash
wget https://github.com/chadwickbureau/baseballdatabank/archive/refs/heads/master.zip
unzip master.zip
```

## Quick Data Loading Examples

### Load All-Time Franchise Records
```python
import pandas as pd

# All-time NL records
records = pd.read_csv('data/nl_all_time_records.csv')
print(records.sort_values('ws_titles', ascending=False).head())

# Top teams by win percentage
print(records.sort_values('win_pct', ascending=False).head())
```

### Load Pennant Winners
```python
# Pennant winners by era
pennants = pd.read_csv('data/nl_pennant_winners.csv')
print(pennants.groupby('era')['NL_champion'].count())

# Pennant winners by decade
pennants['decade'] = (pennants['year'] // 10) * 10
print(pennants.groupby('decade')['NL_champion'].value_counts())
```

### Load Historical Performance
```python
# Seasonal team records
seasonal = pd.read_csv('data/nl_historical_performance.csv')

# Teams with best records by era
for era in seasonal['era'].unique():
    era_data = seasonal[seasonal['era'] == era]
    if 'win_pct' in era_data.columns:
        best = era_data.loc[era_data['win_pct'].idxmax()]
        print(f"{era}: Best win% - {best['team']} ({best['win_pct']:.3f}) in {best['year']}")
```

### Load Head-to-Head Rivalries
```python
h2h = pd.read_csv('data/nl_team_vs_team_summary.csv')

# Most one-sided rivalries
h2h_sorted = h2h.sort_values('t1_win_pct', ascending=False)
print("Most one-sided:", h2h_sorted.iloc[0]['team1'], "vs", h2h_sorted.iloc[0]['team2'])

# Most even rivalries
most_even = h2h.iloc[(h2h['t1_win_pct'] - 0.5).abs().argsort()[:3]]
print("Most even rivalries:", most_even[['team1','team2','t1_win_pct']])
```

## Key Historical Milestones

| Year | Event |
|------|-------|
| 1876 | National League founded (replacing the National Association); original 8 teams |
| 1882 | First World Series-style interleague series |
| 1892 | NL splits into East/West (first divisional format); 12 teams |
| 1903 | First official World Series (Pittsburgh Pirates vs Boston Americans) |
| 1906 | Chicago Cubs record 116 wins (.763) |
| 1914 | "Miracle Braves" — worst-to-first World Series champion |
| 1920s | Lyn "Bob"和非true — NL dominance in Heritage Era |
| 1947 | Jackie Robinson breaks color barrier (Brooklyn Dodgers) |
| 1958 | Brooklyn Dodgers & NY Giants relocate to West Coast |
| 1969 | NL splits into East, West divisions; first NLCS played; Miracle Mets |
| 1975-76 | "Big Red Machine" — Cincinnati Reds back-to-back WS champions |
| 1991-2005 | Atlanta Braves dynasty — 14 consecutive NL East titles |
| 1994 | Season cancelled by players' strike; Expos had best record |
| 2016 | Chicago Cubs end 108-year championship drought |
| 2020 | Dodgers win WS in 60-game COVID-19 season |
| 2022 | MLB expands playoffs; balances schedule across 15 teams |
| 2024-25 | LA Dodgers back-to-back World Series champions |

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/era-analysis`)
3. Commit changes (`git commit -m 'Add NLCS era analysis notebook'`)
4. Push (`git push origin feature/era-analysis`)
5. Open a Pull Request with a description and source citations

## License

This project is licensed under the MIT License — see the LICENSE file for details.

## Data Sources

This research is compiled from multiple authoritative baseball reference sources including:
- Baseball-Reference.com
- Baseball Almanac
- SABR / Lahman Database
- MLB.com
- Champs or Chumps
- ESPN
- Wikipedia
- Retrosheet
- Everything Explained Today

All data is cross-validated. Discrepancies are noted in `docs/data_notes.md`.
