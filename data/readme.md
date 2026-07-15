# NL Team Trends - Data Directory

This directory contains all source data files for historical National League team performance analysis.

## File Inventory

### Core Data Files
| File | Description | Coverage |
|------|-------------|----------|
| `nl_all_time_records.csv` | All-time franchise win-loss totals by team | 1876–2025 |
| `nl_historical_performance.csv` | Multi-era season-by-season data (NL champions) | 1876–2025 |
| `nl_championship_trends.csv` | Championship highlights organized by era | 1876–2025 |
| `nl_recent_standings.csv` | Full standings with playoff results | 2020–2025 |
| `nl_pennant_winners_recent.csv` | NL pennant winners + WS results | 1995–2025 |
| `nl_notable_records.csv` | Notable single-season and franchise records | All-time |

### References
| File | Description |
|------|-------------|
| `source_references.md` | Detailed source attribution and methodology |

## Usage Notes
- All CSVs use comma delimiters and UTF-8 encoding
- Win% = Wins / Games Played (not all-win percentage)
- Pre-1961 seasons use 154-game schedule; 1961+ uses 162-game schedule
- 2020 season (60 games) is noted as a special case
- Franchise histories include pre-relocation totals
- See `../docs/data_notes.md` for methodology and conventions