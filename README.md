# NL Team Trends — Comprehensive README

**Research project compiling historical NL team performance data, win-loss records, season trends & championship history from 1876 to present. For analyzing team dominance, franchise trajectories & the evolving NL competitive landscape.**

## Research Sources

- **Baseball-Reference** (baseball-reference.com/leagues/NL/) — Official NL standings 1876-present
- **Baseball Almanac** (baseball-almanac.com) — NL team-vs-team W-L matrices, year-by-year
- **SABR Lahman DB** (sabr.org/lahman-database) — Free CSV 1871-2025
- **Baseball Data Hub** (baseballdatahub.com) — Complete season archives
- **StatsCrew** (statscrew.com/baseball/l-NL) — NL rosters, standings, leaders

## Key NL Facts

- **NL Founded**: February 2, 1876 (8 original teams)
- **Schedule eras**: Variable (1876-84) → 154G (1892-1961) → 162G (1962-2019) → 60G COVID (2020) → 162G (2021+)
- **Original 8 (1876)**: Boston Red Caps, Chicago White Stockings, Cincinnati Reds, Hartford Dark Blues, Louisville Grays, Philadelphia Athletics, Brooklyn Mutuals, St. Louis Browns
- **Key relocations**: Brooklyn→LA (1958), NY Giants→SF (1958), Montreal→Washington (2005)

## Most All-Time Wins (NL, through 2025)

| Rank | Franchise | Wins | WS Titles | Pennants | Key Era |
|------|-----------|------|-----------|----------|---------|
| 1 | SF Giants (NY/SSF) | 11,663 | 8 | 23 | NY Giants dynasty; SF 2010-2014 |
| 2 | St. Louis Cardinals | 11,413 | **11** | 19 | Cards dynasty 1942-46; most WS titles ever |
| 3 | Chicago Cubs | 11,474 | 3 | 17 | 1906 best NL season; 2016 WS ended 108-yr drought |
| 4 | LA Dodgers (Brooklyn/LA) | 11,586 | 8 | **26** | Brooklyn 1950s; LA dynasty 2017-2025 (NL record pennants) |
| 5 | Cincinnati Reds | 11,060 | 5 | 10 | Big Red Machine (1970s); 1919 WS |
| 6 | Atlanta Braves | 11,245 | 4 | 18 | 14 straight division titles 1991-2005 |
| 7 | Pittsburgh Pirates | 10,959 | 5 | 9 | Early NL powerhouse (1880s-1900s) |
| 8 | Philadelphia Phillies | 10,357 | 2 | 8 | Most NL losses (11,865); 2008 & 2025 WS champs |

## Championship Highlights by Era

| Era | Dominant Theme |
|-----|----------------|
| 1876-1900 | Founding era; Chicago & Boston dominated |  
| 1901-1919 | Dead Ball Era; Cubs 1906 best NL season (116-36 .763) |
| 1920-1945 | Cardinals dynasty emerges; Miracle Braves 1914 |
| 1946-1960 | Dodgers/Monsters dynasty; Giants→SF migration; Braves move |
| 1961-1980 | Big Red Machine; Mets 1969 Miracle; Pirates 3 WS titles |
| 1981-2000 | Braves dynasty 14 straight div titles 1991-2005 |
| 2001-2025 | Dodgers dynasty (9 pennants), Cubs 2016 (108yr drought), Giants 3 WS in 5 years |

## Notable NL Records

- **Best NL season ever**: 1906 Cubs — 116-36 (.763)
- **Best 162-game record**: 2022 LAD — 111-51 (.685)  
- **Best shortened season**: 2020 LAD — 43-17 (.717)
- **Most consecutive division titles**: Braves 1991-2005 (14 straight)
- **Back-to-back WS champions**: LAD (2024, 2025)
- **Most WS titles (NL)**: Cardinals (11)
- **Most NL pennants**: Dodgers (26 through 2025)
- **Longest drought ended**: Cubs (108 years without a WS, ended 2016)

## Data Files

| File | Description |
|------|-------------|
| `data/nl_historical_performance.csv` | Year-by-year champion standings + WS results |
| `data/nl_all_time_records.csv` | 15 NL franchise stats through 2025 |
| `data/nl_championship_trends.csv` | Championship distribution by era |
| `data/nl_notable_records.csv` | Key milestones & single-season records |
| `docs/research_notes.md` | Research methodology & source library |
| `source_references.md` | Full source attribution |

## Visualization Roadmap (planned)
- Win% trend lines per franchise 1876→2025
- Era-based championship heatmaps  
- Head-to-head matchup matrices (Baseball Almanac data)
- Interactive Streamlit dashboard

## License: MIT