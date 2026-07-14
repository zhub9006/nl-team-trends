# NL Team Trends

Comprehensive research project compiling historical **National League (NL)** team performance data, win-loss records, season trends, and championship history from 1876 to present. For analyzing team dominance, franchise trajectories, and the evolving NL competitive landscape.

## Overview

The National League is baseball's oldest professional league, founded on **February 2, 1876** as the first fully professional baseball organization to survive to the present day. This repository serves as a centralized research hub for all NL franchise records, head-to-head performance matrices, era-specific trends, and win-loss analysis — providing a foundation for statistical analysis, visualization, and historical inquiry.

## 📊 Data Sources

| Source | Description | Coverage |
|--------|-------------|----------|
| **[Baseball Almanac](https://www.baseball-almanac.com)** | NL team-vs-team win-loss matrices | 1876–2026 |
| **[Baseball Reference](https://www.baseball-reference.com/leagues/NL/)** | Year-by-year NL standings & leaders | 1876–present |
| **[Baseball Data Hub](https://baseballdatahub.com/seasons/)** | Complete season standings archive | 1871–2026 |
| **[SABR Lahman DB](https://sabr.org/lahman-database/)** | Full historical team & batting/pitching stats | 1871–2025 |
| **[StatsCrew](https://www.statscrew.com/baseball/l-NL)** | NL rosters, standings & statistical leaders | 1876–present |
| **[Grokipedia](https://grokipedia.com)** | All-time franchise W-L records & pennant history | 1876–2025 |

## 📁 Repository Structure

```
nl-team-trends/
├── README.md                              ← Research overview & key findings
├── data/
│   ├── nl_all_time_records.csv            ← All-time franchise win-loss totals
│   ├── nl_pennant_winners_recent.csv       ← NL pennant winners 1995–2025
│   ├── nl_recent_standings.csv             ← Full standings 2020–2025
│   ├── nl_key_seasons.csv                  ← Key season standings (existing, 204 rows)
│   └── data_notes.md                       ← Data notes (legacy, moved to docs/)
├── docs/
│   └── data_notes.md                       ← Methodology, conventions & caveats (updated)
├── visualizations/
│   └── README.md                           ← Visualization roadmap & tools
└── notebooks/                              ← (planned) analysis Jupyter notebooks
```

## 🏆 All-Time NL Franchise Records (through end of 2025 season)

| Franchise | First MLB Year | Division | Wins | Losses | Win% | Pennants | WS Titles |
|-----------|----------------|----------|------|--------|------|----------|-----------|
| San Francisco Giants | 1883 | NL West | 11,622 | 10,100 | **.535** | 23 | 8 |
| Los Angeles Dodgers | 1883 | NL West | 11,525 | 10,137 | .531 | 26 | 8 |
| St. Louis Cardinals | 1882 | NL Central | 11,363 | 10,486 | .520 | 19 | 11 |
| Chicago Cubs | 1876 | NL Central | 11,419 | 10,837 | .516 | 17 | 3 |
| Cincinnati Reds | 1882 | NL Central | 11,017 | 10,845 | .505 | 10 | 5 |
| Atlanta Braves (oldest) | 1871 | NL East | 11,190 | 11,035 | .504 | 18 | 4 |
| Pittsburgh Pirates | 1882 | NL Central | 10,910 | 10,910 | .500 | 9 | 5 |
| Philadelphia Phillies | 1883 | NL East | 10,303 | 11,392 | .475 | 8 | 2 |
| New York Mets | 1962 | NL East | 4,899 | 5,227 | .485 | 2 | 2 |
| Modern Expansion (all 6) | — | — | — | — | .465 avg | 6 total | 6 total |

### Record Milestones

| Metric | Value | Team |
|--------|-------|------|
| Most all-time NL wins | 11,622 | San Francisco Giants |
| Highest NL win% (.535) | .535 | San Francisco Giants |
| Most all-time NL losses | 11,392 | Philadelphia Phillies |
| Lowest NL win% | .456 | Colorado Rockies |
| Most games played | 22,417 | Chicago Cubs |
| Best single-season NL record | 116-37 (.763) | 1906 Chicago Cubs |
| Best full 162G NL season | 111-51 (.685) | 2022 LA Dodgers |
| Best shortened-season record | 43-17 (.717) | 2020 LA Dodgers |
| Most consecutive Division titles | 14 (1991–2005) | Atlanta Braves |
| Only franchise w/o NL pennant | Milwaukee Brewers* | — |

*\*Brewers won an AL pennant (1982) before moving leagues in 1998*

## 🏅 Notable Pennant Winners & Championship Highlights

| Year | Team | Record | Notable |
|------|------|--------|---------|
| 1876 | Chicago White Stockings | 52–14 | Inaugural NL champion |
| 1906 | Chicago Cubs | 116-37 | Best NL record ever (.763) |
| 1909 | Pittsburgh Pirates | 110-42 (.723) | 154G era NL benchmark |
| 1914 | Boston Braves | 94-59 | "Miracle" turnaround |
| 1919 | Cincinnati Reds | 96-44 | First WS after Black Sox |
| 1926 | St. Louis Cardinals | 89-65 | First of 11 titles |
| 1951 | NY Giants | 98-59 | "Shot Heard 'Round the World" |
| 1955 | Brooklyn Dodgers | 98-55 | First Brooklyn WS title |
| 1969 | NY Mets | 100-62 | "Miracle Mets" |
| 1975-76 | Cincinnati Reds | 108-54 / 102-60 | Big Red Machine dynasty |
| 1986 | NY Mets | 108-54 | Famous October comeback |
| 1995 | Atlanta Braves | 90-54 | 14-division streak begins |
| 2001 | AZ Diamondbacks | 92-70 | 2nd-year team championship |
| 2012-2014 | SF Giants | 94-68+ | 3 WS titles in 5 years |
| 2016 | Chicago Cubs | 103-58 | Ended 108-year drought |
| 2020 | LA Dodgers | 43-17 | 7th straight NL West |
| 2021 | Atlanta Braves | 88-73 | 1st WS since 1995 |
| 2025 | LA Dodgers | 93-69 | Back-to-back WS champions |

### Most NL Pennants (among active franchises)

| Pennants | Team | Last Pennant | WS Titles |
|----------|------|-------------|-----------|
| 26 | LA Dodgers | 2025 | 8 |
| 23 | SF Giants | 2014 | 8 |
| 19 | St. Louis Cardinals | 2024 | 11 |
| 18 | Atlanta Braves | 2021 | 4 |
| 17 | Chicago Cubs | 2016 | 3 |
| 10 | Cincinnati Reds | 1995 | 5 |
| 9 | Pittsburgh Pirates | 1979 | 5 |
| 8 | Philadelphia Phillies | 2025 | 2 |

## 📈 Recent Season Standings (Full 15-Team NL)

← See `data/nl_recent_standings.csv` for complete standings matrix

| Year | East Champ | Central Champ | West Champ | WS Winner |
|------|-----------|---------------|------------|-----------|
| 2025 | Philadelphia (96-66) | Milwaukee (97-65) | LA Dodgers (93-69) | **LA Dodgers** |
| 2024 | Atlanta (89-73) | Milwaukee (93-69) | LA Dodgers (98-64) | **LA Dodgers** |
| 2023 | Atlanta (104-58) | Milwaukee (92-70) | LA Dodgers (100-62) | TX Rangers (AL) |
| 2022 | Atlanta (101-61) | St. Louis (93-69) | LA Dodgers (111-51) | HOU (AL) |

## 📊 Notable NL Eras

| Era | Theme | Key Insight |
|-----|-------|-------------|
| 1876–1892 | Founding Era | Chicago dominance; franchise churn & contraction |
| 1900–1919 | Dead Ball Era | Cubs/Pirates/NYG cyclical; best single-season records |
| 1920–1950 | Power Transition | Cardinals/Giants; 4 NL championships for B&O |
| 1950–1980 | Relocation Period | Dodgers & Giants move West; Braves migrate |
| 1991–2005 | Braves Dynasty | Historic 14 consecutive division titles |
| 2006–2016 | Resurgence Cycle | Cardinals, Phils, Giants, Cubs all win titles |
| 2017–present | Dodgers Dynasty | 8 straight NL West; 5 pennants since 2017 |

## 🔬 Research Directions

- Franchise win-loss trajectories across eras
- Divisional realignment impact on balance (2→3 divisions)
- Pennant conversion → WS title rates by era
- Interleague play effects post-1997
- Run environment analysis across scoring eras
- Franchise longevity, relocation & name change analysis
- Wild card vs division champion postseason performance
- Home/away split trends through decades

## 💻 Getting Started

```bash
git clone https://github.com/zhub9006/nl-team-trends.git
cd nl-team-trends/data
python -c "import pandas as pd; df = pd.read_csv('nl_all_time_records.csv'); print(df.nlargest(5, 'Win_Pct'))"
```

## 🤝 Contributing

Fork and submit a PR! Priority areas:

- Additional season-by-season CSV files (full NL history)
- Visualization scripts (Python/Matplotlib, R/ggplot2, D3.js)
- Statistical analyses & trend reports
- Data corrections for 2024–2025 seasons

## 📄 License

Open-source for research. Data sourced from publicly available MLB records.

## 🔗 Key External Links

- [Baseball Almanac — NL H2H](https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml)
- [Baseball Reference — NL](https://www.baseball-reference.com/leagues/NL/)
- [Baseball Data Hub — All Seasons](https://baseballdatahub.com/seasons/)
- [SABR Lahman Database](https://sabr.org/lahman-database/)
- [StatsCrew — NL Teams](https://www.statscrew.com/baseball/l-NL)
- [Lahman CSV on GitHub](https://github.com/chadwickbureau/mlb)
