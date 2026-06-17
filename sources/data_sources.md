# Data Sources & Reference Links

This document catalogs all sources used to compile the NL historical performance data in this repository.

## Primary Sources

### StatMuse
- URL: https://www.statmuse.com/mlb
- Data retrieved: All-time franchise win-loss records for all 15 NL teams
- Queries used:
  - `every mlb teams all-time win loss record`
  - `mlb teams by all-time winning percentage`
  - `dodgers all-time win loss record`
  - `cardinals all-time win loss record`
  - `phillies all-time win loss record`
  - `mets all-time win loss record`
  - `padres nationals brewers marlins diamondbacks Rockies all-time win loss record`
- Coverage: Through end of 2025 regular season
- Notes: StatMuse provides season-by-season breakdowns with cumulative totals. All 15 NL franchise records were confirmed individually.

### Baseball Almanac
- URL: https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml
- Data retrieved: NL team-vs-team win-loss matrix (1876 through 2026)
- Coverage: All head-to-head matchups between NL franchises from 1876 to present
- Notes: Franchise moves are included (e.g., SF Giants data includes NY Giants era). Updated daily during regular season.
- Related pages:
  - Year-by-year history: https://www.baseball-almanac.com/yearmenu.shtml
  - Games won by teams records: https://www.baseball-almanac.com/recbooks/rb_gam3.shtml

### Grokipedia / Wikipedia
- URL: https://grokipedia.com/page/List_of_all-time_Major_League_Baseball_win-loss_records
- URL: https://en.wikipedia.org/wiki/List_of_all-time_Major_League_Baseball_win%E2%80%93loss_records
- Data retrieved: Contextual franchise history, explanatory notes on record definitions, era descriptions
- Coverage: Through end of 2025 regular season
- Key facts sourced:
  - NL founded 1876; AL founded 1901
  - Braves are oldest continuously operating pro sports franchise (since 1871)
  - Phillies hold the record for most losses by any MLB franchise
  - Rockies have the lowest all-time winning percentage among current franchises
  - Ties were common pre-1920; excluded from Win% calculation
  - 243,136 total MLB games played through end of 2025

### Lahman Baseball Database (SABR)
- URL: https://sabr.org/lahman-database/
- Data available: Complete batting/pitching/fielding statistics back to 1871, standings, team stats, managerial records, postseason data
- Coverage: 1871 through most recent completed season
- Notes: Created by SABR member Sean Lahman. Now includes Negro Leagues data. Ideal for deeper statistical analysis beyond win-loss records.

### Baseball-Reference.com
- URL: https://www.baseball-reference.com/
- URL: https://www.baseball-reference.com/leagues/NL/NL.shtml
- URL: https://www.baseball-reference.com/leagues/index.shtml
- Data available: Complete major league player, team, and league stats; awards, records, leaders, rookies, scores
- Coverage: Full historical coverage
- Notes: The gold standard for baseball statistical reference. League-level pages provide year-by-year standings and team performance data.

## Secondary Sources

### StatsCrew.com
- URL: https://www.statscrew.com/baseball/l-NL
- URL: https://www.statscrew.com/baseball/standings/l-NL
- Data available: NL team rosters, statistics, historical standings data

### Baseball Data Hub
- URL: https://baseballdatahub.com/seasons/
- Data available: 156 MLB seasons from 1871 to 2026; team standings, statistics, and records for every season
- Notes: Useful for browsing specific historical seasons

### ESPN MLB History
- URL: https://www.espn.com/mlb/history
- Data available: Career leaders and single-season leaders in various categories

## Data Verification

All win-loss records in `nl_all_time_records.csv` were cross-referenced across multiple sources:
- StatMuse individual franchise pages (primary)
- StatMuse aggregate all-time percentage rankings (secondary check)
- Grokipedia/Wikipedia contextual data (validation)
- Baseball Almanac head-to-head matrix (consistency check)

Winning percentages were recalculated from raw W/L totals to confirm accuracy:
- Formula: Win% = W / (W + L)
- Ties excluded per standard MLB convention

## Last Updated

- **Date**: June 2026
- **Data through**: End of 2025 regular season (September 28, 2025)
- **Next update**: After completion of 2026 regular season
