# NL Team Trends — Data Documentation

This directory contains all historical National League performance datasets compiled for the `nl-team-trends` repository.

## File Descriptions

### nl_historical_performance.json
Comprehensive NL historical data including:
- **best_records**: Single-season records ranked by win% (154+ games or equivalent)
- **franchise_alltime**: All-time franchise win-loss totals with founding year and seasons played
- **standings_by_year**: Full NL standings snapshots for key years (1876, 1890, 1901, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2024, 2025)

### nl_team_seasons_all_time.csv
Pre-1969 season-by-season records for the original 8 National League franchises (1876–1968).
Columns: `season, team, wins, losses, win_pct, division, playoff_result`

Note: Pre-division era teams are listed with "N/A" for the division column. Franchise names reflect the names used in each season.

### nl_team_seasons_1969_2024.csv
Modern era NL team season records (1969–2024) with post-1969 divisional alignment.
Columns: `season, team, wins, losses, win_pct, rs, ra, run_diff, division, playoff_result`

### nl_team_wins.csv
All-time franchise-level win-loss totals compiled from Baseball Reference and Retrosheet.
Columns: `franchise, founded, relocated, total_wins, total_losses, win_pct, seasons, ws_titles, nl_pennants, notes`

### nl_champions.csv
Year-by-year NL postseason results from 1903 to 2024.
Columns: `year, nl_pennant_winner, nl_runner_up, ws_champion, ws_opponent, ws_result, key_note`

### nl_era_trends.csv
Aggregated NL era performance summaries covering 1876–present.
Columns: `era, years, teams, runs_per_game, top_franchise, top_franchise_win_pct, defining_features, key_milestones`

## Data Sources

All data compiled from Baseball Reference, Retrosheet, Baseball Almanac, Lahman Database (SABR/GitHub), MLB.com, StatsCrew, and Baseball Data Hub.

## Data Validation

All win-loss records cross-referenced with at least two sources. Discrepancies noted in `notes` fields. Modern era data (1969+) includes run differential from Baseball Reference.

## Usage

### Python / Pandas
```python
import pandas as pd
df = pd.read_csv('data/nl_team_seasons_1969_2024.csv')
print(df.head())
```

## Citation

If used in research, cite: Baseball Reference, Retrosheet, SABR Lahman Database.

## License

Data: Public domain. Code: MIT.