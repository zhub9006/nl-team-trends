# NL Team Trends — GitHub Repository

Reposistory: https://github.com/zhub9006/nl-team-trends

Created by: zhub9006
Purpose: Research historical National League performance data and team trends across past MLB seasons

## Quick-Start

```bash
git clone https://github.com/zhub9006/nl-team-trends.git
cd nl-team-trends
```

## Key Data Files

| File | Columns | Period | Seasons |
|------|---------|--------|---------|
| `nl_champions.csv` | Year, Champion, Record, WinPct, Key Notes | 1960–2025 | 65 |
| `nl_team_wins.csv` | Year, Team, Wins, Losses, WinPct, GB, Division, Playoff_Result | 2011–2025 | 39 |
| `data/nl_historical_data.csv` | season, team, modern_name, division, wins, losses, win_pct, playoff_result, era | 1876–Present (selected key seasons) | 129 |
| `data/nl_historical_data_complete.csv` | season, team, modern_name, division, wins, losses, win_pct, playoff_result, era | 1876–2025 (all key seasons) | ~0 (placeholder for expansion) |
| `data/franchise_summary.csv` | franchise, modern_name, seasons, wins, losses, win_pct, ws_titles, pennants, first_season, last_championship, dominant_era | 1 files | 1 rows x 15 |
| `data/era_analysis.csv` | era, start_year, end_year, num_teams, num_seasons, avg_games_per_season, avg_win_pct, most_dominant_team, top_win_pct, ws_championships, notable_features | 7 eras | 7 rows |
| `data/CHAMPIONS.md` | md | 1869–2025 | 126 lines |
| `data/readme.md` | md | all | 58 lines |

## Visualizations (to build)

- NL Era Win% Heatmap
- Franchise Win-Loss Trend Lines
- Championship Drought Chart
- ERA Win% Correlation
- Division Dominance Maps