# Source References for NL Team Trends Repository
# Comprehensive list of data sources for National League historical performance research
# Data through end of 2025 MLB season

## Primary Data Sources

| Source | URL | Coverage | Description |
|--------|-----|----------|-------------|
| Baseball-Reference (NL) | https://www.baseball-reference.com/leagues/NL/ | 1876–present | Official year-by-year NL standings & team stats |
| Baseball Almanac | https://www.baseball-almanac.com/ | 1876–present | NL team-vs-team W-L matrices & year-by-year history |
| SABR Lahman Database | https://sabr.org/lahman-database/ | 1871–2025 | Free downloadable CSV dataset (full team/batting/pitching stats) |
| Baseball Data Hub | https://baseballdatahub.com/seasons/ | 1871–2026 | Complete season standings & stats archive |
| StatsCrew (NL) | https://www.statscrew.com/baseball/l-NL | 1876–present | NL rosters, standings & leaders |
| StatMuse | https://www.statmuse.com/mlb/ask/most-national-league-titles | 1876–2026 | NL championship leaders & franchise stats |
| OpenIntro MLB Dataset | https://www.openintro.org/data/index.php?data=mlb_teams | Multi-year | ML-ready MLB team data in R format |
| Everything Explained | https://everything.explained.today | 1876–2025 | All-time franchise W-L & postseason data |
| Baseball Briefs | https://baseballbriefs.com/ | 1876–2023 | Franchise win totals analysis |
| Linger and Look | https://www.lingerandlook.com/Names/BaseballStandings.php | 1901–present | Year-by-year standings with managers |
| ESPN (World Series) | https://www.espn.com/mlb/worldseries/history/winners | 1903–present | World Series champions by year |
| Wikipedia (NL Pennants) | https://en.wikipedia.org/wiki/List_of_National_League_pennant_winners | 1876–present | Complete pennant winner list with WS results |
| Retrosheet | https://www.retrosheet.org/ | 1871–present | Box scores, team records, and play-by-play data |
| Project Ballpark | https://www.projectballpark.org/ | 1876–present | Historical ballpark attendance & demographics |

## Key Data Points

- NL Founded: February 2, 1876 (replacing National Association)
- 150th Anniversary: 2026
- Best single-season: 1906 Cubs (116-36, .763)
- Most WS titles (NL): St. Louis Cardinals (11)
- Most pennants: LA Dodgers (26, 2025)
- Most all-time NL wins: SF Giants (11,663)
- Most all-time NL losses: Phillies (11,865)
- Braves: 14 consecutive division titles (1991-2005)
- Dodgers: 8 straight NL West (2018-2025), back-to-back WS (2024-2025)
- 1994 season voided by players' strike — no WS/pennant
- NL expanded: 8 teams (1876) to 15 teams (1998-present)

## Data Conventions

- Win% = Wins / Games Played
- 162-game schedule adopted 1961; pre-1961 = 154 or fewer games
- Milwaukee Brewers moved from AL to NL Central in 1998
- Montreal Expos relocated to Washington Nationals in 2005
- 2020 season was 60 games due to COVID-19
- All-time records include pre-relocation franchise totals
- Pre-1903 pennants = NL championship only (no WS)
- Split seasons in 1892 and 1981
- Interleague play began 1997; full schedule 2023

## Data File Reference

| File | Description |
|------|-------------|
| data/nl_all_time_records.csv | All-time franchise win-loss totals by team |
| data/nl_historical_performance.csv | Championship-season highlights with era labels |
| data/nl_historical_performance_detailed.csv | Year-by-year NL champion + 2nd place + WS results 1876-2025 |
| data/nl_pennant_winners_recent.csv | NL pennant winners and WS results 1995-2025 |
| data/nl_championship_trends.csv | Era-based championship trends |
| data/nl_notable_records.csv | Key single-season and franchise records |