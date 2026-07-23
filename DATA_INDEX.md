# NL Team Trends — Data Index

Comprehensive index of all data files in this repository with column definitions and usage notes.

## Data Files

### 1. `data/nl_all_time_franchise_records.csv`
Season-by-season collapse within era.
columns per row:
- table: / data/nl_all_time_records)
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
| `franchise_since` | Year franchise joined NL (includes predecessor cities where applicable) |
| `division` | Current NL division (East, Central, West) |
| `notable_era` | Most historically dominant run or era |

### 2. `data/nl_historical_performance.csv`
Key historical NL championship seasons.
| Column | Description |
|--------|-------------|
| `year` | MLB season year |
| `season_games` | Total games in that season (varies by era) |
| `nl_champion` | NL pennant-winning team |
| `nl_wins` / `nl_losses` | Champion's W-L record that season |
| `nl_win_pct` | Champion's winning percentage |
| `ws_champion` | World Series champion |
| `era` | Baseball history era categorization |
| `notes` | Key historical context |

### 3. `data/nl_recent_championships.csv`
NL championship results from 2015–2025.
| Column | Description |
|--------|-------------|
| `year` | Season year |
| `nl_champion` | NL Championship team |
| `nl_wins` / `nl_losses` | Regular-season record |
| `ws_champion` | World Series winner |
| `ws_result` | Outcome of the World Series |

### 4. `data/nl_team_vs_team_summary.csv`
H2H W-L summary for key NL rivalries (20 matchups). Full 15×15 matrix available on Baseball Almanac.
| Column | Description |
|--------|-------------|
| `team_1` / `team_2` | The two teams in the rivalry |
| `t1_wins` / `t2_wins` | Total wins for each team since 1876 |
| `t1_win_pct` | Team 1's win percentage in the matchup |
| `era_dominant` | Which era was historically dominant for the leading team |


Now you should build out the next Notebook or Untitled script and explore it. Create a `notebooks` directory with Jupyter notebooks, interactive Plotly/PlotlyDash dashboards, or a Python script to fetch the #NlTeamTrends