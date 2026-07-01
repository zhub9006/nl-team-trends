# NL Team Trends — Research Insights

Key findings, patterns, and analytical observations derived from historical National League performance data (1876–2025).

---

## 1. Dynasty Eras

| Dynasty | Team | Period | Key Stats |
|---------|------|--------|-----------|
| **Cardinal dynasty** | St. Louis Cardinals | 1926–1934, 1942–1946, 1964–1968, 2006–2015 | 11 WS titles; 143 seasons; 4,723 NL wins |
| **Braves 14-year streak** | Atlanta Braves | 1991–2005 | 14 consecutive division titles; 5 NL pennants in that span |
| **Dodgers modern dominance** | Los Angeles Dodgers | 2014–2025 | 8 of 10 NL pennants; 6 WS titles in 12 years |
| **Giants 3-peat** | San Francisco Giants | 2010–2014 | 3 WS titles in 5 seasons; .555 H2H vs Cardinals |
| **Mets Miracle** | New York Mets | 1969, 1986 | 2 WS titles despite 59 seasons (.519 Win%) |

## 2. Championship Droughts (as of 2025)

| Team | Last WS Title | Drought (years) | Notes |
|------|---------------|-----------------|-------|
| Cincinnati Reds | 1990 | 35 | Longest active NL drought |
| Pittsburgh Pirates | 2013 | 12 | Second-longest active NL drought |
| San Diego Padres | — | Never | 45 seasons, 0 titles |
| Colorado Rockies | — | Never | 33 seasons, 0 titles; .443 Win% (worst NL franchise) |
| Milwaukee Brewers | — | Never | 49 NL seasons (moved from AL 1998) |

## 3. All-Time NL Franchise Rankings (Win%)

| Rank | Franchise | Win% | WS Titles | Pennants |
|------|-----------|------|-----------|----------|
| 1 | St. Louis Cardinals | .529 | 11 | 19+ |
| 2 | San Francisco Giants | .514 | 8 | 21+ |
| 3 | Los Angeles Dodgers | .512 | 7 | 25+ |
| 4 | Pittsburgh Pirates | .500 | 5 | 9 |
| 5 | Chicago Cubs | .499 | 3 | 17+ |
| 6 | Cincinnati Reds | .487 | 5 | 10 |
| 7 | Atlanta Braves | .487 | 4 | 18+ |
| 8 | Philadelphia Phillies | .479 | 2 | 8 |
| 9 | Montreal Expos/Washington | .488 | 1 | 1 |
| 10 | New York Mets | .519 | 2 | 5 |
| 11 | Colorado Rockies | .443 | 0 | 0 |
| 12 | Florida Marlins/Miami | .484 | 2 | 2 |
| 13 | San Diego Padres | .478 | 0 | 2 |
| 14 | Arizona Diamondbacks | .459 | 1 | 1 |
| 15 | Milwaukee Brewers | .473 | 0 | 5 |

## 4. H2H Rivalries (from team-vs-team matrix)

| Rivalry | H2H Win% | Margin | Notes |
|---------|----------|--------|-------|
| Cardinals vs Reds | .531 | +164 games | Historic NL Central rivalry |
| Dodgers vs Giants | .504 | +10 games | Nearly even; Transit Series era |
| Mets vs Phillies | .500 | Even | Perfectly balanced modern rivalry |
| Braves vs Mets | .500 | Even | 1990s playoff battles |
| Dodgers vs Padres | .827 | +187 games | Dodgers dominate recently |
| Cubs vs Cardinals | .472 | -182 games | Cardinals lead this classic rivalry |
| Braves vs Phillies | .574 | +91 games | Braves strong in 1990s matchups |

## 5. Single-Season Records

| Record | Team | Year | Value |
|--------|------|------|-------|
| Best Win% (154+ games) | Chicago Cubs | 1906 | .763 (116-36) |
| Most Wins | Chicago Cubs | 1906 | 116 |
| Worst Win% (full season) | 1962 Mets | 1962 | .250 (40-120) |
| Most Losses | 1962 Mets | 1962 | 120 |
| Most WS Games Won | St. Louis Cardinals | Various | 11 titles |
| Longest Pennant Streak | Atlanta Braves | 1991-2005 | 14 consecutive |

## 6. Era-Level Competitive Balance

| Era | Avg Win% Range (champions) | Competitive Balance |
|-----|---------------------------|---------------------|
| Pre-Modern | .550–.798 | Low — 2-3 teams dominated |
| Dead Ball | .641–.741 | Low — Pirates/Giants/Cubs |
| Live Ball | .578–.688 | Moderate — Cardinals/Dodgers |
| Post-War | .564–.681 | Moderate — Dodgers/Cardinals |
| Expansion | .543–.667 | Increasing diversity |
| Divisional (1994+) | .516–.654 | High — 7 different champions in 30 years |
| Modern (2020+) | .519–.717 | High — Dodgers + wildcards |

## 7. Expansion Impact Analysis

| Expansion Wave | Year | Teams Added | Effect on NL |
|----------------|------|-------------|--------------|
| First expansion | 1962 | Mets, Colt .45s (now Astros) | Broke Dodgers/Cardinals duopoly |
| Second expansion | 1969 | Royals, Pilots (now Brewers), Expos, Padres | Further diluted talent; first Wild Card |
| Third expansion | 1977 | Blue Jays, Mariners (AL only) | Minimal NL impact |
| Fourth expansion | 1993 | Rockies, Marlins | Shortened Dodgers/Cardinals dominance |
| Realignment | 1998 | Brewers move to NL | 15-team parity; wild card expand |
| Digital era | 2020+ | 12-team playoff | More teams in postseason; shorter series |

## 8. Emerging Trends (2020–2025)

- **Dodgers dominance**: 6 NL pennants in 7 years (2017-2023 runner-up, 2020-2025 champion)
- **Wild Card rise**: Diamondbacks (2023), Phillies (2022) reached WS as non-division winners
- **Shortened season anomaly**: 2020 Dodgers (.717) — could be unsustainable
- **Universal DH**: Adopted 2022; benefits AL-style teams in NL
- **12-team playoff**: More teams make postseason; dilutes regular-season urgency
- **Interleague play**: Year-round since 2023; NL teams face AL competition continuously

## 9. Data Quality Notes

- Pre-1969 data has fewer games per season (60-154), making direct Win% comparisons across eras problematic
- Franchise relocations (Boston→Milwaukee→Atlanta; Brooklyn→LA; NY Giants→SF) are tracked with `modern_name` field
- The 1994 season was canceled — no champion recorded
- 1981 season split by players' strike; Cardinals won WS but had below-.500 first-half record
- 2020 season: 60 games only; compressing to full-season equivalent is non-trivial

## 10. Suggested Analyses

1. **Rolling 10-year win% trend lines** — plot all 15 franchises to visualize trajectory shifts
2. **Era heatmap** — franchise × era colored by Win% to spot dynasty periods
3. **Championship drought chart** — bars showing time since last WS title per franchise
4. **H2H network graph** — nodes are teams, edges weighted by H2H win%
5. **Run differential correlation** — does run diff predict playoff success better than win%?
6. **Division winner probability** — historical likelihood of division winner making WS
7. **Wild card vs division title WS probability** — does path to postseason matter?