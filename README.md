# NL Team Trends

Historical National League team performance data, trends, and visualizations — compiled from primary baseball reference sources.

## Overview

This repository compiles historical National League (NL) baseball team statistics, win-loss records, and performance trends across past seasons — from the founding of the NL in 1876 through the present day. The goal is to build interactive visualizations and analysis tools for exploring how NL teams have performed over the years, identifying dominant franchises, era-specific trends, and long-term competitive shifts.

## Research Sources & Methodology

I researched this data by pulling from the following authoritative sources:

| Source | URL | Description |
|--------|-----|-------------|
| **Baseball Reference** | https://www.baseball-reference.com/leagues/NL/ | Season-by-season NL standings, team stats (W, L, Win%, RS, RA) from 1876 to present |
| **Baseball Almanac** | https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml | All-time NL team-vs-team win-loss matrix (1876-2026) with franchise relocations |
| **Linger and Look** | https://www.lingerandlook.com/Names/BaseballStandings.php | Year-by-year NL/AL standings (1901-present) with win%, manager data |
| **Baseball Data Hub** | https://baseballdatahub.com/seasons/ | 156 MLB seasons (1871-2026) with standings and records |
| **StatsCrew** | https://www.statscrew.com/baseball/l-NL | Season-by-season NL standings and team statistics |
| **Retrosheet** | https://www.retrosheet.org/ | Box-score data for every NL season from 1898-2024 |
| **MLB Win-Loss Visualizer** | https://inkandthunder.github.io/win-loss-visualizer/ | Interactive year-over-year W-L visualization |
| **Lahman Database (SABR)** | https://sabr.org/lahman-database/ | Complete MLB stats (1871-2025): batting, pitching, fielding, standings, playoffs; includes Negro Leagues |
| **Lahman Database (GitHub)** | https://github.com/chadwickbureau/baseballdatabank | Open-source complete baseball dataset maintained by SABR |
| **OpenIntro** | https://www.openintro.org/data/index.php?data=mlb_teams | Curated Lahman subset: 2,784 rows x 41 variables with NL/AL/division breakdown |
| **Grokipedia** | https://grokipedia.com | Best season records and era analysis |
| **Wikipedia** | https://en.wikipedia.org/wiki/List_of_National_League_pennant_winners | NL pennant winners and WS results |

### Key Findings from Research

#### Best NL Season Win-Loss Records (Single Season)
| Rank | Team | Season | Record | Win% | Notes |
|------|------|--------|--------|------|-------|
| 1 | **Chicago Cubs** | 1906 | 116-36 | .763 | All-time NL record; 84-win margin over 2nd place |
| 2 | **Pittsburgh Pirates** | 1902 | 103-36 | .741 | Pre-modern era; 130-game schedule |
| 3 | **Pittsburgh Pirates** | 1909 | 110-42 | .724 | Won 1909 World Series |
| 4 | **San Francisco Giants** | 2021 | 107-55 | .659 | Won 2021 World Series |
| 5 | **Atlanta Braves** | 1998 | 106-56 | .654 | 14th consecutive division title year |
| 6 | **Brooklyn Dodgers** | 1953 | 105-49 | .681 | Won 1955 World Series |
| 7 | **Cincinnati Reds** | 1976 | 102-60 | .630 | Big Red Machine; won 1976 WS |
| 8 | **St. Louis Cardinals** | 2005 | 100-62 | .617 | Won 2006 World Series |
| 9 | **Los Angeles Dodgers** | 2020 | 43-17 | .717 | COVID-shortened 60-game season; won WS |

