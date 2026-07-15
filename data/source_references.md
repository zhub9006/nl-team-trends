# NL Team Trends — Source References & Methodology

> Central source attribution and data methodology for all NL team performance files.
> All data through end of 2025 MLB season.

## Primary Data Sources

| # | Source | URL | Coverage | Type |
|---|--------|-----|----------|------|
| 1 | [Baseball Reference - NL](https://www.baseball-reference.com/leagues/NL/) | baseball-reference.com/leagues/NL/ | 1876–present | Year-by-year NL standings & leaders |
| 2 | [Baseball Almanac - NL Team-vs-Team](https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml) | baseball-almanac.com | 1876–2026 | Head-to-head W-L matrices |
| 3 | [SABR Lahman Database](https://sabr.org/lahman-database/) | sabr.org/lahman-database/ | 1871–2025 | Full CSV dataset (stats, pitching, teams) |
| 4 | [Baseball Data Hub](https://baseballdatahub.com/seasons/) | baseballdatahub.com/seasons/ | 1871–2026 | Complete season standings archive |
| 5 | [StatsCrew - NL](https://www.statscrew.com/baseball/l-NL) | statscrew.com/baseball/l-NL | 1876–present | NL rosters, standings & leaders |
| 6 | [StatMuse - NL Titles](https://www.statmuse.com/mlb/ask/most-national-league-titles) | statmuse.com/mlb | 1876–2026 | NL championship leaders & franchise stats |
| 7 | [OpenIntro MLB Dataset](https://www.openintro.org/data/index.php?data=mlb_teams) | openintro.org/data/ | Multi-year | ML-ready CSV dataset |
| 8 | [Wikipedia - NL Pennant Winners](https://en.wikipedia.org/wiki/List_of_National_League_pennant_winners) | wikipedia.org | 1876–present | Official pennant winner lists |
| 9 | [ESPN - World Series History](https://www.espn.com/mlb/worldseries/history/winners) | espn.com/mlb/worldseries | 1903–present | WS champions by year w/ scores |
| 10 | [Baseball-Reference - Postseason](https://www.baseball-reference.com/postseason/) | baseball-reference.com/postseason/ | 1903–present | Detailed postseason results by year |

## Conventions & Definitions

- **Win%** = Wins / Games Played; no ties counted after 1920s
- **Pennants** = NL championship awards (pre-1969: best regular-season record; 1969+: LCS winner)
- **WS Titles** = World Series championships won as NL team
- **154-game schedule** through 1960; **162-game schedule** from 1961; **60-game season** in 2020 (COVID)
- ** Milwaukee Brewers** moved from AL to NL Central in 1998
- **Montreal Expos** relocated to Washington Nationals in 2005
- **1994 season voided** by players' strike — no pennant or WS awarded
- **Pre-WS era (1876-1902)** pennants determined by best regular-season record only
- **Interleague play** began 1997; full schedule 2023

## Data Accuracy Note

The following years have been verified against Baseball Reference and ESPN:
- 1903–1919: 8thinning race records, WS scores from ESPN [ref 9]
- 1920–1968: Pennant winners from SABR lahman database [ref 3], WS from ESPN [ref 9]
- 1969–2025: NL champion and WS results verified against Baseball Reference [ref 1, ref 10]

## Files & Dependencies

| File | Format | Content |
|------|--------|---------|
| `nl_all_time_records.csv` | CSV | 15 teams, franchise-level cumulative W-L, pennants, WS titles |
| `nl_historical_performance.csv` | CSV | One row per NL championship season, 1876–2025, with era labels |
| `nl_historical_performance_detailed.csv` | CSV | Year-by-year: Champion, 2nd place, W-L, WS result, era |
| `nl_pennant_winners_recent.csv` | CSV | NL pennant winners and WS outcomes 1995–2025 (verified)
| `nl_recent_standings.csv` | CSV | Full divisional standings 2020–2025 (verified)
| `nl_championship_trends.csv` | CSV | Era-dimensioned championship trends |
| `nl_notable_records.csv` | CSV | Five-tier tier list of NL's most remarkable single-season & franchise records |
| `source_references.md` | MD | This file |

## Recommended Update Workflow

1. After each MLB season (Feb–Mar):
   - Pull updated standings from Baseball Reference [ref 1]
   - Update `nl_all_time_records.csv` with year-end cumulative totals
   - Append new row to `nl_historical_performance.csv` and `nl_historical_performance_detailed.csv`
   - Append new row to `nl_pennant_winners_recent.csv` (shift off oldest year)
   - Update `nl_recent_standings.csv` with full 2025 or new season
   - Update README.md with new record tables and timeline
2. After adding SABR updated lahman CSV files:
   - Verify all W-L records across all CSV files
   - Recompute `nl_all_time_records.csv` from raw SABR data
3. When adding visualization scripts:
   - Update `visualizations/README.md` roadmap statuses
   - Add script path to `requirements.txt` if new runtime

---