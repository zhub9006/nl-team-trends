# Research Sources — NL Team Trends

Comprehensive list of all sources consulted to compile the historical National League performance data, win-loss records, and championship information in this repository.

---

## Primary Statistical Databases

### 1. Baseball Data Hub (baseballdatahub.com)
- **URL**: https://baseballdatahub.com/seasons/
- **Description**: Complete season-by-season MLB history from 1871 to 2026, including final standings, batting and pitching leaders, postseason results, and team records for every season. Pages for individual seasons (e.g. `/seasons/1876`, `/seasons/1906`, `/seasons/1969`, `/seasons/1975`, `/seasons/1984`, `/seasons/1995`, `/seasons/1998`, `/seasons/2020`, `/seasons/2023`, `/seasons/2024`, `/seasons/2025`) were fetched and used for all season standings data in `data/season-standings.csv`.
- **Data extracted**: Final divisional standings, league leaders (batting, pitching), postseason brackets, FAQ context for notable seasons.
- **Date consulted**: July 2026.

### 2. SABR Lahman Database (Society for American Baseball Research)
- **URL**: https://sabr.org/lahman-database/
- **Description**: The canonical open-source baseball dataset, containing complete batting and pitching statistics from 1871 to 2025, plus fielding statistics, standings, team stats, managerial records, postseason data, and Negro Leagues data. Available in SQL, Microsoft Access, and CSV formats.
- **Data extracted**: Structural reference for all numerical data in this repository. All franchise records, historical win-loss totals, and era definitions align with Lahman conventions.
- **License**: Creative Commons (CC BY 3.0)
- **Date consulted**: July 2026.

### 3. Baseball-Reference.com
- **URL**: https://www.baseball-reference.com/leagues/NL/index.shtml
- **Description**: The most comprehensive box-score and statistical database for MLB history. The NL-specific page provides league leaders, seasonal summaries, and franchise-level records. Standings pages (e.g. `/leagues/majors/2024-standings.shtml`) provide divisional breakdowns.
- **Data extracted**: League leader context, team-level statistics, postseason results used for cross-referencing other sources.
- **Date consulted**: July 2026.

### 4. Baseball Almanac
- **URL**: https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml (team-vs-team NL win-loss, 1876-2026)
- **URL**: https://www.baseball-almanac.com/yearmenu.shtml (year-by-year NL history)
- **URL**: https://www.baseball-almanac.com/yearly/yr2024n.shtml (2024 NL season)
- **Description**: Comprehensive year-by-year historical research project including NL standings for every season, all-time NL team-vs-team win-loss matrix (every head-to-head matchup from 1876 through 2026), and leader data. Franchise moves are included.
- **Data extracted**: All-time NL team-vs-team win-loss matrix (used for network analysis possibilities); 2024 NL standings and leaders; historical context notes; year-by-year roster data pointers.
- **Date consulted**: July 2026.

### 5. StatsCrew.com
- **URL**: https://www.statscrew.com/baseball/l-NL/y-2024 (2024 NL standings)
- **Description**: Detailed season-by-season team standings and rosters. Each season page provides final standings, award winners, league leaders, and All-Star rosters.
- **Data extracted**: 2024 NL final standings (all 15 teams, all 3 divisions).
- **Date consulted**: July 2026.

### 6. Statpedia
- **URL**: https://www.statpedia.net/team-stats.html
- **Description**: Interactive team stat explorer allowing users to explore any MLB team's performance across every season. Features stat-by-season charts with benchmark tiers, current season game logs, division standings, and detailed breakdowns for both regular season and postseason.
- **Data extracted**: Conceptual framework for visualization tiering system (benchmark tiers used in `visualizations/visualize.py`); team-level stat tool concepts.
- **Date consulted**: July 2026.

---

## Encyclopedic Sources

### 7. Wikipedia — List of All-Time MLB Win-Loss Records
- **URL**: https://en.wikipedia.org/wiki/List_of_all-time_Major_League_Baseball_win%E2%80%93loss_records
- **Description**: Authoritative list of all-time regular season win-loss records for every MLB franchise, including NL teams. Describes formation of AL (1901) and NL (1876), and provides franchise-level historical context.
- **Data extracted**: All-time NL franchise W-L records used in `data/nl-franchise-records.csv`; recognition of NL and AL formation dates (1876 and 1901).
- **Date consulted**: July 2026.

### 8. Wikipedia — List of National League Pennant Winners
- **URL**: https://en.wikipedia.org/wiki/List_of_National_League_pennant_winners
- **Description**: Complete list of NL pennant winners from the league's founding in 1876 to the present, including pre-playoff era champions and modern-era playoff pennant winners.
- **Data extracted**: All NL pennant winners (used in the README pennant tables for franchise-level counts).
- **Date consulted**: July 2026.

### 9. MiscSchedule.net — World Series Winners by Year
- **URL**: https://www.mlbschedule.net/blog/world-series-winners-by-year
- **Description**: Complete year-by-year list of World Series winners and runners-up from 1903 to 2025, including series results and notable context. Includes explanation of the 1904 and 1994 cancellations.
- **Data extracted**: All World Series results from 1903-2025, used to cross-reference NL champion outcomes and identify NL champions who won or lost the Fall Classic. Division data noted for modern-era context.
- **Date consulted**: July 2026.

---

## Official Sources

### 10. MLB.com
- **URL**: https://www.mlb.com/standings/regular-season/mlb/2023 (2023 official standings)
- **Description**: Official MLB standings and postseason results, with division and league standings for regular season and playoff formats.
- **Data extracted**: Cross-referencing divisional results; official recognition of playoff and Wild Card formats.
- **Date consulted**: July 2026.

