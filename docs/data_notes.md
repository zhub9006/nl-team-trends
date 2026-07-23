# Data Notes & Methodology

This document provides detailed notes on data conventions, caveats, and usage guidelines for the nl-team-trends project.

## Data Files Overview

| File | Format | Rows | Description |
|------|--------|------|-------------|
| nl_all_time_records.csv | CSV | 15 rows | All-time franchise records (WS titles, games, W/L) |
| nl_pennant_winners.csv | CSV | ~150 rows | NL pennant winners by year with WS results |
| nl_championship_trends.csv | CSV | 9 rows | Championship highlights organized by era |
| nl_historical_performance.csv | CSV | 18 rows | Key seasons (1876–2025) with detailed performance |
| nl_notable_records.csv | CSV | 15 rows | Key single-season and franchise records |
| nl_recent_standings.csv | CSV | 12 rows | Divisional standings 2014–2025 |
| nl_team_vs_team_summary.csv | CSV | 22 rows | H2H W-L summary for key rivalries |
| nl_season_by_year.json | JSON | Multiple sections | Comprehensive season data (eras, sample seasons, championship frequency) |
| research_data_supplement.json | JSON | Multiple sections | Extra research data (division titles, H2H insights, franchise history) |

## Key Conventions

### Team Naming
- Modern names are used throughout for consistency
- Historical context is provided in notes columns

### Record Format
- Win-loss records are in traditional W-L format (e.g., "103-58")
- Win percentages are decimal values (e.g., 0.636)
- Fractional games (e.g., .5 games) are used for standings differences

### Special Values
- N/A = Record did not exist or is not applicable
- Season cancelled = 1994 strike
- No WS played = Pre-WS era years

## Limitations

1. 19th-century records may differ across sources
2. Relocated franchises treated as continuous
3. Interleague play generally excluded
4. COVID-19 2020 seasons (60 games) included but flagged
5. Negro Leagues data from SABR 2025 Lahman release included but mostly from 1948 and earlier

## Recommended Analysis Workflow

1. Start with nl_all_time_records.csv for franchise-level overview
2. Use nl_pennant_winners.csv for year-by-year championship tracking
3. Cross-reference with nl_historical_performance.csv for specific seasons
4. Explore rivalries via nl_team_vs_team_summary.csv
5. Use nl_season_by_year.json for programmatic access to all structured data
6. Reference research_data_supplement.json for division title analysis and H2H insights

## Extending the Dataset

To add more seasons to nl_historical_performance.csv:
1. Download the Lahman Baseball Database from https://sabr.org/lahman-database/
2. Import Teams.csv into pandas
3. Filter for NL teams only
4. Select relevant columns (year, team, W, L, rank, etc.)
5. Calculate win_pct and append to the CSV