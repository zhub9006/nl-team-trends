# Sources & Methodology

## Research Sources Used

This repository compiles data from the following primary and secondary sources for National League team performance analysis.

### Primary Sources

1. **Baseball Reference – NL Standings**
   - URL: https://www.baseball-reference.com/leagues/NL/
   - Coverage: Season-by-season NL standings, team stats (1876–present)
   - Reliability: ★★★★★ — The gold standard for baseball statistics

2. **Retrosheet**
   - URL: https://www.retrosheet.org/
   - Coverage: Box-score and play-by-play data for NL seasons (1898–2024)
   - Reliability: ★★★★★ — Original box scores; gold standard for play-by-play data

3. **Lahman Database (SABR)**
   - URL: https://sabr.org/lahman-database/
   - Coverage: Complete MLB stats (1871–2025); batting, pitching, fielding, standings, playoffs
   - Reliability: ★★★★★ — Standard academic/research dataset

4. **MLB.com – National League**
   - URL: https://www.mlb.com/national-league

### Secondary Sources

- **Baseball Almanac** – team-vs-team matrix (1876–2026)
- **Linger & Look** – year-by-year standings
- **Baseball Data Hub** – 156 seasons browsable
- **StatsCrew** – season standings
- **Lahman Database GitHub** – open-source dataset
- **OpenIntro mlb_teams** – curated Lahman subset
- **Wikipedia** – NL pennant winners
- **Baseball Hall of Fame** – franchise milestones

## Data Validation

- Cross-reference franchise totals with Baseball Reference and Retrosheet
- For head-to-head data: use Baseball Almanac
- Flag discrepancies > 0.5% win differential between sources in GitHub Issues