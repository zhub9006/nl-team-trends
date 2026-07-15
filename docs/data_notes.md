# NL Team Trends — Data Notes & Methodology

## Conventions

- **Win%** = Wins / Games Played (excluding ties in early eras)
- **Pennants** = League Championship titles (NL pennant winner or division champion)
- **WS Titles** = World Series championships won as an NL franchise
- **ERA** = Earned Run Average; in pre-modern eras, lower was common due to pitching mounds
- **All data** through end of 2025 MLB season

## Schedule Eras

| Era | Years | Games per Season | Notes |
|-----|-------|------------------|-------|
| Pre-Modern | 1876-1891 | 66-132 | Very small schedules; tied games replayed |
| Dead Ball | 1892-1919 | 140-154 | 154-game schedule begins 1892; low-scoring |
| Live Ball | 1920-1941 | 154 | MLB lowered mound 1920; home run explosion |
| Wartime | 1942-1945 | 154 | 1945 had reduced rosters |
| Integration | 1946-1960 | 154 | Jackie Robinson era begins 1947; NL expands |
| Expansion | 1961-1990 | 162 (post-1961) | 1962: 10-team league; 1969: 12 teams; 1993: 14 teams |
| Modern | 1991-2025 | 162 | 1994 strike cancel season; 1998: 16 teams; 2020: 60-game COVID season |

## Key Caveats

1. **Tied games** (pre-1920s): Tied games were replayed; this inflates win% because only non-tied games count toward percentage
2. **Pre-1903**: No World Series existed; pennant winners were league champions only
3. **1918 season**: 140 games due to WWI; not a full 154-game season
4. **1981 season**: Split-season format due to player strike; division leaders from each half met in playoffs
5. **2020 season**: 60-game COVID season; .717 Dodgers best-ever shortened record
6. **Brewers**: Moved from AL to NL Central in 1998; AL records still count for some historical context
7. **Nationals**: Expos relocated to DC in 2005; Montreal/Washington records separate
8. **Team mergers**: Early NL merged with AA and other leagues; not all teams survived

## Data Source Prioritization

1. **Primary**: SABR Lahman Database (most complete, cleaned historical data)
2. **Secondary**: Baseball-Reference (extensive standings and leader data)
3. **Tertiary**: Baseball Almanac (team-vs-team matrices,_ALL_ NL history)

## Visualization Guidance

- Use **log scale** when comparing across centuries due to schedule size differences
- Normalize by games played when comparing across different eras
- Mark special seasons (strike years, COVID, split season) as distinct categories
- For head-to-head matrices, only compare NL vs NL (pre-1997 interleague)