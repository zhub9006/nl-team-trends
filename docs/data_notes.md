# Methodology, Conventions & Caveats

## Data Conventions

### Team Names
- Canonical NL team names are used throughout
- Franchise movements are noted parenthetically (e.g., "Brooklyn Superbas/Dodgers", "NY Giants/SF Giants")
- Historical names preserved where relevant (e.g., "Chicago White Stockings" for the 1876–1890s era)
- Relocated franchises treated as continuous entities (NY Giants → SF Giants, Brooklyn → LA Dodgers, Montreal Expos → Washington Nationals)

### Win-Loss Format
- Standard W-L-T format (Wins-Losses-Ties)
- Ties are excluded from win percentage calculations
- Win % = W / (W + L), rounded to 3 decimal places
- Regular-season wins only; postseason results tracked in separate fields

### Schedule Eras
| Era | Games/Season | Notes |
|-----|-------------|-------|
| 1876 | 60 | First season (varied) |
| 1878 | 84 | First full season |
| 1880s | 84–112 | Itinerant schedules |
| 1892 | 154 | Standard 154-game schedule begins |
| 1962 | 162 | Expansion to 162 games |
| 2020 | 60 | Shortened COVID season |
| 2021–present | 162 | Full 162-game schedule |

### Win Percentage by Era
- 154-game era: ~.564 = .500 (average)\\
- 162-game era: ~.560 = .500 (average)
- Use era-adjusted benchmarks when comparing across schedule lengths
- The 116-36 (.763) 1906 Cubs record was within a 154-game-era schedule (120 games that year)

## Key Caveats

1. **Schedule length variation**: Pre-1892 schedules varied from 60–140+ games per team. Do not compare raw win totals across eras without adjusting for schedule length.

2. **League composition changes**: The NL had as few as 4 teams in some years (1876–1882) and as many as 12 by 1900. Playoff structures also changed over time.

3. **Interleague play**: From 1997 onward, NL teams play regular-season games against AL opponents. Win-loss records in LCS/WS include both leagues.

4. **H2H data limitations**: Baseball Almanac's H2H matrices include historical team names but may have gaps in early years. Cross-reference with Lahman Database for highest accuracy.

5. **Tie handling**: Before 1920, ties were common. Many sources drop ties from W% calculations. Our convention excludes ties.

6. **Franchise continuity**: When a franchise relocated (NY Giants → SF Giants, Brooklyn → LA Dodgers, Montreal → Washington Nationals), all historical wins are attributed to the current franchise. This is the standard convention in MLB record-keeping.

7. **1994 season**: The MLB players' strike cut the 1994 NL season short (no WS was held). No NL champion was crowned.

## Data Quality Assurance

- Primary source: Lahman Baseball Database (CSV, updated quarterly)
- Verification: Cross-referenced against Baseball-Reference and Baseball Almanac
- H2H matrices: Sourced from Baseball Almanac (updated daily during season)
- Seasonal standings: Validated against multiple sources

## Suggested Analysis Approaches

1. **Era comparison**: Normalize W% by schedule length before comparing across eras
2. **H2H trends**: Track how head-to-head records shift over decades to identify the "evolving rivalry"
3. **Dynasty identification**: Use rolling 5-year windows to identify sustained periods of excellence
4. **Drought analysis**: Measure time since last championship for each franchise
5. **Visualization**: Use the interactive tools at https://inkandthunder.github.io/win-loss-visualizer/ as a reference for YoY W-L plotting