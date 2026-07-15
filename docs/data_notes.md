# NL Team Trends – Data Collection & Methodology Notes

## Data Sources Used

| Source | URL | Coverage | Value |
|--------|-----|----------|-------|
| **Baseball Almanac** | baseball-almanac.com/teams/teamvsteam-nl | 1876–2026 | Team-vs-team W-L matrices updated daily |
| **Baseball Reference** | baseball-reference.com/leagues/NL | 1876–present | Season-by-season standings, leaders & stats |
| **Baseball Data Hub** | baseballdatahub.com/seasons | 1871–2026 | 156 MLB seasons with full stats <br>*(Sampled: 1876, 1900, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2015, 2020)* |
| **SABR Lahman DB** | sabr.org/lahman-database | 1871–2025 | Complete historical team, batting, pitching stats |
| **StatsCrew** | statscrew.com/baseball/l-NL | 1876–present | NL rosters, standings & statistical leaders |
| **Everything Explained** | everything.explained.today | 1876–2025 | Franchise records, postseason analysis |
| **Wikipedia** | wikipedia.org | 1876–present | Pennant winners, franchise histories, all-time records |

## National League Historical Context

- **Founded**: February 2, 1876 — world's oldest continuously operating professional sports league
- **Original 8 teams**: Boston Red Stockings, Chicago White Stockings, Hartford Dark Blues, Louisville Grays, Mutuals NY, Philadelphia Athletics, St. Louis Brown Stockings, Cincinnati Red Stockings
- **Key expansion milestones**:
  - 1962: NY Mets, Houston Colt .45s added
  - 1969: San Diego Padres, Montreal Expos added; divisions created
  - 1993: Colorado Rockies, FL/Miami Marlins added
  - 1998: AZ Diamondbacks; Milwaukee Brewers moved from AL Central
- **Divisions (current)**: East, Central, West since 1995; 15 teams per league
- **Interleague play**: Started 1997; full-season since 2023
- **Wild Card**: Introduced 1994/95; 2nd WC added 2012

## Data Conventions

| Convention | Description |
|-----------|-------------|
| Win% = W ÷ (W+L) | Rounded to 3 decimal places; ties excluded |
| Franchise Continuity | Relocated teams = continuous entity (SF Giants → NY Giants roots) |
| Schedule Length | 40–80 (1870s) → 154 (1892–1960) → 162 (1961–present) |
| Pre-1900 Ties | Common due to darkness; excluded from percentage calc |
| 1994 Season | Cancelled postseason; no NL pennant winner |
| 2020 Season | 60-game COVID season; separate normalized metrics apply |

## Franchise Relocation Map

| Current Team | Historical Names (in order) | Years Active |
|-------------|----------------------------|-------------|
| San Francisco Giants | NY Giants, NY Gothams | 1883–1957 → 1958–present |
| Atlanta Braves | Red Stockings, Beaneaters, Doves, Rustlers, Braves, Bees, Milwaukee Braves | 1871–1875, 1876–1952, 1953–1965, 1966–present |
| LA Dodgers | Brooklyn Bridegrooms, Superbas, Robins, Dodgers | 1883–1957 → 1958–present |
| Washington Nationals | Montreal Expos | 1969–2004 → 2005–present |

## Known Data Quality Issues

1. **Pre-1900 records** may contain inconsistencies from variable scheduling and incomplete logs
2. **Dead-ball era stats** (pre-1920) may not be directly comparable to modern seasons due to different ball construction
3. **Shortened seasons** (1994, 2020) require careful normalization for cross-era analysis
4. **1876–1882 seasons** used unbalanced schedules (40–80 games), making W-L percentages unreliable for cross-era comparison

## Recommended Analysis Approaches

- Use **ERA-adjusted win percentage** for cross-era comparisons
- Normalize by **games played** for pre-1962 data
- Apply **Elo ratings** for ordinal team strength across eras
- Segment analysis by **era** (Dead Ball → Live Ball → Expansion → Modern)
- Account for **division alignment changes** when analyzing competitive balance