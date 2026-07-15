# NL Team Trends - Data Notes

## How to Use This Repository

### Data Files Overview
| File | Description | Use Case |
|------|-------------|----------|
| `data/nl_all_time_records.csv` | Franchise totals (15 NL teams) | All-time rankings, franchise comparisons |
| `data/nl_pennant_winners_1876_2025.csv` | Year by year NL champion + WS results | Time series analysis, era classification |
| `data/nl_championship_by_decade.csv` | Era-level aggregated stats | Era comparisons, trend analysis |
| `data/nl_recent_standings_2020_2025.csv` | Divisional standings 2020-2025 | Recent competitive balance analysis |
| `data/nl_all_time_detailed.csv` | Franchise summary with key insights | Quick reference, research starting points |
| `data/nl_historical_performance.csv` | Championship-season highlights | Quick era-level snapshots |
| `data/nl_championship_trends.csv` | Championship trends by era | Era-based comparison |
| `data/nl_notable_records.csv` | Single-season and franchise records | Record tracking |
| `docs/source_references.md` | Source attribution and methodology | Data provenance |

## Data Conventions
- **Win%** = Wins / Games Played
- **Pennants** = NL championship awards (pre-Wild Card era)
- **WS Titles** = World Series championships won as NL team
- **Era columns** may have slightly different class definitions
- Pre-1961: 154-game; 1962+: 162-game; 2020: 60-game (special)
- Teams include predecessor city lineages (e.g., SF Giants includes NY Giants)

## Known Data Issues
1. 1940s/1950s entries may have incomplete WS MVP data
2. 1994 season: no WS was played due to strike
3. 2020 season is a shortened 60-game season
4. Some 2020-era NLLS results are approximate (baseball-reference recommended)
5. Eventual consistency across era definitions

## Recommended Data Cleaning Pipeline
```python
import pandas as pd
# Load data
df = pd.read_csv('data/nl_pennant_winners_1876_2025.csv')
# Filter eras
eras = df.groupby('Era')
# Analyze trends
windows = df.rolling('5Y', on='Year')
```

## Key Sources for Cross-Referencing
1. [Baseball Reference NL](https://www.baseball-reference.com/leagues/NL/) - Gold standard
2. [SABR Lahman Database](https://sabr.org/lahman-database) - Complete CSV dataset
3. [Baseball Data Hub](https://baseballdatahub.com/seasons/) - Season standings
4. [Linger & Look](https://www.lingerandlook.com/Names/BaseballStandings.php) - Multi-year W-L data
5. [Baseball Almanac](https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml) - H2H matrices

## Citation Format
If using this data in research:
nl-team-trends (2025), zhub9006/nl-team-trends, GitHub Repository
