# Data Index & Conventions

This file indexes all data files in the `data/` directory and documents conventions used.

## File Index

| File | Description | Format | Years |
|------|-------------|--------|-------|
| `nl_historical_performance.csv` | Season-by-season NL standings & champions | CSV | 1876–2026 |
| `nl_pennant_winners.csv` | All NL pennant winners with records & WS results | CSV | 1876–2025 |
| `nl_all_time_records.csv` | All-time NL franchise records (W/L/%, pennants, div titles) | CSV | 1876–2026 |
| `nl_all_time_records_v2.csv` | Expanded all-time records (H2H + franchise wins + droughts) | CSV | 1876–2026 |
| `nl_all_time_records_complete.csv` | Complete all-time NL records with H2H leads, droughts, detailed notes | CSV | 1876–2026 |
| `nl_championship_trends.csv` | Championship highlights by era | CSV | 1876–2026 |
| `nl_championship_milestones.csv` | Key championship milestones by decade/era | CSV | 1876–2026 |
| `nl_notable_records.csv` | Key single-season & franchise records | CSV | 1876–2026 |
| `nl_team_vs_team_summary.csv` | H2H W-L summary matrix (key matchups) | CSV | 1876–2026 |
| `nl_team_vs_team_full.csv` | Full NL H2H matrix (all pairings, 1876-2026) | CSV | 1876–2026 |
| `nl_recent_standings.csv` | Divisional standings 2014-2026 | CSV | 2014–2026 |
| `nl_seasonal_standings.csv` | Full seasonal breakdown with division splits | CSV | 1876–2026 |
| `nl_season_standings_2025_2026.csv` | 2025-2026 season-by-season division standings with detailed records | CSV | 2025–2026 |
| `nl_divisional_titles.csv` | Division title winners by year & division | CSV | 1969–2025 |
| `nl_wild_card_winners.csv` | Wild card/playoff winners by year | CSV | 1994–2025 |

## Conventions
- **Team names**: Canonical NL team names; franchise movements noted parenthetically
- **W-L format**: Wins-Losses (e.g., 98-55)
- **Win%**: W/(W+L), 3 decimal places
- **Franchise continuity**: Relocated teams treated as continuous entities
- **Eras**: 154G (1909-1961) → 162G (1962-2019) → 60G (2020) → 162G (2021+)
- **Data sources**: Baseball Almanac (H2H), Baseball Reference, MLB.com, ESPN, Surprise Sports

## Research Sources Used
| Source | URL | Coverage | Key Data |
|--------|-----|----------|----------|
| Baseball-Reference (NL) | https://www.baseball-reference.com/leagues/NL/ | 1876–present | Official year-by-year NL standings & team stats |
| Baseball Almanac | https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml | 1876–2026 | 15×15 H2H W-L matrices for every NL team pair |
| StatMuse (NL Championships) | https://www.statmuse.com/mlb | 1876–2026 | NL championship leaders & franchise W/L/G stats |
| Champs or Chumps | https://champsorchumps.us/mlb | 1876–present | Win% rankings, droughts, streaks, postseason records |
| StatsCrew (NL) | https://www.statscrew.com/baseball/l-NL | 1876–present | NL rosters, standings & leaders |
| Her Sports Corner | https://hersportscorner.com/3374-2/ | NL Central teams | All-time W-L, pennants, championships by NL Central team |
| Grokipedia | https://grokipedia.com/page/List_of_all-time_Major_League_Baseball_win–loss_records | 1871–present | All-time MLB W-L records with era comparisons |
| Wikipedia (NL Pennants) | https://en.wikipedia.org/wiki/List_of_National_League_pennant_winners | 1876–present | Complete pennant winner list with WS results |

## Recent Updates (July 2026)
- Added `nl_all_time_records_complete.csv` with expanded franchise data including H2H leads vs top rivals, longest droughts, team notes, and detailed franchise history
- Added `nl_season_standings_2025_2026.csv` with 2025-2026 season partial standings by division with detailed records
- All-time records enriched with franchise start, division, games, pennants, division titles
- Added comprehensive H2H W-L matrix for all key NL rivalries
- Added championship trends by era with detailed pennant/theme breakdown
- Added NL pennant winners complete list through 2025
- Added notable records: best winning %, best 162G, best shortened season, droughts, franchise milestones
- Added recent standings CSV with full divisional breakdown (2014-2026)
- Cardinals last WS title corrected to 2011
- Braves last WS title corrected to 2021
- Dodgers analytics through 2025: back-to-back titles, 8 straight NL West
- Phillies 2023 WS loss, 2025 NL runner-up added
- LA Dodgers 3 WS titles in 5 years (2020, 2024, 2025); 26 pennants all-time
- NL West dominance by Dodgers 2018-2025 (8 straight) documented
- 150th anniversary of NL (founded 1876) — 2026 milestone marked
- Data file count expanded to 15+ CSVs plus research README
- 2026 partial season data added (through mid-July)