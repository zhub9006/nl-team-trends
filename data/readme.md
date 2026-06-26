# NL Team Trends — Data File Documentation

## Overview

This directory contains curated National League team performance data compiled from primary baseball reference sources for analysis and visualization.

## Files

### nl_historical_performance.json
Comprehensive JSON file containing:
- **best_nl_records**: Top single-season NL records (best win% for each team)
- **franchise_alltime**: All-time franchise win-loss totals with founding year and seasons played
- **standings_by_year**: Year-by-year NL standings for key seasons (1990, 2000, 2024, 2025)

*Primary source: Baseball Reference nl standings pages; cross-referenced with Baseball Almanac*

### nl_team_seasons_1969_2024.csv
Season-by-season records for all NL teams (1969–2024).
Columns: Season, Team, W, L, WinPct, RS, RA, RunDiff, Division, PlayoffResult

*Primary source: Lahman Database / Baseball Reference; covers post-split-squad era*

### nl_team_wins.csv
All-time franchise win-loss totals for the 15 current NL teams.
Columns: Franchise, Founded, Relocated, TotalWins, TotalLosses, WinPct, Seasons, WorldSeriesTitles, NationalLeaguePennants, Notes

*Primary source: Baseball Reference; includes predecessor franchise history*

### nl_champions.csv
NL pennant winners, World Series champions, and results year by year (1903–2024).
Columns: Year, NLPennantWinner, NLPennantRunnerUp, WorldSeriesChampion, WorldSeriesOpponent, WSResult, KeyNote

*Primary source: Baseball Reference; Wikipedia cross-reference*

### nl_era_trends.csv
NL era-by-era performance summary.
Columns: Era, Years, Teams, RunsPerGame, TopFranchiseWinPct, DefiningFeatures

*Primary source: Synthesis from Baseball Reference era data, Baseball Almanac, Lahman Database*

### readme.md
This file.

## Data Consistency Notes

- All franchise names use modern team names (e.g., "Los Angeles Dodgers" covers all eras)
- Colorado Rockies and Atlanta Braves have the longest continuous NL membership among expansion teams
- Milwaukee Brewers counted as NL team only since 1998 (moved from AL)
- 1994 season data includes strike-shortened records where available
- 2020 season data is for the 60-game COVID-affected schedule
- Win percentages are rounded to 3 decimal places
- Run Differentials are integers (RS - RA)

## Recommended Analysis Workflow

1. Load `nl_team_seasons_1969_2024.csv` into Pandas for season-level analysis
2. Load `nl_team_wins.csv` for franchise-level comparisons
3. Load `nl_champions.csv` for championship timeline analysis
4. Load `nl_era_trends.csv` for era-specific trend identification
5. Use `nl_historical_performance.json` for quick lookups of best records and franchise totals

## Suggested Visualizations

- Win% seasonal heatmap (team × year) with Seaborn
- Run differential timeline (line chart) per franchise
- Championship drought horizontal bar chart
- Division winner treemap by decade
- Era comparison box plots (Win% by era)
- Head-to-head matrix as a Seaborn heatmap
