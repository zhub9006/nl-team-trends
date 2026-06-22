# NL Team Trends

Historical National League (NL) team performance data and trend analysis across past seasons.

## Overview

This repository compiles all-time win-loss records, franchise histories, and performance trends for all 15 current National League teams. Data spans from the founding of the National League in **1876** through the end of the **2025** regular season.

The National League is the older of MLB's two leagues, established in 1876 — 25 years before the American League (1901). Interleague play between the NL and AL began in 1997.

## Key Findings

| Insight | Detail |
|---------|--------|
| **Highest NL all-time Win%** | San Francisco Giants (.535) |
| **Most NL wins** | San Francisco Giants (11,651) |
| **Most NL losses** | Philadelphia Phillies (11,425) |
| **Oldest franchise** | Atlanta Braves (continuous since 1871) |
| **Lowest all-time Win%** | Colorado Rockies (.455) |
| **Best single-season NL record** | 1906 Cubs (116-36, .763) |
| **Only .500 franchise** | Pittsburgh Pirates (10,947-10,947) |

## Data Sources

- **Baseball Reference** — Baseball-Reference.com | Comprehensive league and team encyclopedias
- **Baseball Almanac** — Baseball-Almanac.com | NL team-vs-team win-loss matrix (1876–2026)
- **Lahman Database (SABR)** — github.com/chadwickbureau/baseballdatabank | Complete stats from 1871
- **StatMuse** — StatMuse.com | AI-powered sports statistics queries
- **Wikipedia / Grokipedia** — Franchise history context and explanatory notes
- **MLB.com** — Official MLB statistics portal for current-season verification

## Repository Structure

```
nl-team-trends/
├── README.md                     # This file
├── data/
│   ├── nl_all_time_records.csv   # All-time franchise records (CSV) ✓ Complete
│   ├── nl_team_vs_team.csv       # NL head-to-head win-loss matrix (CSV) ✓ Complete
│   └── nl_era_summary.csv        # Era-based performance summaries (CSV) ✓ Complete
├── notebooks/                    # Analysis & visualization notebooks
├── visualizations/               # Generated charts and plots
└── sources/                      # Reference links and methodology notes
```

## Data Highlights

### All-Time Records (Through 2025)

The `data/nl_all_time_records.csv` file contains the complete all-time regular-season records for all 15 current NL franchises, including:
- Total wins, losses, and winning percentage
- Games played (including ties from the pre-1920 era)
- First year in the NL
- Prior franchise names and city relocations
- Division alignment (East, Central, West)

### Team-vs-Team Head-to-Head ✓ Complete

The `data/nl_team_vs_team.csv` file contains the complete NL head-to-head win-loss matrix covering every matchup between all 15 NL franchises from 1876 through 2025. Includes 105 pairwise matchups with win totals and winning percentages.

### Era-Based Trends ✓ Complete

The `data/nl_era_summary.csv` file breaks down franchise performance across five major MLB eras:
- **Founding Era** (1876–1900)
- **Dead-Ball Era** (1901–1919)
- **Live-Ball / Golden Age** (1920–1960)
- **Expansion Era** (1961–1992)
- **Wild Card / Interleague Era** (1993–present)

## Planned Visualizations

1. **All-time winning percentage bar chart** — Ranking all 15 NL franchises
2. **Decade-by-decade trend lines** — How each franchise's Win% shifted over time
3. **Head-to-head heatmap** — NL team-vs-team win rates as a color matrix
4. **Expansion team trajectories** — Comparing post-1960 franchises vs originals
5. **Above/below .500 timeline** — Seasons each team spent above or below .500
6. **Win total accumulation curves** — Cumulative wins over franchise history

## Methodology Notes

- All records reflect **regular-season games only**; postseason is excluded.
- Ties (common in the pre-1920 era) are excluded from winning percentage calculations (Win% = W / (W + L)).
- Franchise relocations are treated as continuous entities (e.g., Brooklyn Dodgers → Los Angeles Dodgers).
- The Milwaukee Brewers record includes their AL tenure (1969–1997) since this repo tracks franchise history.
- The Washington Nationals record includes the Montreal Expos era (1969–2004).
- Data is current through the end of the **2025 regular season**.

## Getting Started

```bash
git clone https://github.com/zhub9006/nl-team-trends.git
cd nl-team-trends
pip install pandas matplotlib seaborn jupyter
```

Open any notebook in `notebooks/` to explore the data and generate visualizations.

## License

This project is for educational and analytical purposes. The underlying baseball data is sourced from publicly available records. All historical statistics are property of Major League Baseball.