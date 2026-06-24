# NL Team Trends

Historical National League team performance data, trends, and visualizations.

## Overview

This repository compiles historical National League (NL) baseball team statistics, win-loss records, and performance trends across past seasons — from the early 1900s through the present day. The goal is to build interactive visualizations and analysis tools for exploring how NL teams have performed over the years, identifying dominant franchises, era-specific trends, and long-term competitive shifts.

## Data Sources

| Source | URL | Description |
|--------|-----|-------------|
| **Baseball Reference** | [baseball-reference.com/leagues/NL](https://www.baseball-reference.com/leagues/NL/) | Comprehensive season-by-season team stats including wins, losses, win percentage, runs scored/allowed, and more. |
| **Retrosheet** | [retrosheet.org](https://www.retrosheet.org) | Play-by-play data and season summaries for historical NL teams dating back to the 1800s. |
| **MLB Stats API** | [statsapi.mlb.com](https://statsapi.mlb.com) | Official MLB statistics for current and historical NL team performance. |
| **Sean Lahman's Database** | [lahmandatabase.com](https://www.lahmandatabase.com) | Publicly available baseball data with team-level season records spanning 1871–present. |
| **Baseball Hall of Fame** | [baseballhall.org](https://www.baseballhall.org) | Historical context, franchise timelines, and archival records. |

## Data Files

| File | Description |
|------|-------------|
| `data/nl_team_seasons_1969_2024.csv` | NL team season records (1969–2024) including W, L, Win%, RS, RA, Division, Win/Loss streaks, playoff status, and championship info |
| `data/nl_historical_trends.json` | Aggregated era-by-era and franchise-by-franchise performance summaries with key trend metrics |

## Key Historical Trends

### Dominant NL Franchises (by 10+ year Win%)

| Franchise | Era | Win% | Key Achievements |
|-----------|-----|------|-----------------|
| **Atlanta Braves** | 1991–2005 | .548 | 14 consecutive division titles, 1995 WS champion |
| **San Francisco Giants** | 2010–2022 | .555 | 3 World Series titles (2010, 2012, 2014) |
| **St. Louis Cardinals** | 2000–2013 | .541 | 2 World Series titles (2006, 2011) |
| **Los Angeles Dodgers** | 2013–2024 | .550 | 3 World Series titles (2020, 2024) |
| **Cincinnati Reds** | 1970–1979 | .610 | 2 World Series titles (1975, 1976), Big Red Machine |
| **Pittsburgh Pirates** | 1970–1979 | .561 | 2 World Series titles (1971, 1979) |

### Era Breakdown

| Era | Years | Avg Runs/Game | Dominant Team | Win% |
|-----|-------|---------------|---------------|------|
| Dead Ball | 1900–1919 | ~3.4 | Pittsburgh Pirates | .580 |
| Live Ball | 1920–1945 | ~4.7 | St. Louis Cardinals | .558 |
| Post-War | 1946–1968 | ~4.3 | Brooklyn/LA Dodgers | .580 |
| Modern Expansion | 1969–1992 | ~4.5 | Cincinnati Reds | .610 |
| Divisional | 1993–2024 | ~4.7 | Atlanta Braves | .560 |

### Notable Anomalies

- **1994**: Season canceled due to players' strike; no NL champion crowned
- **2020**: COVID-affected 60-game season; Dodgers won shortened World Series
- **2022**: NL adopted DH; approved 12-team playoff format

## Visualization Ideas

1. **Win% Heatmap**: Team × Season matrix showing performance over time
2. **Run Differential Trend Lines**: RS vs. RA for top franchises across decades
3. **Division Dominance Maps**: Which team dominated each NL division by decade
4. **Championship Drought Tracker**: Years since last title for each franchise
5. **Playoff Appearance Frequency**: Bar chart of postseason appearances

## Getting Started

### Analysis Tools
- **Python + Pandas** for data wrangling
- **Matplotlib / Seaborn / Plotly** for visualizations
- **Jupyter Notebooks** for interactive exploration

## Contributing

Contributions welcome! Please focus on:
- Adding season-level data for missing years/teams (especially pre-1969)
- Building new visualization notebooks
- Improving data validation and source citations

## License

Data: Public domain (Baseball Reference, Retrosheet, MLB, Lahman Database)
Code: MIT