# NL Team Trends — Data Methodology & Conventions

> Documentation of the methodology, data conventions, and caveats used across all NL performance data files in this repository.

## Data Sources & Cross-Validation

All data files were compiled from multiple verified sources and cross-referenced:

| Source | Primary Use | Reliability |
|--------|-------------|-------------|
| Baseball-Reference.com | Official standings & team stats | ★★★★★ Gold standard |
| Baseball Almanac | H2H matrices & franchise records | ★★★★☆ Excellent |
| SABR Lahman Database | Season-by-season CSV data | ★★★★★ Gold standard |
| StatMuse | 23-year trend queries | ★★★★☆ Excellent |
| Everything Explained Today | All-time W-L records | ★★★★☆ Excellent |
| Wikipedia | Pennant winner lists | ★★★★☆ Excellent |

## Key Conventions

### Win Percentage Calculation
- Win % = Wins / (Wins + Losses)
- Tie games are excluded from win% calculations (they don't count in standings)
- Modern (2007+): Ties only occur when monsoon-shortened game doesn't affect playoff positioning
- Pre-2007 ties exist in early-era data; most sources exclude or count them separately

### Franchise Counting Method
- Relocated franchises are counted as a single continuous franchise (e.g., Brooklyn → LA Dodgers, NY Giants → SF Giants, Montreal → Washington Nationals)
- Franchise totals include pre-relocation eras under the original name
- All-time records for a franchise include data from ALL cities the team has occupied

### Schedule Era Definitions
| Era | Years | Games/Season | Notes |
|-----|-------|-------------|-------|
| Early NL | 1876-1891 | 60-112 | Short varied schedules; inaugural seasons |
| Transition | 1892-1900 | 100-154 | Standard 154-game schedule begins ~1892 |
| 154-Game Era | 1901-1961 | 154 |consistent schedule; 100 wins = .649 win% |
| 162-Game Era | 1962-2019 | 162 | Modern standard; 107 wins = .660 |
| COVID Shortened | 2020 | 60 | Not comparable to 162-game seasons |
| Full Modern | 2021-2026 | 162 | Back to full schedule; 2023 adds full interleague |

## Data File Index

### CSV Files (all in `data/` directory)

| File | Description | Key Columns |
|------|-------------|-------------|
| `nl_all_time_records.csv` | Franchise-level all-time W/L/WS/Pennants | Team, WS_Titles, Games, Wins, Losses, Win_Pct |
| `nl_pennant_winners.csv` | NL pennant winners by year with WS results | Year, Team, W_L, W_L_Pct, WS_Result |
| `nl_historical_performance.csv` | Season-by-season NL champion data | Year, NL_Champion, Champion_W, Champion_L, Champion_WPct, WS_Champion |
| `nl_championship_trends.csv` | Championship highlights by era | Year, Champion, W-L, WS_Title, Milestone |
| `nl_notable_records.csv` | Key single-season & franchise milestones | Record_Type, Team, Year, Achievement, Value |
| `nl_team_vs_team_summary.csv` | H2H W-L summary for key rivalries | Team_1, Team_2, Team_1_Wins, Team_2_Wins, Team_1_Win_Pct |
| `nl_recent_standings.csv` | Divisional standings 2013-2026 | Year, Div_Winners, NL_Champion, WS_Champion |
| `nl_recent_trends_2000_2024.csv` | 23-year window franchise trends (StatMuse) | Team, Games, Wins, Losses, Win_Pct, Notes |
| `nl_all_franchises_historical.csv` | All 15 NL franchises with comprehensive stats | Team, All_Time_Wins, WS_Titles, Pennants, Division_Titles |

### Documentation Files
| File | Description |
|------|-------------|
| `nl_source_references.md` | Complete documentation of all research sources |
| `visualizations/README.md` | Visualization roadmap with Python code examples |
| `docs/data_notes.md` | This file — methodology and data conventions |

## Analysis Workflow

### Recommended Data Loading (Python/Pandas)
```python
import pandas as pd
records = pd.read_csv('data/nl_all_time_records.csv').set_index('Team')
pennants = pd.read_csv('data/nl_pennant_winners.csv')
performance = pd.read_csv('data/nl_historical_performance.csv')
trends = pd.read_csv('data/nl_recent_trends_2000_2024.csv')
h2h = pd.read_csv('data/nl_team_vs_team_summary.csv')
franches = pd.read_csv('data/nl_all_franchises_historical.csv')
standings = pd.read_csv('data/nl_recent_standings.csv')
```

## Disclaimer

This repository is a community research project. Data is compiled from publicly available sources and may contain minor inaccuracies. Users should verify against primary sources (Baseball-Reference, SABR Lahman) for publication-grade research.

MIT License.