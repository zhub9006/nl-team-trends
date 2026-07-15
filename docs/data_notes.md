# Data Notes: Methodology, Conventions & Caveats

## Methodology

1. **Source Triangulation** — All figures cross-referenced against at least 2 sources (Baseball Reference + SABR Lahman / Baseball Almanac)
2. **Era Classification** — Eras defined by both schedule format changes and competitive shifts (e.g., 1969 division split, 1994 playoff reform, 2020 COVID season)
3. **Franchise Continuity** — Team records trace franchise lineage including relocated/renamed teams (e.g., Brooklyn Dodgers → LA Dodgers; Boston Braves → Milwaukee → Atlanta)
4. **Win-Loss Accuracy** — Postseason records included in regular-season totals for championships; separate postseason data tracked in key_seasons.csv

## Conventions

| Convention | Detail |
|------------|--------|
| Record Format | Win-Loss (e.g., 116-36) |
| Win Percentage | 3 decimal places (.XXX) |
| Division | Current division assignment (not historical) |
| Era Boundaries | Based on both schedule format AND competitive periods |
| Championship Count | World Series wins only (not pennants) |
| Games | Scheduled regular-season games (adjusted for shortened seasons) |

## Known Caveats

- **1876–1891**: No divisions existed; W-L records based on full-season totals
- **1994 Season**: Strike ended season early; Atlanta Braves had best record at time of cancellation (68-46 .596)
- **2020 Season**: 60-game schedule; records not comparable to full seasons
- **Interleague Play** (1997–2022): Teams played uneven interleague schedules; Win% slightly affected
- **2022+**: 12-team playoff format changes competitive dynamics significantly
- **Franchise Relocations**: Some stats may differ across sources due to how they count Milwaukee Braves / Washington Nationals history
- **1906 Cubs**: 116-36 is the official record; some sources list 116-37 due to tie games

## Data Quality Notes

- Pre-1900 data is most susceptible to scoring discrepancies
- 1876–1892 seasons had ties that were sometimes replayed, occasionally counted differently
- The 1994 strike makes the "best record" stat ambiguous for that year
- The 2020 COVID season is the most radically altered schedule in modern history
