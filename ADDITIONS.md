## Addition History (July 2026 Branch: enrich-h2h-matrix-and-div-titles)

New data files added beyond the original 12 CSV files:

### 1. `nl_h2h_detail.csv`
- 40+ team-vs-team matchup rows extracted from Baseball Almanac (1876-2026) NL Team-vs-Team matrix
- Column flags: `confirmed` (direct from BA source) or `NO` (estimated/cross-ref)
- Edge cases documented: franchise re-locations, era transitions, NL expansion
- [Source: Baseball Almanac NL Team-vs-Team 1876-2026](https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml)

### 2. `nl_divisional_titles_recent.csv`
- Year-by-year NL division title summaries 2011-2025 (88 rows across 3 divisions × 15 seasons)
- Columns: year, division, team, record, WS_result, era_note
- Key patterns documented: LAD 8 consecutive NL West titles (2018-2025), Braves 6 consecutive NL East titles (2018-2023), Cardinals resurgent 2022
- [Source: MLB.com "Teams with most division titles" + Baseball Reference](https://www.mlb.com/news/mlb-teams-with-most-division-titles)

### Research Sources Used
All original sources verified in the repository README remain valid:
| Source | NL Coverage | Data Contributed |
|--------|-------------|-----------------|
| Baseball Almanac (H2H) | 1876-2026 | Team-vs-team W-L matrix |
| Baseball Almanac (year-by-year) | 1876-2026 | Raw pennant/data validation |
| MLB.com (division titles) | 1969-2025 | Division title counts & recent seasons |
| Baseball Data Hub | 1871-2026 | Season-by-season archive |
| Baseball-Reference (NL) | 1876-2026 | Official standings & team stats |
| SABR/Lahman Database | 1871-2025 | Free CSV download link |
| ESPN (World Series history) | 1903-2025 | WS results & champions |
| Wikipedia (NL Pennant Winners) | 1876-2025 | Pennant winner list |