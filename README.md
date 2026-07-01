# NL Team Trends

Historical National League team performance data, win-loss records, seasonal trends, and visualizations spanning the NL's founding in 1876 through the present day.

## Overview

This repository compiles historical win-loss records, seasonal performance trends, and key statistics for every National League franchise dating back to the league's founding in 1876. The goal is to provide a comprehensive dataset for analyzing team dominance, franchise trajectories, divisional realignments, and the evolving competitive landscape of baseball's oldest league.

**Core coverage:** 1876–2025 (150 NL seasons spanning all 15 NL franchises)

## Data Sources

The primary sources used to compile the historical NL data in this repository are:

| Source | Description | URL |
|---|---|---|
| **Baseball-Reference** | Complete NL team wins records, year-by-year standings | [baseball-reference.com/leagues/NL](https://www.baseball-reference.com/leagues/NL/index.shtml) |
| **Baseball Data Hub** | All MLB seasons 1871–2026 with final standings, stats leaders, postseason results | [baseballdatahub.com/seasons](https://baseballdatahub.com/seasons/) |
| **SABR Lahman Database** | Complete batting, pitching, fielding, standings, team stats, postseason data from 1871–2025 (CSV/SQL) | [sabr.org/lahman-database](https://sabr.org/lahman-database/) |
| **Retrosheet** | Play-by-play game data for all AL/NL seasons from 1910–2025 | [retrosheet.org](https://www.retrosheet.org/) |
| **FBref.com** | Advanced NL season statistics (post-1993) | [fbref.com/en/comps/34/history/](https://fbref.com/en/comps/34/history/) |
| **Baseball Almanac** | Team-vs-team H2H records | [baseball-almanac.com](https://www.baseball-almanac.com/) |
| **StatsCrew** | Historical NL standings | [statscrew.com/baseball/l-NL](https://www.statscrew.com/baseball/l-NL) |

## Key Historical Trends

### Franchise Longevity & Dominance
- **Atlanta Braves** — 14+ division titles across multiple decades; the only franchise to win a division in every decade since the 1980s
- **St. Louis Cardinals** — Most NL pennants (19) and most World Series titles among NL teams (11)
- **San Francisco Giants** — Most World Series titles in the NL (8 since moving to SF), 23 total pennants
- **Los Angeles Dodgers** — 24 NL pennants, 7 World Series titles; dominant in the 1950s–80s and recently (8 of last 10 NL pennants, 2014–2025)
- **Cincinnati Reds** — 5 World Series titles, strong Big Red Machine era (1970s)
- **Chicago Cubs** — 1906: all-time NL season record (116-36, .763 Win%)
- **Colorado Rockies** — Worst all-time NL franchise (.443 Win%, 2,618W-3,292L)

### Era-Specific Trends

| Era | Years | Teams | Key Characteristics |
|-----|-------|-------|---------------------|
| **Pre-Modern** | 1876–1899 | 8–12 | 60–154 game seasons; no pitcher mound; single-table standings |
| **Dead Ball** | 1900–1919 | 8 | Lively ball emerging; first WS 1903; Ruth HR surge |
| **Live Ball** | 1920–1945 | 8 | Jackie Robinson (1947); WWII roster impact |
| **Post-War** | 1946–1968 | 10–12 | Dodgers dynasty; Braves to Milwaukee (1953); expansion to 10 (1962) |
| **Expansion** | 1969–1992 | 12 | Two-division NL; Wild Card introduced (1969) |
| **Divisional** | 1994–2019 | 14–15 | Three divisions + Wild Card (1994); Braves 14-year division title streak (1991–2005) |
| **COVID-Modern** | 2020–present | 15 | 60-game (2020); universal DH (2022); 12-team playoff (2022+) |

### Structural Changes Timeline
- **1876–1892** — Single-table format; no divisions
- **1892–1968** — Split into East & West divisions
- **1969** — Wild Card introduced alongside two-division format
- **1994** — Three-division structure (East, Central, West) + Wild Card expanded
- **1997** — Interleague play begins
- **1998** — Milwaukee Brewers move from AL to NL; Arizona Diamondbacks join
- **2005** — Montreal Expos relocate as Washington Nationals
- **2013** — Houston Astros leave NL (15 teams per league)
- **2020** — COVID-19: 60-game shortened season
- **2022** — 12-team playoff introduced; universal DH adopted

### The 1994 Strike
- Season interrupted August 12, 1994; postseason and World Series cancelled
- Only year without a World Series since 1904
- Montreal Expos were leading the NL at the time of the strike
- Reshaped labor relations and salary structures across baseball
- Demonstrated vulnerability of season-based competitive frameworks

### Notable Seasons & Records
- **1968** — "Year of the Pitcher": Bob Gibson 1.12 ERA; MLB lowered the mound the following year
- **2019** — MLB-wide record: 6,776 home runs across both leagues
- **1906** — Cubs set all-time NL season record: 116-36 (.763)

## Repository Structure

```
nl-team-trends/
├── README.md                         ← This file (overview, sources, trends)
├── COPYING                           ← License (MIT)
├── nl_champions.csv                  ← NL postseason champions & results (1960–2025)
├── nl_team_wins.csv                  ← All-time win totals per franchise
├── requirements.txt                  ← Python dependencies
├── SOURCES.md                        ← Data sources & methodology
├── data/
│   ├── nl_historical_data.csv                ← Key NL seasons (1876–present)
│   ├── nl_historical_data_complete.csv       ← Fuller sampled dataset (1876–2025)
│   ├── franchise_summary.csv                 ← All-time franchise win-loss summaries
│   ├── era_analysis.csv                      ← NL era-level aggregates (7 eras)
│   ├── CHAMPIONS.md                          ← Detailed NL championship timeline (1869-2025)
│   ├── readme.md                             ← Data folder documentation
│   ├── nl_all_time_franchise_records.csv     ← Single-season records & championship droughts
│   └── nl_team_trends_data_dictionary.md     ← Schema documentation
├── src/
│   └── nl_viz.py                   ← Standalone 5-chart PNG generator
└── notebooks/
    └── nl_visualizations.ipynb    ← Jupyter notebook version
```

## Visualizations

All charts are generated with `python src/nl_viz.py` or by running the Jupyter notebook:

| # | Chart | Description |
|---|-------|-------------|
| 1 | Franchise Win% + Era Win% | Horizontal bar + side-by-side era comparison |
| 2 | 10-Year Rolling Win% Trend Lines | Franchise trajectories (1876-2025) |
| 3 | Era Win% Heatmap | Franchise × Era colored by Win% |
| 4 | Championship Drought Tracker | Time between NL WS titles per franchise |

## Quick-Start

```bash
# Clone
git clone https://github.com/zhub9006/nl-team-trends.git
cd nl-team-trends

# Option 1 — Pandas analysis
pip install pandas matplotlib seaborn
python -c "import pandas as pd; df = pd.read_csv('data/nl_historical_data.csv'); print(df.head())"

# Option 2 — Run all 5 charts
python src/nl_viz.py
ls plots/*.png          # see generated charts

# Option 3 — JupyterLab
jupyter lab             # then open notebooks/nl_visualizations.ipynb
```

## Contributing

This is a research/compilation project. Contributions welcome:
- Additional historical seasons from verified data sources
- Statistical analysis or Jupyter notebooks
- Visualization outputs and commentary
- Data corrections or validation

## License

Code: MIT (see [LICENSE](LICENSE))
Data: Public domain (CC0 equivalent)
