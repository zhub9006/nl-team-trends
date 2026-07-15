# NL Team Trends 🏟️

Comprehensive research project compiling historical **National League (NL)** team performance data, win-loss records, season trends, and championship history from 1876 to present — built for statistical analysis, visualization, and historical inquiry.

## Overview

The National League is baseball's oldest professional league, founded on **February 2, 1876** as the first fully professional baseball organization to survive to the present day — replacing the National Association. This repository serves as a centralized research hub for all NL franchise records, head-to-head performance matrices, era-specific trends, and win-loss analysis.

## 📂 Repository Structure

```
nl-team-trends/
├── README.md                              ← Research overview & key findings
├── requirements.txt                       ← Python dependencies
├── source_references.md                    ← Detailed source attribution
├── visualization_roadmap.md               ← Visualization roadmap
├── scripts/
│   └── nl_analysis.py                     ← Starter analysis script
├── data/
│   ├── nl_all_time_records.csv            ← All-time franchise by team
│   ├── nl_historical_performance.csv      ← Championship highlights with era labels (1876-2025)
│   ├── nl_historical_performance_detailed.csv  ← Year-by-year champion + 2nd + WS results
│   ├── nl_pennant_winners_recent.csv      ← NL pennant winners and WS (1995-2025)
│   ├── nl_championship_trends.csv         ← Championship trends by era
│   ├── nl_notable_records.csv             ← Notable single-season & franchise records
│   ├── nl_division_realignments.csv       ← NL divisional structure timeline
│   ├── nl_top_seasons_by_win_pct.csv      ← Top NL seasons by win%
│   ├── nl_team_era_dominance.csv          ← Team dominance periods by era
│   └── nl_season_records_all_teams.csv    ← Year-by-year for all teams (1876-2025)
├── docs/
│   └── data_notes.md                      ← Methodology convention & caveats
└── visualizations/
    └── README.md                          ← Visualization roadmap
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

## 📈 Notable Records

| Record | Team/Detail | Value | Year |
|--------|-------------|-------|------|
| Best NL winning % | 1906 Chicago Cubs | .763 (116-36) | 1906 |
| Best 162-game NL record | 2022 LA Dodgers | 111-51 (.685) | 2022 |
| Best shortened NL record | 2020 LA Dodgers | 43-17 (.717) | 2020 |
| Most NL pennants | LA Dodgers | 26 | Through 2025 |
| Most WS titles (NL) | St. Louis Cardinals | 11 | Through 2025 |
| Most consecutive division titles | Atlanta Braves | 14 (1991-2005) | 1991-2005 |
| Most all-time NL wins | SF Giants | 11,663 | Through 2025 |
| Most all-time NL losses | Philadelphia Phillies | 11,865 | Through 2025 |
| Longest WS drought | Chicago Cubs | 108 years | 1908-2016 |
| First NL CWS championship | St. Louis Cardinals | 1926 | 1926 |

## ⏳ NL Historical Timeline

| Milestone | Year | Detail |
|-----------|------|--------|
| NL Founded | 1876 | 8 original franchises; Chicago first champion |
| First 154-game season | 1892 | Schedule standardization begins |
| First World Series | 1903 | NL vs AL format established |
| 162-game schedule adopted | 1961 | Modern schedule era begins |
| Divisions created (E/W) | 1969 | 2-division format; LCS introduced |
| 3 divisions (+ Wild Card) | 1994 | Expanded playoff format |
| Interleague play begins | 1997 | NL vs AL regular-season games |
| Full interleague schedule | 2023 | Every team plays every other team |
| Milwaukee Brewers move | 1998 | Switch from AL to NL Central |
| Nats relocation | 2005 | Montreal Expos → Washington Nationals |

## 🔍 Key Historical Highlights

- **1906 Chicago Cubs**: 116-36 (.763 Win%), best season record in MLB history — still unbroken in an MLB regular season
- **1918 Season**: Reduced to 140 games due to WWI
- **1968 — "Year of the Pitcher"**: Bob Gibson's 1.12 ERA; league-wide batting averages dropped so dramatically that MLB lowered the pitcher's mound the following year
- **1994 Strike Season**: No World Series was played; the only year the WS was not played since 1904
- **2017 & 2019 Home Run Eras**: 6,776 HRs combined in 2019; record-setting offensive output
- **2020 COVID Season**: 60-game format; Dodgers won with .717 win percentage
- **Dodgers Dynasty (2017-2025)**: 8 straight NL West titles; 5 WS championships in 9 seasons
- **Braves Megadynasty (1991-2005)**: 14 consecutive division titles — longest such streak in any major American pro sport
- **Cubs' 108-Year Drought (1908-2016)**: Longest championship drought in North American pro sports history

## 📉 Era-by-Era Win% Comparison

| Era | Typical Top Team Win% | Context |
|-----|----------------------|---------|
| 1876-1891 | .700-.789 | Small schedules; tied games; no mound rule |
| 1892-1919 | .650-.763 | Low-scoring; pitchers dominated |
| 1920-1945 | .600-.680 | Mound lowered in 1920; home run surge begins |
| 1946-1960 | .580-.660 | Post-war; integrated; expansion discussed |
| 1961-1990 | .560-.670 | 162-game schedule; division play begins |
| 1991-2025 | .500-.717 | Modern era; expanded playoffs |

**Key observation**: Top-team win% has generally declined over time, reflecting the longer schedule (154→162 games) and increased competitive balance through expanded playoffs (2→5+ teams).

## 🛠 Quick Analysis Guide

### Python Starter
```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/nl_season_records_all_teams.csv', comment='#')
modern = df[df['Games'] >= 160]
top_teams = modern.groupby('Team')['WinPct'].mean().sort_values(ascending=False)
top_teams.head(10).plot(kind='barh', figsize=(10,6))
plt.title('NL Franchise Avg Win% — Modern Era')
plt.savefig('visualizations/modern_win_pct.png', dpi=150)
plt.show()
```

### R Starter
```r
library(ggplot2)
df <- read.csv('data/nl_season_records_all_teams.csv', comment.char = "#")
modern <- df %>% filter(Games >= 160)
modern %>% group_by(Team) %>% summarise(avg = mean(WinPct)) %>% arrange(desc(avg)) %>% head(10) %>%
  ggplot(aes(x = reorder(Team, avg), y = avg)) + geom_bar(stat = 'identity') + coord_flip()
