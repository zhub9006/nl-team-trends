# Data Sources for NL Team Trends

This document catalogs all data sources used to compile the historical National League performance data in this repository.

## Primary Sources

### 1. Baseball Reference — Baseball-Reference.com
- **URL:** https://www.baseball-reference.com/leagues/NL/
- **URL:** https://www.baseball-reference.com/teams/NL/
- **Description:** The most comprehensive online database of MLB statistics. Provides season-by-season team records, franchise all-time leaders, league standings, and advanced metrics back to the founding of the National League in 1876.
- **Data Used:** All-time win-loss records, single-season franchise bests, division alignment history.

### 2. StatMuse — StatMuse.com
- **URL:** https://www.statmuse.com/
- **Description:** AI-powered sports search engine that aggregates and querying baseball statistics naturally. Useful for quick lookups of all-time franchise records and season-level comparisons.
- **Data Used:** Franchise win-loss totals and winning percentages referenced in initial data compilation.

### 3. Baseball Almanac — Baseball-Almanac.com
- **URL:** https://www.baseball-almanac.com/
- **Description:** Extensive baseball history resource with team-by-team head-to-head records, franchise timelines, and historical season summaries.
- **Data Used:** NL team-vs-team head-to-head win-loss matrix; franchise relocation and name-change timelines.

### 4. Lahman Baseball Database (SABR) — GitHub / SABR
- **URL:** https://github.com/chadwickbureau/baseballdatabank
- **Description:** The open-source Lahman Database, maintained by the Society for American Baseball Research (SABR). The most complete public baseball dataset, covering player and team statistics from 1871 onward.
- **Data Used:** Foundation dataset for all-time records, era-based analysis, and any future deep-dive statistical modeling.

### 5. Wikipedia / Grokipedia
- **URL:** https://en.wikipedia.org/wiki/National_League_(baseball)
- **Description:** General reference for franchise histories, expansion timelines, and contextual notes (e.g., franchise relocations, name changes).
- **Data Used:** Franchise founding dates, relocation history, World Series title counts, and pennant counts.

### 6. MLB.com Official Statistics
- **URL:** https://www.mlb.com/stats/
- **Description:** Official MLB statistics portal. Authoritative for current-season data and playoff records.
- **Data Used:** Verification of recent season records (2020–2025).

## Source Reliability Ranking

| Priority | Source | Reason |
|----------|--------|--------|
| 🥇 1st | Baseball Reference | Most comprehensive, consistently updated, community-verified |
| 🥈 2nd | Lahman Database (SABR) | Open-source, complete historical coverage, widely used in academic research |
| 🥉 3rd | MLB.com | Official source, authoritative for current data |
| 4th | Baseball Almanac | Good historical context, team-vs-team matrix |
| 5th | StatMuse | Convenient for quick queries, aggregates from other sources |
| 6th | Wikipedia | Useful for narrative context, but should be cross-referenced |

## Data Attribution

All data in this repository is compiled from publicly available records. Key attribution:

- **All-time franchise records** → Baseball Reference / Lahman Database
- **Team-vs-team head-to-head** → Baseball Almanac
- **Franchise histories and relocations** → Wikipedia / Baseball Reference
- **Era definitions and boundaries** → Standard MLB era classifications (per Baseball Reference)

## Methodology Notes

- Regular-season games only; postseason records excluded from all-time totals
- Ties (pre-1920) excluded from winning percentage calculations
- Franchise relocations treated as continuous entities (e.g., Brooklyn → LA Dodgers)
- Milwaukee Brewers' NL record begins at 1998 (transfer from AL)
- Washington Nationals' record includes Montreal Expos era (1969–2004)

---

*Last updated: 2025-2026 season*
