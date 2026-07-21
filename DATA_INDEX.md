# NL Team Trends — Data Index

This file catalogs all data files in the `data/` directory with descriptions and source references.

---

## Data Files

| File | Description | Key Columns |
|------|-------------|-------------|
| `nl_all_time_records.csv` | All-time franchise W-L records for all 15 NL teams (1876–2025) | team, franchise_since, games, wins, losses, win_pct, ws_titles, division_titles, current_division |
| `nl_era_trends.csv` | Era-by-era breakdown of NL competitive landscape | era, start_year, end_year, dominant_team, theme, notable_records |
| `nl_pennant_winners.csv` | Complete NL pennant winners and WS champions 1876–2025 | year, pennant_winner, ws_champion, league_record, notes |
| `nl_recent_season_performance.csv` | Selected recent seasons (2018–2025) with division splits | team, year, wins, losses, win_pct, division_finish, www, losses_in_clin, runs_scored, runs_allowed, notes |
| `nl_h2h_rivalry_summary.csv` | Head-to-head W-L summary for major NL rivalries (1876–2025) | team, teammate, t1_wins, t2_wins, t1_win_pct, games_played, notes |
| `nl_notable_records.csv` | Key franchise and single-season records across NL history | record_type, team, value, year, details |

---

## Data Sources

All data has been compiled from the following verified sources:

1. **Baseball-Reference** — [https://www.baseball-reference.com/leagues/NL/](https://www.baseball-reference.com/leagues/NL/) — Official NL standings and team stats
2. **Baseball Almanac** — [https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml](https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml) — H2H team-vs-team W-L matrix (1876–2026)
3. **StatMuse** — [https://www.statmuse.com/mlb](https://www.statmuse.com/mlb) — All-time franchise W-L records
4. **SABR Lahman Database** — [https://sabr.org/lahman-database/](https://sabr.org/lahman-database/) — Full season-by-season CSV dataset (1871–2025)
5. **Wikipedia** — [https://en.wikipedia.org/wiki/National_League_(baseball)](https://en.wikipedia.org/wiki/National_League_(baseball)) — NL history and evolution
6. **Baseball Almanac Year-by-Year** — [https://www.baseball-almanac.com/yearmenu.shtml](https://www.baseball-almanac.com/yearmenu.shtml) — Annual NL leadership and records
7. **ESPN** — [https://www.espn.com/mlb/worldseries/history/winners](https://www.espn.com/mlb/worldseries/history/winners) — World Series champions
8. **Champs or Chumps** — [https://champsorchumps.us/mlb](https://champsorchumps.us/mlb) — Win%, droughts, streaks
9. **RetroSeasons** — [https://www.retroseasons.com/leagues/nl-national-league/history/records/](https://www.retroseasons.com/leagues/nl-national-league/history/records/) — NL historical records

---

## File Naming Conventions

- All CSV files use Unix line endings (LF)
- Files are UTF-8 encoded
- Column headers are lowercase with underscores
- Win percentages are stored as decimal (e.g., `0.532` = 53.2%)
- `games_behind` is an integer; `0` means division leader
- Historical team names use the names active during their respective eras (e.g., `Philadelphia Athletics` for 1876, not the modern `A's`)

---

## Contributing New Data

To add new data files or update existing ones:

1. Ensure CSV files have a header row and consistent column naming
2. Add entries to this `DATA_INDEX.md` for any new files
3. Update the corresponding section in `README.md` with new findings
4. For season-by-season data, prefer the Lahman Database format (wide table per entity)
