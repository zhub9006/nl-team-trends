# Data Files Index — nl-team-trends

## Data Files in `data/`

| File | Description | Key Data Points | Source |
|------|-------------|-----------------|--------|
| `nl_historical_performance.csv` | Year-by-year NL standings 1876-present | Champion, 2nd place, W-L, Win%, WS result, era | Baseball+StatMuse+Wikipedia |
| `nl_all_time_records.csv` | All-time franchise records (15 NL teams) | W, L, Games, Win%, WS titles, division | StatMuse NL + All-Time %s |
| `nl_pennant_winners.csv` | All NL pennant winners 1876-2025 | Year, champion, W-L, Win%, WS result, era | Wikipedia NL Pennants + Baseball Almanac |
| `nl_championship_trends.csv` | Championship trends by era | Era-level pennants, WS totals, dominant teams | Surprise Sports + Wikipedia NL Pennants |
| `nl_notable_records.csv` | Key records by category | 30+ record categories per franchise | StatMuse + Baseball Almanac + Champs or Chumps |
| `nl_h2h_rivalries_detailed.csv` | Detailed H2H rivalry data | Win% in head-to-head for 24 key pair matchups | Baseball Almanac NL H2H (1876-2026) |

## Data Conventions
- **Win%** = Wins / Games Played
- **Pre-1903 pennants** = NL Championship only
- **Franchise totals** include pre-relocation data
- **Split seasons** (1892 & 1981) handled with half-designators
- **Milwaukee Brewers**: Moved AL→NL in 1998; AL stats excluded from NL totals
- **Washington Nationals**: Expos (1969-2004) + DC (2005+)
- **LA Dodgers**: Brooklyn (1884-1957) + LA (1958+)
- **SF Giants**: NY Giants (1883-1957) + SF Giants (1958+)

## Companion Docs
- `README.md` — Research overview with key findings
- `source_references.md` — Source attribution for every data point
- `docs/data_notes.md` — Methodology, caveats, Python examples
- `visualizations/README.md` — Visualization roadmap & tools
- `scripts/data_loader.py` — Python utility to load and explore data

> NOTE: All CSV and MD files are in the `data/` directory. For full H2H 15×15 matrix, refer to Baseball Almanac NL H2H page. For season-level raw data (full Lahman-derived), download from SABR.