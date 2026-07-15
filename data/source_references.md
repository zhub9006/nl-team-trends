# Source References for NL Team Trends Research

## Primary Data Sources

| # | Source | URL | Description | Coverage |
|---|--------|-----|-------------|----------|
| 1 | Baseball Reference | https://www.baseball-reference.com/leagues/NL/ | Year-by-year NL standings & statistical leaders | 1876–present |
| 2 | Baseball Almanac | https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml | NL team-vs-team win-loss matrices (full head-to-head) | 1876–2026 |
| 3 | Baseball Almanac | https://www.baseball-almanac.com/year_by_year/NLwinners.shtml | Year-by-year NL pennant & WS winners | 1876–present |
| 4 | SABR Lahman Database | https://sabr.org/lahman-database/ | Complete historical team/batting/pitching stats (open data) | 1871–2025 |
| 5 | Baseball Data Hub | https://baseballdatahub.com/seasons/ | Season standings archive for all MLB seasons | 1871–2026 |
| 6 | Wikipedia | https://en.wikipedia.org/wiki/List_of_all-time_MLB_win–loss_records | All-time franchise records & league comparisons | 1876–present |
| 7 | Wikipedia | https://en.wikipedia.org/wiki/National_League_(baseball) | NL history, structure & franchise timeline | 1876–present |
| 8 | StatsCrew | https://www.statscrew.com/baseball/l-NL | NL rosters, standings & team leaders | 1876–present |
| 9 | StatMuse | https://www.statmuse.com/mlb/ask/most-national-league-titles | NL championship leaders & franchise stats via AI | 1876–2026 |
| 10 | OpenIntro | https://www.openintro.org/data/index.php?data=mlb_teams | ML-ready MLB team dataset for analysis | Multi-year |

## Data Conventions

- Win% = Wins / Games Played (not all-win percentage; some games may not be counted in specific eras)
- Pennants = League championship awards (pre-Wild Card era, typically the team with the best record)
- WS Titles = World Series championships won while representing the NL
- All data through end of 2025 MLB season
- Pre-1961 seasons use a 154-game schedule; 1961+ uses a 162-game schedule
- 2020 season was shortened to 60 games due to COVID-19; noted as special case
- Franchise moves are included (e.g., SF Giants includes NY Giants data; ATL Braves includes Boston/Milwaukee Braves)
- Milwaukee Brewers switched from AL to NL in 1998; included in NL data from that point
- Montreal Expos became Washington Nationals in 2005; data continues from 1969 season

## Key Methodology Notes

1. **Franchise Continuity**: When a team relocated (NY→LA Dodgers, NY→SF Giants, Montreal→Washington), their historical record is combined under the current franchise name.
2. **Era Boundaries**: Era delineations align with major structural changes (division creation 1969, 3-division format 1994, 162-game schedule 1961, interleague play 1997, full interleague 2023).
3. **Head-to-Head Data**: The team-vs-team matrix from Baseball Almanac includes interleague and postseason results; use the all-time records table for pure regular-season franchise totals.
4. **Data Gaps**: Early seasons (1876–1892) have incomplete box scores in some sources; the Lahman Database is the most comprehensive for this period.
