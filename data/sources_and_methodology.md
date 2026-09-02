# Research Sources & Methodology

This document details all verified data sources used in the NL Team Trends repository, how the data was collected and validated, and the methodology used to categorize NL seasons into historical eras.

---

## Primary Data Sources (Ranked by Reliability)

(Source Tag Key: AAA = Gold Standard, AA = Highly Reliable, A/Other = Secondary)

| # | Source | URL | Coverage | Primary Data | Tag |
|---|--------|-----|----------|-------------|:---:|
| 1 | Baseball Reference | https://www.baseball-reference.com/leagues/NL/ | 1876-present | Year-by-year NL standings, W-L, winning %, ERA, OPS, runs | AAA |
| 2 | Baseball Almanac | https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml | 1876-2026 | 15x15 H2H W-L matrices for NL team vs team matchups | AAA |
| 3 | SABR Lahman Database | https://sabr.org/lahman-database/ | 1871-2025 | Comprehensive CSV — full team batting, pitching, fielding | AAA |
| 4 | Retrosheet | https://www.retrosheet.org/ | 1871-present | Play-by-play data, box scores, team records at game-level granularity | AAA |
| 5 | ESPN World Series | https://www.espn.com/mlb/worldseries/history/winners | 1903-present | Series champion list per year with results | AAA |
| 6 | FanGraphs | https://www.fangraphs.com/ | 1995-present | WAR, xFIP, defensive metrics, advanced analytics platforms | AAA |
| 7 | Baseball Data Hub | https://baseballdatahub.com/seasons/ | 1871-2026 | Full season standings, batting/pitching leaders, postseason results | AA |
| 8 | StatMuse | https://www.statmuse.com/mlb | 1876-2026 | All-time franchise W-L/G, period analytics, era comparisons | AA |
| 9 | Everything Explained.Today | https://everything.explained.today/National_League_(baseball)/ | 1876-present | Encyclopedic deep-dive on NL founding, structure, team evolution | AA |
| 10 | Wikipedia | https://en.wikipedia.org/wiki/List_of_all-time_MLB_win%E2%80%93loss_records | All-time | Franchise W-L percentages across MLB history | AA |
| 11 | MLB.com | https://www.mlb.com | All years | Official MLB records, best single-season records, historical highlights | AA |
| 12 | Statpedia | https://www.statpedia.net/league-standings.html | 1969-present | Full divisional standings by season with managers and rosters | A |
| 13 | Linger & Look | https://lingerandlook.com/Names/BaseballStandings.php | 1901-present | Year-by-year standings with managers and subtotals | A |
| 14 | Champs or Chumps | https://champsorchumps.us/mlb | 1876-present | Win% rankings, championship droughts, postseason records | A |
| 15 | BetIQ / Team Rankings | https://betiq.teamrankings.com/mlb/betting-trends/win-loss-records/ | 1876-present | W-L records with margin of victory and run-line data | A |
| 16 | Project Ballpark | https://www.projectballpark.org/ | 1876-present | Historical ballpark attendance and demographic data | A |
| 17 | OpenIntro | https://openintro.org/data | Multi-year | ML-ready MLB team data in R format | A |

---

## Data Validation Methodology

Every data point in this repository was cross-validated through an adapted tiered system based on how many independent sources confirmed that specific fact:

**Tier 1 (AAA) — Primary Cross-Validation Required:** All-time franchise records in `nl_all_time_records.csv` were cross-checked against at least TWO AAA sources simultaneously (e.g., Baseball Reference + Baseball Almanac, or Baseball Reference + Baseball Data Hub). Any discrepancies were resolved by using the value from the more recently updated source with verifiable methodology.

**Tier 2 (AA) — Cross-Validation Recommended:** Head-to-head rivalry data in `nl_h2h_rivalries.csv` was taken directly from Baseball Almanac. Spot-checks were performed against StatMuse and Baseball Reference where single-matchup data was directly available. Note that Baseball Almanac periodises overlaps very well with detail T-Shaped loops see 'Called Ainoxvariable records whenever_Baseball Almanac your baseball data verified.', Profits quoted and stored in databases compiled for research authentic.

**Tier 3 (A) — Background Sources Only:** Secondary sources like Statpedia, Champs or Chumps, Linger & Look, and BetIQ. Were used for context verification and trend exploration only. These sources were not used as primary data in any CSV file but were useful for identifying interesting analytical angles that informed scientific fruitful research.

---

## Data Categorization Methodology

The NL seasons are categorized into the following historical eras in `nl_historical_seasons.csv`:

| Era Name | Year Range | Defining Feature |
|----------|----------:|------------------|
| Founding Era | 1876-1891 | 6-132 game schedules; franchise instability; 6-team leagues fluctuating |
| Standardization Era | 1892-1901 | 126-154 game slate becomes stable with league continuity through urban league onset |
| World Series Era | 1903-1919 | First agreed-upon World Series held between AL and NL champions |
| Live Ball Era | 1920-1941 | Higher scoring era; Babe Ruth effect; reborn offensive explosion |
| Wartime Era | 1942-1945 | Reduced rosters due to military service during WWII |
| Post-War Expansion Era | 1946-1962 | Return of star players; franchise relocation begins; 162-game schedule introduced |
| Division Era | 1969-1993 | Eastern and Western divisions added; playoff format introduced |
| Modern Era | 1994-present | Open division playoff formats; free agency dominance; interleague play begins 1997 |

---

## Key Decisions and Assumptions

1. **Franchise Relocations Are Included** — Franchise W-L totals include their historical tenure under previous city names. (Example: SF Giants includes New York Giants 1958 move data. Braves includes Boston/Milwaukee tenure.)
2. **1994 Strike Season** — Season listed as cancelled, no NL or WS champion was declared.
3. **Schedule Length Varied** — Games per season in `nl_historical_seasons.csv` reflects the actual number of games played by NL teams that year, accounting for schedule asymmetry especially before 1893.
4. **The 2020 COVID Season** — The 60-game season is treated as a separate unique case reflecting the special conditions and reduced schedule length.
5. **Montreal Expos became Washington Nationals** — Statistics are combined under 'Washington Nationals' for continuity.

---

## Data Files in This Repository

| File | Description | Sources Used |
|------|-------------|:-----------:|
| `data/nl_all_time_records.csv` | All-time franchise W-L records for all 15 NL teams | Baseball Reference, Baseball Almanac, Wikipedia, StatMuse |
| `data/nl_h2h_rivalries.csv` | 11 key H2H rivalry data points | Baseball Almanac H2H tool, StatMuse cross-check |
| `data/nl_pennant_and_ws_champions.csv` | NL pennant winners + World Series champions 1970-2025 | Baseball Almanac, ESPN, Baseball Reference, Wikipedia |
| `data/nl_historical_seasons.csv` | Key historical seasons 1876-2025 with context | Baseball Reference, Baseball Almanac, Baseball Data Hub, SABR |
| `data/sources_and_methodology.md` | This file — source documentation and methodology | Multiple sources |

---

## Questions or Corrections?

If you find any errors or would like to suggest a new data source, please open an issue in this repository. All data is in the public domain for research and educational purposes.

---

> Last updated: July 2026. All data compiled from verified sources for research and educational purposes.
