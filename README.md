# NL Team Trends

> Historical National League team performance data, win-loss records, and trend visualizations across past MLB seasons (1876–2025).

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Overview

This repository compiles, curates, and analyzes historical National League (NL) baseball team statistics for all 15 active NL franchises from the league's founding in **1876** through the present day. The goal is to serve as a comprehensive dataset and analysis framework for exploring team dominance, franchise trajectories, divisional realignments, and the evolving competitive landscape of baseball's oldest league.

**Core coverage:** 1876–2025 (150 NL seasons spanning all 15 NL franchises).

## 📂 Repository Structure

```
nl-team-trends/
├── README.md                         ← This file
├── COPYING                       ← License (MIT)
├── nl_champions.csv                ← NL postseason champions & results (1960–2025)
├── nl_team_wins.csv                ← All-time win totals per franchise
├── requirements.txt                ← Python dependencies
├── SOURCES.md                      ← Data sources & methodology
├── data/
│   ├── nl_historical_data.csv      ← Key NL seasons (1876–present)
│   ├── nl_historical_data_complete.csv   ← Fuller sampled dataset (1876–2025)
│   ├── franchise_summary.csv       ← All-time franchise win-loss summaries (15 rows)
│   ├── era_analysis.csv            ← NL era-level aggregates (7 eras)
│   ├── CHAMPIONS.md                ← Detailed NL championship timeline (1869-2025)
│   ├── readme.md                   ← Data folder documentation
│   ├── nl_all_time_franchise_records.csv   ← Single-season records & championship droughts
│   └── nl_team_trends_data_dictionary.md  ← Schema documentation
├── src/
│   └── nl_viz.py                   ← Standalone 5-chart PNG generator
└── notebooks/
    └── nl_visualizations.ipynb    ← Jupyter notebook version
```

## 📊 Visualizations (ready to generate)

All charts are generated with `python src/nl_viz.py` or by running the Jupyter notebook:

| # | Chart | Description |
|---|-------|-------------|
| 1 | Franchise Win% + Era Win% | Horizontal bar + side-by-side era comparison |
| 2 | 10-Year Rolling Win% Trend Lines | Franchise trajectories (1876-2025) |
| 3 | Era Win% Heatmap | Franchise × Era colored by Win% |
| 4 | Championship Drought Tracker | Time between NL WS titles per franchise |

## 📥 Quick-Start

```bash
# Clone
git clone https://github.com/zhub9006/nl-team-trends.git
cd nl-team-trends

# Option 1 — Pandas analysis
pip install pandas matplotlib seaborn
python -c "import pandas as pd; df = pd.read_csv('data/nl_historical_data_complete.csv'); print(df.head())"

# Option 2 — Run all 5 charts
python src/nl_viz.py
ls plots/*.png          # see generated charts

# Option 3 — JupyterLab
jupyter lab             # then open notebooks/nl_visualizations.ipynb
```

## 🔗 Primary Data Sources

| Source | Coverage | URL | Reliability |
|--------|----------|-----|-------------|
| **Baseball Reference** | NL standings 1876–present | https://www.baseball-reference.com/leagues/NL/ | ★★★★★ |
| **Retrosheet** | Play-by-play / box scores 1898–present | https://www.retrosheet.org/ | ★★★★★ |
| **Lahman Database (SABR)** | Complete MLB stats 1871–present | https://sabr.org/lahman-database/ | ★★★★★ |
| **FBref.com** | Advanced NL season statistics | https://fbref.com/en/comps/34/history/ | ★★★★★ |
| **Baseball Almanac** | Team-vs-team H2H records | https://www.baseball-almanac.com/ | ★★★★ |
| **StatsCrew** | Historical NL standings | https://www.statscrew.com/baseball/l-NL | ★★★★ |

## 🏆 Key Research Highlights

- **Cardinals** — All-time NL dynasty with 11 WS titles, 23+ pennants (143 seasons)
- **Giants** — Most championships when NY+SF combined (12 NL titles)
- **Dodgers** — Most NL pennants; 8 of last 10 NL pennants (2014-2025)
- **Braves** — Unprecedented 14-year division title streak (1991-2005)
- **Rockies** — 2,618 wins vs 3,292 losses = worst all-time NL franchise (.443 Win%)
- **Cubs** — 1906: all-time NL season record (116-36, .763)
- **Championship droughts** — Diamondbacks (24y away since 2001), Rockies (22y), Marlins (22y)
- **Recent dominance** — Dodgers won 8 of 10 NL pennants (2014-2023, plus 2024-2025)
- **Expansion disruption** — Every wave (1962/1969/1993/1998) disrupted existing hierarchies
- **Competitive balance** — NL champion Win% range (lowest 2006 Casey .516, most extreme 2006 2023 D-backs .519)

## 📈 Era Breakdown

| Era | Years | Teams | Key Events |
|-----|-------|-------|------------|
| **Pre-Modern** | 1876–1899 | 8-12 | 60–154 game seasons; no pitcher mound |
| **Dead Ball** | 1900–1919 | 8 | Lively ball emerging; first WS 1903; Ruth HR surge |
| **Live Ball** | 1920–1945 | 8 | Jackie Robinson (1947); WWII roster impact |
| **Post-War** | 1946–1968 | 10–12 | Dodgers dynasty; Braves to Milwaukee (1953); expansion to 10 (1962) |
| **Expansion** | 1969–1992 | 12 | Two-division NL; wildcard (1969) |
| **Divisional** | 1994–2019 | 14–15 | Three divisions + wildcard (1994); Braves (1991-2005) |
| **COVID-Modern** | 2020–present | 15 | 60-game (2020); universal DH (2022); 12-team playoff (2022+) |

## 🤝 Contributing

This is a research/compilation project. Contributions welcome:
- Additional historical seasons from verified data sources
- Statistical analysis or Jupyter notebooks
- Visualization outputs and commentary
- Data corrections or validation

## 📄 License

Code: MIT (see [LICENSE](LICENSE))
Data: Public domain (CC0 equivalent)

---

*Created / maintained by zhub9006 • Last updated July 2026*
