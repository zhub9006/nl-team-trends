# Data Index & Conventions

This file indexes all data files in the `data/` directory and documents the conventions used.

---

## File Index

| File | Description | Format | Years Covered |
|------|-------------|--------|---------------|
| `nl_pennant_winners.csv` | All NL pennant winners with records, WS results, and franchise aliases | CSV | 1876–2025 |
| `nl_all_time_records.csv` | All-time NL franchise records (wins, losses, winning %, WS titles, droughts) | CSV | 1876–2025 |
| `nl_championship_trends.csv` | Championship highlights and notable seasons by era | CSV | 1876–2025 |
| `nl_notable_records.csv` | Key single-season and franchise records | CSV | 1876–2026 |
| `nl_recent_standings.csv` | Divisional standings for recent NL seasons (2020–2025) | CSV | 2020–2025 |
| `nl_team_vs_team_summary.csv` | H2H W-L summary matrix (key NL matchups) | CSV | 1876–2026 |

---

## Data Conventions

- **Team names**: Canonical NL team names; franchise movements noted in columns
- **W-L format**: Wins-Losses (e.g., `98-55`); no ties in modern data
- **Win%**: `W / (W + L)`, rounded to 3 decimal places
- **Games played**: Derived from W + L; no ties in modern era
- **ERA boundaries**: "1969" = start of division-era; "1876" = NL founding
- **Franchise continuity**: Relocated teams treated as continuous entities

---

## Data Quality Notes

- Pre-1900 data may have gaps in certain statistical categories
- Ties were more common before 1920 and are excluded from winning percentages
- The 1994 season was strike-shortened; no pennant was awarded
- The 2020 season had only 60 games (COVID-19); records are not normalized to 162 games
- 2026 data is incomplete as of mid-season

---

## Planned Additional Data Files

- [ ] `nl_seasonal_standings.csv` — Complete year-by-year NL standings
- [ ] `nl_wild_card_winners.csv` — Wild card/playoff champions by year
- [ ] `nl_divisional_titles.csv` — Division title winners by year
- [ ] `nl_playoff_records.csv` — Head-to-head playoff matchup history
- [ ] `nl_player_stats_by_year.csv` — Annual leading statistical performers
- [ ] `nl_moving_averages.csv` — Smoothed team performance metrics

---

## Contributing

When adding new data files:
1. Add an entry to this index table
2. Document any new conventions
3. Include a brief description of the data source