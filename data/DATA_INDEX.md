# Data File Index for NL Team Trends

## Overview
This repository compiles National League team performance data since the league's founding in 1876. All data files below are maintained under the `data/` directory.

## File Manifest

| File | Format | Description | Key Columns | Updated |
|------|--------|-------------|-------------|---------|
| `nl_all_time_records.csv` | CSV | Franchise-wide totals (15 teams, through 2025) | Team, Division, Games, Wins, Losses, WinPct, WS, Pennants | Jul 2026 |
| `nl_all_time_records_v2.csv` | CSV | All-time records enriched with H2H leads, droughts, streaks | Adds H2HLeadHT, LongestDrought, StreakSince | Jul 2026 |
| `nl_historical_performance.csv` | CSV | Season-by-season NL standings 1876-2025 | Year, NL_Champion, Champion_W-L, Runner_Up, WS_Result, Era | Jul 2026 |
| `nl_seasonal_standings.csv` | CSV | Divisional breakdowns (144 lines, 1971-2025 more recent subset) | Year, Team, division records, Overall_W% | Jul 2026 |
| `nl_pennant_winners.csv` | CSV | All NL pennant winners with records 1876-2025 | Year, Winner, Record, WS_Opponent, WS_Result, Notable | Jul 2026 |
| `nl_championship_trends.csv` | CSV | Championship highlights organized by era (8 eras) | Era, Dominant_Team, Pennants, Theme, Key_Records | Jul 2026 |
| `nl_championship_milestones.csv` | CSV | Key guaranteed NL historical moments | Year, Milestone, Team, Detail, Significance | Jul 2026 (NEW) |
| `nl_notable_records.csv` | CSV | Single-season & franchise records (20+ entries) | Record_Type, Team, Year, Value, Details | Jul 2026 |
| `nl_team_vs_team_summary.csv` | CSV | Summary of 17 key head-to-head matchups | Team_1, Team_2, T1_Wins, T2_Wins, T1_WinPct | Jul 2026 |
| `nl_team_vs_team_full.csv` | CSV | Full 105-pairing H2H matrix (all NL team combinations) | T1, T2, T1_Wins, T2_Wins, T1_WinPct | Jul 2026 (NEW) |
| `nl_top_seasons_by_win_pct.csv` | CSV | Top seasons (.640+ win%) 1876-2025 | Year, Team, Games, Wins, Losses, WinPct, Notable | Jul 2026 |
| `nl_division_realignments.csv` | CSV | NL division structure evolution 1876-2025 | Year, Event, Divisions, Teams_Affected, Impact | Jul 2026 |
| `nl_team_era_dominance.csv` | CSV | Era-by-era team dominance summary | Team, Era, Pennants, WinPct, Theme | Jul 2026 |
| `nl_recent_standings.csv` | CSV | Divisional standings 2014-2025 quick view | Year, Team, Division, Record, Championship | Jul 2026 |
| `source_references.md` | Markdown | Detailed source attribution & methodology | Source, URL, Coverage, Description | Jul 2026 |

## Directory Structure
```
data/
├── nl_all_time_records.csv          # 15 rows × franchise totals
├── nl_all_time_records_v2.csv       # 15 rows × with drought/H2H columns
├── nl_historical_performance.csv    # 151 seasons × key season data
├── nl_seasonal_standings.csv        # 144 lines × divisional breakouts
├── nl_pennant_winners.csv           # 152 seasons × pennant & WS results
├── nl_championship_trends.csv       # 8 eras × championship themes
├── nl_championship_milestones.csv   # 37 key moments since 1876      ← NEW
├── nl_notable_records.csv          # 20+ row × key records
├── nl_team_vs_team_summary.csv     # 17 row × key matchup summaries
├── nl_team_vs_team_full.csv        # 105 row × 15×15 H2H matrix       ← NEW
├── nl_top_seasons_by_win_pct.csv   # ~45 row × best season records    ← NEW
├── nl_division_realignments.csv    # 14 row × structural changes      ← NEW
├── nl_team_era_dominance.csv       # Multi-row × era-by-era data       ← NEW
├── nl_recent_standings.csv          # 12 row × 2014-2025 fast view
├── source_references.md             # 55 lines × source attribution
└── DATA_INDEX.md                    # This file
```

## Data Conventions

- Team names use canonical NL names with historical names parenthetically notated
- Win% computed as `W / (W + L)`, 3 decimal places
- Ties excluded from W% calculation (rarely occur post-1920)
- Pre-1903 pennants represent NL championship only (no World Series existed)
- 1994 season: no pennant or WS awarded (strike cancelled)
- 2020 season: 60 games; marked as "Shortened"
- Relocated teams' historical stats merged (NYG→SF, Brooklyn→LA, Montreal→WAS)
- All sources documented in `source_references.md`