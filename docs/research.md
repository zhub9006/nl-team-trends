# NL Team Trends – Research Notes

## Overview

This document captures detailed research findings on National League (NL) team performance trends, drawn from multiple historical baseball data sources.

## Key Research Questions

### 1. Franchise Dominance Over Eras
- **St. Louis Cardinals** lead with 19 NL pennants and 11 World Series titles — the most of any NL franchise.
- **San Francisco Giants** hold the all-time NL win record (11,663 wins) and have the highest franchise win percentage (.544).
- **Philadelphia Phillies** have the most NL losses (11,392) but have improved significantly in recent decades.

### 2. Best Single Seasons in NL History
| Rank | Team | Record | Year | Win% |
|------|------|--------|------|------|
| 1 | Chicago Cubs | 116-36 | 1906 | .763 |
| 2 | Chicago Cubs | 104-50 | 1910 | .675 |
| 3 | Pittsburgh Pirates | 110-42 | 1909 | .724 |
| 4 | Chicago Cubs | 107-45 | 1907 | .702 |
| 5 | Cincinnati Reds | 108-54 | 1975 | .667 |

### 3. Longest Pennant Streaks
- **Atlanta Braves**: 14 consecutive division titles (1991–2005)
- **New York/SF Giants**: Multiple stretches of dominance in early 1900s and 2010s
- **St. Louis Cardinals**: Regular contenders with 19 total pennants spread across eras

### 4. Era Analysis
- **Dead Ball Era (1876–1919)**: Low-scoring, pitching-dominated; Giants, Cubs, Reds dominant
- **Live Ball Era (1920–1940)**: Rise of power hitters; Cardinals and Cubs frequent pennant winners
- **Post-War Era (1946–1969)**: Dodgers, Giants, Braves, Mets emerge; expansion era
- **Divisional Era (1969–present)**: Cardinals, Braves, Cubs, Mets, Phillies, Dodgers dominate;
  competitive balance has improved with more franchises contending

### 5. Impact of Expansion
- 1962: Mets and Colt .45s added → NL grew from 8 to 10 teams
- 1969: Royals, Pilots, Expos added → further dilution of talent
- 1993: Rockies and Marlins added → most recent expansion
- 1998: Diamondbacks added, Milwaukee moved from AL → current 16 NL teams

### 6. Interleague Play Effects (post-1997)
- Regular-season interleague games began in 1997
- Effect on NL team records is minimal at the aggregate level
- Some seasonal variation in NL team records when scheduling favors AL matchups

### 7. Run Differential Trends
- Run differentials have generally increased over time as offense has grown
- Modern era (2000-present): higher run differentials correlate more strongly with pennant success
- Pythagorean expectation suggests modern NL teams with >.560 win% are very likely to contend

## Data Visualization Ideas

1. **Win% by decade heat map** — show which franchises dominated each decade
2. **Pennant timeline** — Gantt-style chart showing pennant winners by year
3. **Win-loss trajectory by franchise** — line chart showing winning percentage over time
4. **Division realignment impact** — compare winning percentages before/after 1969 and 1994
5. **Elo ratings over time** — dynamic strength ratings for all NL franchises
6. **Home/away split analysis** — how home field advantage has changed
7. **Postseason performance vs. regular season** — do regular-season dominators win WS?

## Sources

- Baseball Almanac: NL team-vs-team win-loss (1876-2026)
- Baseball Data Hub: Season-by-season standings and stats
- Lahman Baseball Database (SABR): Complete historical team data
- Baseball Reference: NL index and franchise records
- OpenIntro mlb_teams: Curated Lahman subset for R/Python analysis
- Retrosheet: Game-by-game historical records