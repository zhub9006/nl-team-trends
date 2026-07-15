# Source References — NL Team Trends

Detailed attribution for all data sources used in this repository.

## Primary Sources

### 1. Baseball Almanac — NL Team vs Team Win-Loss Records
- **URL:** https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml
- **Coverage:** 1876–2026 (updated daily during NL season)
- **Description:** Comprehensive head-to-head win-loss matrices for every NL franchise, including relocated teams' historical data (e.g., SF Giants includes NY Giants tenure)
- **Data used:** All-time franchise H2H records, most games won/lost, matchup-specific trends

### 2. Baseball Data Hub — Season-by-Season Standings
- **URL:** https://baseballdatahub.com/seasons/
- **Coverage:** 1871–2026 (156 seasons)
- **Description:** Browseable archive of every MLB season with full standings, batting leaders, pitching leaders, and postseason results
- **Data pulled (sample seasons):** 1876, 1900, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2015, 2020
- **Key detail:** Each season page includes NL standings with win-loss records, division placement, and championship markers

### 3. Everything Explained — All-Time MLB Win-Loss Records
- **URL:** https://everything.explained.today/List_of_all-time_Major_League_Baseball_win%E2%80%93loss_records/
- **Coverage:** 1876–2025 (2025 season completed)
- **Description:** Complete all-time franchise records ranked by win-loss percentage, including postseason data
- **Data used:** All-time NL franchise W-L totals, win percentages, games played, postseason records

### 4. SABR Lahman Baseball Database
- **URL:** https://sabr.org/lahman-database/
- **Coverage:** 1871–2025
- **Description:** The gold standard for historical baseball statistics; includes complete team batting, pitching, fielding, standings, managerial records, and postseason data
- **Data used:** Reference for statistical completeness and cross-validation

### 5. Baseball Reference — NL Division
- **URL:** https://www.baseball-reference.com/leagues/NL/
- **Coverage:** 1876–present
- **Description:** Official MLB historical statistics portal; season-by-season NL standings, league leaders, team records
- **Data used:** Verification of standings data and player/team statistics

### 6. Wikipedia — List of National League Pennant Winners
- **URL:** https://en.wikipedia.org/wiki/List_of_National_League_pennant_winners
- **Coverage:** 1876–2025
- **Description:** Complete list of NL pennant winners with pennant type (pre-division vs divisional era), record, and WS outcome
- **Data used:** Pennant winner identification, era classification, championship context

## Historical Context Sources

### National League Founding & Structure
- **Original 8 teams (1876):** Boston Red Stockings, Chicago White Stockings, Hartford Dark Blues, Louisville Grays, Mutuals (NY), Philadelphia Athletics, St. Louis Brown Stockings, Cincinnati Red Stockings
- **First fully professional league** to survive to the present day
- **Divisional era began 1969** (East/West); 3-division era began 1995 (East/Central/West)

### Key Franchise Relocations
| Current Franchise | Historical Names | Key Dates |
|------------------|-----------------|-----------|
| San Francisco Giants | NY Gothams/ Giants | 1883–1957 (NY), 1958–present (SF) |
| Los Angeles Dodgers | Brooklyn Bridegrooms/Superbas/Robins/Dodgers | 1883–1957 (Brooklyn), 1958–present (LA) |
| Atlanta Braves | Red Stockings/Beaneaters/Doves/Rustlers/Braves/Bees | 1871–1952 (Boston), 1953–1965 (Milwaukee), 1966–present (Atlanta) |
| Washington Nationals | Montreal Expos | 1969–2004 (Montreal), 2005–present (Washington) |

## Data Conventions & Caveats

1. **Win% = W ÷ (W+L)** — ties excluded from percentage calculation
2. **Franchise continuity** — relocated teams treated as continuous entities
3. **Schedule lengths:** 40–80 games (1870s) → 154 games (1892–1960) → 162 games (1961–present)
4. **Pre-1900 ties** were common (darkness/weather) and excluded from win percentages
5. **1994 season** — postseason cancelled due to strike; no NL pennant awarded
6. **2020 season** — 60-game COVID season; normalized metrics recommended for cross-era comparison
7. **Interleague play** began 1997; full-season since 2023 (not included in NL-only records)

## Data Validation

All CSV data files in the `data/` directory should be cross-validated against at least two sources when available. The `nl_all_time_records.csv` file uses the most recent verified totals through the end of the 2025 season.

## Acknowledgments

- SABR (Society for American Baseball Research) for maintaining the Lahman Database
- Baseball Almanac for daily-updated H2H matrices
- Baseball Data Hub for accessible season-by-season data
- Chadwick Bureau for the MLB statistical schema