### 11. MLB.com — Dodgers Win 2025 World Series
- **URL**: https://www.mlb.com/news/dodgers-win-2025-world-series
- **Description**: Official coverage of the 2025 World Series, confirming the Dodgers as the repeat champion. Reports that LA defeated Toronto in 7 games, becoming MLB's first repeat champion since 2000 Yankees.
- **Data extracted**: 2025 WS result confirmation; official narrative on Dodgers dynasty status.
- **Date consulted**: July 2026.

---

## Secondary Historical Sources

### 12. Baseball Almanac — MLB History Year-by-Year
- **URL**: https://www.baseball-almanac.com/yearmenu.shtml
- **Description**: High-level year-by-year historical overview of every MLB season, including NL (1876-2027), AL (1901-2027), Federal League (1914-1915), Players League (1890), and Union Association (1884). Each season page includes league leaders, final standings, team rosters, retirements, rookies, salaries, and historical tidbits.
- **Data extracted**: Era handbooks, historical context notes, schedule evolution information.
- **Date consulted**: July 2026.

### 13. Baseball Almanac — 2024 NL Season Summary
- **URL**: https://www.baseball-almanac.com/yearly/yr2024n.shtml
- **Description**: Detailed 2024 NL season recap including team standings, player review (hitting and pitching leaders), rule changes, and management/team changes.
- **Data extracted**: 2024 NL standings (cross-validated with StatsCrew); 2024 NL league leaders; 2024 season context.
- **Date consulted**: July 2026.

### 14. Baseball Almanac — National League Team vs Team Win-Loss Data
- **URL**: https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml
- **Description**: Franchise-versus-franchise all-time win-loss matrix for the National League from 1876 through 2026 (updated daily). Includes all historical franchise relocations.
- **Data extracted**: Head-to-head historical matchup data for potential network analysis, rivalry section visualizations, and cross-franchise dominance analysis.
- **Date consulted**: July 2026.

---

## Other Notable Sources

### 15. Wikipedia — List of World Series Champions
- **URL**: https://en.wikipedia.org/wiki/List_of_World_Series_champions
- **Description**: Comprehensive list of World Series results from 1903 to present, including descriptions of the 1904 boycott and 1994 strike cancellation.
- **Data extracted**: Series results (scores) from 1903 to 2025, which were used to annotate the WS Champions CSV with NL champions and their results.
- **Date consulted**: July 2026.

### 16. Wikiwand — List of National League Pennant Winners
- **URL**: https://www.wikiwand.com/en/List_of_National_League_pennant_winners
- **Description**: Mirror of Wikipedia's NL pennant winner list, with additional context on the Warren C. Giles Trophy and modern playoff format implications.
- **Data extracted**: Pennant winner verification for modern-era seasons.
- **Date consulted**: July 2026.

---

## Blog / News Sources

### 17. LA Times — Dodgers World Series 2025
- **URL**: https://www.latimes.com/sports/dodgers/story/2025-11-01/dodgers-world-series-2025-path-blue-jays
- **Description**: Coverage of the Dodgers' path through the 2025 postseason, including play-by-play of NLDS, NLCS, and WS victories.
- **Data extracted**: 2025 postseason path (Dodgers beat Cincinnati, Philadelphia, Milwaukee, Toronto); context on repeat championship achievement.
- **Date consulted**: July 2026.

### 18. WBSC — Dodgers Win 2025 World Series
- **URL**: https://www.wbsc.org/en/news/los-angeles-dodgers-win-world-series-for-the-ages-confirm-as-champions
- **Description**: International sports body coverage confirming Dodgers' back-to-back title and historical significance (first repeat champion since 2000 Yankees).
- **Data extracted**: Confirmation of 2025 WS result and Dodgers dynasty status.
- **Date consulted**: July 2026.

### 19. Los Angeles City Government — Dodgers Win 2025 WS Title
- **URL**: https://lacity.gov/news/los-angeles-dodgers-win-2025-mlb-world-series-title
- **Description**: Official city press release celebrating the Dodgers' championship. Reports 5-4 Game 7 victory in the 11th inning, franchise's 9th title.
- **Data extracted**: 2025 WS Game 7 details; franchise title count confirmation.
- **Date consulted**: July 2026.

---

## Data Integrity and Cross-Validation Notes

All data in this repository has been cross-validated against at least two sources where possible. Key validation pairs include:
- 2024 NL Standings: Baseball Almanac = ✓ | StatsCrew = ✓ | Baseball-Reference cross-check pending
- 2025 NL Standings: Baseball Data Hub = ✓ | Baseball Almanac cross-check pending
- 2020 NL Standings: Baseball Data Hub = ✓ | Wikipedia cross-check pending
- All-time franchise W-L: Wikipedia = ✓ | Baseball Almanac team-vs-team matrix = ✓
- NL pennant winners: Wikipedia = ✓ | Baseball Almanac = ✓ | MLB postseason history = ✓

The `data/world-series-nl-champions.csv` file uses the Baseball Almanac and Wikipedia combined as primary sources for NL pennant winners 1903-2025, with the MiscSchedule.net World Series data as verification for WS results.

---

## Data Format Notes

CSV files use the following conventions:
- Team names use current MLB names (after franchise relocations, historical names are not retained in CSV data)
- Win-loss records reflect regular season (not postseason) results
- Win percentages are calculated as wins / (wins + losses)
- `NA` values indicate either missing data or that the team does not apply (e.g., no WS title, team folded)
- The 2020 season reflects a 60-game truncated schedule due to COVID-19
- The 1994 season was cancelled mid-season on August 12; no standings are recorded for this year
- The 1904 season had no World Series (NY Giants NL champion refused to play)

All data reflects the end of the 2025 MLB regular season and postseason unless otherwise noted.

---

*For questions about data sources, methodology, or corrections, open a GitHub issue or submit a pull request.*
