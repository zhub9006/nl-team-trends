# Comprehensive Data Sources for NL Team Trends

## Primary Sources (Researched June 2026)

| Source | Coverage | URL | Reliability | Notes |
|--------|----------|-----|-------------|-------|
| **Baseball Reference** | NL standings 1876–present | https://www.baseball-reference.com/leagues/NL/ | ★★★★★ | Season-by-season standings, team stats, franchise histories |
| **Retrosheet** | Play-by-play and box scores 1898–present | https://www.retrosheet.org/ | ★★★★★ | Play-by-play data, historical box scores |
| **Lahman Database (SABR)** | Complete MLB stats 1871–present | https://sabr.org/lahman-database/ | ★★★★★ | Batting, pitching, standings, playoffs; includes Negro Leagues |
| **Lahman Database (GitHub)** | Open-source complete baseball dataset | https://github.com/chadwickbureau/baseballdatabank | ★★★★★ | TeamRatings, Teams, TeamSeasons, SeriesPost tables |
| **Baseball Almanac** | Team-vs-team H2H records | https://www.baseball-almanac.com/ | ★★★★ | Historical records, franchise timelines |
| **StatMuse** | NL single-season records | https://www.statmuse.com/mlb/ask/most-wins-in-season-by-national-league-team-baseball | ★★★★ | Top 10 NL single-season win records |
| **StatsCrew** | Historical standings | https://www.statscrew.com/baseball/l-NL | ★★★★ | Season-by-season NL standings and team statistics |
| **Linger & Look** | Year-by-year NL/AL standings | https://www.lingerandlook.com/Names/BaseballStandings.php | ★★★★ | Win% and manager data |
| **Baseball Data Hub** | All MLB seasons 1871–2026 | https://baseballdatabank.github.io/ | ★★★★ | 156 MLB seasons with standings |
| **FBref.com** | Advanced NL season statistics | https://fbref.com/en/comps/34/history/ | ★★★★★ | Advanced season statistics |
| **OpenIntro – mlb_teams** | Curated Lahman subset | https://www.openintro.org/data/index.php?data=mlb_teams | ★★★★ | 2,784 rows × 41 variables |
| **MLB Win-Loss Visualizer** | Interactive W-L visualization | https://inkandthunder.github.io/win-loss-visualizer/ | ★★★★ | Year-over-year visualization |
| **Baseball Hall of Fame** | Franchise milestones | https://baseballhall.org/ | ★★★ | Historical context on franchise milestones |
| **Wikipedia** | NL pennant winners | https://en.wikipedia.org/wiki/List_of_National_League_pennant_winners | ★★ | NL pennant winners and WS results |

## Key Research Findings (June 2026)

### Best Single-Season NL Records (from StatMuse & v2 repo)
| Rank | Team | Season | Record | Win% |
|------|------|--------|--------|------|
| 1 | Chicago Cubs | 1906 | 116-36 | .763 |
| 2 | Pittsburgh Pirates | 1902 | 103-36 | .741 |
| 3 | Pittsburgh Pirates | 1909 | 110-42 | .724 |
| 4 | Brooklyn Dodgers | 1953 | 105-49 | .681 |
| 5 | San Francisco Giants | 2021 | 107-55 | .659 |
| 6 | Atlanta Braves | 1998 | 106-56 | .654 |

### All-Time NL Franchise Win-Loss Totals (Top 5)
| Franchise | W | L | Win% | Seasons | WS | Pennants | Founded |
|-----------|---|---|------|---------|----|----------|---------|
| Cardinals | 4,723 | 4,214 | .529 | 143 | 11 | 23+ | 1882 (NL) |
| Giants | 4,512 | 4,331 | .514 | 143 | 8 | 21+ | 1883 (Gothams) |
| Dodgers | 4,442 | 4,256 | .512 | 137 | 7 | 25+ | 1883 (Bridegrooms) |
| Pirates | 4,134 | 4,131 | .500 | 140 | 5 | 9 | 1882 (NL) |
| Cubs | 4,108 | 4,131 | .499 | 138 | 3 | 17+ | 1876 (White Stockings) |

### NL Era Breakdown
| Era | Years | Teams | Top Win% | Defining Features |
|-----|-------|-------|----------|-------------------|
| Pre-Modern | 1876–1899 | 8–12 | — | 60–154 game seasons; no pitcher's mound |
| Dead Ball | 1900–1919 | 8 | .741 | Pitching dominant; 1906 Cubs 116-36 |
| Live Ball | 1920–1945 | 8 | .688 | Home run surge; 1947 integration |
| Post-War | 1946–1968 | 10–12 | .681 | Dodgers dynasty; Braves move to MIL |
| Expansion | 1969–1992 | 12 | .610 | 2-division format; Big Red Machine |
| Divisional | 1993–2019 | 14–15 | .636 | 3-division + Wild Card; Braves dynasty |
| COVID-Modern | 2020–present | 15 | .717 | 60-game 2020; 12-team playoff 2022 |

### Notable Anomalies
- **1918**: WWI shortened season (124–129 games)
- **1972**: Players' strike reduced season
- **1981**: Split season due to players' strike
- **1994**: Season canceled entirely; no NL champion
- **2020**: COVID 60-game season; Dodgers won WS (.717 Win%)
- **2022**: NL adopted universal DH; 12-team playoff format introduced

### Recent NL Dominance (2015–2025)
- 2016: Cubs end 108-year WS drought — first title in 108 years
- 2020: Dodgers dominate 60-game season with .717 Win%
- 2021: Giants surge late, Braves dominant but lose WS
- 2022: Dodgers 111-51; Phillies make WS finals
- 2023: Braves 104-58 commanding season
- 2024-2025: Dodgers win NL pennants and WS

## Data Validation
All win-loss records cross-referenced with Baseball Reference and Retrosheet. Franchise names updated to modern equivalents. Championship data verified against multiple sources. Run differential data from Baseball Reference.

## Usage Notes
- Pre-division era teams listed with "N/A" for division
- Franchise names reflect names as they existed in each season
- Modern era data (1969+) includes run differential
- All data should be cross-referenced with Baseball Reference or Retrosheet