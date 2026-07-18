# Data Index & Conventions

This file indexes all data files in the `data/` directory and documents conventions used.

## File Index

| File | Description | Format | Years |
|------|-------------|--------|-------|
| `nl_historical_performance.csv` | Season-by-season NL standings & champions | CSV | 1876–2026 |
| `nl_pennant_winners.csv` | All NL pennant winners with records & WS results | CSV | 1876–2025 |
| `nl_all_time_records.csv` | All-time NL franchise records (W/L/%) | CSV | 1876–2026 |
| `nl_championship_trends.csv` | Championship highlights by era | CSV | 1876–2026 |
| `nl_championship_milestones.csv` | Key championship milestones by decade | CSV | 1876–2026 |
| `nl_notable_records.csv` | Key single-season & franchise records | CSV | 1876–2026 |
| `nl_recent_standings.csv` | Divisional standings 2014-2025 | CSV | 2014–2026 |
| `nl_team_vs_team_summary.csv` | H2H W-L summary matrix (key matchups) | CSV | 1876–2026 |
| `nl_seasonal_standings.csv` | Full seasonal breakdown with division splits | CSV | 1876–2026 |
| `nl_divisional_titles.csv` | Division title winners by year & division | CSV | 1876–2026 |
| `nl_wild_card_winners.csv` | Wild card/playoff winners by year | CSV | 1876–2026 |

## Conventions
- **Team names**: Canonical NL team names; franchise movements noted parenthetically
- **W-L format**: Wins-Losses (e.g., 98-55)
- **Win%**: W/(W+L), 3 decimal places
- **Franchise continuity**: Relocated teams treated as continuous entities
- **Eras**: 154G (1909-1961) → 162G (1962-2019) → 60G (2020) → 162G (2021+)
- **Data sources**: Baseball Almanac (H2H), Baseball Reference, MLB.com, ESPN, Surprise Sports

## Recent Updates
- Cardinals last WS title corrected to 2011 (not 1982)
- Braves last WS title corrected to 2021
- Dodgers analytics through 2025 added (back-to-back titles)
- Phillies 2023 WS result, 2025 NL runner-up added
- NL West dominance by Dodgers 2018-2025 (8 straight) documented
- Added 4 new data files: nl_notable_records.csv, nl_recent_standings.csv, nl_pennant_winners.csv, nl_championship_milestones.csv