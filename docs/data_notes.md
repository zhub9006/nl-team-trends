# NL Team Trends – Data Collection & Methodology Notes

## Data Sources Used

### Primary Sources

| Source | URL | Coverage | Value |
|--------|-----|----------|-------|
| Baseball Almanac | baseball-almanac.com/teams/teamvsteam-nl | 1876–2026 | Team-vs-team W-L matrices updated daily |
| Baseball Reference | baseball-reference.com/leagues/NL | 1876–present | Season-by-season standings, leaders |
| Baseball Data Hub | baseballdatahub.com/seasons | 1871–2026 | 156 MLB seasons with full stats |
| Grokipedia | grokipedia.com | 1876–2025 | All-time franchise W-L records, verified 2025 season |
| Lahman Database (SABR) | sabr.org/lahman-database | 1871–2025 | Complete historical team, batting, pitching stats |
| StatMuse | statmuse.com/mlb | Present | Current NL standings aggregate analysis |

### National League Historical Context

- **Founded**: February 2, 1876 — oldest continuously operating professional sports league
- **Original 8 teams**: Boston Red Stockings, Chicago White Stockings, Hartford Dark Blues, Louisville Grays, Mutuals NY, Philadelphia Athletics, St. Louis Brown Stockings, Cincinnati Red Stockings
- **Key expansion dates**:
  - 1962: NY Mets, Houston Colt .45s
  - 1969: San Diego Padres, Montreal Expos
  - 1993: Colorado Rockies, Florida/Miami Marlins
  - 1998: Arizona Diamondbacks, Milwaukee Brewers (moved from AL)
- **Divisions**: East/Central/West since 1994; 15 teams per league since 1998
- **Interleague play**: Started 1997; expanded to full-season in 2023
- **Wild Card**: Introduced 1994/95; second WC added 2012

## Data Conventions

### Win Percentage Calculation
- Win% = Wins / (Wins + Losses), rounded to 3 decimal places
- Ties (common pre-1920) excluded from denominator
- Pre-1920 games that were suspended/dark: re-seeded or not counted

### Franchise Continuity
Relocated and renamed teams treated as continuous entities:

| Current Franchise | Historical Names |
|-------------------|-----------------|
| San Francisco Giants | New York Giants (1883-1957) |
| Atlanta Braves | Boston Red Stockings (1871-75), Boston (1876-1906), Doves (1907-10), Braves (1912-35, 1941-52), Milwaukee Braves (1953-65) |
| Los Angeles Dodgers | Brooklyn Atlantics/Dodgers/Robins/Superbas/Bridegrooms (1883-1957) |
| Philadelphia Phillies | Same continuously since 1883 |
| Washington Nationals | Montreal Expos (1969-2004) |

### Schedule Length Eras
- **40–80 games**: 1876–1880s (NL's first decade)
- **100–140 games**: 1890s (expansion era)
- **154 games**: 1892–1960 (standard schedule)
- **162 games**: 1961–present (post-expansion)
- **Shortened**: 1918 (WWI, ~130 games), 1981 (player strike, split season), 1994–95 (strike), 2020 (COVID-19, 60 games)

## Known Data Quality Issues

1. **Pre-1900 Records**: May contain inconsistencies from multiple league structures, incomplete game logs, and differences in scoring
2. **Tie Games (T column)**: Inconsistently recorded in early NL eras
3. **Early Franchise Names**: Don't match modern listings (e.g., "Boston Beaneaters" not "Braves")
4. **Pouríts**
5. **Houston Astros**: Played NL 1962-2012, AL from 2013 — NL data truncated
6. **1904 Season**: No World Series played (Giants refused challenge)
7. **1876 NL Season**: Only 6 of 8 teams completed full schedule (Cincinnati folded mid-season)

## Repository File Overview

### `data/nl_team_records.csv`
All-time franchise aggregate records (33 entries including historical/expanded franchises). Columns: team, franchise_start, seasons_played, total_wins, total_losses, win_pct, pennants, pennant_pct, ws_titles, ws_pct, last_pennant, last_ws, notes.

### `data/nl_pennant_winners.csv`
130 rows spanning 1876-2025. Columns: year, team, league, record, win_pct, games_behind, pennant_winner (Y/N), world_series_winner (Y/N), notes. Covers pennant winners only.

### `data/nl_key_seasons.csv`
204 rows spanning 1876, 1906, 1908, 1912, 1916, 1919, 1924, 1926, 1930, 1931, 1937, 1951, 1954, 1955, 1969, 1975, 1976, 1986, 1995, 2012, 2016, 2020, 2021 — full standings per season. Columns: year, team, wins, losses, win_pct, games_behind, division, team_founded, notes.

### `docs/data_notes.md` (this file)
Methodology, source descriptions, conventions, known issues.

## Visualization Suggestions

1. **Franchise Win Trajectory by Era** — Dead Ball (1900-19), Live Ball (1920-41), Post-War (1946-68), Modern Expansion (1969-93), Analytics (1994-Present)
2. **Pennant Frequency Heatmaps** — 5-year rolling window dominance patterns
3. **Win% Distribution by Division** — competitive balance over time
4. **Post-WWII Franchise Longevity** — consecutive winning-season runs
5. **Relocation Impact** — pre/post move franchise performance
6. **Expansion Adjustment Curves** — typical 7-10 year ramp for new franchises
7. **Run Differential Correlation** — run diff vs. pennant wins across eras
8. **Home/Away Splits** — through-the-decades deep-dive

## Contributing

Data corrections and additions welcome via PR. Always cite the primary source for any new data added.