# NL Team Trends - Data Notes

## How to Use This Repository

### Data Files Overview
| File | Description | Use Case |
|------|-------------|----------|
| `data/nl_all_time_records.csv` | Franchise totals (15 NL teams) | All-time rankings, franchise comparisons |
| `data/nl_pennant_winners.csv` | Year-by-year NL champion + WS results (1876-2025) | Time series analysis, era classification |
| `data/nl_championship_trends.csv` | Era-level aggregated stats | Era comparisons, trend analysis |
| `data/nl_recent_standings.csv` | Divisional standings 2020-2025 | Recent competitive balance analysis |
| `data/nl_historical_performance.csv` | Season-by-season NL champion highlights (1876-present) | Quick era-level snapshots |
| `data/nl_notable_records.csv` | Single-season and franchise records | Record tracking |
| `data/nl_notable_seasons.csv` | Significant seasons with key statistics | Contextual research |
| `data/nl_team_vs_team_summary.csv` | Head-to-head W-L summary for key matchups | Rivalry analysis |

## Data Conventions
- **Win%** = Wins / Games Played
- **Pennants** = NL championship awards (pre-Wild Card era)
- **WS Titles** = World Series championships won as an NL team
- **Era columns** use decade ranges (1870s, 1880s, ..., 2020s)
- Pre-1961: 154-game; 1962+: 162-game; 2020: 60-game (special)
- Teams include predecessor city lineages (e.g., SF Giants includes NY Giants)

## Known Data Issues
1. 1940s/1950s entries may have incomplete WS MVP data
2. 1994 season: no WS was played due to player strike
3. 2020 season is a shortened 60-game season
4. Some 2020-era results are approximate (per Baseball-Reference recommendations)
5. Era definitions may vary slightly between source files
6. AL teams formerly in the NL (Milwaukee Brewers, moved AL→NL in 1998) are included as NL teams post-1998

## Data Source Pipeline (Python Example)
```python
import pandas as pd

# Load all NL data files
historical = pd.read_csv("data/nl_historical_performance.csv")
all_time = pd.read_csv("data/nl_all_time_records.csv")
pennants = pd.read_csv("data/nl_pennant_winners.csv")
trends = pd.read_csv("data/nl_championship_trends.csv")
records = pd.read_csv("data/nl_notable_records.csv")
seasons = pd.read_csv("data/nl_notable_seasons.csv")
recent = pd.read_csv("data/nl_recent_standings.csv")
h2h = pd.read_csv("data/nl_team_vs_team_summary.csv")

# Example: filter championship seasons
champions = historical[["Year", "NL_Champion", "Champion_Wins", "Champion_Losses", "Champion_WPct"]]

# Example: rolling 5-year average of champion win%
champions["rolling_wpct"] = champions["Champion_WPct"].rolling(5, min_periods=1).mean()

# Example: cross-reference with all-time records
top_teams = all_time.sort_values("Win_Pct", ascending=False)
print(top_teams[["Franchise", "Total_Wins", "Total_Losses", "Win_Pct", "WS_Titles"]])
```

## Key Sources for Cross-Referencing
1. [Baseball Reference NL](https://www.baseball-reference.com/leagues/NL/) — Gold standard for year-by-year standings
2. [SABR Lahman Database](https://sabr.org/lahman-database) — Complete CSV dataset (1871-2025)
3. [Baseball Data Hub](https://baseballdatahub.com/seasons/) — Season standings archive
4. [Linger & Look](https://lingerandlook.com/Names/BaseballStandings.php) — Multi-year W-L data with managers
5. [Baseball Almanac](https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml) — H2H matrices and year-by-year history
6. [StatMuse](https://www.statmuse.com/mlb) — NL franchise championships and all-time %s
7. [Retrosheet](https://www.retrosheet.org/) — Box scores and play-by-play data
8. [Wikipedia (NL Pennants)](https://en.wikipedia.org/wiki/List_of_National_League_pennant_winners) — Complete pennant winner list

## Citation Format
If using this data in research:
> nl-team-trends (2026), zhub9006/nl-team-trends, GitHub Repository
> https://github.com/zhub9006/nl-team-trends

## License
This repository uses data sourced from public baseball reference sites and aggregated under fair-use research purposes. All original data remains the property of its respective providers (Baseball-Reference.com, Baseball Almanac, SABR, etc.).