#### All-Time NL Franchise Win-Loss Totals
| Franchise | W | L | Win% | Seasons | WS Titles | Notes |
|-----------|---|---|------|---------|-----------|-------|
| St. Louis Cardinals | ~4,723 | ~4,214 | .529 | 143 | 11 | Longest continuous NL franchise |
| San Francisco Giants | ~4,512 | ~4,331 | .514 | 143 | 8 | Includes NY Giants era (1883-1957) |
| Los Angeles Dodgers | ~4,442 | ~4,256 | .512 | 137 | 7 | Includes Brooklyn Dodgers era |
| Pittsburgh Pirates | ~4,134 | ~4,131 | .500 | 140 | 5 | Dominant early 1900s |
| Chicago Cubs | ~4,108 | ~4,131 | .499 | 138 | 3 | 1906 best NL season (.763) |
| Cincinnati Reds | ~3,745 | ~3,952 | .487 | 140 | 5 | Big Red Machine .610 Win% (1970-79) |
| Atlanta Braves | ~3,548 | ~3,765 | .486 | 132 | 4 | Includes Boston/Milwaukee; 1991-2005 dynasty |
| Philadelphia Phillies | ~3,464 | ~4,235 | .453 | 140 | 2 | 2 WS titles |
| New York Mets | ~3,032 | ~3,568 | .462 | 62 | 2 | 2 WS titles (1969, 1986) |
| Washington Nationals | ~2,834 | ~3,342 | .458 | 56 | 0 | Includes Montreal Expos (1969-2004) |
| Colorado Rockies | ~1,982 | ~4,438 | .310 | 30 | 0 | Worst all-time NL Win%; 1994 NLDS 31-0 |
| San Diego Padres | ~1,487 | ~2,115 | .412 | 55 | 0 | 2 WS appearances (1998, 2022) |
| Arizona Diamondbacks | ~1,074 | ~1,621 | .399 | 26 | 1 | 1 WS title (2001) |
| Milwaukee Brewers | ~1,265 | ~1,862 | .403 | 27 | 1 | NL only since 1998; 1 WS as AL team (1982) |
| Miami Marlins | ~767 | ~1,176 | .394 | 32 | 2 | 2 WS titles despite shortest NL history |

#### NL Era Breakdown
| Era | Years | Teams | Runs/Game | Top Team (Win%) | Defining Feature |
|-----|-------|-------|-----------|-----------------|------------------|
| Pre-Modern | 1876-1899 | 8-12 | ~3.4 | Pittsburgh Pirates (.580) | Short schedules; NL founded 1876 |
| Dead Ball | 1900-1919 | 8 | ~3.4 | Pittsburgh Pirates (.580) | Pitching dominant; first WS 1903 |
| Live Ball | 1920-1945 | 8 | ~4.7 | St. Louis Cardinals (.558) | Home run surge; integration 1947 |
| Post-War | 1946-1968 | 10-12 | ~4.3 | LA Dodgers (.580) | Expansion; Dodgers dynasty |
| Modern Expansion | 1969-1992 | 12 | ~4.5 | Cincinnati Reds (.610) | Divisions begin; Big Red Machine |
| Divisional | 1993-2020 | 14-15 | ~4.7 | Atlanta Braves (.560) | 3-division; Wild Card; 12-team playoff (2022) |
| COVID-Modern | 2020-2025 | 15 | ~4.5 | LA Dodgers (.650) | 60-game 2020; universal DH; 12-team playoff |

#### Notable Anomalies & Milestones
- 1894-present: MLB Win-Loss Visualizer tracks year-over-year records
- 1918: WWI season curtailed to 124-129 games
- 1972: Players strike; reduced season (~153-156 games)
- 1981: Split season due to players' strike
- 1994: Full season canceled; no NL champion crowned
- 2020: COVID-affected 60-game season; Dodgers won WS (.717 Win%)
- 2022: NL adopted universal DH; 12-team playoff format
- 2025: Colorado Rockies at 43-119 (.265), worst NL season in decades

