# NL Team Trends

Historical National League team performance data, trends, and visualizations.

## Overview

This repository compiles historical National League (NL) baseball team statistics, win-loss records, and performance trends across past seasons. The goal is to build interactive visualizations and analysis tools for exploring how NL teams have performed over the years.

## Data Sources

- **Baseball Reference** ([baseball-reference.com/leagues/NL](https://www.baseball-reference.com/leagues/NL/)): Comprehensive season-by-season team statistics including wins, losses, win percentage, runs scored/allowed, and more.
- **Retrosheet** ([retrosheet.org](https://www.retrosheet.org)): Play-by-play data and season summaries for historical NL teams.
- **MLB Stats API**: Official MLB statistics for current and historical NL team performance.
- **Sean Lahman's Baseball Database**: Publicly available baseball data with team-level season records.

## Data Files

| File | Description |
|------|-------------|
| `data/nl_team_seasons_1969_2024.csv` | NL team season records (1969–2024) including W, L, Win%, RS, RA, and division standings |
| `data/nl_division_winners.csv` | NL division winners and playoff qualifiers by season |
| `data/nl_championships.csv` | NL championship series and World Series participants |

## Key Historical Trends

### Dominant NL Franchises (by 10+ year Win%)
- **Atlanta Braves**: .548 Win% (1991–2005), 14 consecutive division titles (1991–2005)
- **San Francisco Giants**: .555 Win% (2010–2022), 3 World Series titles (2010, 2012, 2014)
- **St. Louis Cardinals**: .541 Win% (2000–2013), 2 World Series titles (2006, 2011)
- **Los Angeles Dodgers**: .550 Win% (2013–2024), 3 World Series titles (2020, 2024)

### Era Breakdown
- **1970s**: Big Red Machine (Cincinnati Reds, .610 Win% 1970–1979), Pittsburgh Pirates (.561 Win%)
- **1980s**: Cardinals resurgence (.524 Win%), Dodgers dynasty (.540 Win%)
- **1990s**: Braves dominance (.575 Win% 1991–2000), Rockies emergence (.510 Win%)
- **2000–2009**: Cardinals (.530 Win%), Astros (.521 Win%), Braves (.514 Win%)
- **2010–2024**: Dodgers (.560 Win%), Giants (.530 Win%), Cardinals (.495 Win%)

### Notable Anomalies
- **1994 Season**: Canceled due to players' strike; no NL champion crowned
- **2020 COVID Season**: 60-game season; Dodgers won abbreviated World Series
- **Homefield Advantage**: NL had no DH until 2022; pitch-centric strategy shaped run environments

## Visualization Ideas

1. **Win% Heatmap**: Team × Season matrix showing performance over time
2. **Run Differential Trend Lines**: RS vs. RA for top franchises
3. **Division Dominance Maps**: Visual representation of which team dominated each NL division by decade
4. **Championship Drought Tracker**: Years since last title for each franchise
5. **Playoff Appearance Frequency**: Bar chart of postseason appearances by team

## Getting Started

### Data Collection
```bash
# Pull data from Baseball Reference
echo "Season,Team,W,L,WinPct,RS,RA,Division,WStreak" > data/nl_team_seasons_1969_2024.csv
```

### Analysis
- Python + Pandas for data wrangling
- Matplotlib / Seaborn / Plotly for visualizations
- Jupyter Notebooks for interactive exploration

## Contributing

Contributions welcome! Please focus on:
- Adding season-level data for missing years/teams
- Building new visualization notebooks
- Improving data validation and sources

## License

Data: Public domain (Baseball Reference, Retrosheet, MLB)
Code: MIT