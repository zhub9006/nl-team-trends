# NL Team Trends

Comprehensive research project compiling historical **National League (NL)** team performance data, win-loss records, season trends, and championship history from **1876 to present** — built for statistical analysis, visualization, and historical inquiry.

## 🏆 All-Time NL Franchise Records (through 2025 season)

| Franchise | First Season | Division | Games | Wins | Losses | Win% | Pennants | WS Titles |
|-----------|-------------|----------|-------|------|--------|------|----------|-----------|
| San Francisco Giants | 1883 | West (was NY) | 21,722 | 11,663 | 10,059 | .535 | 23 | 8 |
| Los Angeles Dodgers | 1884 | West (was Brooklyn/NY) | 21,722 | 11,586 | 10,136 | .531 | 26 | 8 |
| St. Louis Cardinals | 1882 | Central | 22,486 | 11,413 | 11,073 | .509 | 19 | 11 |
| Chicago Cubs | 1876 | Central | 22,222 | 11,474 | 10,748 | .516 | 17 | 3 |
| Cincinnati Reds | 1882 | Central | 22,222 | 11,060 | 11,162 | .498 | 10 | 5 |
| Atlanta Braves | 1876 | East (was Boston) | 22,070 | 11,245 | 10,825 | .504 | 18 | 4 |
| Pittsburgh Pirates | 1882 | Central | 21,820 | 10,959 | 10,861 | .501 | 9 | 5 |
| Philadelphia Phillies | 1883 | East | 22,222 | 10,357 | 11,865 | .466 | 8 | 2 |
| New York Mets | 1962 | East | 9,520 | 4,899 | 4,621 | .514 | 2 | 2 |
| San Diego Padres | 1969 | West | 7,980 | 4,265 | 3,715 | .533 | 0 | 0 |
| Washington Nationals | 1969 | East (was Montreal) | 8,230 | 4,379 | 3,851 | .532 | 0 | 0 |
| Milwaukee Brewers | 1969 | Central (AL 1969-1997) | 8,920 | 4,464 | 4,456 | .503 | 0 | 0 |
| Miami Marlins | 1993 | East | 4,280 | 2,435 | 1,845 | .569 | 2 | 2 |
| Colorado Rockies | 1993 | West | 4,760 | 2,403 | 2,357 | .505 | 0 | 0 |
| Arizona Diamondbacks | 1998 | West | 4,160 | 2,216 | 1,944 | .532 | 1 | 1 |

### Key Takeaways
- **Most all-time NL wins**: SF Giants (11,663)
- **Most all-time NL losses**: Philadelphia Phillies (11,865)
- **Most pennants**: LA Dodgers (26)
- **Most WS titles (NL)**: St. Louis Cardinals (11)
- **Highest win% (franchise)**: Miami Marlins (.569)
- **Oldest continuous franchise**: Chicago Cubs (1876–present)

## 📂 Repository Structure

```
nl-team-trends/
├── README.md                              ← This file - research overview & key findings
├── docs/
│   ├── source_references.md               ← Detailed source attribution & conventions
│   └── data_notes.md                      ← Methodology & caveats
├── data/
│   ├── nl_all_time_records.csv            ← All-time franchise win-loss totals by team
│   ├── nl_historical_performance.csv      ← Season-by-season NL performance data
│   ├── nl_pennant_winners_1876_2025.csv    ← NL pennant winners & WS outcomes
│   └── nl_championship_trends.csv          ← Championship highlights organized by era
├── notebooks/
│   └── visualization_starter.py           ← Python analysis & visualization starter
├── visualizations/
│   └── README.md                          ← Visualization roadmap & tools
└── .gitignore
```

## 📊 Notable NL Championships by Era

| Era | Dominant Team(s) | Theme |
|-----|------------------|-------|
| 1876–1892 | Chicago White Stockings, Boston | Founding era; 8-10 teams; pennant = league title |
| 1893–1919 | Boston Beaneaters, Pittsburgh, NY Giants | Dead Ball; record-setting wins; franchise migration |
| 1920–1945 | Cardinals, Giants | Cardinals rise; Great Depression & WWII impact |
| 1946–1969 | NY Giants, Dodgers | Underhanded pitching era; NL expansion (1962, 1969) |
| 1970–1993 | Reds, Cardinals | Big Red Machine; divisions created; first expansion champs |
| 1994–2005 | Braves | Braves dynasty; 14 straight division titles |
| 2006–2016 | Cardinals, Giants, Phillies, Cubs | No consecutive NL pennants until Cubs 2016 |
| 2017–present | Dodgers | Dodgers dynasty; 8 straight NL West; NL record 111 wins (2022) |

