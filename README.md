# NL Team Trends

Comprehensive research project compiling historical **National League (NL)** team performance data, win-loss records, season trends, and championship history from 1876 to present — built for statistical analysis, visualization, and historical inquiry.

## Overview

The National League is baseball's oldest professional league, founded on **February 2, 1876** as the first fully professional baseball organization to survive to the present day — replacing the National Association. This repository serves as a centralized research hub for all NL franchise records, head-to-head performance matrices, era-specific trends, and win-loss analysis.

All data is through the end of the **2025 MLB season**.

## 🏆 All-Time NL Franchise Records (through 2025 season)

| Franchise | First Season | Division | Games | Wins | Losses | Win% | Pennants | WS Titles |
|-----------|-------------|----------|-------|------|--------|------|----------|-----------|
| San Francisco Giants | 1883 | West | 21,722 | 11,663 | 10,059 | .535 | 23 | 8 |
| Los Angeles Dodgers | 1884 | West | 21,722 | 11,586 | 10,136 | .531 | 26 | 8 |
| St. Louis Cardinals | 1882 | Central | 22,486 | 11,413 | 11,073 | .509 | 19 | 11 |
| Chicago Cubs | 1876 | Central | 22,222 | 11,474 | 10,748 | .516 | 17 | 3 |
| Cincinnati Reds | 1882 | Central | 22,222 | 11,060 | 11,162 | .498 | 10 | 5 |
| Atlanta Braves | 1876 | East | 22,070 | 11,245 | 10,825 | .504 | 18 | 4 |
| Pittsburgh Pirates | 1882 | Central | 21,820 | 10,959 | 10,861 | .501 | 9 | 5 |
| Philadelphia Phillies | 1883 | East | 22,222 | 10,357 | 11,865 | .466 | 8 | 2 |
| New York Mets | 1962 | East | 9,520 | 4,899 | 4,621 | .514 | 2 | 2 |
| Washington Nationals | 1969 | East | 8,230 | 4,379 | 3,851 | .532 | 0 | 0 |
| San Diego Padres | 1969 | West | 7,980 | 4,265 | 3,715 | .533 | 0 | 0 |
| Milwaukee Brewers | 1969 | Central | 8,920 | 4,464 | 4,456 | .503 | 0 | 0 |
| Miami Marlins | 1993 | East | 4,280 | 2,435 | 1,845 | .569 | 2 | 2 |
| Colorado Rockies | 1993 | West | 4,760 | 2,403 | 2,357 | .505 | 0 | 0 |
| Arizona Diamondbacks | 1998 | West | 4,160 | 2,216 | 1,944 | .532 | 1 | 1 |

### Key Takeaways from All-Time Records
- **Most all-time NL wins**: San Francisco Giants (11,663)
- **Most all-time NL losses**: Philadelphia Phillies (11,865)
- **Most pennants**: LA Dodgers (26)
- **Most WS titles (NL)**: St. Louis Cardinals (11)
- **Highest win% (active franchise)**: Miami Marlins (.569) among post-1960s franchises
- **Oldest continuous franchise**: Chicago Cubs (1876–present)
- **Youngest active franchise**: Arizona Diamondbacks (1998–present)

## 📂 Repository Structure

```
nl-team-trends/
├── README.md                              ← Research overview & key findings (this file)
├── requirements.txt                       ← Python dependencies
├── scripts/
│   └── analyze_nl.py                      ← Analysis & visualization script
├── data/
│   ├── nl_all_time_records.csv            ← All-time franchise win-loss totals by team
│   ├── nl_historical_performance.csv      ← Multi-era season-by-season data (1876–2025)
│   ├── nl_pennant_winners_recent.csv      ← NL pennant winners 1995–2025
│   ├── nl_recent_standings.csv            ← Full standings 2020–2025
│   ├── nl_championship_trends.csv         ← Championship highlights organized by era
│   ├── nl_notable_records.csv             ← Notable single-season and franchise records
│   ├── nl_head_to_head.csv                ← Team-vs-team matchup matrix (college-game format)
│   └── nl_era_comparison.csv              ← Era-by-era comparison metrics
├── docs/
│   └── data_notes.md                      ← Methodology, conventions & caveats
├── visualizations/
│   ├── README.md                          ← Visualization roadmap & tools
│   ├── visualization_roadmap.md           ← Detailed visualization planning
│   └── output/                            ← Generated charts (populated by scripts)
├── notebooks/                             ← (planned) analysis Jupyter notebooks
├── source_references.md                   ← Detailed source attribution
├── .gitignore
└── LICENSE (MIT)
```

## 📊 Notable NL Championships by Era

| Era | Dominant Team(s) | Theme |
|-----|------------------|-------|
| 1876–1892 | Chicago White Stockings, Boston | Founding era; 8-team league |
| 1893–1919 | Cubs, Giants, Pirates, Braves | Dead Ball; record-setting wins |
| 1920–1950 | Cardinals, Giants, Dodgers/NY | Power transition; franchise migration begins |
| 1951–1969 | Giants, Dodgers, Mets, Cardinals | Relocation era; Miracle Mets 1969 |
| 1970–1989 | Reds, Phillies, Cardinals, Mets | Big Red Machine; competitive parity |
| 1990–2005 | Braves, Cardinals, Marlins, D-backs | Braves dynasty; first expansion champions |
| 2006–2016 | Cardinals, Giants, Phillies, Cubs | Resurgence cycle; Cubs end drought 2016 |
| 2017–present | Dodgers | Dodgers dynasty; 8 straight NL West |

## 🏅 Notable Single-Season & Franchise Records

