# NL Team Trends – Data Collection & Methodology Notes

## Data Sources Used

| Source | URL | Coverage | Value |
|--------|-----|----------|-------|
| **Baseball Almanac** | baseball-almanac.com/teams/teamvsteam-nl | 1876–2026 | Team-vs-team W-L matrices updated daily |
| **Baseball Reference** | baseball-reference.com/leagues/NL | 1876–present | Season-by-season standings, leaders & stats |
| **Baseball Data Hub** | baseballdatahub.com/seasons | 1871–2026 | 156 MLB seasons with full stats |
| **Grokipedia** | grokipedia.com | 1876–2025 | All-time franchise W-L records, verified 2025 season |
| **SABR Lahman DB** | sabr.org/lahman-database | 1871–2025 | Complete historical team, batting, pitching stats |
| **StatsCrew** | statscrew.com/baseball/l-NL | 1876–present | NL rosters, standings & statistical leaders |
| **Everything Explained** | everything.explained.today | 1876–2025 | Franchise records, postseason analysis |

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
2. **Tie games** more frequent pre-1920; inconsistent early census
3. **Houston Astros**: Only 1962–2012 in NL; after 2012 in AL West
4. **1904**: No World Series played (Giants boycott)
5. **1876**: 2 of 8 original franchises folded mid-season
6. **Negro Leagues (1876–1948)**: SABR Lahman includes some stats but NL standard records treat as separate era

## Visualization Roadmap

| Plot | Description | Status |
|------|-------------|--------|
| Franchise Win Trajectory by Era | Dead Ball → Live Ball → Islanders → Modern | Planned |
| Pennant Frequency Heatmaps | 5-yr rolling dominance illustrated | Planned |
| Win% Distribution by Division | Competitive balance over time | Planned |
| Run Differential Correlation | Rdiff vs pennant across eras | Planned |
| Expansion Adjustment Curves | New franchise ramp-up shows | Planned |
| H2H Matrix Heatmap | Cross-franchise win-loss network | Planned |

## Contributing
Corrections and additions welcome! Always cite the primary SABR/Lahman source when adding new data.
