# Data Notes — Methodology, Conventions & Caveats

## Overview

This document explains the methodology, conventions, and important caveats for the NL Team Trends research project. All data files should be interpreted in light of these guidelines.

## Methodological Notes

### Win-Loss Records
- Win% = Wins / Games Played
- Pre-1961 seasons used 154-game schedules; 1961+ uses 162-game schedules
- Shortened seasons are flagged in notes (e.g., 2020: 60 games; 1981: split season; 1918: 140 games due to WWI)
- Tied games in early NL (pre-1920s) were replayed, so win-loss totals reflect completed games only

### Pennants vs. World Series
- **Pennants** = League championship awards (pre-Wild Card era = pennant winner determined the NL representative;
  Wild Card era = pennant = division winner; 1969+ = NLCS winner)
- **WS Titles** = World Series championships won as an NL team
- **WS Lost** = Played in and lost the World Series

### Team Name Conventions
- Team names reflect the primary name for each era, with franchise relocations and name changes noted in the notes column
- Examples: Brooklyn Dodgers (pre-1958) = LA Dodgers; NY Giants (pre-1958) = SF Giants; Boston Braves = Milwaukee Braves = Atlanta Braves; Montreal Expos = Washington Nationals

### Division Alignment
- 1876-1968: No divisions; single-table league
- 1969-1993: 2 divisions (East & West)
- 1994-present: 3 divisions (East, Central, West) + Wild Card
- 1998: Milwaukee Brewers moved from AL Central to NL Central
- 2005: Montreal Expos relocated to Washington Nationals (AL East → NL East)

### Schedule Changes
- 1876-1891: ~70-84 games per season
- 1892-1960: 154-game schedule (with exceptions for WWI and COVID)
- 1961-1993: 162-game schedule
- 1994: Season cut short by strike; no WS or pennant awarded
- 2020: 60-game season due to COVID-19 pandemic
- 2023: Full interleague schedule (every team plays every other team)

## Important Caveats

1. **All-time franchise records** include pre-relocation history (e.g., LA Dodgers' Brooklyn and NY totals are counted toward current LA Dodgers franchise)
2. **Pennant counts** may differ depending on whether you count NL pennants vs. division titles vs. WS appearances
3. **The 1906 Cubs record** (.763, 116-36) is the all-time MLB record for winning percentage, not just NL
4. **The 2016 Cubs drought** (108 years) is the longest championship drought in North American professional sports history
5. **The Braves' division streak** (14 consecutive, 1991-2005) is the longest run of any division in any major American pro sport
6. **The Dodgers' 8-year NL West dominance** (2018-2025) is unprecedented in the modern 3-division NL
7. **The 1994 season** was voided by the players' strike — no NL pennant or WS was awarded
8. **The 1995 season** was shortened (144 games) due to the 1994 strike carryover

## Data File Guide

| File | Description | Key Columns |
|------|-------------|-------------|
| `data/nl_all_time_records.csv` | All-time franchise win-loss totals by team | Team, First_Season, Division, Games_Played, Wins, Losses, WinPct, Pennants, WS_Won |
| `data/nl_historical_performance.csv` | Championship-season highlights with era labels | year, champion, record, era, notes |
| `data/nl_historical_performance_detailed.csv` | Year-by-year NL champion + 2nd place + WS results | year, champion, champion_record, 2nd_place, ws_opponent, ws_result, era, notes, division_winners |
| `data/nl_pennant_winners_recent.csv` | NL pennant winners and WS results 1995-2025 | year, champion, record, division, ws_opponent, ws_result, notes |
| `data/nl_championship_trends.csv` | Era-based championship trends | era, dominant_team(s), theme, num_pennants, notes, timeline |
| `data/nl_notable_records.csv` | Key single-season and franchise records | category, record, team_detail, value, year, notes |
| `source_references.md` | Detailed source attribution | Source, URL, Coverage, Notes |

## Visualization Notes

- Use `nl_historical_performance_detailed.csv` for year-by-year trend analysis
- Use `nl_all_time_records.csv` for franchise comparison charts
- Use `nl_pennant_winners_recent.csv` for modern-era (1995+) playoff analysis
- Use `nl_championship_trends.csv` for era-based heatmaps
- Use `nl_notable_records.csv` for highlight/benchmark charts
- Consider using Plotly for interactive charts; matplotlib/seaborn for static charts

## Future Data Needs

- [ ] Year-by-year year-by-year standings (all 15 teams) for each season
- [ ] Head-to-head matchup matrices for team-vs-team analysis
- [ ] Batting/pitching leaders per season (from Lahman DB)
- [ ] Run differential per team per season
- [ ] Attendance data per season
- [ ] Manager win-loss records
- [ ] Home/Away splits
- [ ] Month-by-month performance breakdowns
