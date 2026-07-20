# NL Team Trends — Research Sources & Methodology

## Research Sources Found & Verified

| Source | URL | Coverage | Key Data |
|--------|-----|----------|----------|
| Baseball-Reference (NL) | https://www.baseball-reference.com/leagues/NL/ | 1876–present | Official year-by-year NL standings & team stats |
| Baseball Almanac (Year-by-Year) | https://www.baseball-almanac.com/yearmenu.shtml | 1876–present | NL leadership, W-L records, and fabulous feats per season |
| Baseball Almanac (H2H) | https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml | 1876–2026 | 15x15 H2H W-L matrices for every NL team vs every other team |
| Baseball Data Hub | https://baseballdatahub.com/seasons/ | 1871–2026 | Complete season standings & stats archive |
| SABR Lahman Database | https://sabr.org/lahman-database/ | 1871–2025 | Free downloadable CSV dataset (full team/batting/pitching) |
| StatsCrew (NL) | https://www.statscrew.com/baseball/l-NL | 1876–present | NL rosters, standings & leaders |
| StatMuse (NL Championships) | https://www.statmuse.com/mlb | 1876–2026 | NL championship leaders & franchise W/L/G stats |
| ESPN (World Series) | https://www.espn.com/mlb/worldseries/history/winners | 1903–present | World Series champions & results by year |
| Wikipedia (NL Pennants) | https://en.wikipedia.org/wiki/List_of_National_League_pennant_winners | 1876–present | Complete pennant winner list with WS results |
| Baseball Almanac (NL W-L Records) | https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml | 1876–2026 | Comprehensive franchise vs franchise win-loss records |
| MLB Win-Loss Visualizer | https://inkandthunder.github.io/win-loss-visualizer/ | 1894–present | Interactive YoY W-L visualization tool |
| Champs or Chumps | https://champsorchumps.us/mlb | 1876–present | Win% rankings, droughts, streaks, postseason records |

## Methodology

- **Data normalization**: All win percentages are calculated as wins / (wins + losses + ties). Tie games were common before 1920 and are accounted for in win_pct calculations.
- **Era boundaries**: Defined by major rule changes and schedule lengths (60→84→126→154→162 games per season). The 1969 expansion, 1993 expansion, and 1998 realignment are key inflection points.
- **Relocation impact**: Brooklyn→LA (1958), NY Giants→SF (1958), Montreal→Washington (2005) significantly altered the competitive landscape.
- **Data quality notes**: Pre-1900 records may contain inaccuracies due to inconsistent record-keeping. Abandoned/transferred teams (e.g., Hartford, Louisville) are included where records exist.
- **Update policy**: CSV files should be updated at season-end with final standings and WS results.

## Key Historical Data Points

### NL Founding & Evolution
- NL Founded: February 2, 1876 (replacing the National Association)
- Original 8 teams: Boston Red Caps, Chicago White Stockings, Cincinnati Reds, Hartford Dark Blues, Louisville Grays, Philadelphia Athletics, Brooklyn Mutuals, St. Louis Browns
- NL expanded: 8→12→16→15 teams
- Key relocations: Brooklyn→LA (1958), NY Giants→SF (1958), Montreal Expos→Washington Nationals (2005)

### Schedule Eras
| Era | Games/Season |
|-----|-------------|
| 1876–1884 | 60–112 |
| 1885–1908 | 126–154 |
| 1909–1961 | 154 |
| 1962–2019 | 162 |
| 2020 | 60 |
| 2021–present | 162 |

### All-Time NL Franchise Records (through 2025)
| Team | WS Titles | Games | Wins | Losses | Win% | Last WS Title |
|------|----------|-------|------|--------|-------|---------------|
| St. Louis Cardinals | 11 | 20,863 | 10,633 | 10,099 | .513 | 2011 |
| LA Dodgers | 9 | 21,115 | 11,176 | 9,819 | .532 | 2025 |
| SF Giants | 8 | 21,981 | 11,663 | 10,155 | .535 | 2014 |
| Cincinnati Reds | 5 | 21,139 | 10,511 | 10,501 | .500 | 1990 |
| Pittsburgh Pirates | 5 | 21,519 | 10,724 | 10,661 | .501 | 1979 |
| Atlanta Braves | 4 | 22,474 | 11,245 | 11,075 | .504 | 2021 |
| Chicago Cubs | 3 | 22,513 | 11,473 | 10,879 | .516 | 2016 |
| Miami Marlins | 2 | 5,271 | 2,434 | 2,837 | .462 | 2003 |
| NY Mets | 2 | 10,231 | 4,939 | 5,284 | .483 | 1986 |
| Philadelphia Phillies | 2 | 21,907 | 10,357 | 11,435 | .475 | 2008 |
| Arizona Diamondbacks | 1 | 4,530 | 2,216 | 2,314 | .489 | 2001 |
| Washington Nationals | 1 | 9,097 | 4,379 | 4,714 | .482 | 2019 |
| Milwaukee Brewers | 0 | 8,920 | 4,464 | 4,456 | .503 | N/A |
| Colorado Rockies | 0 | 4,760 | 2,403 | 2,357 | .505 | N/A |
| San Diego Padres | 0 | 7,980 | 4,265 | 3,715 | .534 | N/A |

### Championship Trends by Era
| Era | Dominant Team(s) | Theme |
|-----|-----------------|-------|
| 1876–1900 | Chicago (4 pennants), Boston (5) | Founding era |
| 1900–1920 | Cubs (2), Pirates (2) | Record-setting wins |
| 1920–1940 | Cardinals (5), NY Giants (4) | Power transition |
| 1940–1960 | Cardinals (9), Dodgers/Giants | Cards dynasty; relocation |
| 1960–1980 | Dodgers (5), Reds, Mets (1969) | Expansion era |
| 1981–2000 | Braves (14 div titles 1991–2005), Reds | Braves dynasty |
| 2001–2015 | Cardinals, Giants, D-backs | Resurgence cycle |
| 2016–2025 | Dodgers (3 pennants, 8 straight NL West) | Modern Dodgers dynasty |

### Key H2H Rivalries (1876–2026)
| Team 1 | Team 2 | T1 Wins | T2 Wins | T1 Win% |
|--------|--------|---------|---------|---------|
| LA Dodgers | Chicago Cubs | 278 | 122 | .695 |
| St. Louis Cardinals | Chicago Cubs | 1,315 | 1,185 | .525 |
| LA Dodgers | SF Giants | 272 | 246 | .523 |
| Chicago Cubs | Cincinnati Reds | 1,209 | 1,074 | .530 |
| Atlanta Braves | NY Mets | 290 | 237 | .550 |
| St. Louis Cardinals | Pittsburgh Pirates | 1,423 | 927 | .606 |
| St. Louis Cardinals | LA Dodgers | 508 | 437 | .538 |
| SF Giants | Chicago Cubs | 1,295 | 1,330 | .492 |
| Cincinnati Reds | Atlanta Braves | 1,068 | 1,338 | .441 |

## Data File Index

| File | Description |
|------|-------------|
| `data/nl_all_time_records.csv` | All-time franchise records with W/L, pennants, WS titles |
| `data/nl_historical_performance.csv` | Seasonal NL standings & records (1876–2025) |
| `source_references.md` | This file — source attribution & methodology |
