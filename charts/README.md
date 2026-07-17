# Charts Directory

Output directory for generated visualization charts.

## Naming Convention

`charts/<year>-<chart_type>_<descriptor>.png`

## Examples

- `2025-pentant_winners_by_franchise.png`
- `2025-162_game_win_pct_comparison.png`
- `2025-championship_drought_timeline.png`
- `2025-h2h_w_l_heatmap.png`

## Generating Charts

```bash
pip install -r requirements.txt
python scripts/data_loader.py
```

## Planned Chart Types

| Chart | Description | Data Source |
|-------|-------------|-------------|
| Pennant Winners by Franchise | Bar chart of pennant titles per team | nl_pennant_winners.csv |
| 162-Game Win% Comparison | Top 10 teams by win% | nl_all_time_records.csv |
| Championship Drought Timeline | Years since last WS title | nl_all_time_records.csv |
| H2H W-L Heatmap | 15×15 team-vs-team matrix | nl_team_vs_team_summary.csv |
| NL West Dominance | Dodgers' consecutive titles | nl_recent_standings.csv |
| Era-Based Win% Comparison | Grouped bar by era | nl_pennant_winners.csv |
| Run Differential Over Time | Year-by-year run differential | nl_recent_standings.csv |
| Division Dominance | Stacked area by division | nl_recent_standings.csv |
