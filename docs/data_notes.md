# Methodology, Conventions & Caveats

## Data Methodology

- All data sourced from public baseball reference archives and historical databases.
- Franchise-wide win-loss totals include all NL seasons from founding year through present.
- Season-by-season data focuses on division winners, pennant winners, and key performance metrics.
- Park factors, ERA, and advanced metrics are included where reliably available.

## Key Conventions

1. Schedule length: Pre-1893 seasons varied (mostly 120-140 games). 1893-1961 seasons had 154 games. 1962-present (mostly) 162 games. Some shortened seasons noted (1995 strike, 2020 COVID, 1994 strike).
2. Division alignment: NL had East/West from 1969-1993. Central division added 1994. 2024 realignment: 15 teams evenly split.
3. Franchise naming: Current names used for all entries; historical names cross-referenced in notes.
4. Pennant counting: Includes both pre-WS (pre-1903) and modern pennants.

## Known Limitations

- Pre-1900 data may have incomplete records or conflicts between sources.
- Early franchise totals vary across sources depending on whether preseason/exhibition games are included.
- Park factors are only available from roughly 1950 onward with reliable normalization.
- The 1994 season is incomplete; division winners shown but no postseason results.
- 2020 data is from a 60-game season — use caution comparing to full 162-game seasons.

## Suggested Analyses

- EDA on pennant frequency by team and era
- Win% trends over decades (moving averages)
- Championship drought analysis (time between titles)
- Head-to-head matchup win rates over time
- Correlation between spring training performance and regular season outcomes
- Park factor impact on win totals by decade
- Subdivision analysis: How often do division winners also win the WS?

## Visualization Roadmap

| Chart | Type | Data File | Insight |
|-------|------|-----------|---------|
| Win% by decade | Heatmap | nl_seasonal_standings.csv | Dominant eras & decline trends |
| Pennant timeline | Gantt chart | nl_pennant_winners.csv | Championship streaks & gaps |
| Franchise wins bar chart | Horizontal bar | nl_all_time_records.csv | Giants, Dodgers, Cards lead |
| H2H matrix | 16×16 heatmap | nl_team_vs_team_summary.csv | Rivalry intensity visualization |
| Drought chart | Strip plot | nl_championship_milestones.csv | Time between titles |
| Moving average trend | Line chart | nl_historical_performance.csv | League parity over time |
| Season-by-season rollout | Faceted line | nl_seasonal_standings.csv | Individual franchise trajectories |