# NL Team Trends

Historical National League team performance data, win-loss records, and trend visualizations across past seasons.

## Overview

This repository compiles historical National League (NL) data for the MLB National League (baseball) and the English National League (soccer) to enable cross-sport performance analysis, trend identification, and visualization building.

## Data Coverage

### 1. MLB National League (Baseball)
- **Founded:** 1876 — the oldest continuously operating professional sports league in North America
- **Teams:** 15 franchises (tracking franchise moves: Giants include NY tenure; Dodgers include Brooklyn)
- **Data Span:** 1876–2025 (150 seasons)
- **Key Metrics:** Year-by-year win-loss records, all-time H2H records, single-season best records, era breakdowns

#### NL Era Breakdown
| Era | Years | Defining Features |
|-----|-------|-------------------|
| **Pre-Modern** | 1876–1899 | 8–12 teams; 60–154 game schedules; AA merger |
| **Dead Ball** | 1900–1919 | Pitching dominant; 1906 Cubs 116-36 (.763); WS begins 1903 |
| **Live Ball** | 1920–1945 | Home run surge (Ruth); 1947 Jackie Robinson; WWII impact |
| **Post-War** | 1946–1968 | Dodgers dynasty; Braves move to Milwaukee (1953); 1962 expansion |
| **Expansion** | 1969–1992 | Two-division; Big Red Machine (.610 Win%); Wild Card era begins |
| **Divisional** | 1993–2019 | Three-division + WC; Braves 14 straight division titles (1991–2005); 1994 strike |
| **Modern** | 2020–present | 60-game 2020; universal DH (2022); 12-team playoff (2022+) |

#### Best Single-Season NL Records
| Rank | Team | Season | Record | Win% | Notes |
|------|------|--------|--------|------|-------|
| 1 | **Chicago Cubs** | 1906 | 116-36 | .763 | All-time NL record |
| 2 | **Pittsburgh Pirates** | 1902 | 103-36 | .741 | 130-game season |
| 3 | **Brooklyn Dodgers** | 1953 | 105-49 | .681 | Won 1955 WS |
| 4 | **Pittsburgh Pirates** | 1909 | 110-42 | .724 | Won 1909 WS |
| 5 | **Atlanta Braves** | 1998 | 106-56 | .654 | 14th straight division title |
| 6 | **San Francisco Giants** | 2021 | 107-55 | .659 | Won 2021 WS |

#### Key All-Time Head-to-Head Records
- **Cardinals vs Cubs:** W931 L1268 (Cubs edge)
- **Giants vs Dodgers:** W271 L213 (Giants edge, incl. NY tenure)
- **Mets vs all NL:** W1034 L885 (Mets dominant since 1962)
- **Dodgers vs all NL:** W2781 L2071 (Dodgers all-time leader)

### 2. English National League (Soccer)
- **Founded:** 1979 (Alliance Premier League → Football Conference → National League)
- **Teams:** 24 clubs; Step 1 of National League System (5th tier English football)
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
| 2018/19 | **Macclesfield Town** | — | Aldershot Town | — |
| 2017/18 | **Macclesfield Town** | 82 | Sutton United | 72 |
| 2016/17 | **Lincoln City** | 99 | Tranmere Rovers | 95 |

## Research Highlights

### MLB NL — Dominant Franchises by Era
- **Cardinals** — 11 WS titles, 19+ pennants; most successful modern NL franchise
- **Giants** — 8 WS titles (NY + SF era), dynasty 2010–2014
- **Dodgers** — 7 WS titles, 25+ pennants; most pennants but title gap vs Giants/Cardinals
- **Braves** — 4 WS titles; 14 straight division titles (1991–2005)
- **Reds** — Big Red Machine (.610 Win%); 5 WS titles concentrated in 3 decades
- **Mets/Pirates** — Competitive mid-century; Mets most productive expansion franchise
- **Phillies/Cubs/Nats** — Intermittent champions reflecting competitive parity in later eras

### Key Trends
1. **Competitive Balance Shift:** Low (1876–1920) → Moderate → High (1969–2005) → Lower (2020+)
2. **Champion Win% Range (1960–2025):** .516 (2006 Cardinals) to .717 (2020 Dodgers)
3. **Wild Card Era (1994+):** Lower Win% champions due to broader playoff field
4. **Dodgers Supremacy (2020–):** 199+ wins (2022), 5 NL West titles, 3 NLCS, 1 WS
5. **Cinderella Possible:** 2023 D-backs won WS at .519 Win% from Wild Card

### Franchise H2H Snapshot (Sample)
| Matchup | Cardinals Wins | Dodgers Wins | Notes |
|---------|---------------|--------------|-------|
| Cardinals vs Cubs | ~931 | ~1268 | Cubs lead all-time |
| Giants vs Dodgers | ~271 | ~213 | Giants lead incl. NY |
| Mets vs all NL | 1034 | 885 | Mets most H2H wins |
| Dodgers vs all NL | — | 2781 | Dodgers lead all-time |

## Files

- `README.md` — This file (overview + research highlights)
- `nl_team_wins.csv` — Year-by-year NL team records (2015–2025)
- `nl_champions.csv` — NL champion history (1960–2025)
- `data/nl-historical-performance.json` — Structured data: franchise moves, H2H, era breakdowns, English NL
- `data/nl_historical_performance_v2.json` — Comprehensive era-by-era dominant team data
- `SOURCES.md` — Source URLs and methodology
- `notebooks/` — Planned Jupyter notebooks for visualization

## Data Sources

| Source | Coverage | URL |
|--------|----------|-----|
| Baseball Reference | NL standings 1876–present | https://www.baseball-reference.com/leagues/NL/ |
| Retrosheet | Box scores 1898–present | https://www.retrosheet.org/ |
| Lahman Database (SABR) | Complete MLB stats 1871–present | https://sabr.org/lahman-database/ |
| Baseball Almanac | Team-vs-team H2H | https://www.baseball-almanac.com/ |
| FBref.com | Advanced NL stats | https://fbref.com/en/comps/34/history/ |
| Wikipedia | NL pennant winners | https://en.wikipedia.org/wiki/National_League_(baseball) |
| Sporting Life | English NL tables | https://www.sportinglife.com/ |

## Visualization Ideas

1. **NL Franchise Win-Loss Trend Lines** (1876–2025) — Era-by-era dominance mapping
2. **NL Head-to-Head Win Matrix** — Heatmap of franchise matchup records
3. **Champion Win% Distribution** (1960–2025) — Competitive balance histogram
4. **English NL Points Distribution** — Bar chart of champion points by season
5. **Cross-League Dominance Comparison** — NL champions by decade in both sports
6. **Franchise Longevity vs Performance** — Scatter plot analysis
7. **Era-by-Era Playoff Appearance Map** — Heatmap of playoff entry depth

## Getting Started

1. Open `data/nl-historical-performance.json` for structured raw data
2. Review `SOURCES.md` for primary/secondary research sources
3. Load CSVs with pandas for quick tabular analysis
4. Build visualizations with Python (Matplotlib/Plotly/Seaborn) or R (ggplot2)
5. Cross-reference season data with Baseball Reference for advanced stats
