# Data Files Index - nl-team-trends

## Data Files in data/

| File | Description | Key Data Points | Source |
|------|-------------|-----------------|--------|
| nl_historical_performance.csv | Year-by-year NL standings 1876-2026 | Champion, 2nd place, WS result, era | Baseball Almanac + StatMuse + Wikipedia |
| nl_all_time_records.csv | All-time franchise records (all 15 NL teams) | W, L, Games, Win%, WS titles, division | StatMuse NL Championships + All-Time %s |
| nl_notable_records.csv | Key records by category | 30+ record categories per franchise | StatMuse + Baseball Almanac + Champs or Chumps |
| nl_championship_trends.csv | Championship trends by era | WC/pennant totals, responsive teams | Surprise Sports + Wikipedia NL Pennants |
| nl_notable_seasons.csv | Significant seasons (1876-2025) | Season milestones, records, context | Baseball Almanac NL Year-by-Year + StatMuse |

## Data Conventions
- **Win%**: Wins / Games Played (not rounded to .500)
- **Pre-1903 pennants**: NL Championship only (no World Series existed until 1903)
- **Franchise totals**: Include pre-relocation data (SF Giants = NY Giants + SF Giants)
- **2026 status**: Ongoing season — Stats reflect real-time data through latest completed games
- **Split seasons**: 1892 & 1981 handled with first-half / second-half designators
- **Milwaukee Brewers**: Moved from AL to NL Central in 1998 (AL era blamed separately)
- **Washington Nationals**: Includes Montreal Expos (1969-2004 relocation merged)
- **Los Angeles Dodgers**: Includes Brooklyn/LA franchise every game since 1884

## How to Use These Files
- **Beginning analysts**: Start with nl_all_time_records.csv for the full 15 NL team comparison
- **Era researchers**: Use nl_championship_trends.csv for decade-level dominance analysis
- **Recent performance**: nl_historical_performance.csv has the last 150 seasons of NL historical win-loss
- **Milestone reasearchers**: nl_notable_records.csv covers all records with contextual notes
- **Deep dives**: nl_notable_seasons.csv has season-specific historic details with year-by-year granularity

## External Data Cross-References
- [SABR Lahman Database](https://sabr.org/lahman-database/) - All 15 NL franchise CSV datasets
- [Baseball Almanac NL Team-vs-Team](https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml) - Full 15×15 W-L matrix for all seasons
- [StatMuse NL Commands](https://www.statmuse.com/mlb) - Real-time NL championship leader queries
- [Champs or Chumps](https://champsorchumps.us/mlb) - Drought streaks, percentage analysis

## Repository Structure
```
nl-team-trends/
├── README.md                    ← Research overview & key findings
├── DATA_PLACEHOLDER.md          ← This file: data index & conventions
├── source_references.md         ← Detailed source attribution list
├── requirements.txt             ← Python dependencies for analysis
├── data/
│   ├── nl_historical_performance.csv      ← Year-by-year NL champion, 2nd place, WS outcomes (1876-2025)
│   ├── nl_all_time_records.csv            ← All-time franchise records W/L/G/%
│   ├── nl_notable_records.csv             ← Key single-season & franchise records
│   ├── nl_championship_trends.csv         ← Championship highlights by era
│   └── nl_notable_seasons.csv             ← Notable seasons with key statistics
├── docs/
│   └── data_notes.md                   ← Methodology & caveats
├── visualizations/
│   └── README.md                     ← Visualization roadmap & tools
├── notebooks/                        ← Jupyter notebooks for analyses
├── scripts/                        ← Data collection & processing scripts
└── visualizations/                  ← Charts, heatmaps & dashboards
```