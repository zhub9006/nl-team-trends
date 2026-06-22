# NL Team Trends

Historical National League (NL) team performance data, trend analysis, and visualizations across past seasons.

## Overview

This repository compiles all-time win-loss records, franchise histories, season-by-season performance data, and performance trends for all 15 current National League teams. Data spans from the founding of the National League in **1876** through the end of the **2025** regular season.

The National League is the older of MLB's two leagues, established in 1876 — 25 years before the American League (1901). Interleague play between the NL and AL began in 1997.

## Key Findings

| Insight | Detail |
|---------|--------|
| **Highest NL all-time Win%** | San Francisco Giants (.535) |
| **Most NL wins** | San Francisco Giants (11,651) |
| **Most NL losses** | Philadelphia Phillies (11,425) |
| **Oldest franchise** | Atlanta Braves (continuous since 1871) |
| **Lowest all-time Win%** | Colorado Rockies (.455) |
| **Best single-season NL record** | 1906 Cubs (116-36, .763) |
| **Only .500 franchise** | Pittsburgh Pirates (10,947-10,947) |
| **Most WS titles (NL)** | St. Louis Cardinals (11) |
| **NL team with most pennants** | San Francisco Giants (23) |

## NL Dominance Eras — Key Historical Trends

The National League has seen distinct eras of franchise dominance over its 150-year history:

### Founding Era Dominance (1876–1900)
- The **Boston/Worcester** dynasty dominated the late 1870s, winning multiple consecutive pennants
- **Chicago White Stockings** (now Cubs) won 6 pennants in 7 years (1876–1882, 1885–1886)
- **Providence Grays** and **Boston Beaneaters** were also dominant forces
- The original NL franchises — Braves, Cubs, Reds, Giants, Phillies, Pirates — established the league's foundation

### Early 1900s Rivalries (1901–1920)
- The **Pittsburgh Pirates** and **Chicago Cubs** were fierce early-1900s rivals
- The **New York Giants** entered their long reign under John McGraw (1904–1905, 1911–1913, 1917–1924 pennants)
- The **1914 Boston Braves** — "Miracle Braves" — went from last place on July 4 to winning the World Series
- The **1919 Cincinnati Reds** won the World Series amid the Black Sox scandal

### Giants Dynasty & Golden Age (1920–1960)
- The **NY Giants** dominated the 1920s–1930s under McGraw and Bill Terry (1921–1922, 1933 WS titles)
- **St. Louis Cardinals** emerged as the NL's powerhouse with three WS titles in the 1926–1934 window
- The **Brooklyn Dodgers** and **NY Giants** began their legendary rivalry
- The **1955 Brooklyn Dodgers** won the franchise's first World Series
- The **1957 Milwaukee Braves** ended the Yankees' dynastic streak

### Dodgers–Giants–Cardinals Axis (1960–1990)
- The **Los Angeles Dodgers** won 5 WS titles in the 1955–1988 era
- The **Cardinals** remained NL dominant with 4 WS titles (1964, 1967, 1982)
- The **Pittsburgh Pirates** won 3 WS titles (1960, 1971, 1979)
- The **"Big Red Machine" Cincinnati Reds** won back-to-back WS titles (1975–1976)
- The **1969 Miracle Mets** — the first expansion team to win a World Series

### Modern Dominance (1990–Present)
- The **Atlanta Braves** won 14 consecutive division titles (1991–2005) and the 1995 WS title
- The **St. Louis Cardinals** entered their greatest modern era with 3 WS titles (2006, 2011)
- The **San Francisco Giants** won 3 WS titles in 5 years (2010, 2012, 2014)
- The **Chicago Cubs** ended a 108-year championship drought in 2016
- The **Washington Nationals** won their first WS title in 2019
- The **Los Angeles Dodgers** have dominated the 2020s with 3 WS titles (2020, 2024)

## Expansion & Realignment Impact

### Expansion Waves
| Year | Teams Added | Impact |
|------|-------------|--------|
| **1962** | New York Mets | Filled NL East; first expansion in 20 years |
| **1969** | Montreal Expos, San Diego Padres | NL expanded to 12 teams; first divisional play (East/West) |
| **1993** | Colorado Rockies, Florida Marlins | NL expanded to 14 teams; both teams reached WS within 5 years |
| **1998** | Arizona Diamondbacks | NL expanded to 15 teams; moved to 3-division format |

### Divisional Realignment
- **1969**: Split from 2 divisions (East/West) to enable first-ever divisional play and NLCS
- **1994**: Split from 2 to 3 divisions (East/Central/West) + Wild Card round introduced
- **1998**: Milwaukee Brewers moved from AL to NL Central; Arizona Diamondbacks added to NL West
- **2022**: Competitive Balance Wild Card game introduced for small-market NL teams

## Data Sources

The data compiled here is drawn from the following authoritative sources:

