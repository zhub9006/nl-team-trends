# NL Team Trends

Comprehensive research project compiling historical **National League (NL)** team performance data, win-loss records, season trends, and championship history from 1876 to present — built for statistical analysis, visualization, and historical inquiry.

## Overview

The National League is baseball's oldest professional league, founded on **February 2, 1876** as the first fully professional baseball organization to survive to the present day — replacing the National Association. This repository serves as a centralized research hub for all NL franchise records, head-to-head performance matrices, era-specific trends, and win-loss analysis.

### Key Research Sources Discovered

| Source | Description | Coverage | Key Finding |
|--------|-------------|----------|-------------|
| **[Baseball Almanac](https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml)** | NL team-vs-team W-L matrices | 1876–2026 | Every NL team vs every other team since founding |
| **[Baseball Reference](https://www.baseball-reference.com/leagues/NL/)** | Year-by-year NL standings & leaders | 1876–present | Official league statistics |
| **[Baseball Data Hub](https://baseballdatahub.com/seasons/)** | Complete season standings archive | 1871–2026 | 156 MLB seasons; 1876 NL founding snapshot available |
| **[SABR Lahman DB](https://sabr.org/lahman-database/)** | Full historical team, batting, pitching, fielding stats | 1871–2025 | Free downloadable CSV dataset (statsw/rest) |
| **[StatsCrew](https://www.statscrew.com/baseball/l-NL)** | NL rosters, standings & leaders | 1876–present | Comprehensive NL historical reference |
| **[Everything Explained](https://everything.explained.today)** | All-time franchise W-L records & postseason | 1876–2025 | Structured franchise data |
| **[StatMuse](https://www.statmuse.com/mlb/ask/most-national-league-titles)** | NL championship leaders & franchise stats | 1876–2026 | Cardinals 11 titles; Dodgers 9 pennants, 8 titles |
| **[Baseball Briefs](https://baseballbriefs.com/most-wins-in-national-league-history/)** | Franchise win totals analysis | 1876–2023 | Giants lead with 11,461 wins; Dodgers second at 11,334 |
| **[Her Sports Corner](https://hersportscorner.com/3374-2/)** | NL Central all-time records | 1876–2015 | Cubs 10,608-10,130; Cardinals 10,571-9,763 |
| **[OpenIntro MLB Dataset](https://www.openintro.org/data/index.php?data=mlb_teams)** | Machine-learning-ready MLB team data | Multi-year | R-accessible format for statistical modeling |

## 📁 Repository Structure

```
nl-team-trends/
├── README.md                              ← Research overview & key findings (this file)
├── data/
│   ├── nl_all_time_records.csv            ← All-time franchise win-loss totals by team
│   ├── nl_key_seasons.csv                 ← Key individual season standings (204 rows)
│   ├── nl_pennant_winners_recent.csv      ← NL pennant winners 1995–2025
│   ├── nl_recent_standings.csv            ← Full standings 2020–2025
│   ├── nl_championship_trends.csv         ← Championship highlights organized by era
│   ├── nl_notable_records.csv             ← Notable single-season and franchise records
│   ├── nl_historical_performance.csv      ← Multi-era season-by-season data (1876–2025)
│   └── source_references.md               ← Detailed source attribution
├── docs/
│   └── data_notes.md                      ← Methodology, conventions & caveats
├── visualizations/
│   └── README.md                          ← Visualization roadmap & tools
└── notebooks/                              ← (planned) analysis Jupyter notebooks
```

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

### Record Milestones

| Metric | Value | Team/Detail |
|--------|-------|-------------|
| Most all-time NL wins | 11,663 | San Francisco Giants |
| Highest NL win% (.535) | .535 | San Francisco Giants |
| Most all-time NL losses | 11,865 | Philadelphia Phillies |
| Best single-season NL record | 116–36 (.763) | 1906 Chicago Cubs |
| Best full 162G NL season | 111–51 (.685) | 2022 LA Dodgers |
| Best shortened-season record | 43–17 (.717) | 2020 LA Dodgers |
| Most consecutive division titles | 14 | Atlanta Braves (1991–2005) |
| Most NL pennants | 26 | LA Dodgers (2025) |
| Most WS titles | 11 | St. Louis Cardinals |

## 🏅 Notable Pennant Winners & Championship Highlights

| Year | Team | Record | Notable |
|------|------|--------|---------|
| 1876 | Chicago White Stockings | 52–14 | Inaugural NL champion |
| 1906 | Chicago Cubs | 116–36 | Best NL season ever (.763) |
| 1909 | Pittsburgh Pirates | 110–42 (.723) | 154G era NL benchmark |
| 1914 | Boston Braves | 94–59 | "Miracle" 26-game midseason turnaround |
| 1919 | Cincinnati Reds | 96–44 | First WS after Black Sox scandal |
| 1926 | St. Louis Cardinals | 89–65 | First of 11 Cardinals titles |
| 1951 | NY Giants | 98–59 | "Shot Heard 'Round the World" |
| 1955 | Brooklyn Dodgers | 98–55 | First Brooklyn WS title |
| 1969 | NY Mets | 100–62 | "Miracle Mets" |
| 1975–76 | Cincinnati Reds | 108–54 / 102–60 | Big Red Machine dynasty |
| 1986 | NY Mets | 108–54 | Famous October comeback |
| 1995 | Atlanta Braves | 90–54 | 14-division streak begins |
| 2001 | AZ Diamondbacks | 92–70 | 2nd-year team championship |
| 2012–14 | SF Giants | 94–68+ | 3 WS titles in 5 years |
| 2016 | Chicago Cubs | 103–58 | Ended 108-year drought |
| 2020 | LA Dodgers | 43–17 | Best shortened-season record |
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

## 📈 Notable NL Championships by Era

See `data/nl_championship_trends.csv` for detailed year-by-year championship results organized by era:

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

## 📊 Recent Season Standings (Full 15-Team NL)

← See `data/nl_recent_standings.csv` for complete standings matrix

| Year | East Champ | Central Champ | West Champ | WS Winner |
|------|-----------|---------------|------------|-----------|
| 2025 | Philadelphia (96-66) | Milwaukee (97-65) | LA Dodgers (93-69) | **LA Dodgers** |
| 2024 | Atlanta (89-73) | Milwaukee (93-69) | LA Dodgers (98-64) | **LA Dodgers** |
| 2023 | Atlanta (104-58) | Milwaukee (92-70) | LA Dodgers (100-62) | TX Rangers (AL) |
| 2022 | Atlanta (101-61) | St. Louis (93-69) | LA Dodgers (111-51) | HOU (AL) |
| 2021 | Atlanta (88-73) | Milwaukee (95-67) | LA Dodgers (106-56) | **Atlanta Braves** |
| 2020 | Atlanta (35-25) | Cincinnati (31-29) | LA Dodgers (43-17) | **LA Dodgers** |

## 🏛️ Notable Single-Season & Franchise Records

← See `data/nl_notable_records.csv` for comprehensive record collection

| Record | Team/Detail | Value |
|--------|-------------|-------|
| Best NL winning percentage | 1906 Chicago Cubs | .763 (116-37) |
| Best 162-game NL record | 2022 LA Dodgers | 111-51 (.685) |
| Best shortened NL record | 2020 LA Dodgers | 43-17 (.717) |
| Most NL pennants | LA Dodgers | 26 (through 2025) |
| Most WS titles (NL) | St. Louis Cardinals | 11 |
| Largest margin of victory (era) | 1876 Chicago | 38 wins (.721) |
| Highest HR season (both leagues) | 2019 MLB-wide | 6,776 total |
| Most consecutive division titles | Atlanta Braves | 14 (1991-2005) |
| Only franchise w/o NL pennant (active) | Milwaukee Brewers | Won AL pen 1982 |

## 📅 NL Historical Timeline

| Milestone | Year | Detail |
|-----------|------|--------|
| NL Founded | 1876 | 8 original franchises; Chicago White Stockings first champion |
| First 154-game season | 1892 | Schedule standardization begins |
| First World Series | 1903 | NL vs AL format established |
| 162-game schedule adopted | 1961 | Modern schedule era begins |
| Divisions created (E/W) | 1969 | 2-division format; LCS introduced |
| 3 divisions (+ Wild Card) | 1994 | Expanded playoff format (1994 strike delayed implementation) |
| Interleague play begins | 1997 | NL vs AL regular-season games |
| Full interleague schedule | 2023 | Every team plays every other team |
| Milwaukee Brewers move | 1998 | Switch from AL to NL Central |
| Nats relocation | 2005 | Montreal Expos → Washington Nationals |
| Diaz era begins | 2012 | Current competitive parity cycle |

## 📅 Notable NL Eras

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

## 🔍 Research Insights

### Franchise Dominance Patterns
- **San Francisco Giants** hold the all-time NL wins lead (11,663 through 2025), reflecting over 140 years of continuous play spanning NY Giants era
- **LA Dodgers** achieved the most NL pennants (26) and tied for 2nd-most WS titles (8) as of 2025
- **St. Louis Cardinals** lead all NL franchises with 11 World Series titles, uniquely sustained over 100+ years
- **Chicago Cubs** went from worst franchise win% (.491 pre-2015) to champion — the 2016 title ended a 108-year championship drought

### League Balance Shifts
- Pre-1969: 8→10→12 teams; dominant cycles lasted decades (Cubs 1906-09, Cardinals 1926-46)
- 1969–1993: 12 teams in 2 divisions; competitive balance improved but仍是 cyclical
- Post-1994: 15 teams in 3 divisions + Wild Card; more teams make playoff push but Dodgers dynasty emerges

### Scoring Environment Evolution
| Era | Avg Runs/Game | Key Factor |
|-----|---------------|------------|
| 1876–1900 | ~4.0 | Dead ball, no gloves, pitcher-friendly |
| 1901–1919 | ~4.5 | Live ball introduction, inside basepaths |
| 1920–1960 | ~4.5–4.8 | Lived ball era peak; 1930 season: 5.64 RPG |
| 1961–1968 | ~3.6 | "Year of the Pitcher"; Gibson 1.12 ERA (1968) |
| 1969–1992 | ~4.3 | Mound lowered; DH introduced (AL only) |
| 1993–2019 | ~4.6–4.8 | Juiced ball; launch angle revolution |
| 2020–2026 | ~4.7 | Record HR seasons; analytics-driven |

## 🔬 Research Directions

- [ ] Franchise win-loss trajectories across eras (10-year rolling averages)
- [ ] Divisional realignment impact on competitive balance (2→3 divisions)
- [ ] Pennant conversion → WS title rates by era
- [ ] Interleague play effects post-1997
- [ ] Run environment analysis across scoring eras (Dead Ball → Live Ball → Juiced Ball)
- [ ] Franchise longevity, relocation & name change analysis
- [ ] Wild card vs division champion postseason performance
- [ ] Home/away split trends through decades
- [ ] Head-to-head historical matrices between all 15 NL franchises  
- [ ] Elo ratings evolution across decades
- [ ] ERA-adjusted win percentage for cross-era comparison
- [ ] Pace of play (games per season, inning duration) trends

## 💻 Getting Started

```bash
git clone https://github.com/zhub9006/nl-team-trends.git
cd nl-team-trends

# Quick data exploration
python -c "import pandas as pd;
df = pd.read_csv('data/nl_all_time_records.csv');
print('Top 5 NL franchises by Win%:');
print(df.nlargest(5, 'Win_Pct')[['Franchise','Win_Pct','Wins','Losses','Pennants','WS_Titles']])
"

# View championship trends
python -c "import pandas as pd;
ct = pd.read_csv('data/nl_championship_trends.csv');
print(ct[['Year','Franquise','WS_Result','Notable_Event']].dropna(subset=['WS_Result']))
"
```

## 🤝 Contributing

Fork and submit a PR! Priority areas:

- [ ] Full 162-game season-by-season CSV for all 15 NL teams (1876–2025)
- [ ] Visualization scripts (Python/Matplotlib, R/ggplot2, D3.js)
- [ ] Statistical analyses & trend reports
- [ ] Data corrections for 2024–2025 seasons
- [ ] Jupyter notebooks for historical analysis
- [ ] Additional era-by-era breakdowns

## 📋 License

Open-source for research. Data sourced from publicly available MLB records.

## 🔗 Key External Links

- [Baseball Almanac — NL H2H](https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml)
- [Baseball Reference — NL](https://www.baseball-reference.com/leagues/NL/)
- [Baseball Data Hub — All Seasons](https://baseballdatahub.com/seasons/)
- [SABR Lahman Database](https://sabr.org/lahman-database/)
- [StatsCrew — NL Teams](https://www.statscrew.com/baseball/l-NL)
- [Lahman CSV on GitHub](https://github.com/chadwickbureau/mlb)