```

## 📦 Data Files Reference

| File | Description |
|------|-------------|
| `data/nl_all_time_records.csv` | All-time franchise win-loss totals by team |
| `data/nl_historical_performance.csv` | Championship-season highlights with era labels |
| `data/nl_historical_performance_detailed.csv` | Year-by-year NL champion + 2nd place + WS results |
| `data/nl_pennant_winners_recent.csv` | NL pennant winners and WS results 1995-2025 |
| `data/nl_championship_trends.csv` | Championship trends organized by era |
| `data/nl_notable_records.csv` | Key single-season and franchise records |
| `data/nl_division_realignments.csv` | NL divisional structure changes timeline |
| `data/nl_top_seasons_by_win_pct.csv` | Top NL seasons ranked by winning percentage |
| `data/nl_team_era_dominance.csv` | Team dominance periods by era |
| `data/nl_season_records_all_teams.csv` | Year-by-year NL records for all teams |

## 📋 Visualization Roadmap

- [x] Win-loss trend lines per franchise (1876–2025)
- [x] Pennant/win-heatmap by era
- [x] Head-to-head matchup matrix heatmap
- [x] Championship drought duration chart
- [x] Win% distribution by decade
- [x] Interactive dashboard (Plotly / Streamlit)
- [ ] NL East vs West vs Central competitive balance over time
- [ ] Pennant-to-WS conversion rate by era

## 🌐 Key Research Sources

| Source | Description | Coverage |
|--------|-------------|----------|
| [Baseball-Reference (NL)](https://www.baseball-reference.com/leagues/NL/) | Year-by-year NL standings & team stats | 1876–present |
| [SABR Lahman Database](https://sabr.org/lahman-database/) | Full historical team/batting/pitching stats | 1871–2025 |
| [Baseball Almanac](https://www.baseball-almanac.com/yearmenu.shtml) | NL year-by-year history; team-vs-team matrices | 1876–2026 |
| [Baseball Data Hub](https://baseballdatahub.com/seasons/) | Complete season standings archive | 1871–2026 |
| [StatsCrew (NL)](https://www.statscrew.com/baseball/l-NL) | NL rosters, standings & leaders | 1876–present |
| [StatMuse](https://www.statmuse.com/mlb/ask/most-national-league-titles) | NL championship leaders & franchise stats | 1876–2026 |
| [OpenIntro MLB Dataset](https://www.openintro.org/data/index.php?data=mlb_teams) | ML-ready MLB team data | Multi-year |

## ⚠️ Data Caveats

1. **Win%** = Wins / Games Played (excluding ties in early eras)
2. **Pennants** = League championship awards (pre-Wild Card era)
3. **WS Titles** = World Series championships won as an NL team
4. **Pre-1903**: No World Series existed.
5. **Pre-1961**: 154-game schedule; 1961+: 162-game schedule.
6. **Shortened seasons** (1918, 1981, 2020) are noted as special cases.
7. **Tied games** in early NL (pre-1920s) were replayed.
8. **Brewers** moved from AL to NL Central in 1998.
9. **Nationals** = relocated Expos in 2005.

## 🚀 Getting Started

1. Clone: `git clone https://github.com/zhub9006/nl-team-trends.git`
2. Install deps: `pip install -r requirements.txt`
3. Explore `data/` for historical records
4. Use `scripts/nl_analysis.py` as your starting script
5. Build visualizations in `visualizations/`
6. Contribute new data, notebooks, or analysis!

## 📄 License

MIT

## 🔗 Links

- GitHub: https://github.com/zhub9006/nl-team-trends
- Clone: `git clone https://github.com/zhub9006/nl-team-trends.git`