| Source | Description | URL |
|--------|-------------|-----|
| [Baseball-Reference.com – NL Standings](https://www.baseball-reference.com/leagues/NL/) | Season-by-season standings, team statistics, and franchise histories | baseball-reference.com |
| [Retrosheet.org](https://www.retrosheet.org/) | Play-by-play data and historical box scores | retrosheet.org |
| [MLB.com – National League](https://www.mlb.com/national-league) | Official MLB National League records and archives | mlb.com |
| [Hall of Fame – NL Exhibits](https://baseballhall.org/) | Historical context on franchise milestones | baseballhall.org |
| [SABR – National League Chapter](https://sabr.org/) | Research from the Society for American Baseball Research | sabr.org |
| [Lahman Baseball Database (SABR)](https://sabr.org/lahman-database/) | Complete major league stats from 1871 | github.com/chadwickbureau/baseballdatabank |
| [Baseball Almanac](https://www.baseball-almanac.com/) | Historical records and franchise timelines | baseball-almanac.com |

## Repository Structure

```
nl-team-trends/
├── README.md                     # This file
├── data/
│   ├── nl_all_time_records.csv       # All-time franchise records (CSV) ✓ Complete
│   ├── nl_team_vs_team.csv           # NL head-to-head win-loss matrix (CSV) ✓ Complete
│   ├── nl_era_summary.csv            # Era-based performance summaries (CSV) ✓ Complete
│   └── nl_season_by_season.csv       # Season-by-season historical performance (CSV) ✓ Complete
├── notebooks/                      # Analysis & visualization notebooks
├── visualizations/                 # Generated charts and plots
└── sources/                        # Reference links and methodology notes
```

## Data Highlights

### All-Time Records (Through 2025)

The `data/nl_all_time_records.csv` file contains the complete all-time regular-season records for all 15 current NL franchises, including:
- Total wins, losses, and winning percentage
- Games played (including ties from the pre-1920 era)
- First year in the NL
- Prior franchise names and city relocations
- Division alignment (East, Central, West)

### Team-vs-Team Head-to-Head

The `data/nl_team_vs_team.csv` file contains the complete NL head-to-head win-loss matrix covering every matchup between all 15 NL franchises from 1876 through 2025. Includes 105 pairwise matchups with win totals and winning percentages.

### Era-Based Trends

The `data/nl_era_summary.csv` file breaks down franchise performance across five major MLB eras:
- **Founding Era** (1876–1900)
- **Dead-Ball Era** (1901–1919)
- **Live-Ball / Golden Age** (1920–1960)
- **Expansion Era** (1961–1992)
- **Wild Card / Interleague Era** (1993–present)

### Season-by-Season Historical Performance

The `data/nl_season_by_season.csv` file contains season-by-season records for key franchise milestones across all 15 current NL teams, including:
- Championship seasons (World Series winners, NL pennant winners)
- Representative seasons across each franchise's five eras
- Division assignments reflecting realignment changes
- Context notes explaining each season's significance

## World Series Champions — NL Teams (1905–2024)

| Year | Champion | Score | Opponent (AL) |
|------|----------|-------|---------------|
| 1905 | New York Giants | 4–1 | Philadelphia A's |
| 1906 | Chicago Cubs | 4–2 | Chicago White Sox |
| 1908 | Chicago Cubs | 4–1 | Detroit Tigers |
| 1914 | Boston Braves | 4–0 | Philadelphia A's |
| 1919 | Cincinnati Reds | 3–2 | Chicago White Sox |
| 1921 | New York Giants | 4–3 | NY Yankees |
| 1922 | New York Giants | 4–0 | NY Yankees |
| 1926 | St. Louis Cardinals | 4–3 | NY Yankees |
| 1931 | St. Louis Cardinals | 4–2 | Philadelphia A's |
| 1933 | New York Giants | 4–1 | Washington Senators |
| 1934 | St. Louis Cardinals | 4–3 | Detroit Tigers |
| 1942 | St. Louis Cardinals | 4–1 | NY Yankees |
| 1944 | St. Louis Cardinals | 4–2 | St. Louis Browns |
| 1946 | St. Louis Cardinals | 4–3 | Boston Red Sox |
| 1954 | New York Giants | 4–0 | Cleveland Indians |
| 1955 | Brooklyn Dodgers | 4–3 | NY Yankees |
| 1957 | Milwaukee Braves | 4–3 | NY Yankees |
| 1959 | Los Angeles Dodgers | 4–2 | Chicago White Sox |
| 1960 | Pittsburgh Pirates | 4–3 | NY Yankees |
| 1963 | Los Angeles Dodgers | 4–0 | NY Yankees |
| 1964 | St. Louis Cardinals | 4–3 | NY Yankees |
| 1965 | Los Angeles Dodgers | 4–3 | Minnesota Twins |
| 1967 | St. Louis Cardinals | 4–3 | Boston Red Sox |
| 1969 | New York Mets | 4–1 | Baltimore Orioles |
| 1971 | Pittsburgh Pirates | 4–3 | Baltimore Orioles |
| 1975 | Cincinnati Reds | 4–3 | Boston Red Sox |
| 1976 | Cincinnati Reds | 4–0 | NY Yankees |
| 1979 | Pittsburgh Pirates | 4–3 | Baltimore Orioles |
| 1980 | Philadelphia Phillies | 4–2 | Kansas City Royals |
| 1981 | Los Angeles Dodgers | 3–2 | NY Yankees |
| 1982 | St. Louis Cardinals | 4–3 | Milwaukee Brewers |
| 1986 | New York Mets | 4–3 | Boston Red Sox |
| 1988 | Los Angeles Dodgers | 4–1 | Oakland A's |
| 1990 | Cincinnati Reds | 4–0 | Oakland A's |
| 1995 | Atlanta Braves | 4–2 | Cleveland Indians |
| 1997 | Florida Marlins | 4–3 | Cleveland Indians |
| 2001 | Arizona Diamondbacks | 4–3 | NY Yankees |
| 2003 | Florida Marlins | 4–2 | NY Yankees |
| 2006 | St. Louis Cardinals | 4–1 | Detroit Tigers |
| 2008 | Philadelphia Phillies | 4–1 | Tampa Bay Rays |
| 2010 | San Francisco Giants | 4–1 | Texas Rangers |
| 2011 | St. Louis Cardinals | 4–3 | Texas Rangers |
| 2012 | San Francisco Giants | 4–0 | Detroit Tigers |
| 2014 | San Francisco Giants | 4–3 | Kansas City Royals |
| 2016 | Chicago Cubs | 4–3 | Cleveland Indians |
| 2019 | Washington Nationals | 4–3 | Houston Astros |
| 2020 | Los Angeles Dodgers | 4–2 | Tampa Bay Rays |
| 2021 | Atlanta Braves | 4–2 | Houston Astros |
| 2024 | Los Angeles Dodgers | 4–1 | NY Yankees |

## NL Championship Totals (Through 2025)

| Franchise | WS Titles | Pennants |
|-----------|-----------|----------|
| San Francisco Giants | 8 | 23 |
| St. Louis Cardinals | 11 | 23 |
| Los Angeles Dodgers | 7 | 24 |
| Atlanta Braves* | 4 | 17 |
| Pittsburgh Pirates | 5 | 9 |
| Cincinnati Reds | 5 | 10 |
| Chicago Cubs | 3 | 17 |
| Philadelphia Phillies | 2 | 8 |
| New York Mets | 2 | 5 |
| Florida/Miami Marlins | 2 | 2 |
| Boston Braves* | 1 | 1 |
| Brooklyn Dodgers* | 1 | 1 |
| Milwaukee Braves* | 1 | 1 |
| Arizona Diamondbacks | 1 | 1 |
| Washington Nationals | 1 | 3 |
| Colorado Rockies | 0 | 1 |
| San Diego Padres | 0 | 2 |

*Count includes prior city incarnations as continuous franchise history*

## Planned Visualizations

1. **All-time winning percentage bar chart** — Ranking all 15 NL franchises
2. **Decade-by-decade trend lines** — How each franchise's Win% shifted over time
3. **Head-to-head heatmap** — NL team-vs-team win rates as a color matrix
4. **Expansion team trajectories** — Comparing post-1960 franchises vs originals
5. **Above/below .500 timeline** — Seasons each team spent above or below .500
6. **Win total accumulation curves** — Cumulative wins over franchise history
7. **Championship timeline** — WS titles per franchise across eras
8. **Dominance era heatmap** — Win% by franchise × era matrix
9. **Division dominance chart** — Pennant winners by division across eras
10. **Expansion impact analysis** — Win distribution before and after each expansion wave

## Methodology Notes

- All records reflect **regular-season games only**; postseason is excluded (except where noted).
- Ties (common in the pre-1920 era) are excluded from winning percentage calculations (Win% = W / (W + L)).
- Franchise relocations are treated as continuous entities (e.g., Brooklyn Dodgers → Los Angeles Dodgers).
- The Milwaukee Brewers record includes their AL tenure (1969–1997) since this repo tracks franchise history.
- The Washington Nationals record includes the Montreal Expos era (1969–2004).
- Data is current through the end of the **2025 regular season**.

## Getting Started

```bash
git clone https://github.com/zhub9006/nl-team-trends.git
cd nl-team-trends
pip install pandas matplotlib seaborn jupyter
```

Open any notebook in `notebooks/` to explore the data and generate visualizations.

## Contributing

Contributions are welcome! If you have additional historical data, corrections, or new analyses, please open an issue or submit a pull request.

### Data Validation
All data should be cross-referenced with [Baseball-Reference](https://www.baseball-reference.com) or [Retrosheet](https://www.retrosheet.org). Please include source citations when adding new records.

## License

This project is for educational and analytical purposes. The underlying baseball data is sourced from publicly available records. All historical statistics are property of Major League Baseball.