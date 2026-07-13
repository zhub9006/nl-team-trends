# NL Team Trends - Data Notes & Methodology

## Core Data Sources

1. **Baseball Almanac**: NL team-vs-team win-loss matrix (1876-2026)
2. **Baseball Reference**: Year-by-year NL standings and team stats
3. **StatMuse**: Aggregate all-time team statistics
4. **Grokipedia**: Franchise win-loss rankings through 2025
5. **Baseball Data Hub**: All MLB seasons 1871-2026 directory

## Franchise Continuity

When a team relocates or changes name, historical records merge:
- Boston Red Stockings → Boston Braves → Milwaukee Braves → Atlanta Braves
- New York Giants (1883-1957) → San Francisco Giants (1958-)
- Brooklyn Dodgers → Los Angeles Dodgers (1958)
- Montreal Expos → Washington Nationals (2005)
- Florida Marlins → Miami Marlins (2012)

## Conventions

- **Ties**: Excluded from win% calculations per MLB rules
- **Interleague Play**: Introduced 1997; included in all-season totals
- **Postseason**: Regular-season only; tracked separately in pennant CSV
- **Pre-1900 ties**: May be approximate due to inconsistent records

## Data Timestamps

- `nl_team_records.csv`: All-time records through 2025 regular season
- `nl_pennant_winners.csv`: Pennant data from 1876 to 2025 NLCS
- `nl_team_vs_team.csv`: Subset of full 15x15 Baseball Almanac matrix
- `nl_key_seasons.csv`: Notable single-season franchise performances

## Known Limitations

- Early NL records (1876-1882) may have gaps from team folding/reabsorption
- 1994 postseason cancelled (player strike); reflected in pennant data
- 2020 season shortened to 60 games; win% not directly comparable
- Complete 15x15 H2H matrix available from Baseball Almanac source