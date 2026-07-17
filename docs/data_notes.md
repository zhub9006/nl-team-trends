# Data Notes

Methodology, conventions, and limitations for the NL Team Trends project data.

## Methodology
- Primary data sources: Baseball-Reference, Baseball Almanac, SABR Lahman Database
- Secondary sources: StatMuse, Wikipedia, Grokipedia, AP News, ESPN
- All data verified against at least two independent sources
- Franchise continuity: Relocated teams treated as single continuous franchises (e.g., Brooklyn Superbas → LADodgers)
- Era notation: Win% calculated as W/(W+L); ties excluded from percentage
- Pre-1900 data uses 154-game era conventions; post-1961 uses 162-game conventions
- 2026 season data is partial (season in progress as of July 2026)

## Conventions
- **Team names**: Canonical NL team names; franchise movements noted parenthetically
  - E.g., "Brooklyn Superbas/Dodgers" for Brooklyn → LA Dodgers migration
  - E.g., "NY Giants/SF Giants" for NY → San Francisco migration
  - E.g., "Montreal Expos/Washington Nationals" for Montreal → Washington migration
- **W-L format**: Wins-Losses (e.g., 98-55)
- **Winning %**: Calculated as W / (W + L), rounded to 3 decimal places
- **Schedule eras**:
  - 1876–1884: 60–112 games per season (varied)
  - 1885–1908: 126–154 games (standardization begins)
  - 1909–1961: 154 games (consistent)
  - 1962–2019: 162 games (modern era)
  - 2020: 60 games (COVID-19 shortened season)
  - 2021–present: 162 games (restored)
- **World Series notation**: "NL won WS" or "NL lost WS" or "N/A (no WS)"
- **1994 season**: Struck out; division titles not awarded; pennant winners not determined officially

## Data File Schemas

### nl_historical_performance.csv
- Year, NL_Champion, Champion_Wins, Champion_Losses, Champion_WPct, Second_Place, Second_Wins, Second_Losses, Second_WPct, WS_Champion, WS_Result, Era

### nl_pennant_winners.csv
- Year, Team, Record, WinPct, Notable, WS_Champion

### nl_all_time_records.csv
- Team, First_Season, Division, Games, Wins, Losses, WinPct, Pennants, WS_Titles, Current_Division

### nl_seasonal_standings.csv
- Year, Team, East_W, East_L, Central_W, Central_L, West_W, West_L, Overall_W, Overall_L, Overall_WPct, Division, Notes

### nl_divisional_titles.csv
- Year, Division, Champion, Wins, Losses, WinPct, Second_Place, Second_Wins, Second_Losses, Second_WPct

### nl_wild_card_winners.csv
- Year, WCLeader, Wins, Losses, WinPct, WC_Game, WC_Result, Notes

### nl_championship_trends.csv
- Year, Champion, W-L, WS_Title, Key_Franchise, Milestone

### nl_notable_records.csv
- Record_Type, Team, Year, Achievement, Value, Context

### nl_recent_standings.csv
- Year, NL_East_W, NL_East_L, NL_Central_W, NL_Central_L, NL_West_W, NL_West_L, NL_Champion, AL_Champion, WS_Winner

### nl_team_vs_team_summary.csv
- Team_1, Team_2, Team_1_Wins, Team_2_Wins, Team_1_Win_Pct, Games_Played, Most_Recent_Winner

## Limitations
1. Pre-1900 data may have gaps in statistical categories
2. 2026 season data is incomplete (season in progress as of July 2026)
3. Win percentages not adjusted for era-specific factors (e.g., 154G vs 162G differences)
4. Interleague play data excluded from franchise-vs-franchise comparisons
5. 1994 season data is absent (strike cancelled season)
6. Standings from 1876-1891 may not use modern division format (pre-division era)
7. Team name changes and franchise relocations require careful cross-referencing

## Key Research Questions Addressable
- Which NL franchise has the highest all-time winning percentage?
- How has NL competitive balance changed over eras?
- What is the average duration of NL championship droughts?
- How do H2H W-L matchups reflect historical rivalry patterns?
- Which division has been most consistently dominant?
- What role did expansion play in eroding franchise dominance?
- How do shortened-season records compare to full 162-game records?