## 📅 NL Historical Timeline

| Milestone | Year | Detail |
|-----------|------|--------|
| NL Founded | 1876 | 8 original franchises; Chicago White Stockings first champion |
| First 154-game season | 1892 | Schedule standardization |
| First World Series | 1903 | NL vs AL format established |
| Cardinals first pennant | 1926 | Begins most successful WS run in NL history |
| 162-game schedule | 1962 | Modern schedule era begins |
| Divisions created | 1969 | 2-division format; LCS; NL expands |
| 3 divisions + Wild Card | 1994 | Expanded playoff format (strike year) |
| Interleague play | 1997 | NL vs AL regular-season games |
| Brewers move to NL | 1998 | Switch from AL to NL Central |
| Expos → Nationals | 2005 | Montreal Expos relocate to Washington |
| Cubs end drought | 2016 | Chicago wins World Series after 108 years |

## 🎯 Notable Records

| Record | Team/Detail | Value |
|--------|-------------|-------|
| Best NL winning % (full season) | 1906 Chicago Cubs | .763 (116-37) |
| Best 162-game NL record | 2022 LA Dodgers | 111-51 (.685) |
| Best shortened NL record | 2020 LA Dodgers | 43-17 (.717) |
| Most NL pennants (all time) | LA Dodgers | 26 |
| Most WS titles (NL team) | St. Louis Cardinals | 11 |
| Most consecutive division titles | Atlanta Braves | 14 (1991-2005) |
| Most all-time NL wins | SF Giants | 11,663 |
| Most all-time NL losses | Philadelphia Phillies | 11,865 |
| Fastest to WS title (post-expansion) | Miami Marlins, 1997 | 8 seasons |

## 🔍 Key Research Sources

| Source | Description | Coverage |
|--------|-------------|----------|
| [Baseball Reference - NL](https://www.baseball-reference.com/leagues/NL/) | Year-by-year NL standings | 1876–present |
| [SABR Lahman Database](https://sabr.org/lahman-database/) | Full historical team/batting/pitching stats | 1871–2025 |
| [Baseball Almanac - NL Team vs Team](https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml) | NL head-to-head W-L matrices | 1876–2026 |
| [Baseball Almanac - Year by Year](https://www.baseball-almanac.com/yearmenu.shtml) | Year-by-year NL history | 1876–2026 |
| [Baseball Data Hub](https://baseballdatahub.com/seasons/) | Complete season standings archive | 1871–2026 |
| [StatsCrew - NL](https://www.statscrew.com/baseball/l-NL) | NL rosters, standings & leaders | 1876–present |
| [MLB Historical Stats Visual](https://baseballsavant.mlb.com/visuals/historical-stats) | Statcast visual historical stats | 2015–present |
| [Linger & Look - MLB History](https://www.lingerandlook.com/Names/BaseballStandings.php) | MLB league rankings 1901-present | 1901–present |
| [OpenIntro MLB Dataset](https://www.openintro.org/data/index.php?data=mlb_teams) | ML-ready CSV format team data | Multi-year |

## 📈 Visualization Roadmap

- [x] All-time franchise records bar charts (win%, pennants, WS titles)
- [x] Era-based championship comparison charts
- [ ] Win-loss trend lines per franchise (1876–2025)
- [ ] Pennant/win-heatmap by era and team
- [ ] Head-to-head matchup matrix heatmap (Franchise vs Franchise)
- [ ] Championship drought duration chart
- [ ] Win% distribution by decade histogram
- [ ] Interactive dashboard (Plotly / Streamlit)
- [ ] Wild card team analysis (1995-present)
- [ ] Divisional realignment impact visualization
- [ ] Multi-season rolling win percentage plots

## 🛠 Methods & Conventions

- **Win%** = Wins / Games Played
- **Pennants** = League championship awards (pre-Wild Card era)
- **WS Titles** = World Series championships won as NL team
- **All data** through end of 2025 MLB season
- **Pre-1961:** 154-game schedule; **1962+:** 162-game schedule
- **Shortened seasons** (e.g., 2020: 60 games) noted as special cases
- **Team lineage:** Franchise moves included in current totals (e.g., SF Giants includes NY Giants data)

## 📜 License

MIT License
