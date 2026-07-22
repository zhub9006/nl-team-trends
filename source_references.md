# NL Team Trends — Source References & Methodology

## Primary Data Sources

### 1. Baseball-Reference (NL)
- **URL**: https://www.baseball-reference.com/leagues/NL/
- **Coverage**: 1876–present
- **Data**: Official year-by-year NL standings, team batting/pitching stats, league leaders
- **Authority**: Gold-standard public baseball statistics reference maintained by Sports Reference

### 2. Baseball Almanac (Year-by-Year)
- **URL**: https://www.baseball-almanac.com/yearmenu.shtml
- **Coverage**: 1876–present
- **Data**: NL leadership, W-L records by franchise, fabulous feats, seasonal summaries
- **Authority**: Independent one of the longest-running baseball research archives

### 3. Baseball Almanac (H2H Matrix)
- **URL**: https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml
- **Coverage**: 1876–2026
- **Data**: 15×15 head-to-head win-loss matrix for every NL team vs every other NL team
- **Note**: Includes franchise moves (e.g. SF Giants line includes NY Giants era)

### 4. Baseball Data Hub
- **URL**: https://baseballdatahub.com/seasons/
- **Coverage**: 1871–2026
- **Data**: Complete season-by-season standings, batting/pitching leaders, postseason results
- **Strength**: Clean data export; browsable by season with full leaderboards

### 5. SABR Lahman Database
- **URL**: https://sabr.org/lahman-database/
- **Coverage**: 1871–2025 (plus Negro Leagues)
- **Data**: Free downloadable CSV dataset with full team, batting, pitching, fielding, standings, manager, and postseason data
- **Key Note**: Industry-standard format for programmatic MLB analysis

### 6. Baseball Almanac (World Series Winners)
- **URL**: https://www.baseballstandard.com/list-of-mlb-world-series-winners-4290706/
- **Coverage**: 1903–present
- **Data**: Complete WS winners list by year with results

### 7. StatMuse MLB
- **URL**: https://www.statmuse.com/mlb
- **Coverage**: 1876–2026
- **Data**: League/national standings, franchise W/L/G, championships, batting/pitching aggregates, various search queries

### 8. ESPN (World Series History)
- **URL**: https://www.espn.com/mlb/worldseries/history/winners
- **Coverage**: 1903–present
- **Data**: World Series champions, opponents, series results

### 9. Wikipedia Articles
- **NL Pennant Winners**: https://en.wikipedia.org/wiki/List_of_National_League_pennant_winners
- **All-Time W-L Records**: https://en.wikipedia.org/wiki/List_of_all-time_Major_League_Baseball_win-loss_records
- **Coverage**: 1876–present

### 10. Champs or Chumps
- **URL**: https://champsorchumps.us/mlb
- **Coverage**: 1876–present
- **Data**: Win% rankings, longest droughts, winning/losing streaks, postseason series records

## Source Cross-Verification Principles

1. **NL standings data** (per-season): Primary = Baseball Data Hub; Verified = Baseball-Reference NL; Cross-checked = Baseball Almanac.
2. **All-time W-L totals**: Primary = StatMuse; Verified = Grokipedia/Wikipedia.
3. **H2H matrices**: Primary = Baseball Almanac NL team-vs-team page (1876–2026).
4. **Championship & pennant results**: Primary = Baseball Almanac WS list; Verified = ESPN and Wikipedia NL pennant winners.
5. **ERA classification**: Based on conventional baseball history eras.

## Known Limitations & Caveats

- **1994 season**: Incomplete — 68–46 for the Reds (best record cancelled by players' strike). No postseason or World Series.
- **2020 season**: 60-game COVID-19 shortened season. Records not directly comparable to full 162-game seasons.
- **Pre-WS era (pre-1903)**: Champions determined by best regular-season record (or AA interleague Series). WS records noted separately.
- **Franchise relocations**: Brooklyn → LA (1958), NY Giants → SF (1958), Montreal Expos → Washington Nationals (2005), Milwaukee Braves → Atlanta (1966). Cumulative records transfer with the franchise.
- **H2H data**: Includes all games under NL-only and interleague formats. Interleague play began in 1997.
- **Ties**: Pre-1900 ties were more common; modern format requires extra innings until decisive result.

## Data Conventions

1. All win-loss records refer to **regular-season** games only (noted exceptions for WS/NLCS results).
2. "NL_champion" refers to the NL pennant winner (not necessarily the WS champion).
3. Postseason results listed when applicable (WS and NLCS, when applicable).
4. 1994 season marked with "Season cancelled by strike."
5. Franchise names given as current canonical name with historical aliases noted.
6. Pre-1900 seasons may have non-standard game counts (60–112 games).
7. Win percentages rounded to 3 decimal places.
8. Era classifications:
   - **Founding Era**: 1876–1881 (original 8 teams, varied schedules, pre-WS)
   - **Merger Era**: 1882–1891 (12+ teams, AA competitors, pre-WS)
   - **Transition Era**: 1892–1902 (12 teams, first NLCS, first WS)
   - **Expansion Era**: 1903–1960 (first expansion; 154-game schedule)
   - **Modern Era**: 1961–present (162-game schedule, division format, playoffs)
