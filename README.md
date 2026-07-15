# NL Team Trends

Comprehensive research project compiling historical **National League (NL)** team performance data, win-loss records, season trends, and championship history from 1876 to present — built for statistical analysis, visualization, and historical inquiry.

## Overview

The National League is baseball's oldest professional league, founded on **February 2, 1876** as the first fully professional baseball organization to survive to the present day. This repository serves as a centralized research hub for all NL franchise records, head-to-head performance matrices, era-specific trends, and win-loss analysis.

## 📊 Data Sources

| Source | Description | Coverage | URL |
|--------|-------------|----------|-----|
| **Baseball Almanac** | NL team-vs-team win-loss matrices | 1876–2026 | [baseball-almanac.com/teams/teamvsteam-nl](https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml) |
| **Baseball Reference** | Year-by-year NL standings & leaders | 1876–present | [baseball-reference.com/leagues/NL](https://www.baseball-reference.com/leagues/NL/) |
| **Baseball Data Hub** | Complete season standings & leaders | 1871–2026 | [baseballdatahub.com/seasons](https://baseballdatahub.com/seasons/) |
| **SABR Lahman DB** | Full historical team, batting, pitching stats | 1871–2025 | [sabr.org/lahman-database](https://sabr.org/lahman-database/) |
| **StatsCrew** | NL rosters, standings & statistical leaders | 1876–present | [statscrew.com/baseball/l-NL](https://www.statscrew.com/baseball/l-NL) |
| **Everything Explained** | All-time franchise W-L records & postseason | 1876–2025 | [everything.explained.today](https://everything.explained.today/List_of_all-time_Major_League_Baseball_win%E2%80%93loss_records/) |

## 📁 Repository Structure

```
nl-team-trends/
├── README.md                              ← Research overview & key findings (this file)
├── data/
│   ├── nl_all_time_records.csv            ← All-time franchise win-loss totals by team
│   ├── nl_key_seasons.csv                 ← Key individual season standings (204 rows)
│   ├── nl_pennant_winners_recent.csv      ← NL pennant winners 1995–2025
│   ├── nl_recent_standings.csv            ← Full standings 2020–2025
│   ├── nl_historical_performance.csv      ← Multi-era season-by-season data (1876–2025)
│   └── source_references.md               ← Detailed source attribution
├── docs/
│   └── data_notes.md                      ← Methodology, conventions & caveats
├── visualizations/
│   └── README.md                          ← Visualization roadmap & tools
└── notebooks/                              ← (planned) analysis Jupyter notebooks
```

## 🏆 All-Time NL Franchise Records (through 2025 season)

| Franchise | First Season | Division | G | W | L | Win% | Pennants | WS Titles |
|-----------|-------------|----------|---|---|---|------|----------|-----------|
| San Francisco Giants | 1883 | West | 21,885 | 11,663 | 10,059 | .535 | 23 | 8 |
| Los Angeles Dodgers | 1884 | West | 21,801 | 11,586 | 10,136 | .531 | 26 | 8 |
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

### Record Milestones

| Metric | Value | Team/Detail |
|--------|-------|-------------|
| Most all-time NL wins | 11,663 | San Francisco Giants |
| Highest NL win% | .535 | San Francisco Giants |
| Most all-time NL losses | 11,865 | Philadelphia Phillies |
| Best single-season NL record | 116–36 (.763) | 1906 Chicago Cubs |
| Best full 162G NL season | 111–51 (.685) | 2022 LA Dodgers |
| Best shortened-season record | 43–17 (.717) | 2020 LA Dodgers |
| Most consecutive division titles | 14 | Atlanta Braves (1991–2005) |
| Most NL pennants | 26 | LA Dodgers |
| Most WS titles | 11 | St. Louis Cardinals |

## 🏅 Notable Pennant Winners & Championship Highlights

| Year | Team | Record | Notable |
|------|------|--------|---------|
| 1876 | Chicago White Stockings | 52–14 | Inaugural NL champion |
| 1892 | Boston Beaneaters | 102–48 | Best ERA-era record (.680) |
| 1906 | Chicago Cubs | 116–36 | Best NL season ever (.763) |
| 1914 | Boston Braves | 94–59 | "Miracle" 26-game midseason turnaround |
| 1919 | Cincinnati Reds | 96–44 | First WS after Black Sox scandal |
| 1926 | St. Louis Cardinals | 89–65 | First of 11 Cardinals titles |
| 1930 | St. Louis Cardinals | 92–62 | Champions in the 1930 NL |
| 1940 | Cincinnati Reds | 100–53 | Dominant 65.4% win rate |
| 1951 | New York Giants | 98–59 | "Shot Heard 'Round the World" |
| 1955 | Brooklyn Dodgers | 98–55 | First Brooklyn WS title |
| 1960 | Pittsburgh Pirates | 95–59 | Bill Mazeroski walk-off WS |
| 1969 | New York Mets | 100–62 | "Miracle Mets" |
| 1970 | Cincinnati Reds | 102–60 | NL West champions |
| 1975–76 | Cincinnati Reds | 108–54 / 102–60 | Big Red Machine dynasty |
| 1980 | Philadelphia Phillies | 91–71 | Won NL East & WS |
| 1990 | Pittsburgh Pirates | 95–67 | Last pre-division-rap champion |
| 1995 | Atlanta Braves | 90–54 | 14-division streak begins |
| 2000 | Atlanta Braves | 95–67 | League-leading 58.6% |
| 2004 | St. Louis Cardinals | 105–57 | Highest win% in Cardinals history |
| 2012–14 | SF Giants | 94–68+ | 3 WS titles in 5 years |
| 2016 | Chicago Cubs | 103–58 | Ended 108-year drought |
| 2020 | LA Dodgers | 43–17 | 7th straight NL West |
| 2022 | LA Dodgers | 111–51 | Best 162-game season in NL history |
| 2025 | LA Dodgers | 93–69 | Back-to-back WS champions |

### Most NL Pennants (Active Franchises)

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

## 📈 Notable NL Eras

| Era | Theme | Key Insight |
|-----|-------|-------------|
| 1876–1892 | Founding Era | 8 teams; Chicago dominance; franchise churn & contraction; no divisions |
| 1893–1919 | Dead Ball Transition | Best single-season records (116W by Cubs 1906); cyclical team strengths |
| 1920–1950 | Power & Resilience | Cardinals/Giants rise; Braves' "Miracle" 1914; pennant races with 154-game schedule |
| 1950–1980 | Relocation & Expansion | Dodgers & Giants move West; Braves migrate to Milwaukee then Atlanta; 1969 division split |
| 1981–1993 | Pre-Division Rap | 12-team NL without divisions; Pirates' back-to-back; Cubs' 1984 NL East "first" |
| 1994–2005 | Braves Dynasty | Historic 14 consecutive division titles; Cardinals resurgence |
| 2006–2016 | Resurgence Cycle | Cardinals, Phils, Giants, Cubs all win pennants; 2016 Cubs end drought |
| 2017–present | Dodgers Dynasty | 8 straight NL West division titles; 5 pennants since 2017; 3 WS appearances |

## 🔍 Research Directions

- Franchise win-loss trajectories across eras
- Divisional realignment impact on competitive balance (2→3 divisions)
- Pennant conversion → WS title rates by era
- Interleague play effects post-1997
- Run environment analysis across scoring eras (Dead Ball → Live Ball → Juiced Ball)
- Franchise longevity, relocation & name change analysis
- Wild card vs division champion postseason performance
- Home/away split trends through decades
- Head-to-head historical matrices between all 15 NL franchises
- Elo ratings evolution across decades

## 💻 Getting Started

```bash
git clone https://github.com/zhub9006/nl-team-trends.git
cd nl-team-trends/data
python -c "import pandas as pd; df = pd.read_csv('nl_all_time_records.csv'); print(df.nlargest(5, 'Win_Pct'))"
```

## 🤝 Contributing

Fork and submit a PR! Priority areas:

- Additional season-by-season CSV files (full NL history 1876–2025)
- Visualization scripts (Python/Matplotlib, R/ggplot2, D3.js)
- Statistical analyses & trend reports
- Data corrections for 2024–2025 seasons
- Jupyter notebooks for historical analysis

## 📄 License

Open-source for research. Data sourced from publicly available MLB records.

## 🔗 Key External Links

- [Baseball Almanac — NL H2H](https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml)
- [Baseball Reference — NL](https://www.baseball-reference.com/leagues/NL/)
- [Baseball Data Hub — All Seasons](https://baseballdatahub.com/seasons/)
- [SABR Lahman Database](https://sabr.org/lahman-database/)
- [StatsCrew — NL Teams](https://www.statscrew.com/baseball/l-NL)
- [Lahman CSV on GitHub](https://github.com/chadwickbureau/mlb)