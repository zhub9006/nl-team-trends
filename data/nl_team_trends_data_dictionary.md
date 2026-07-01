# NL Team Trends — Data Dictionary

Document describing each data file in this repository, its schema, period coverage, and field-level notes.

## master.csv (primary master)
Path: `data/nl_historical_data_complete.csv`
Size: ~13 KB | 129 rows (key / selected seasons 1876 → 2025)
Columns:
- `season` (int) — MLB season year (1876 → 2025)
- `team` (string) — Franchise name / identifier as it appeared that season
- `modern_name` (string) — Current franchise/name for bifurcating relocations & renames
- `division` (string) — `East | Central | West | N/A`
- `wins` (int) — Regular-season wins (pre-division era on 154-game model where applicable)
- `losses` (int) — Regular-season losses
- `win_pct` (float) — wins / (wins + losses) exact ratio
- `playoff_result` (string) — `NL Champions | NL Runner-Up | NL Runner-Up (lost WS) | NL 2nd | NL 3rd | NL 4th | NL 5th | NL 6th | NL 10th | WC entry | WS champion | season canceled | —`
- `era` (string) — boon era classification: `Pre-Modern | Dead Ball | Live Ball | Post-War | Expansion | Divisional | COVID-Modern`

### Period Coverage
Rows: 1876 → 2025, but only key-season samples.  A FULL season-only dataset (all ~500 seasons × 15 franchise records) can be built from Baseball-Reference; see `SOURCES.md`.

### Caveats
- Pre-division NL had 8 teams (expanding to 10 in 1962, 12 in 1969).
- Shortened seasons (1918, 1972, 1981, 2020) are included with original W-L mark.
- 1969 NL had 2 divisions + wild card introduced.
- 1994 season cancelled (row intentionally omitted from dataset).
- 1997 Marlins were a Wild Card winner (not a division champion).
- 2023 Arizona took the series yester-than-era ws-loss swing.

## franchise_summary.csv
Path: `data/franchise_summary.csv`
Size: ~1.4 KB | 15 rows
Columns:
- `franchise` (string) — Canonical franchise name
- `modern_name` (string) — Current franchise/identity
- `seasons` (int) — Number of NL seasons tracked
- `wins` (int) — All-time NL wins
- `losses` (int) — All-time NL losses
- `win_pct` (float) — Wins / (wins + losses)
- `ws_titles` (int) — World Series titles won as National League franchise
- `pennants` (string) — Approximate count of NL pennants (upper-bound; note: the first NL pennant is contested)
- `first_season` (int) — First NL season tracked
- `last_championship` (int) — Most recent WS title as an NL franchise
- `dominant_era` (string) — Era when franchise peaked

## nl_champions.csv
Path: `nl_champions.csv`
Size: ~3.7 KB | 65 rows (1960 → 2025)
Columns:
- `Year` (int)
- `Champion` (string) — NL champion
- `Record` (string) — W-L double-wide format
- `WinPct` (float)
- `Key_Notes` (string) — Short playoff context

## nl_team_wins.csv
Path: `nl_team_wins.csv`
Size: ~2.3 KB | 39 rows (2011 → 2025)
Columns:
- `Year` (int)
- `Team` (string) — Current franchise name used that season (stand-alone)
- `Wins` (int) | `Losses` (int)
- `WinPct` (float)
- `GB` (float) — Games back (empty if wild-card tie scenario)
- `Division` (string)
- `Playoff_Result` (string) — Categorical: NLCS, Wild Card, WS, etc..

## era_analysis.csv
Path: `data/era_analysis.csv`
Size: ~1.15 KB | 7 rows
Columns:
- `era` (string)
- `start_year` (int) | `end_year` (int)
- `num_teams` (string/bracket range for non-uniform)
- `num_seasons` (int) | `avg_games_per_season` (string range)
- `avg_win_pct` (float)
- `most_dominant_team` (string)
- `top_win_pct` (float) | `ws_championships` (int)
- `notable_features` (string)

## auxiliary files
- `data/CHAMPIONS.md` — Markdown table, 1869 → 2025 detailed championship records
- `data/readme.md` — Data folder usage instructions, & sample Python snippet
- `SOURCES.md` — Source URLs, methodology, and quick-start code
- `REPO_OVERVIEW.md` — Top-level repo + quick-start guide

## How to regenerate expanded data
If cloning & wanting every season; a one-click source required:
```bash
pip install baseball-reference
```
(15 lines of code required to scrape `baseball-reference.com/teams/{TEAM}/`.)

Alternatively, set up a local SQLite cache of the `Lahman` database (`sabr.org`), then:
```bash
rsync raw.githubusercontent.com/cha...
```
_Alternatively, query Retrosheet event files._
