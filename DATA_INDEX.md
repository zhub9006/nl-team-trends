# Data File Index

This document describes all CSV and JSON data files in the `data/` directory and their column definitions.

## CSV Files

### nl_all_time_records.csv
Records all-time franchise records for the 15 current National League teams.

| Column | Description |
|--------|-------------|
| team | Franchise name (current name) |
| ws_titles | Number of World Series championships |
| games | Total regular-season games played |
| wins | Total regular-season wins |
| losses | Total regular-season losses |
| win_pct | Winning percentage (wins / total games) |
| last_ws_title | Year of most recent World Series title (N/A if none) |

### nl_pennant_winners.csv
Complete list of NL pennant winners and World Series results by year.

| Column | Description |
|--------|-------------|
| year | Season year |
| team | NL pennant winner |
| ws_champion | World Series champion |
| ws_result | World Series outcome description |
| record | NL champion's regular season record (W-L) |

### nl_recent_standings.csv
Season-by-season divisional standings for 2020-2025.

| Column | Description |
|--------|-------------|
| team | Franchise name |
| division | NL division (East, Central, West) |
| year | Season year |
| wins | Regular season wins |
| losses | Regular season losses |
| win_pct | Winning percentage |
| gb | Games behind division leader |

### nl_recent_trends_2000_2024.csv
Best NL teams ranked by win percentage over 23-year spans (StatMuse data).

| Column | Description |
|--------|-------------|
| rank | Ranking position |
| team | Franchise name |
| record | W-L record over the span |
| win_pct | Winning percentage over the span |
| games | Total games played over the span |

### nl_notable_records.csv
Key single-season and franchise records in NL history.

| Column | Description |
|--------|-------------|
| category | Type of record |
| team | Category leader |
| record_value | Record value |
| season | Year the record occurred |
| notes | Additional context |

### nl_championship_trends.csv
Championship highlights organized by era.

| Column | Description |
|--------|-------------|
| era | Time period |
| nl_champions | Number of NL champions in the era |
| nl_ws_titles | Number of NL World Series winners |
| top_team | Most successful franchise in the era |
| top_ws | Their WS titles |
| key_trends | Notable trends for the era |

### nl_team_vs_team_summary.csv
Head-to-head win-loss summary for key NL rivalries.

| Column | Description |
|--------|-------------|
| team1 | First franchise |
| team2 | Second franchise |
| t1_wins | Team 1 total wins vs Team 2 |
| t2_wins | Team 2 total wins vs Team 1 |
| t1_win_pct | Team 1's winning percentage vs Team 2 |
| era_dominant | Which franchise has dominated the rivalry and when |

## JSON Files (Planned)

### nl_season_by_year.json
Comprehensive season-by-season data 1876-2025, including standings, stats, and notable events.

### research_data_supplement.json
Extra research data including the full H2H matrix and division title history.