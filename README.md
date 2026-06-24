# NL Team Trends

Historical National League team performance data, trends, and visualizations across past MLB seasons.

## Overview

This repository compiles historical National League win-loss records, pennant winners, World Series outcomes, and key team trends spanning decades of MLB play. The goal is to provide a clean, structured dataset for analysis and visualization of how NL teams have performed over time.

## Contents

- **`data/nl_team_performance.csv`** — Season-by-season win-loss records, pennant flags, and division rankings for NL teams (1990–2024)
- **`data/nl_pennant_winners.json`** — Historical NL pennant and World Series winners
- **`notebooks/`** — Jupyter notebooks for analysis and visualization (to be added)
- **`src/`** — Utility scripts for data processing (to be added)

## Data Sources

The historical data in this repository is compiled from:

- **Baseball-Reference.com** — Comprehensive season-by-season team statistics and records
- **MLB.com / Official MLB Records** — Pennant winners, postseason results, and franchise history
- **Retrosheet** — Play-by-play and season summary data for historical accuracy
- **Sean Lahman's Baseball Database** — Public dataset for archival season records

## Key Historical Trends

### Era of Dominance
| Team | Era | Notable Achievement |
|------|-----|---------------------|
| Atlanta Braves | 1991–2005 | 14 consecutive division titles; 1995 World Series champions |
| San Francisco Giants | 2010–2014 | 3 World Series titles in 5 years (2010, 2012, 2014) |
| Los Angeles Dodgers | 2017–2024 | 5 NL pennants in 7 years; 2020 World Series champions |

### Division Structure
- **NL East**: Braves, Mets, Phillies, Nationals, Marlins
- **NL Central**: Cardinals, Brewers, Cubs, Pirates, Reds
- **NL West**: Dodgers, Giants, Padres, Rockies, Diamondback

*(Note: Houston Astros were in the NL from 1962–2012; Milwaukee Brewers have been in the NL Central since 1998)*

## How to Use

1. **Explore the data**: Open `data/nl_team_performance.csv` in any spreadsheet tool or Python/pandas.
2. **Analyze trends**: Use the notebooks in `notebooks/` to run trend analyses.
3. **Build visualizations**: Create charts for win percentages, pennant races, and decade-over-decade changes.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests to add:
- Additional historical seasons (pre-1990 data)
- Advanced metrics (WAR, OPS+, defensive runs saved)
- Player-level performance linked to team trends
- Interactive dashboards

## License

This project is open source. Data sourced from public MLB records and Baseball-Reference.com.