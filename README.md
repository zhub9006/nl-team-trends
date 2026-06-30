# NL Team Trends

> Historical National League team performance data, win-loss records, and trend visualizations across past MLB seasons (1876–2025).

## Overview

This repository compiles, curates, and analyzes historical National League (NL) baseball team statistics for all 15 active franchises from the league's founding in 1876 through the present day. The goal is to serve as a comprehensive dataset and analysis framework for exploring team dominance, franchise trajectories, divisional realignments, and the evolving competitive landscape of baseball's oldest league.

**Current coverage:** 1876–2025 (150 NL seasons spanning all 15 NL franchises).

## Data Files

| File | Description | Rows |
|------|-------------|------|
| `data/nl_historical_data.csv` | Year-by-season records for all NL teams (1876–2025) | ~500+ entries |
| `data/franchise_summary.csv` | All-time franchise win-loss totals, championships, and peaks | 15 rows |
| `nl_champions.csv` | NL pennant winners and World Series champions (1960–2025) | 65 entries |
| `nl_team_wins.csv` | Recent season-by-season team records (2015–2025) | 150+ entries |
| `data/CHAMPIONS.md` | Complete NL championship timeline with all key results (1869–2025) | — |

### Key Data Columns
- **season** — MLB season year
- **team** — Franchise name as it existed that season
- **modern_name** — Current franchise name (accounts for relocations/renames)
- **division** — NL East / Central / West (N/A for pre-division eras)
- **wins / losses / win_pct** — Regular-season record
- **playoff_result** — Pennant, WS, Wild Card, Division Title, or —
- **era** — Era classification (Pre-Modern, Dead Ball, Live Ball, Post-War, Expansion, Divisional, Modern)

## Research Highlights

### NL Era Breakdown
| Era | Years | Teams | Key Features |
|-----|-------|-------|-------------|
| **Pre-Modern** | 1876–1899 | 8–12 | 60–154 game seasons; no pitcher's mound; AA merger |
| **Dead Ball** | 1900–1919 | 8 | Pitching dominant; 1906 Cubs 116-36 (.763 record); WS begins 1903 |
| **Live Ball** | 1920–1945 | 8 | Home run surge (Ruth); 1947 Jackie Robinson integration; WWII impact |
| **Post-War** | 1946–1968 | 10–12 | Dodgers dynasty; Braves move to Milwaukee (1953); 1962 expansion |
| **Expansion** | 1969–1992 | 12 | Two-division format; Big Red Machine (.610 Win%); two expansion waves |
| **Divisional** | 1993–2019 | 14–15 | Three-division + Wild Card (1994); Braves dynasty 1991–2005 |
| **Modern** | 2020–present | 15 | 60-game 2020 season; universal DH (2022); 12-team playoff (2022+) |

### Best Single-Season NL Records
| Rank | Team | Season | Record | Win% | Notes |
|------|------|--------|--------|------|-------|
| 1 | **Chicago Cubs** | 1906 | 116-36 | .763 | All-time NL record; 84-win margin |
| 2 | **Pittsburgh Pirates** | 1902 | 103-36 | .741 | Pre-modern era; 130-game schedule |
| 3 | **Pittsburgh Pirates** | 1909 | 110-42 | .724 | Won 1909 World Series |
| 4 | **Brooklyn Dodgers** | 1953 | 105-49 | .681 | Won 1955 World Series |
| 5 | **San Francisco Giants** | 2021 | 107-55 | .659 | Won 2021 World Series |
| 6 | **Atlanta Braves** | 1998 | 106-56 | .654 | 14th consecutive division title |

### All-Time NL Franchise Win-Loss Totals (Top 5)
| Franchise | W | L | Win% | Seasons | WS Titles | Pennants |
|-----------|---|---|------|---------|-----------|----------|
| Cardinals | 4,723 | 4,214 | .529 | 143 | 11 | 19+ |
| Giants | 4,512 | 4,331 | .514 | 143 | 8 | 21+ |
| Dodgers | 4,442 | 4,256 | .512 | 137 | 7 | 24+ |
| Pirates | 4,134 | 4,131 | .500 | 140 | 5 | 9 |
| Cubs | 4,108 | 4,131 | .499 | 138 | 3 | 17+ |

### Championship Counts (as of 2025)
- 🥇 **Cardinals** — 11 WS titles, 19+ pennants
- 🥈 **Giants** — 8 WS titles (NY + SF era)
- 🥉 **Dodgers** — 7 WS titles, 25+ pennants (most pennants)
- **Braves** — 4 WS titles; 14 straight division titles (1991–2005)
- **Reds** — 5 WS titles; Big Red Machine (.610 Win%)
- **Mets** — 2 WS titles; most productive expansion franchise
- **Phillies** — 2 WS titles
- **Marlins** — 2 WS titles from 3 pennants

