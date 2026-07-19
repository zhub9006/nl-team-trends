# Data File Index

This document describes all data files in the `data/` directory and their contents.

## CSV Data Files

| File | Description | Rows | Columns | Key Fields |
|------|-------------|------|---------|------------|
| `nl_historical_performance.csv` | Season-by-season NL standings with W-L% and division winners | 150+ | — | year, team, division, W, L, W%, GB, playoff, WS |
| `nl_all_time_records.csv` | All-time franchise records including WS titles, pennants, division titles | 15 | 13 | team, games, wins, losses, win_pct, ws_titles |
| `nl_championship_trends.csv` | Championship highlights organized by era | 8 | 8 | era, dominant_team, ws_titles, pennants, theme |
| `nl_championship_milestones.csv` | Key single-season and franchise milestone achievements | 16+ | 4 | team, year, achievement, details |
| `nl_notable_records.csv` | Key single-season and franchise records across multiple categories | 19 | 6 | category, record, value, team, year, notes |
| `nl_team_vs_team_summary.csv` | H2H W-L summary matrix for key NL matchups | 17 | 9 | team1, team2, t1_wins, t2_wins, t1_win_pct |
| `nl_recent_standings.csv` | Divisional standings for 2013–2025 with WS results | 13 | 9 | year, nl_champion, ws_result, nl_east/central/west_winner |
| `nl_seasonal_standings.csv` | Full NL seasonal breakdown with division, playoff, and WS results | 100+ | 13 | year, season, team, division, W, L, win_pct, gb, playoff, ws_result |
| `nl_pennant_winners.csv` | Complete list of NL pennant winners with W-L records | 100+ | 7 | year, team, wins, losses, win_pct, finish, notes |

## Recommended Data Files to Download Separately

| File | Source | Format | Description |
|------|--------|--------|-------------|
| Teams.csv | Lahman Database | CSV | All teams (active and historical) |  
| TeamSeasons.csv | Lahman Database | CSV | All team season records (W, L, W%) |
| SeriesPost.csv | Lahman Database | CSV | Postseason series results |
| AwardsManagers.csv | Lahman Database | CSV | Manager awards by year |

## File Conventions

- All CSV files use UTF-8 encoding with comma delimiters.
- Team names use canonical NL form (e.g., "LA Dodgers" not "Los Angeles Dodgers").
- Win percentage is calculated as W/(W+L) to 3 decimal places.
- Only regular-season records used in W-L calculations; postseason tracked separately.
- Years reflect the baseball season (e.g., 2025 = 2025 MLB season).

## Data Validation

- Cross-reference with Baseball-Reference and Baseball Almanac for accuracy.
- Lahman Database used as ground truth for season-by-season records.
- H2H matrices sourced from Baseball Almanac (updated daily during season).