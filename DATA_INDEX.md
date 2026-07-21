# NL Team Trends — Data Index (Updated)

## Data Files Added/Updated (July 2025)

| File | Description | Rows | Status |
|------|-------------|------|--------|
| `data/nl_pennant_winners.csv` | Complete NL pennant winners 1876-2025 | 150 | Complete |
| `data/nl_all_time_records.csv` | All-time franchise records | 15 | Updated 2025 |
| `data/nl_all_time_records_extended.csv` | Extended records with franchise notes | 15 | New |
| `data/nl_championship_events.csv` | Key NL championship milestones timeline | 22 | New |
| `data/nl_franchise_droughts.csv` | Franchise drought data | 10 | New |
| `data/nl_divisional_champions.csv` | Division winners 1969-2025 | 114 | New |
| `data/nl_recent_standings.csv` | Divisional standings 2014-2025 | 12 | Updated |
| `data/nl_seasonal_standings.csv` | Full seasonal breakdown | 146 | Complete |
| `data/nl_historical_performance.csv` | Season-by-season champion records | 156 | Updated 2025 |
| `data/nl_h2h_rivalries_detailed.csv` | H2H rivalry matrix with era notes | 20 | Complete |
| `data/nl_team_vs_team_summary.csv` | H2H W-L summary matrix | 12 | Complete |
| `data/nl_championship_trends.csv` | Championship highlights by era | 8 | Complete |
| `data/nl_championship_milestones.csv` | Championship milestones by phenomenon | 16 | Complete |
| `data/nl_notable_records.csv` | Key single-season & franchise records | 16 | Complete |

---

## Supplementary Documents (Added )

| File | Description | Status |
|------|-------------|--------|
| `source_references.md` | Detailed source attribution & methodology notes | New |
| `data/nl_historical_trends_analysis.md` | Comprehensive era-by-era historical trends analysis | New |
| `docs/data_notes.md` | Data methodology, conventions & caveats | New |

---

## Repository Structure

```
nl-team-trends/
├── README.md                              # Research overview & key findings
├── DATA_INDEX.md                          # This file — data index & conventions
├── source_references.md                   # Detailed source attribution
├── requirements.txt                       # Python dependencies
├── data/
│   ├── nl_all_time_records.csv            # All-time franchise records
│   ├── nl_all_time_records_extended.csv   # Extended records with notes
│   ├── nl_championship_events.csv         # Championship milestones timeline
│   ├── nl_franchise_droughts.csv          # Franchise drought data
│   ├── nl_divisional_champions.csv        # Division winners 1969-2025
│   ├── nl_historical_performance.csv      # Season-by-season standings
│   ├── nl_historical_trends_analysis.md   # Era-by-era analysis
│   ├── nl_h2h_rivalries_detailed.csv      # H2H rivalry matrix
│   ├── nl_notable_records.csv             # Key records
│   ├── nl_pennant_winners.csv             # Complete pennant winners 1876-2025
│   ├── nl_recent_standings.csv            # Divisional standings 2014-2025
│   ├── nl_seasonal_standings.csv          # Full seasonal breakdown
│   └── nl_team_vs_team_summary.csv        # H2H W-L summary matrix
├── docs/
│   └── data_notes.md                      # Methodology & caveats
├── visualizations/
│   └── README.md                          # Visualization roadmap
└── notebooks/                             # (planned) analysis notebooks
```

---

## Conventions

- **CSV files**: UTF-8 encoded, comma-separated, with header row
- **Markdown files**: UTF-8, standard markdown with headers and tables
- **Renaming**: Modern franchise names used where possible; historical names noted
- **H2H data**: Includes interleague games since 1997; pre-1997 is intra-NL only
- **Through 2025**: All data current through end of 2025 regular season and postseason

---

## 2025 Championships

- **World Series Champion**: LA Dodgers (beat Toronto Blue Jays 4-3)
- **NL East**: Philadelphia Phillies (96-66)
- **NL Central**: Milwaukee Brewers (97-65)
- **NL West**: LA Dodgers (95-67) — 8th straight NL West title
- **NL Pennant**: LA Dodgers

## Last Updated
July 21, 2025 — 2025 season complete