### Dominant Franchise Trends
- **Cardinals** — Most consistently successful modern NL franchise across all metrics
- **Giants** — Dynasty 2010–2014 (3 WS titles); strong across both NY and SF eras
- **Dodgers** — Most pennants but smallest WS-to-pennant ratio; modern dominance since 2020
- **Braves** — Unprecedented 14-year division title streak (1991–2005)
- **Cubs** — Historic high-water mark (1906), ended 108-year WS drought in 2016
- **Rockies** — 4,438 losses is the worst all-time record in the NL

## Key Research Findings

### Competitive Balance by Era
1. **Low (1876–1920):** Few teams; dynasties lasted years (Boston, Cubs, Giants)
2. **Moderate (1920–1968):** Cardinals, Giants, Dodgers forged multi-decade rivalries
3. **High (1969–2005):** Expansion + Wild Card increased parity; diverse champions
4. **Lower (2006–present):** Dodgers supremacy; more equitable remaining field

### Champion Win% Range (1960–2025)
- **Highest:** .717 (2020 Dodgers, shortened season)
- **Lowest:** .516 (2006 Cardinals), .519 (2023 D-backs)
- **Trend:** Wild Card era produces lower Win% champions due to broader playoff field

### Notable Anomalies
- **1918:** WWI shortened season (124–129 games)
- **1972:** Players' strike reduced season
- **1981:** Split season due to players' strike
- **1994:** Season canceled entirely; no NL champion
- **2020:** COVID 60-game season; Dodgers won WS (.717 Win%)
- **2022:** NL adopted universal DH; 12-team playoff format introduced

### Franchise H2H Highlights
- Cardinals vs Cubs: Cubs lead (~931 vs ~1,268)
- Giants vs Dodgers: Giants lead incl. NY era (~271 vs ~213)
- Mets vs all NL: Mets lead all-time H2H wins
- Dodgers vs all NL: Dodgers hold the all-time edge across all opponents

## Data Sources

| Source | Coverage | URL | Reliability |
|--------|----------|-----|-------------|
| **Baseball Reference** | NL standings, team stats 1876–present | https://www.baseball-reference.com/leagues/NL/ | ★★★★★ |
| **Retrosheet** | Play-by-play and box scores 1898–present | https://www.retrosheet.org/ | ★★★★★ |
| **Lahman Database (SABR)** | Complete MLB stats 1871–present | https://sabr.org/lahman-database/ | ★★★★★ |
| **Baseball Almanac** | Team-vs-team H2H records | https://www.baseball-almanac.com/ | ★★★★ |
| **FBref.com** | Advanced NL season statistics | https://fbref.com/en/comps/34/history/ | ★★★★★ |
| **Baseball Data Hub** | All MLB seasons browsable | https://baseballdatabank.github.io/ | ★★★★ |
| **StatsCrew** | Historical standings | https://www.statscrew.com/ | ★★★★ |
| **Linger & Look** | Year-by-year NL standings | https://www.lingerandlook.com/ | ★★★★ |
| **Wikipedia** | NL pennant winners, franchise histories | https://en.wikipedia.org/wiki/ | ★★★ |

## Visualization Ideas

1. **NL Franchise Win-Loss Trend Lines** (1876–2025) — Era-by-era dominance mapping
2. **NL Head-to-Head Win Matrix** — Heatmap of franchise matchup records
3. **Champion Win% Distribution** (1960–2025) — Competitive balance histogram
4. **ERA Win% Heatmap** — Team × Season colored by win percentage
5. **Run Differential Trend Lines** — RS vs RA by franchise across decades
6. **Division Dominance Maps** — NL division winners by decade
7. **Championship Drought Tracker** — Years since last title per franchise
8. **Playoff Appearance Frequency** — Postseason bar charts by decade
9. **Expansion Impact Analysis** — Win distribution before/after expansion waves
10. **Dynasty Detection** — Rolling 5-year and 10-year win averages

## Getting Started

```bash
# Clone the repo
git clone https://github.com/zhub9006/nl-team-trends.git
cd nl-team-trends

# Load data with Python/pandas
import pandas as pd
df = pd.read_csv('data/nl_historical_data.csv')
franc = pd.read_csv('data/franchise_summary.csv')
champs = pd.read_csv('nl_champions.csv')
wins = pd.read_csv('nl_team_wins.csv')

# Quick analysis
print(f"Seasons: {df['season'].min()}–{df['season'].max()}")
print(f"Teams: {df['modern_name'].nunique()}")
print(franc.sort_values('win_pct', ascending=False))
```

## Planned Visualizations

Work in progress — see visualization ideas above. Target tools: Python (Matplotlib/Plotly/Seaborn), R (ggplot2), or Observable/D3.js for web-based interactive dashboards.

## Contributing

This is a research/compilation project. Contributions welcome:
- Additional historical data from verified sources
- Statistical analysis and notebooks
- Visualization outputs and interpretations
- Corrections and data validation
