# Contributing to NL Team Trends

Thank you for your interest in contributing to this historical National League research project! This repository compiles NL team performance data, win-loss records, season trends, and championship history from 1876 to present.

## How to Contribute

### Data Contributions
- **Fix errors**: Open an issue with the source URL for any data discrepancy.
- **Add records**: Welcome additional season rows to `nl_historical_performance.csv` and milestone data to `nl_all_time_records.csv`.
- **Expand H2H**: The full 15×15 matrix from Baseball Almanac can be added to `data/nl_team_vs_team_full.csv`.
- **Update trends**: Extend or update `nl_recent_trends_2000_2024.csv` with newer date ranges.

### Analysis Contributions
- **Jupyter Notebooks**: Add analysis notebooks to `notebooks/` covering specific trends or questions.
- **Visualization Scripts**: Add Python scripts to `scripts/` for reproducible charting.
- **Statistical Models**: If you develop regression or ML models for NL performance prediction, share them here.

### Code Style
- Use Python 3.10+ with type hints where practical.
- Follow PEP 8 conventions.
- Document functions with docstrings.
- Include sample output or charts with new analysis scripts.

### Review Process
1. Fork the repository and create a feature branch.
2. Make your changes with clear commit messages.
3. Open a pull request describing the changes and their purpose.
4. At least one review approval required before merge.

## Data Entry Standards
- Always use UTF-8 encoding for CSV files.
- Use snake_case for column names.
- Use `N/A` for missing data.
- Keep win percentages as decimals with 3 places (e.g., 0.535).
- Separate multiple values in a single cell with semicolons.

## Key Data Sources
| Source | URL | Coverage |
|--------|-----|----------|
| Baseball-Reference (NL) | https://www.baseball-reference.com/leagues/NL/ | 1876–present |
| Baseball Almanac H2H | https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml | 1876–2026 |
| Baseball Almanac (Yearly) | https://www.baseball-almanac.com/yearmenu.shtml | 1876–present |
| SABR Lahman Database | https://sabr.org/lahman-database/ | 1871–2025 |
| Baseball Data Hub | https://baseballdatahub.com/seasons/ | 1871–2026 |
| StatMuse | https://www.statmuse.com/mlb | 1876–2026 |
| Retrosheet | https://www.retrosheet.org/ | 1871–present |

## Questions?
Open an issue and tag it with the `question` label.