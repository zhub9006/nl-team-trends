# NL Team Trends - Research Notes & Methodology

## Research Phase 1: Source Discovery

### Searches Conducted
- National League MLB team win-loss records historical statistics by season
- MLB National League team performance trends historical data all-time
- National League NL team standings by year 1876 to 2024 complete historical data
- site:baseball-almanac.com National League year by year history standings 1876

### Top Sources Identified
1. Baseball-Reference.com - Official NL year-by-year standings
2. BaseballAlmanac.com - NL team-vs-team W-L matrices (1876-2026)
3. SABR Lahman Database - Free downloadable CSV (1871-2025)
4. BaseballDataHub.com - Complete season standings archive
5. StatsCrew.com - NL rosters, standings & leaders
6. Retrosheet.org - Box scores and team records
7. StatMuse.com - NL championship leaders & franchise stats
8. OpenIntro.org/data - ML-ready MLB team data

## Research Phase 2: Key Data Extracted

### NL Founding & Evolution
- NL Founded: February 2, 1876 (replacing National Association); 150th anniversary: 2026
- Original 8 teams (1876): Boston Red Caps, Chicago White Stockings, Cincinnati Reds, Hartford Dark Blues, Louisville Grays, Philadelphia Athletics, Brooklyn Mutuals, St. Louis Browns
- NL expanded: 8 (1876) -> 12 (1900) -> 16 (1969) -> 15 (1998)
- Key relocations: Brooklyn -> LA (1958), NY Giants -> SF (1958), Montreal -> Washington (2005)

### Schedule Eras
- 1876-1884: 60-112 game schedules, variable
- 1885-1908: 126-154 games, 154-game era begins ~1892
- 1909-1961: 154-game consistent schedule
- 1962-2019: 162-game schedule
- 2020: 60-game COVID season
- 2021-present: Full 162 games

### Championship Highlights
- Best single-season win%: 1906 Cubs (116-36, .763) - NL record
- Most WS titles (NL): St. Louis Cardinals (11)
- Most NL pennants: LA Dodgers (26 through 2025) tied with Cardinals
- Longest pennant drought: Chicago Cubs (108 years, 1945-2016)
- Back-to-back WS champions: LA Dodgers (2024, 2025)
- 8 straight NL West: LA Dodgers (2018-2025)
- 14 consecutive division titles: Atlanta Braves (1991-2005)
- 1994 season voided by players' strike

### All-Time W-L Matrix (Baseball Almanac, 1876-2026)
- LA Dodgers: 278W-122L vs CHN (.695); 272W-128L vs all NL (.680)
- SF Giants: 272W-128L vs all NL (.680)
- Cincinnati Reds: 278W-122L vs all NL (.695)
- Atlanta Braves franchise: historically dominant through relocations

### Year-by-Year Highlights
- 1876: Chicago WSS 52-14 (.788) - 1st NL champion
- 1878: Boston Red Caps 41-19 (.683) - first non-Chicago champion
- 1906: Chicago Cubs 116-36 (.763) - best NL single-season record
- 1914: Boston Braves 94-59 (.613) - NL champion & WS champs
- 1969: NY Mets 100-62 - Miracle Mets NL champ/WS champs
- 1975: Cincinnati Reds 108-54 - Big Red Machine
- 1994: Season voided
- 2016: Chicago Cubs 103-58 - 108-year NL pennant drought ends
- 2024: LA Dodgers 98-64 (.605) - NL pennant; WS runner-up
- 2025: LA Dodgers 93-69 - back-to-back WS champions

## Research Phase 3: Data Compilation

### CSV Files Compiled
- nl_historical_performance.csv: Year-by-year NL champion + 2nd place + WS outcomes
- nl_all_time_records.csv: All-time franchise win-loss totals and championship counts
- nl_notable_records.csv: Key records with context notes
- nl_championship_trends.csv: Era-based championship trend data
- nl_notable_seasons.csv: Significant seasons with key statistics

### Historical Data Gaps & Limitations
- NL pennant winners before 1903 have no WS data (WS began in 1903)
- 1994 and 1981 split-season data requires special handling
- Early-season team names differ from modern names
- Negro Leagues data being integrated (Lahman 2025+)

## Methodology

1. Source Validation: Cross-referenced Baseball Almanac with Baseball-Reference
2. Franchise Continuity: All records include pre-relocation data
3. Era Classification: 10-year buckets (1870s, 1880s, etc.)
4. Win% Normalization: Not directly comparable across schedule lengths
5. Pennant Counting: Counts NL pennants incl. pre-WS era
6. WS Counting: Counts NL appearances in WS

## Next Steps
- Build win% trend visualizations per franchise
- Create era-based heatmaps of championship distribution
- Add head-to-head matchup matrices from Baseball Almanac
- Develop interactive Streamlit dashboard
- Cross-reference with Lahman CSV data for player-level stats
- Add NLCS & World Series series-level data