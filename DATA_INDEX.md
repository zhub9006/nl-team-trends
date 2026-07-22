# NL Team Trends — Repository Documentation

## Data Files Index

This document describes each data file in the `data/` directory, including column definitions, data sources, and usage notes.

| File | Description | Source | Records | Update Frequency |
|------|-------------|--------|---------|------------------|
| `nl_all_time_records.csv` | All-time franchise records with W/L, pennants, WS titles | Baseball-Reference, Wikipedia | 15 rows (current NL teams) | Annual (post-season) |
| `nl_championship_trends.csv` | Championship results by era with team dominance flags | Baseball Almanac, ESPN | ~150 rows (one per season) | Annual |
| `nl_historical_performance.csv` | Season-by-season standings for all NL teams | Lahman Database, Baseball-Reference, Baseball Data Hub | Key-season comprehensive (500+ rows across 14 seasons) | Quarterly |
| `nl_notable_records.csv` | Single-season and franchise records, H2H Rivalries | Baseball Almanac, SABR | ~100+ rows | As needed |
| `nl_pennant_winners.csv` | Complete NL pennant winners from 1876 to present | Wikipedia, Baseball-Reference | ~150 rows (one per season) | Annual |
| `nl_recent_standings.csv` | Divisional standings 2014–2025 | Baseball-Reference, MLB.com | ~12 years × 15 teams | Annual |
| `nl_team_vs_team_summary.csv` | H2H W-L summary for key NL rivalries | Baseball Almanac | 11 key rivalry rows | Biannual |

## Column Definitions

### nl_historical_performance.csv
- `year`: Season year
- `era`: Historical era classification (Founding Era, Merger Era, Transition Era, Expansion Era, Modern Era)
- `division`: NL division (NL East, NL Central, NL West, or NL for pre-division era)
- `team`: Franchise name (current canonical name)
- `wins`: Regular-season wins
- `losses`: Regular-season losses
- `win_pct`: Winning percentage (wins / (wins + losses))
- `games_played`: Total games played in season
- `pennant`: Yes/No — was this team the NL pennant winner?
- `ws_result`: World Series or postseason result
- `notes`: Contextual notes on team, era, or unusual circumstances

### nl_all_time_records.csv
- `team`: Official franchise name (current name)
- `ws_titles`: Number of World Series championships won as NL representative
- `games`: Total regular-season games played (franchise history)
- `wins`: Total regular-season wins
- `losses`: Total regular-season losses
- `win_pct`: Winning percentage (wins / (wins + losses))
- `last_ws_title`: Year of most recent World Series victory ("N/A" if none)
- `first_season`: Year franchise first played in NL
- `franchise_origin`: Original franchise name or notable transition
- `pennant_count`: Total number of NL pennants won
- `pennant_years`: Semicolon-separated list of pennant-winning years

### nl_championship_trends.csv
- `year`: Season year
- `era`: Historical era classification
- `champion_string`: NL pennant winner / WS champion
- `ws_result`: Series result vs AL champion
- `champion_record`: Regular-season record of NL champion

### nl_notable_records.csv
- `category`: Type of record (franchise_wins, franchise_losses, single_season_wins, etc.)
- `team`: Franchise name
- `value`: Record value
- `season`: Year (for single-season records)
- `notes`: Additional context

### nl_pennant_winners.csv
- `year`: Season year
- `era`: Historical era
- `NL_champion`: NL pennant winner
- `ws_result`: World Series result vs AL champion
- `champion_record`: Regular-season record

### nl_recent_standings.csv
- `year`: Season year
- `era`: Historical era
- `NL_champion`: NL champion
- `ws_result`: World Series result
- `champion_record`: Regular-season record
- `division_winner_1`, `_2`, `_3`: Division winners by division

### nl_team_vs_team_summary.csv
- `team1`, `team2`: Pair of NL franchises (alphabetical order within matchup)
- `t1_wins`: Team 1 total wins vs Team 2
- `t2_wins`: Team 2 total wins vs Team 1
- `t1_win_pct`: Winning percentage of Team 1 in this matchup
- `era_dominant`: Which franchise dominated most eras

## Data Conventions

1. All win-loss records refer to **regular-season** games only unless otherwise noted.
2. "NL_champion" refers to the NL pennant winner (not necessarily the WS champion).
3. Pre-WS era (pre-1903) champions are based on best regular-season record or postseason series.
4. 1994 season is incomplete due to players' strike (68–46 at time of cancellation).
5. 2020 season was a 60-game COVID-19 shortened season.
6. Franchise names are given as the current canonical name with historical aliases noted.
7. Franchise movement is reflected in the franchise_origin field (e.g., NY Giants → SF Giants).
8. Win-loss records for relocated/renamed franchises carry forward cumulative totals.

## Known Limitations

- Pre-1903 NL champion data is incomplete for some seasons.
- H2H data includes all games played under NL-only and interleague formats.
- Season-by-season historical performance is a work in progress — current data covers key representative seasons across all eras.
- Penant counts for some franchises may vary slightly depending on source (e.g., pre-1903 pennants).
- 1885 NL-AA series ended in a tie with no clear winner in some historical sources.
