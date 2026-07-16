# NL Team Trends - Research Notes & Methodology
# Detailed findings from the research conducted for this repository

## Research Phase 1: Source Discovery

### Searches Conducted
- National League MLB team win-loss records historical statistics by season
- MLB National League team performance trends historical data all-time
- National League NL team standings by year 1876 to 2024 complete historical data
- site:baseball-almanac.com National League year by year history standings 1876

### Top Sources Identified
1. Baseball-Reference.com - Official NL year-by-year standings, team-vs-team records
2. BaseballAlmanac.com - NL team-vs-team W-L matrices (1876-2026), year-by-year team reviews
3. SABR Lahman Database - Free downloadable CSV dataset covering 1871-2025
4. BaseballDataHub.com - Complete season standings & stats archive
5. StatsCrew.com - NL rosters, standings & leaders data
6. Retrosheet.org - Box scores and team records (1871-present)
7. StatMuse.com - NL championship leaders & franchise stats
8. OpenIntro.org/data - ML-ready MLB team data

## Research Phase 2: Data Extraction

### NL Founding & Evolution
- NL Founded: February 2, 1876 (replacing the National Association)
- 150th Anniversary: 2026
- Original 8 teams (1876): Boston Red Caps, Chicago White Stockings, Cincinnati Reds, Hartford Dark Blues, Louisville Grays, Philadelphia Athletics, Brooklyn Mutuals, St. Louis Browns
- NL expanded: 8 teams -> 12 (1900) -> 16 (1969) -> 15 (1998)
- Key relocations: Brooklyn -> LA (1958), NY Giants -> SF (1958), Montreal -> Washington (2005)

### Schedule Era Transitions
- 1876-1884: 60-112 game schedules, variable format
- 1885-1908: 126-154 games, 154-game era begins ~1892
- 1909-1961: 154-game consistent schedule
- 1962-2019: 162-game schedule
- 2020: 60-game COVID season
- 2021-present: Full 162 games

### Championship Highlights
- Best single-season win%: 1906 Cubs (116-36, .763)
- Most WS titles (NL): St. Louis Cardinals (11)
- Most NL pennants: LA Dodgers (26 through 2025) tied with Cardinals
- Longest pennant drought: Chicago Cubs (108 years, 1945-2016)
- Back-to-back WS champions: LA Dodgers (2024, 2025)
- 8 straight NL West: LA Dodgers (2018-2025)
- 14 consecutive division titles: Atlanta Braves (1991-2005)
- 1994 season voided by players' strike

### All-Time W-L Matrix (from Baseball Almanac, 1876-2026)
- LA Dodgers: 278W-122L vs CHN (.695), 272W-128L vs all NL (.680)
- SF Giants: 272W-128L vs all NL (.680)
- Cincinnati Reds: 278W-122L vs all NL (.695)
- Atlanta Braves franchise: historically dominant through relocations

### Year-by-Year Standings Highlights
- 1876: Chicago WSS 52-14 (.788) - 1st NL champion
- 1878: Boston Red Caps 41-19 (.683) - first non-Chicago champion
- 1906: Chicago Cubs 116-36 (.763) - best NL single-season record
- 1914: Boston Braves 94-59 (.613) - unexpected NL champion & WS champs
- 1969: NY Mets 100-62 - Miracle Mets NL champion & WS champs
- 1975: Cincinnati Reds 108-54 - Big Red Machine
- 1994: Season voided - no pennant or WS
- 2016: Chicago Cubs 103-58 - 108-year NL pennant drought ends
- 2024: LA Dodgers 98-64 (.605) - NL pennant; WS runner-up
- 2025: LA Dodgers 93-69 - back-to-back WS champions

## Research Phase 3: Data Compilation

### History significant seasons were compiled into CSV files:
- nl_historical_performance.csv: Year-by-year NL champion + 2nd place + WS outcomes
- nl_all_time_records.csv: All-time franchise win-loss totals and championship numbers
- nl_notable_records.csv: Key records with context notes
- nl_championship_trends.csv: Era-based championship trend data
- nl_notable_seasons.csv: Significant seasons with key statistics

### Historical Data Gaps & Limitations
- NL pennant winners before 1903 have no WS data (WS began in 1903)
- 1994 and 1981 split-season data requires special handling
- Early-season team names (Chicago WSS, Brooklyn Bridegrooms) differ from modern names
- Some 1940s/1950s WS MVP data may need verification against Baseball Reference
- Negro Leagues data is being integrated (Lahman 2025+ includes Seamheads data)

## Methodology & Cross-Referencing

1. Source Validation: Cross-referenced Baseball Almanac W-L matrices with Baseball-Reference standings for key eras
2. Franchise Continuity: All franchise W-L records include pre-relocation data (e.g., SF Giants = NY Giants + SSF Giants totals)
3. Era Classification: 10-year buckets (1870s, 1880s, etc.) except modern era adjustments for 2020 COVID season
4. Win% Normalization: Not directly comparable across schedule lengths (154 vs 162 vs 60 games)
5. Pennant Counting: Counts NL pennants (including pre-WS era); excludes AL pennants
6. WS Counting: Counts NL appearances in WS (not NL losses to AL)

## Next Steps
- Build win% trend visualizations per franchise using nl_historical_performance.csv
- Create era-based heatmaps of championship distribution using nl_championship_trends.csv
- Add head-to-head matchup matrices from Baseball Almanac data
- Develop interactive Streamlit dashboard
- Cross-reference with Lahman CSV data for richer player-level stats
- Add NLCS & World Series series-level data