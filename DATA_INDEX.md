# NL Team Trends — Data Index

Comprehensive index of all data files in this repository with column definitions and usage notes. Updated July 2026.

## Data Files

### 1. `data/nl_all_time_records.csv`
All-time franchise win-loss records for every NL team through 2025.
| Column | Description |
|--------|-------------|
| `team` | NL franchise name (relocations included in continuity) |
| `ws_titles` | Number of World Series championships won |
| `games` | Total regular-season games played through 2025 |
| `wins` | Total regular-season wins |
| `losses` | Total regular-season losses |
| `win_pct` | Win percentage (wins / total games) |
| `last_ws_title` | Year of most recent World Series title |
| `last_pennant` | Year of most recent NL pennant |
| `division` | Current NL division (East, Central, West) |
| `franchise_since` | Year franchise joined NL (includes predecessor cities where applicable) |
| `notes` | Key historical notes about franchise |

### 2. `data/nl_season_by_year_full.csv` ⭐ NEW
Comprehensive season-by-season NL championship data from 1876 to 2025.
| Column | Description |
|--------|-------------|
| `year` | MLB season year (1876-2025) |
| `team` | NL pennant-winning team |
| `games` | Total games played in that season |
| `wins` | Pennant winner's regular-season wins |
| `losses` | Pennant winner's regular-season losses |
| `win_pct` | Pennant winner's winning percentage |
| `division` | Division of pennant winner |
| `ws_result` | WS outcome: Won WS, Lost WS, No WS, or No Champion |
| `pennant` | Yes/No indicator |
| `notes` | Key historical context, records, and storylines |

**Usage**: Load with pandas to analyze NL champion records by era, compare winning percentages across decades, and track franchise trajectories over 150 years. 150 rows covering every NL commissioner to 2025.

### 3. `data/nl_era_win_pct_comparison.csv` ⭐ NEW
Cross-era win percentage comparison and championship trends across 9 historical eras.
| Column | Description |
|--------|-------------|
| `era` | Era period label |
| `start_year` | First year of era |
| `end_year` | Last year of era |
| `dominant_team` | Most successful team in that era |
| `pennant_count` | Number of NL pennants won in era |
| `ws_titles` | Number of WS titles won in era |
| `win_pct_range` | Range of winning percentages across era |
| `num_champions` | Number of different NL champions in era |
| `theme` | Key theme or story of the era |
| `key_insight` | Summary insight about that era |

**Usage**: Compare competitive balance across eras; track which teams dominated each period; analyze how schedule changes (60→154→162 games) affected win rates.

### 4. `data/nl_historical_performance.csv`
Key historical NL championship seasons highlighting record-setting performances.
| Column | Description |
|--------|-------------|
| `year` | MLB season year |
| `team` | NL pennant winner |
| `record` | W-L record string |
| `games` | Total games played |
| `wins` / `losses` | Regular-season record |
| `win_pct` | Winning percentage |
| `division` | Division |
| `league` | NL |
| `ws_won` | Yes if won WS |
| `ws_result` | WS result |
| `pennant` | Yes if pennant winner |
| `notes` | Context and records |

### 5. `data/nl_championship_trends.csv`
Championship highlights organized by era.
| Column | Description |
|--------|-------------|
| `era` | Era name/label |
| `start_year` | First year of era |
| `end_year` | Last year of era |
| `dominant_team` | Dominant team(s) in that era |
| `pennant_count` | Number of pennants |
| `ws_titles` | Number of WS titles |
| `theme` | Historical theme of the era |

### 6. `data/nl_notable_records.csv`
Notable single-season and franchise records in NL history.
| Column | Description |
|--------|-------------|
| `category` | Type of record |
| `record_holder` | Team holding the record |
| `value` | Record value |
| `year` | Year the record was set |
| `details` | Additional context |

### 7. `data/nl_recent_standings.csv`
Divisional standings for 2014-2025 with Wild Card information.
| Column | Description |
|--------|-------------|
| `year` | Season year |
| `NL_Central_winner` | NL Central division winner |
| `NL_Central_W` | Central winner's record |
| `NL_East_winner` | NL East division winner |
| `NL_East_W` | East winner's record |
| `NL_West_winner` | NL West division winner |
| `NL_West_W` | West winner's record |
| `Wild_Card_1` | First Wild Card team |
| `Wild_Card_2` | Second Wild Card team |
| `Notes` | Seasonal context |

### 8. `data/nl_pennant_winners_recent.csv`
NL pennant winners from 1995-2025 with WS results.
| Column | Description |
|--------|-------------|
| `year` | Season year |
| `champion` | NL pennant winner |
| `record` | Regular-season W-L record |
| `division` | Division of champion |
| `ws_opponent` | WS opponent (AL team) |
| `ws_result` | WS outcome (W/L) |
| `notes` | Key context for each year |

### 9. `data/nl_team_vs_team_summary.csv`
H2H W-L summary for key NL rivalry matchups (20 pairs plus cross-city).
| Column | Description |
|--------|-------------|
| `team_1` | First team in matchup |
| `team_2` | Second team in matchup |
| `t1_wins` | Team 1 total wins in H2H |
| `t2_wins` | Team 2 total wins in H2H |
| `total_games` | Total games played in rivalry |
| `t1_win_pct` | Team 1 winning percentage |
| `era_dominant` | Era of dominance |
| `rivalry_type` | Nature of the rivalry |

## Data Methodology Notes

1. **Franchise continuity**: Relocations (Brooklyn→LA, NY Giants→SF, Montreal→Washington) INCLUDE all historical data. Chicago Cubs count includes Chicago White Stockings days (1876).
2. **H2H data**: Baseball Almanac includes 15×15 H2H W-L matrices for all 15 NL teams vs all 15 NL teams (225 unique matchups). Summary file covers top rivalry matchups.
3. **Schedule eras**: Variable schedule lengths (60-154 games pre-1962, 162 from 1962-present, 60 in 2020 COVID season). Win percentages provided for cross-era comparison.
4. **Interleague play**: Beginning in 1997 and permanent since 2023. H2H data is NL-only; interleague results tracked separately.
5. **Championship verification**: All results verified against ESPN World Series data and Baseball-Almanac records.

## Data Source Attribution
Primary sources: Baseball-Reference, Baseball Almanac, SABR Lahman Database, StatsCrew, StatMuse, Baseball Data Hub, Retrosheet, Everything Explained, Linger & Look, ESPN, Wikipedia, MLB.com, OpenIntro.