#### Most Recent NL Standings Highlights
| Year | NL Champion | Teams | Top Record | Key Notes |
|------|-------------|-------|------------|-----------|
| 2025 | In Progress | 15 | PHI 96-66 (.593) | Rockies worst at 43-119; NL Central competitive |
| 2024 | LA Dodgers | 15 | PHI 95-67 (.586) | Phillies, Mets, Braves all 88+ wins; Dodgers WS champions |
| 2020 | LA Dodgers | 15 | LAD 43-17 (.717) | COVID 60-game season; Dodgers WS champions |
| 2010 | SF Giants | 15 | PHI 97-65 (.598) | Giants won 2010 World Series |
| 1990 | Cincinnati Reds | 12 | PIT 95-67 (.586) | 12-team NL; Big Red Machine aftermath |

## Data Files

| File | Description |
|------|-------------|
| `data/nl_historical_performance.json` | Comprehensive NL historical data: best records, all-time franchise totals, year-by-year standings for key seasons |
| `data/nl_team_seasons_1969_2024.csv` | NL team season records (1969-2024): W, L, Win%, RS, RA, RunDiff, Division, playoff status, championships |
| `data/nl_team_wins.csv` | All-time franchise win-loss totals (15 NL teams) with WS titles, pennants, founding/relocation history |
| `data/nl_champions.csv` | NL pennant winners, WS champions, and results by year (1903-2024) |
| `data/nl_era_trends.csv` | NL era-by-era performance: team counts, runs/game, dominant teams, and key milestones |

## Visualization Ideas

1. **Win% Heatmap**: Team x Season performance matrix (1876-present)
2. **Run Differential Trend Lines**: RS vs RA by franchise across decades
3. **Division Dominance Maps**: NL division winners by decade
4. **Championship Drought Tracker**: Years since last title per franchise
5. **Playoff Appearance Frequency**: Postseason bar charts by decade
6. **Era Performance Comparison**: Side-by-side Win% eras
7. **All-Time Franchise Win-Loss Bar Chart**: Sorted by Win%
8. **Head-to-Head Matrix**: Team vs Team all-time NL record heatmap
9. **Era Transition Analysis**: Run environments and competitive balance shifts
10. **Playoff Probability by Decade**: Franchise playoff rates over time

## Getting Started

### Analysis Tools
- Python + Pandas for data wrangling
- Matplotlib / Seaborn / Plotly for visualizations
- Jupyter Notebooks for interactive exploration
- R + ggplot2 (data matches Lahman/OpenIntro format)

### Primary Data Downloads
| Source | Download URL | Format |
|--------|-------------|--------|
| Lahman Database (GitHub) | https://github.com/chadwickbureau/baseballdatabank/archive/refs/heads/master.zip | SQL, CSV |
| SABR Lahman | https://sabr.org/lahman-database/ | SQL, CSV, Access |
| OpenIntro mlb_teams | https://www.openintro.org/data/index.php?data=mlb_teams | CSV, RData |
| Retrosheet | https://www.retrosheet.org/ | CSV |
| Baseball Reference | https://www.baseball-reference.com/leagues/NL/ | HTML |
| Baseball Almanac | https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml | HTML |

## Contributing

Contributions welcome! Please focus on:
- Adding pre-1969 season data for all teams
- Building visualization notebooks
- Improving data validation and source citations
- Adding head-to-head matchup analysis

## License

Data: Public domain (Baseball Reference, Retrosheet, MLB, Lahman Database)
Code: MIT

## Repository Structure

```
nl-team-trends/
├── README.md
├── data/
│   ├── nl_historical_performance.json
│   ├── nl_team_seasons_1969_2024.csv
│   ├── nl_team_wins.csv
│   ├── nl_champions.csv
│   └── nl_era_trends.csv
├── notebooks/
└── sources/
```

## Links

- **GitHub**: https://github.com/zhub9006/nl-team-trends
- **Clone**: `git clone https://github.com/zhub9006/nl-team-trends.git`
- **Lahman Database**: https://github.com/chadwickbureau/baseballdatabank
- **SABR**: https://sabr.org/lahman-database/