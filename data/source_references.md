# Data Sources — Provenance & Versioning

This file tracks the provenance of all data files within the `data/` directory.

## Source Attribution per File

| File | Primary Source | Secondary Verification | Last Verified |
|------|---------------|----------------------|---------------|
| `nl_pennant_winners.csv` | OoCities NLPBC History, Wikipedia (NL Pennants) | Baseball-Reference NL | July 2025 |
| `nl_all_time_records.csv` | StatMuse, Baseball Almanac, ESPN | Wikipedia (NL teams) | July 2025 |
| `nl_championship_trends.csv` | Grokipedia, OoCities, SportzSpark | ESPN WS History | July 2025 |
| `nl_championship_milestones.csv` | Baseball Almanac, Grokipedia, ESPN | Wikipedia (NL Pennants) | July 2025 |
| `nl_notable_records.csv` | Baseball Almanac (H2H), Baseball-Reference | MLB.com, StatMuse | July 2025 |
| `nl_team_vs_team_summary.csv` | Baseball Almanac H2H matrices (1876-2026) | Lahman Database | July 2025 |
| `nl_recent_standings.csv` | StatMuse (2014-2025), MLB.com (2026) | ESPN Standings | July 2026 |
| `nl_seasonal_standings.csv` | Baseball-Reference NL, Baseball Almanac year-by-year | StatsCrew NL | July 2025 |
| `nl_season_standings_2025_2026.csv` | MLB.com Standings, ESPN | Baseball-Reference | July 2026 |
| `nl_historical_performance.csv` | Baseball-Reference NL, Baseball Almanac, Lahman DB | StatsCrew, StatMuse | July 2025 |

## Data Download Links

- **Lahman Database**: https://sabr.org/lahman-database/
- **Baseball-Reference NL**: https://www.baseball-reference.com/leagues/NL/
- **Baseball Almanac H2H**: https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml
- **StatMuse NL**: https://www.statmuse.com/mlb

## Update Notes
- Files are updated after each MLB season concludes
- Playoff results verified against ESPN WS History
- H2H matrices source: Baseball Almanac (primary), cross-ref with Lahman
- 2025 season data finalized post-WS; 2026 data is live/in-progress
