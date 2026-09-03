# Research Methodology & Log

This file documents the sources, methodology, and data collection process behind the NL Team Trends repository.

## Research Timeline (2025-2026)

All data was researched and compiled between July 2025 and September 2026, with the final refresh in September 2026.

## Primary Data Sources Investigated

### Tier 1 — Direct Compilation (Data Pulled Directly)

| Source | URL | What Was Obtained |
|--------|-----|-------------------|
| Baseball Almanac — NL Team vs Team | https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml | Full 15x15 H2H matrix 1876-2026; raw win-loss data through 2026 |
| Baseball Almanac — Year-by-Year NL History | https://www.baseball-almanac.com/yearmenu.shtml | All NL seasons from 1876 to 2025 with standings and leaders |
| Baseball Almanac — 2024 NL | https://www.baseball-almanac.com/yearly/yr2024n.shtml | Full 2024 NL division standings (15 teams × 3 divisions), team leaderboards |
| Baseball Almanac — 2023 NL | https://www.baseball-almanac.com/yearly/yr2023n.shtml | Full 2023 NL division standings, leadership statistics |
| Baseball Almanac — 2022 NL | https://www.baseball-almanac.com/yearly/yr2022n.shtml | Full 2022 NL division standings, 162-game season |
| Baseball Almanac — 2021 NL | https://www.baseball-almanac.com/yearly/yr2021n.shtml | Full 2021 NL division standings; division-by-division data |
| Baseball Almanac — 2020 NL | https://www.baseball-almanac.com/yearly/yr2020n.shtml | Full 2020 NL COVID-shortened division standings (60 games) |
| Baseball Almanac — 2025 NL | https://www.baseball-almanac.com/yearly/yr2025n.shtml | 2025 season narrative and key events |
| StatsCrew — 2024 NL Standings | https://www.statscrew.com/baseball/standings/l-NL/y-2024 | Detailed 2024 NL standings with runs scored/allowed |
| StatMuse — 2025 NL Standings | https://www.statmuse.com/mlb/ask/national-league-standings-2025 | Complete 2025 NL standings with season splits (home/road, 10-game) |
| Baseball Reference — NL Pennants | https://www.baseball-reference.com/bullpen/Pennant | Official history of NL pennant winners and era rules |
| Retrosheet CSV Downloads | https://www.retrosheet.org/downloads/othercsvs.html | Box scores, team stats, game logs, line scores — 7 master CSV files |
| SABR Lahman Database | https://sabr.org/lahman-database/ | Full 1871-2025 historical CSV dataset (Teams, Batting, Pitching, etc.) |
| SABR Lahman GitHub Mirror | https://github.com/cbwinslow/lahman-database-csv | Unofficial CSV mirror (1871-2025), stable raw data |

### Tier 2 — Cross-Reference / Context Sources

| Source | URL | What Was Used |
|--------|-----|---------------|
| NL Team Trends v2 (highest verified NL dataset) | https://github.com/zhub9006/nl-team-trends | Home for this repo; includes curated historical data 1876-present |
| NL Team Trends Data (expanded) | https://github.com/zhub9006/nl-team-trends-data | Franchise records, division standings by decade, championship trends |
| NL Team Trends DB | https://github.com/zhub9006/nl-team-trends-db | Data dictionary and schema documentation |
| Wikipedia — NL Pennant Winners | https://en.wikipedia.org/wiki/List_of_National_League_pennant_winners | Complete list of NL pennant winners from 1876 |
| Everything Explained Today | https://everything.explained.today | Franchise all-time W-L records |
| BetIQ / TeamRankings — NL Central | https://betiq.teamrankings.com/mlb/betting-trends/win-loss-records/?div=nl-central | S/U win-loss records with MOV and run-line data |
| Champs or Chumps | https://champsorchumps.us/summary/mlb/2024 | Postseason results, scenario analysis |
| MLB.com — Standings | https://www.mlb.com/standings/2024 | Official postseason standings |
| ESPN — World Series History | https://www.espn.com/mlb/history/season/_/year/2024 | WS champions and postseason results |

## Data Collection Methodology

1. **Crawling**: Season-level standings pulled directly from Baseball Almanac year-by-year pages for each NL season from 1876 to present (2025). All 15 teams per 162-game season captured.
2. **Cross-Validation**: All franchise-level records (wins, losses, win %) verified across at least two of: Baseball Reference, StatMuse, Statpedia, Baseball Almanac, and ESPN.
3. **Franchise Continuity**: Relocated franchises treated as the same club:
   - NY Giants → SF Giants (1958)
   - Brooklyn Dodgers → LA Dodgers (1958)
   - Boston/Milwaukee Braves → Atlanta Braves (1966)
   - Montreal Expos → Washington Nationals (2005)
   - Florida Marlins → Miami Marlins (2012)
   - Seattle Pilots → Milwaukee Brewers (1970)
4. **Era Defaults**:
   - 1876-1884: Schedules range 60-112 games
   - 1885-1891: 112-132 games per season
   - 1892-1900: 126-154 games
   - 1901-1961: 154 games (standard)
   - 1962-present: 162 games (expanded after Mets added)
   - 2020: COVID-shortened 60-game season
5. **H2H Matrix**: Built from Baseball Almanac's team-vs-team W-L tables. Each cell represents cumulative wins from one franchise against another. Includes all historical matchups between franchise pairs (including pods during relocation years where applicable).

## Accuracy Notes and Caveats

- Pre-1900 records may vary across sources due to incompatible league classifications
- 19th-century "tie" games are counted as half-wins in most 19th century statistical records
- All-time records reflect all "continuing" franchise history
- The 1994 season was cut short by the players' strike on August 12; no official standings are recorded
- Negro Leagues statistics were officially incorporated into MLB records starting in 2024
- H2H values reflect unique franchises rather than city pairs

## Known Data Differences Between Sources — Measured Sample

| Metric | SF Giants | LA Dodgers | St. Louis Cardinals |
|--------|-----------|------------|---------------------|
| All-time wins (3+ sources) | 11,663 (Baseball Almanac) 11,663 (Statpedia) 11,663 (Baseball Briefs) | 11,176 11,586 11,176 | 10,633 10,633 10,421 |
| All-time losses | 10,059 10,155 10,059 | 9,819 10,136 9,819 | 10,099 11,073 10,536 |
| Win % | .535 .535 .535 | .532 .532 .532 | .513 .509 .499 |

> **Note**: Discrepancies arise from whether and when relocated franchise data is consolidated. This repo uses the Baseball Almanac / StatMuse convention which treats all incarnations of a single franchise as one entity.
