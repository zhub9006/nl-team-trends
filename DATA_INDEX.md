# NL Team Trends — Data Index

This file documents all data files in the `data/` directory, their schemas, sources, and usage conventions.

---

## Table of Contents

1. [Data Files](#data-files)
2. [Schema Conventions](#schema-conventions)
3. [Source Attribution](#source-attribution)
4. [Update Schedule](#update-schedule)

---

## Data Files

| File | Description | Key Fields | Rows (approx.) | Last Updated |
|------|-------------|-----------|----------------|-------------|
| `nl_historical_performance.csv` | Season-by-season NL standings from 1876–present | season, year, team, games, wins, losses, ties, win_pct, division, league_champion, pennant_winner, ws_champion, runs_scored, runs_allowed, notes | ~61 key-season rows + original 8-team 1876 | July 2025 |
| `nl_all_time_records.csv` | All-time franchise records with W/L, pennants, WS titles | team, ws_titles, games, wins, losses, win_pct, last_ws_title, last_pennant, division_titles, current_division | 15 | July 2025 |
| `nl_championship_trends.csv` | Championship highlights by era | era, start_year, end_year, dominant_team(s), theme, pennants, ws_titles | 8 | July 2025 |
| `nl_championship_milestones.csv` | Championship milestones by decade/era | decade, team, milestone, year, detail | 40+ | July 2025 |
| `nl_notable_records.csv` | Key single-season & franchise records | record_type, team, year, value, notes | 19 | July 2025 |
| `nl_team_vs_team_summary.csv` | H2H W-L summary matrix (key matchups) | team1, team2, total_games, team1_wins, team2_wins, t1_win_pct, notable_trend | 12 | July 2025 |
| `nl_h2h_rivalries_detailed.csv` | Detailed H2H rivalry data with era dominance and historical notes | team_1, team_2, total_games, team_1_wins, team_2_wins, t1_win_pct, era_dominant, notes | 20 | July 2026 |
| `nl_historical_trends_analysis.md` | Comprehensive era-by-era historical trends analysis | era, team, pennants, ws_titles, themes, records, notes | — | July 2026 |
| `nl_recent_standings.csv` | Divisional standings 2014–2025 | year, team, division, wins, losses, win_pct, division_pos | ~72 | July 2025 |
| `nl_seasonal_standings.csv` | Full seasonal breakdown with division splits | year, team, division, wins, losses, win_pct | TBD | Planned |
| `nl_pennant_winners.csv` | All NL pennant winners 1876–2025 | year, team, ws_result | ~145 | July 2025 |

---

## Schema Conventions

- **Team names**: Canonical NL team names; franchise movements parenthetically (e.g., "Brooklyn Superbas/Dodgers").
- **W-L-T**: Standard wins-losses-ties format; ties excluded from win percentage calculations.
- **Winning %**: Calculated as W/(W+L), 3 decimal places.
- **Seasons**: Regular-season only; postseason data is in separate fields.
- **Franchise continuity**: Relocated teams treated as continuous entities (NY Giants → SF Giants, Brooklyn → LA Dodgers, Montreal Expos → Washington Nationals).
- **Division names**: E (East), C (Central), W (West), NA (pre-division era).
- **Boolean flags**: league_champion, pennant_winner, ws_champion use Yes/No.

---

## Source Attribution

| Source | URL | Coverage | Priority |
|--------|-----|----------|----------|
| Baseball-Reference (NL) | https://www.baseball-reference.com/leagues/NL/ | 1876–present | Primary |
| Baseball Almanac (H2H) | https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml | 1876–2026 | Primary (H2H) |
| Baseball Almanac (Year-by-Year) | https://www.baseball-almanac.com/yearmenu.shtml | 1876–present | Primary |
| SABR Lahman Database | https://sabr.org/lahman-database/ | 1871–2025 | Primary (bulk CSV) |
| Baseball Data Hub | https://baseballdatahub.com/seasons/ | 1871–2026 | Secondary |
| StatsCrew (NL) | https://www.statscrew.com/baseball/l-NL | 1876–present | Secondary |
| StatMuse (NL Championships) | https://www.statmuse.com/mlb | 1876–2026 | Secondary |
| ESPN (World Series) | https://www.espn.com/mlb/worldseries/history/winners | 1903–present | Secondary |
| Wikipedia (NL Pennants) | https://en.wikipedia.org/wiki/List_of_National_League_pennant_winners | 1876–present | Secondary |
| MLB Win-Loss Visualizer | https://inkandthunder.github.io/win-loss-visualizer/ | 1894–present | Tertiary |
| Champs or Chumps | https://champsorchumps.us/mlb | 1876–present | Tertiary |

---

## Update Schedule

- **Seasonal data**: Updated after each NL regular season concludes, typically in autumn
- **H2H matrices**: Baseball Almanac updates daily during the regular season
- **Championship data**: Updated within one week of World Series conclusion
- **New franchise records**: As teams play each new season, cumulative records are recalculated

---

## Data Versioning

Data files in this repository target the **2025 MLB season** as the latest complete season. Incomplete seasons (e.g., 2026 season in progress) are treated with the following conventions:
- In-progress seasons marked with `*` suffix in team records
- H2H data includes all completed games through the last completed date
- Seasonal standings include only teams with a completed season
