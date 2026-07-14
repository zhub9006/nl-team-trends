# NL Team Trends

Comprehensive research project compiling historical **National League (NL)** team performance data, win-loss records, season trends, and championship history from 1876 to present.

The National League is baseball's oldest professional league, founded in 1876. This repository includes all-time franchise records, pennant winners, seasonal standings, and team-vs-team matrices for every NL franchise.

## 📊 Data Sources

| Source | Description | Coverage |
|--------|-------------|----------|
| **Baseball Almanac** | NL team-vs-team win-loss matrices | 1876–2026 |
| **Baseball Reference** | Year-by-year NL standings & leaders | 1876–present |
| **Baseball Data Hub** | Complete season standings & stats | 1871–present |
| **Lahman Baseball Database** | Full historical team, batting, & pitching stats | 1871–2025 |
| **SABR / Retrosheet** | Play-by-play records & research data | 1871–present |
| **OpenIntro (mlb_teams)** | Curated subset of Lahman data in R/data frame | 1871–2023 |

## 🗂️ Repository Structure

```
nl-team-trends/
├── README.md                  ← This file
├── data/
│   ├── nl_team_records.csv           ← All-time franchise win-loss records
│   ├── nl_pennant_winners.csv        ← NL pennant & World Series winners
│   ├── nl_team_vs_team.csv           ← Team-vs-team head-to-head matrices
│   ├── nl_key_seasons.csv            ← Key seasons with full NL standings
│   └── data_notes.md                 ← Notes on data collection & methodology
├── visualizations/
│   └── (plots, dashboards, etc.)
└── docs/
    └── research.md                   ← Detailed research notes
```

## 🏆 Key Historical Highlights

### All-Time Franchise Records

| Metric | Value | Team |
|--------|-------|------|
| Most all-time NL wins | 11,663 | San Francisco Giants |
| Highest NL win% | .535 | San Francisco Giants |
| Most MLB losses | 11,392 | Philadelphia Phillies |
| Lowest NL win% | .455 | Colorado Rockies |
| Oldest franchise (154+ seasons) | Atlanta Braves |
| Best single season (NL) | 116-37 (.763) | 1906 Chicago Cubs |
| Most division titles in a row | 14 straight | Atlanta Braves (1991–2005) |

### Notable NL Pennant Winners & Championship Highlights

| Year | Champion | Record | Notable |
|------|----------|--------|---------|
| 1876–1883 | Boston / Chicago | — | Early NL powerhouses |
| 1905–1908 | NY Giants / Cubs | — | Giants 3 pennants in 4 years |
| 1906 | Chicago Cubs | 116-37 | Best single-season NL record ever |
| 1914 | Boston Braves | — | "Miracle" late-season run |
| 1919 | Cincinnati Reds | — | First WS after Black Sox scandal |
| 1921–1924 | Giants / Cardinals | — | Giants 4 pennants in 5 years |
| 1955 | Brooklyn Dodgers | — | First Brooklyn WS title |
| 1969 | New York Mets | 100-62 | "Miracle Mets" |
| 1975–1976 | Cincinnati Reds | 108-54 (1975) | "Big Red Machine" |
| 1986 | New York Mets | 108-54 | Famous 1986 WS comeback |
| 1995 | Atlanta Braves | 90-54 | 14-division-title streak begins |
| 2001 | Arizona Diamondbacks | 92-70 | 2nd-year franchise to WS title |
| 2012–2014 | SF Giants | 94-68 (2012) | 3 WS titles in 5 years |
| 2016 | Chicago Cubs | 103-58 | Ended 108-year drought |
| 2020 | LA Dodgers | 43-17 (shortened) | 7th straight NL West |
| 2021 | Atlanta Braves | 88-73 | 1st WS since 1995 |
| 2025 | — | — | Most recent completed season |

## 🔬 Research Directions

- Franchise win-loss trajectory across eras
- Divisional realignment impact on competitive balance
- Playoff performance vs. regular season dominance
- Interleague play effects (post-1997)
- Franchise longevity, relocation & name changes
- Season-by-season visualizations & trend analysis
- Run differential as a predictor of pennant success
- Home/away splits through the decades

## 📈 Data File Overview

### `nl_key_seasons.csv`
Selected NL seasons with full standings data including:
- Team name, W, L, Win%, games behind, division/league winner flags
- Covers key eras: 1876 (founding), 1906 (best record), 1908, 1912, 1916, 1919, 1926, 1930, 1937, 1951, 1954, 1955, 1969, 1975, 1976, 1986, 1995, 2012, 2016, 2021, 2025

### `nl_pennant_winners.csv`
All NL pennant winners from 1876–present with:
- Year, champion team, record, league champion flag, WS winner

### `nl_team_records.csv`
All-time franchise aggregate records for all 15 active NL teams

### `nl_team_vs_team.csv`
Head-to-head win-loss matrices for all NL franchises

## 💻 Getting Started

```bash
# Clone the repository
git clone https://github.com/zhub9006/nl-team-trends.git

# Navigate to the data directory
cd nl-team-trends/data

# The CSV files are ready for analysis in Python (pandas), R, or Excel
```

## 🤝 Contributing

Contributions welcome! Fork and submit a pull request.

Areas for contribution:
- Additional season data files
- Visualization scripts (Python/Matplotlib, R/ggplot2, etc.)
- Statistical analyses and trend reports
- Data corrections or updates

## 📜 License

Open-source for research purposes.

## 🔗 Useful Links

- [Baseball Almanac — NL Team-vs-Team](https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml)
- [Baseball Reference — NL Index](https://www.baseball-reference.com/leagues/NL/index.shtml)
- [Baseball Data Hub — All Seasons](https://baseballdatahub.com/seasons/)
- [Lahman Baseball Database (SABR)](https://sabr.org/lahman-database/)
- [Retrosheet](https://www.retrosheet.org/)
- [OpenIntro mlb_teams Dataset](https://openintrostat.github.io/openintro/reference/mlb_teams.html)