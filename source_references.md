# Detailed Source References for NL Team Trends

## Primary Data Sources

| Source | URL | Coverage | Key Data |
|--------|-----|----------|----------|
| **Baseball Reference** | https://www.baseball-reference.com/leagues/NL/ | 1876–present | Year-by-year NL standings & leaders |
| **Baseball Almanac** | https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml | 1876–2026 | NL team-vs-team head-to-head matrices |
| **SABR Lahman Database** | https://sabr.org/lahman-database/ | 1871–2025 | Free downloadable CSV dataset (team, batting, pitching, fielding) |
| **Baseball Data Hub** | https://baseballdatahub.com/seasons/ | 1871–2026 | Complete season standings archive |n| **StatsCrew** | https://www.statscrew.com/baseball/l-NL | 1876–present | NL rosters, standings & leaders |
| **Everything Explained** | https://everything.explained.today | 1876–2025 | All-time franchise W-L and postseason records |
| **StatMuse** | https://www.statmuse.com/mlb/ask/most-national-league-titles | 1876–2026 | NL championship leaders & franchise stats |
| **Baseball Briefs** | https://baseballbriefs.com/most-wins-in-national-league-history/ | 1876–2023 | Franchise win totals analysis |
| **Her Sports Corner** | https://hersportscorner.com/3374-2/ | 1876–2015 | NL Central all-time records |
| **OpenIntro Dataset** | https://www.openintro.org/data/index.php?data=mlb_teams | Multi-year | Machine-learning-ready MLB team data |

## Recommended Data Downloads

1. **SABR Lahman Database** — Download `Teams.csv`, `AllTimeSeason.csv` for complete historical team stats
2. **Baseball Data Hub** — Download full NL standings JSON/CSV for every season 1871–2026
3. **Baseball Reference** — Scrape or use provided API for year-by-year standings tables

## Data Conventions

- Win-loss records use standard W-L format (e.g., 116-36)
- Win percentages rounded to 3 decimal places (.XXX format)
- Division alignment reflects current division assignment
- "Championship" = World Series win; "Pennant" = NL league championship
- Shortened seasons noted with original scheduled games
- MVP words corrected to standard formatting