| Record | Team/Detail | Value |
|--------|-------------|-------|
| Best NL winning percentage | 1906 Chicago Cubs | .763 (116-37) |
| Best 162-game NL record | 2022 LA Dodgers | 111-51 (.685) |
| Best shortened NL record | 2020 LA Dodgers | 43-17 (.717) |
| Most NL pennants | LA Dodgers | 26 (through 2025) |
| Most WS titles (NL) | St. Louis Cardinals | 11 |
| Most consecutive division titles | Atlanta Braves | 14 (1991-2005) |
| Most all-time NL wins | San Francisco Giants | 11,663 |
| Most all-time NL losses | Philadelphia Phillies | 11,865 |
| Longest championship drought | Chicago Cubs | 108 years (1908-2016) |
| Highest modern win% (162-game) | 2022 LA Dodgers | .685 (111-51) |
| Most pennants without WS title | Padres/Dodgers/etc. | Various |

## 📅 NL Historical Timeline

| Milestone | Year | Detail |
|-----------|------|--------|
| NL Founded | 1876 | 8 original franchises; Chicago White Stockings first champion |
| First 154-game season | 1892 | Schedule standardization begins |
| First World Series | 1903 | NL vs AL format established |
| 162-game schedule adopted | 1961 | Modern schedule era begins |
| Divisions created (E/W) | 1969 | 2-division format; LCS introduced |
| 3 divisions (+ Wild Card) | 1994 | Expanded playoff format |
| Interleague play begins | 1997 | NL vs AL regular-season games |
| Full interleague schedule | 2023 | Every team plays every other team |
| Milwaukee Brewers move | 1998 | Switch from AL to NL Central |
| Nats relocation | 2005 | Montreal Expos → Washington Nationals |

## 🔍 Key Research Sources

| Source | Description | Coverage |
|--------|-------------|----------|
| [Baseball Reference](https://www.baseball-reference.com/leagues/NL/) | Year-by-year NL standings & leaders | 1876–present |
| [SABR Lahman DB](https://sabr.org/lahman-database/) | Full historical team/batting/pitching stats | 1871–2025 |
| [Baseball Almanac](https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml) | NL team-vs-team W-L matrices | 1876–2026 |
| [Baseball Data Hub](https://baseballdatahub.com/seasons/) | Complete season standings archive | 1871–2026 |
| [StatsCrew](https://www.statscrew.com/baseball/l-NL) | NL rosters, standings & leaders | 1876–present |
| [StatMuse](https://www.statmuse.com/mlb/ask/most-national-league-titles) | NL championship leaders & franchise stats | 1876–2026 |
| [OpenIntro MLB Dataset](https://www.openintro.org/data/index.php?data=mlb_teams) | ML-ready MLB team data | Multi-year |

## 📈 Visualization Roadmap

- [ ] Win-loss trend lines per franchise (1876–2025) — run `scripts/analyze_nl.py --trend`
- [ ] Pennant/win heatmap by era
- [ ] Head-to-head matchup matrix heatmap (included in head-to-head CSV)
- [ ] Championship drought duration chart — run `scripts/analyze_nl.py --drought`
- [ ] Win% distribution by decade (box plot)
- [ ] Era comparison bar chart — run `scripts/analyze_nl.py --era`
- [ ] Pennant winners timeline — run `scripts/analyze_nl.py --pennant`
- [ ] Notable records chart — run `scripts/analyze_nl.py --records`
- [ ] Interactive dashboard (Plotly / Streamlit)

## 🛠 Methods & Conventions

- Win% = Wins / Games Played
- Pennants = League championship awards (pre-Wild Card era)
- WS Titles = World Series championships won as an NL team
- All data through end of 2025 MLB season
- Pre-1961 seasons use 154-game schedule; 1961+ uses 162-game schedule
- Shortened seasons (e.g., 2020: 60 games) are noted as special cases
- Franchise continuity: relocated teams (NY→LA Dodgers, NY→SF Giants, Montreal→Washington) are combined under current franchise name
- Win% is not directly comparable across 154-game and 162-game eras for cumulative records

## 📥 Quick Start

```bash
# Clone the repo
git clone https://github.com/zhub9006/nl-team-trends.git
cd nl-team-trends

# Install dependencies
pip install -r requirements.txt

# Run all visualizations
python scripts/analyze_nl.py

# Or run specific visualizations
python scripts/analyze_nl.py --trend    # Win-loss trends
python scripts/analyze_nl.py --era      # Era comparison
python scripts/analyze_nl.py --h2h      # Head-to-head
python scripts/analyze_nl.py --drought  # Championship droughts
python scripts/analyze_nl.py --pennant  # Pennant timeline
python scripts/analyze_nl.py --records  # Notable records

# Output charts will be saved to visualizations/output/
```

## 📖 Data Files Summary

| File | Description | Rows |
|------|-------------|------|
| `data/nl_all_time_records.csv` | Franchise-level all-time W-L records | 15 teams |
| `data/nl_historical_performance.csv` | Season-by-season NL champions & highlights | ~150 rows (selected seasons) |
| `data/nl_pennant_winners_recent.csv` | NL pennant winners 1995–2025 | 31 rows |
| `data/nl_recent_standings.csv` | Division champions & WS outcomes 2020–2025 | 6 rows |
| `data/nl_championship_trends.csv` | Championship highlights organized by era | 8 rows |
| `data/nl_notable_records.csv` | Notable single-season and franchise records | 15 records |
| `data/nl_head_to_head.csv` | Team-vs-team matchup matrix | 15×15 matrix |
| `data/nl_era_comparison.csv` | Era-by-era comparison metrics | 8 eras |

## License

MIT
