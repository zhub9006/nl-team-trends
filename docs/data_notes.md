# NL Team Trends — Data Notes & Methodology

## Overview

This document provides detailed methodology notes, data conventions, and caveats for the datasets in the `data/` directory. **This version has been updated with comprehensive research data** compiled from primary and secondary baseball reference sources.

---

## Data Collection Approach

### Primary Collection
- Manual extraction from authoritative baseball reference sources
- Cross-referencing across multiple sources for accuracy
- Integration of franchise movement data for historical continuity

### Additional Data Sources Used (Current Version)
| Source | URL | Coverage | Data Used For |
|--------|-----|----------|---------------|
| Baseball Almanac (NL H2H) | https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml | 1876-2026 | Complete head-to-head 15x15 matrix |
| Everything Explained Today | https://everything.explained.today | 1876-2025 | All-time franchise W-L & postseason data |
| Champs or Chumps | https://champsorchumps.us | 1876-2026 | NL division champions, best/worst records |
| Linger & Look | https://lingerandlook.com | 1901-present | Year-by-year standings with managers |
| MLB.com | https://www.mlb.com | All seasons | WS champions, team records, franchise history |
| Baseball Data Hub | https://baseballdatahub.com | 1871-2026 | Complete season archives, standings |
| ESPN | https://www.espn.com | 1903-present | WS champions, series results |
| Wikipedia | https://en.wikipedia.org | All eras | Pennant winners, NL history |
| Retrosheet | https://www.retrosheet.org | 1871-present | Box scores, team records |
| SABR Lahman Database | https://sabr.org | 1871-2025 | Free downloadable CSV datasets |

---

## Era Definitions

| Era | Years | Teams | Schedule Games | Key Characteristics |
|-----|-------|-------|----------------|---------------------|
| Founding Era | 1876–1891 | 8 (variable) | 60–140 | Original 8 teams; small rosters; two-league era ends |
| Merger Era | 1892–1902 | 12→8 | 132–154 | NL-AA merger; 154-game schedule; league shrinkage |
| Transition Era | 1903–1919 | 8–10 | 154 | First modern WS; Dead Ball Era; 1919 Black Sox scandal |
| Expansion Era | 1920–1968 | 8–10 | 154 (1962+) | Integration; franchise mobility; pitching dominates (1968) |
| Modern Era | 1969–present | 12–15 | 162 | Divisional split; NLCS/NLDS; free agency; labor disputes; 3-division from 1995 |

---

## Schedule Lengths by Era

- **1876–1877**: ~60-66 games
- **1878–1882**: ~84 games
- **1883**: ~98 games
- **1884**: ~112 games
- **1885–1891**: ~126-136 games
- **1892–1900**: ~130-154 games
- **1901–1961**: 154 games
- **1962–2019**: 162 games
- **2020**: 60 games (COVID-19 pandemic)
- **2021–present**: 162 games (plus interleague play guidelines)

---

## Franchise Movement History

| Original Franchise | Current Status | Notes |
|-------------------|----------------|-------|
| Boston Red Stockings | Atlanta Braves | Est. 1871; Boston→Milwaukee→Atlanta |
| Brooklyn Atlantics | — | NL original 1876; departed after 1876 |
| New York Mutuals | — | NL original 1876; expelled after 1876 |
| Philadelphia Athletics | — | NL original 1876; expelled after 1876 |
| St. Louis Brown Stockings | — | NL original 1876; folded (SA scandal then) |
| Hartford Dark Blues | — | NL original 1876; folded 1877 |
| Louisville Grays | — | NL original 1876; folded 1878 |
| Cincinnati Reds (1876) | Cincinnati Reds today | Continuous NL franchise (oldest, 1876) |
| Chicago White Stockings | Chicago Cubs today | Continuous NL franchise (1876 oldest identity) |
| Brooklyn → LA Dodgers | LA Dodgers today | Moved to LA 1958 |
| New York → SF Giants | San Francisco Giants today | Moved to SF 1958 |
| Montreal Expos → Washington Nationals | Washington Nationals today | Moved to DC 2005 |

---

## Division Realignment Timeline

| Period | Structure | Notes |
|--------|-----------|-------|
| Pre-1969 | No divisions | Best regular-season record wins NL pennant |
| 1969–1993 | NL East, NL West (2 divisions) | Excess of rivals; 1969 Mets Miracle |
| 1994 (Aug) | NL East, NL Central, NL West | Owners voted to restructure mid-season |
| 1995-present | NL East, NL Central, NL West + Wild Card | 3-division format with wild card |
| 2022-present | 6 divisions, 3 wild cards per league | 12-team postseason field; balanced schedule |

---

## Notable Anomalies & Data Considerations

### Tie Games
- Ties were common pre-1920s; many 1876-1884 seasons have ties
- 2007 rule change: ties only occur if last scheduled matchup and no postseason implications
- Modern eras: Tie games are extremely rare

### 1994 Season
- Players' strike began Aug 12; remainder of season and postseason cancelled
- Montreal Expos had MLB's best record at time of cancellation (74-40)
- Only season since 1904 without a World Series

### 2020 Season
- COVID-19 pandemic reduced season to 60 games
- 10-game doubleheaders; expanded playoffs (16 teams)
- LA Dodgers won the shortened-season WS

### Pre-WS Era (1884-1902)
- 1884-1902: Interleague "World Series" or championship series played between NL and AA
- 1900-1902: NL pennant team technically best record without formal World Series
- 1903: First official modern World Series
- 1904: NY Giants declined to play World Series

### Franchise Relocation Impact
- Brooklyn Dodgers → LA Dodgers (1958): Split Dodgers fanbase; West Coast identity
- NY Giants → SF Giants (1958): Ended NY baseball landscape; "1951 Shot" became SF foreshadowing
- Boston/Milwaukee → Atlanta Braves (1966): Moved to capitalize on growing South
- Montreal → Washington Nationals (2005): Returned baseball to DC after 33-year absence

### Data Discrepancies
- Some sources report slightly different franchise game counts due to classification (e.g., did pre-1876 NA counts, franchise move treatment)
- H2H data sourced from Baseball Almanac (updated daily) may differ slightly from Retrosheet or Lahman database counts
- All-time win percentages are cross-validated but may reflect slightly different inclusion criteria (e.g., interleague play pre-1997)
- All data in this repository reflects the **current NL 15-team format consistent with modern franchise names**

---

## Data File Conventions

### CSVs
- All datetime values are ISO 8601 format (YYYY-MM-DD)
- Team names are canonical current NL names
- Win percentages are stored as decimals (0.000-1.000)
- Division abbreviations: NL East, NL Central, NL West

### JSON
- Supplementary data with nested structures
- Sourced from primary sources; data in nested objects match the CSV contents
- Used for relationship & hierarchy data that doesn't fit flat CSV format

---

## Replication & Auditing

Researchers and contributors are encouraged to:
1. Cross-reference all Oscar data with ret sourceys
2. Use the SABR Lahman Database as computational baseline
3. Submit corrections via GitHub issues with source citations
4. Annual audit after each World Series season
