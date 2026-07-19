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
| `nl_all_time_records.csv` | All-time franchise records with W/L, pennants, WS titles | team, ws_titles, games, wins, losses, win_pct, last_ws_title | 15 | July 2025 |
| `nl_championship_trends.csv` | Championship highlights by era | era, start_year, end_year, dominant_team(s), theme, pennants, ws_titles | 8 | July 2025 |
| `nl_championship_milestones.csv` | Championship milestones by decade/era | decade, team, milestone, year, detail | 40+ | July 2025 |
| `nl_notable_records.csv` | Key single-season & franchise records | record_type, team, year, value, notes | 19 | July 2025 |
| `nl_team_vs_team_summary.csv` | H2H W-L summary matrix (key matchups) | team1, team2, t1_wins, t2_wins, t1_win_pct | 66 | July 2025 |
| `nl_recent_standings.csv` | Divisional standings 2014–2025 | year, team, division, wins, losses, win_pct, division_pos | ~72 | July 2025 |
| `nl_seasonal_standings.csv` | Full seasonal breakdown w/ division splits | year, team, division, wins, losses, win_pct | TBD | Planned |
| `nl_pennant_winners.csv` | All NL pennant winners 1876–2025 | year, team, ws_result | ~145 | July 2025 |

---

## Schema Conventions

- **Team names**: Canonical NL team names; franchise movements parenthetically (e.g., "Brooklyn Superbas/Dodgers").
- **W-L-T**: Standard wins-losses-ties format; ties excluded from W%.
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
| Baseball Data Hub | https://baseballdatahub.com/seasons/ | 1871–2026 | Secondary |
| SABR Lahman Database | https://sabr.org/lahman-database/ | 1871–2025 | Secondary |
| ESPN (World Series) | https://www.espn.com/mlb/worldseries/history/winners | 1903–present | Tertiary |
| Wikipedia (NL Pennants) | https://en.wikipedia.org/wiki/List_of_National_League_pennant_winners | 1876–present | Tertiary |
| StatMuse | https://www.statmuse.com/mlb | 1876–2026 | Tertiary |

---

## Update Schedule

- **Pre-season**: Update `nl_seasonal_standings.csv` and `nl_recent_standings.csv` with new-season data.
- **Post-season**: Update pennant winners, WS results, and all-time records.
- **Annually**: Refresh from Lahman Database (Dec release) and Baseball Almanac.
