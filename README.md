# NL Team Trends

Historical National League team performance data, win-loss records, and trend visualizations across past seasons.

## Overview

This repository compiles historical National League (NL) data spanning **two distinct leagues** — the MLB National League (baseball) and the English National League (soccer) — to enable cross-sport performance analysis, trend identification, and visualization building.

### Why Both Leagues?

While both are called "National League," they represent entirely different sports, eras, and competitive structures. Comparing their patterns of dominance, competitive balance, and franchise trajectories reveals fascinating parallels in how professional leagues evolve over time.

## Data Coverage

### 1. MLB National League (Baseball)
- **Founded:** 1876 — the oldest continuously operating professional sports league in North America
- **Teams:** 15 franchises (with full tracking of franchise moves, e.g., Giants include NY tenure; Dodgers include Brooklyn tenure)
- **Data Span:** 1876–2026 (150 seasons)
- **Key Metrics:** Year-by-year win-loss records, all-time head-to-head records, single-season best records, era breakdowns

#### NL Era Breakdown
| Era | Years | Defining Features |
|-----|-------|-------------------|
| **Pre-Modern** | 1876–1899 | 8–12 teams; no pitcher's mound; 60–154 game schedules; AA merger |
| **Dead Ball** | 1900–1919 | Pitching dominant; 1906 Cubs 116-36 (.763); Merkle incident; WS begins 1903 |
| **Live Ball** | 1920–1945 | Home run surge (Ruth); 1947 Jackie Robinson integration; WWII impact |
| **Post-War** | 1946–1968 | Dodgers dynasty; Braves move to Milwaukee (1953); 1962 expansion to 10 teams |
| **Modern Expansion** | 1969–1992 | Two-division format; Big Red Machine (.610 Win%); two expansion waves |
| **Divisional** | 1993–2019 | Three-division + Wild Card; Braves 14 straight division titles (1991-2005); 1994 strike |
| **COVID-Modern** | 2020–2025 | 60-game 2020 season; universal DH (2022); 12-team playoff format |

#### Best Single-Season NL Records
| Rank | Team | Season | Record | Win% | Notes |
|------|------|--------|--------|------|-------|
| 1 | **Chicago Cubs** | 1906 | 116-36 | .763 | All-time NL record |
| 2 | **Pittsburgh Pirates** | 1902 | 103-36 | .741 | 130-game season |
| 3 | **Brooklyn Dodgers** | 1953 | 105-49 | .681 | Won 1955 WS |
| 4 | **Pittsburgh Pirates** | 1909 | 110-42 | .724 | Won 1909 WS |
| 5 | **Atlanta Braves** | 1998 | 106-56 | .654 | 14th straight division title |
| 6 | **San Francisco Giants** | 2021 | 107-55 | .659 | Won 2021 WS |

#### Key All-Time Head-to-Head Records (Sample)
- **Cardinals vs Cubs:** W931 L1268 (Cubs edge)
- **Giants vs Dodgers:** W271 L213 (Giants edge, incl. NY tenure)
- **Mets vs all NL:** W1034 L885 (Mets dominant since 1962)
- **Dodgers vs all NL:** W2781 L2071 (Dodgers all-time leader)

### 2. English National League (Soccer)
- **Founded:** 1979 (originally Alliance Premier League; renamed Football Conference 1986; National League 2004)
- **Teams:** 24 clubs
- **Tier:** Step 1 of the National League System, 5th tier of English football
- **Data Span:** 1979–2025 (46 seasons)

#### Recent English NL Champions
| Season | Champion | Pts | Runners-Up | Runners-Up Pts |
|--------|----------|-----|------------|----------------|
| 2024/25 | **Barnet** | 102 | York City | 96 |
| 2023/24 | **Chesterfield** | 98 | Barnet | 86 |
| 2022/23 | **Wrexham** | 111 | Notts County | 107 |
| 2021/22 | **Stockport County** | 94 | Wrexham | 88 |
| 2020/21 | **Sutton United** | 84 | Torquay United | 80 |
| 2019/20 | **Barrow** | 70 | Harrogate Town | 66 |
| 2018/19 | **Fylde** | — | Aldershot Town | — |
| 2017/18 | **Macclesfield Town** | 82 | Sutton United | 72 |
| 2016/17 | **Lincoln City** | 99 | Tranmere Rovers | 95 |

## Files

- `README.md` — This file
- `data/nl-historical-performance.json` — Structured historical performance data for both leagues
- `notebooks/` — Jupyter notebooks for visualization and analysis (planned)

## Data Sources

| Source | Coverage | URL |
|--------|----------|-----|
| Baseball-Reference | MLB NL team year-by-year stats | https://www.baseball-reference.com/leagues/NL/ |
| Baseball Almanac | NL team-vs-team H2H records (1876–2026) | https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml |
| Baseball Data Hub | All MLB seasons 1871–2026 | https://baseballdatahub.com/seasons/ |
| Sporting Life | English NL past season tables | https://www.sportinglife.com/football/league-tables/english-national-league/7/seasons |
| FBref.com | National League season history | https://fbref.com/en/comps/34/history/ |
| Wikipedia | English National League structure | https://en.wikipedia.org/wiki/National_League_(division) |

## Visualization Ideas

1. **MLB NL Franchise Win-Loss Trend Lines** (1876–2026) — Era-by-era dominance mapping
2. **English NL Championship Points Distribution** (2016/17–2024/25) — Competitive balance analysis
3. **NL Head-to-Head Win Matrix** (MLB) — Heatmap of franchise matchups
4. **English NL Relegation Battle Timeline** — Points scatter plot for bottom teams
5. **Cross-League Dominance Comparison** — NL Champions in both sports by decade
6. **Franchise Longevity vs. Performance** — Correlation analysis

## Getting Started

1. Open `data/nl-historical-performance.json` for structured raw data
2. Explore the source links above for deeper drill-down into specific seasons
3. Build visualizations using Python (Matplotlib/Plotly/Seaborn) or R (ggplot2)
4. Reference the era breakdown tables above for contextual analysis
