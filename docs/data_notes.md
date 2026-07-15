# MNL Team Trends — Data Notes

## Methodology & Conventions

### Data Sources
All historical data was compiled from multiple authoritative baseball statistics sources:
- **Baseball Reference** — Year-by-year NL standings
- **Baseball Almanac** — Team-vs-team W-L matrices
- **SABR Lahman Database** — Complete CSV datasets for statistical modeling
- **StatsCrew** — Rosters, standings, and leaders

### Key Conventions
| Convention | Detail |
|-----------|--------|
| Win% Formula | Wins / (Wins + Losses) |
| Schedule Eras | Pre-1892: variable; 1893-1960: 154 games; 1961-present: 162 games |
| Division Format | 2 divisions (E/W) from 1969; 3 divisions (E/C/W) from 1994 |
| Wild Cards | Introduced 1994; 1 WC from 1994-2011; 2 WCs from 2012 |

### Important Caveats
- The 1994 season was canceled by a players' strike; no pennant or WS was awarded.
- The 2020 season was shortened to 60 games due to COVID-19; Win% is still comparable but use context when benchmarking.
- Milwaukee Brewers moved from the AL to NL Central in 1998.
- The Montreal Expos relocated and became the Washington Nationals in 2005.
- Some very early seasons (1876-1892) had varying game counts (e.g., 70, 80, 84 games).
- Interleague play began in 1997 and became full-time in 2023, so AL-vs-NL comparisons should account for this.

### Data File Descriptions
| File | Description |
|------|-------------|
| `nl_all_time_records.csv` | All-time franchise win-loss totals for all 15 NL teams |
| `nl_key_seasons.csv` | Notable individual seasons with highlights |n| `nl_pennant_winners_recent.csv` | NL pennant winners 2000-2025 with WS results |
| `nl_recent_standings.csv` | Full standings matrix 2020-2025 for all NL teams |
| `nl_championship_trends.csv` | Era-by-era championship summary |
| `nl_notable_records.csv` | Single-season and franchise record collection |
| `source_references.md` | Full source attribution and methodology |

## Recommended Next Steps
1. Download the [SABR Lahman Database](https://sabr.org/lahman-database/) for complete season-by-season team-level CSV datasets.
2. Add Python analysis notebooks in the `notebooks/` directory.
3. Build interactive visualizations using Plotly, Altair, or Matplotlib.
4. Cross-reference with historical newspaper archives for context on pennant races.
