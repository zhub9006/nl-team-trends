# NL Team Trends — Data Documentation

## Repository Overview

This repository compiles historical National League (NL) baseball team statistics, win-loss records, and performance trends from the founding of the NL in **1876** through the present day.

## Data Files

### `nl_historical_summary.json`
Curated JSON dataset containing:
- All-time franchise win-loss totals (15 teams, 1876–present)
- Best single-season NL records (top 8)
- Recent season highlights (2015–2024)
- Era breakdown with defining features
- Notable anomalies & milestones
- Key aggregate statistics

**Schema:** Each record includes `season`, `team`, `franchise`, `league`, `wins`, `losses`, `win_pct`, `era`, `notes`, and `source` fields.

### `nl_era_breakdown.csv`
CSV file with 7 rows (one per era) containing:
- Era name and date range
- Min/max team count
- Average runs per game
- Top franchise by win%
- Defining historical features

### `nl_franchise_totals.csv`
CSV file with 15 rows (one per active/franchise) containing:
- Franchise name
- All-time wins, losses, win%
- Seasons played
- World Series titles
- Pennants won
- Founding year
- Current status (Active/Defunct)

## Data Sources (Cross-Referenced)

| Source | URL | Coverage |
|--------|-----|----------|
| Baseball Reference – NL Standings | https://www.baseball-reference.com/leagues/NL/ | 1876–present |
| Retrosheet | https://www.retrosheet.org/ | 1898–2024 |
| SABR – Lahman Database | https://sabr.org/lahman-database/ | 1871–2025 |
| Baseball Almanac | https://www.baseball-almanac.com/ | 1876–present |
| StatsCrew | https://www.statscrew.com/baseball/l-NL | 1876–present |
| MLB.com – National League | https://www.mlb.com/national-league | Official records |

## Recommended Analysis Workflow

1. **Load data**: Use `pandas` to read the CSV/JSON files
2. **Clean**: Normalize franchise names (e.g., "Gothams" → "Giants", "Bridegrooms" → "Dodgers")
3. **Merge**: Join with full Lahman Database for deeper stats
4. **Analyze**: Compute rolling Win%, run differentials, era comparisons
5. **Visualize**: Use `matplotlib`/`seaborn`/`plotly` for interactive charts

## Key Considerations

- **Franchise name changes**: Many teams changed names multiple times (e.g., Chicago White Stockings → Colts → Orphans → Cubs)
- **Schedule length**: Varied from 60 to 162 games per season across eras
- **League composition**: NL had 8 teams in early years, now 15
- **Strike seasons**: 1972 (partial), 1981 (split), 1994 (canceled), 2020 (60-game)
- **Expansion waves**: 1892, 1962, 1969, 1993, 1998, 2012

## Usage Example

```python
import pandas as pd
import json

# Load JSON summary
with open('data/nl_historical_summary.json') as f:
    data = json.load(f)

# Load franchise totals
franchises = pd.read_csv('data/nl_franchise_totals.csv')

# Load era breakdown
eras = pd.read_csv('data/nl_era_breakdown.csv')

# Best season by win%
best = franchises.nlargest(5, 'win_pct')
print(best[['franchise', 'win_pct', 'ws_titles']])
```

## License

Data: Public domain (Baseball Reference, Retrosheet, MLB, Lahman Database)
Code & Documentation: CC BY 4.0