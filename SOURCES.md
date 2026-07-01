# Sources & Methodology

## Primary Sources (★★★★★)
| Source | Coverage | URL | Reliability |
|--------|----------|-----|-------------|
| **Baseball Reference** | NL standings 1876–present | https://www.baseball-reference.com/leagues/NL/ | ★★★★★ |
| **Retrosheet** | Play-by-play and box scores 1898–present | https://www.retrosheet.org/ | ★★★★★ |
| **Lahman Database (SABR)** | Complete MLB stats 1871–present | https://sabr.org/lahman-database/ | ★★★★★ |
| **FBref.com** | Advanced NL season statistics | https://fbref.com/en/comps/34/history/ | ★★★★★ |

## Tier 2 Reference Sources (★★★★☆)
| Source | Coverage | URL | Reliability |
|--------|----------|-----|-------------|
| **Baseball Almanac** | Team-vs-team H2H records 1876–2026 | https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml | ★★★★ |
| **StatsCrew** | Historical NL standings | https://www.statscrew.com/baseball/l-NL | ★★★★ |
| **Wikipedia — All-Time MLB Win-Loss Records** | All-time franchise records | https://en.wikipedia.org/wiki/List_of_all-time_Major_League_Baseball_win%E2%80%93loss_records | ★★★★ |
| **RetroSeasons.com** | NL historical records & league history | https://www.retroseasons.com/leagues/nl/history/records/ | ★★★ |

## Methodology
1. Cross-referenced season-by-season NL standings across Baseball Reference, Retrosheet, and Baseballdatabank
2. Franchise tracking uses modern team names; relocations/name changes are noted in all data files
3. Championship data verified against multiple sources
4. Era classification follows conventional baseball history periods with structural-change markers
5. Win% comparisons account for schedule length variation (60-154 games pre-1884, 162 games modern)

## Key Data Notes
- **1962**: NL expanded to 10 teams | 1969: Two-division format + Wild Card
- **1994**: Season canceled — no NL champion | 1998: Brewers moved AL→NL
- **2005**: Expos relocated as Nationals | 2013: Astros left NL (15 teams) | 2020: COVID 60-game season
- **2022**: 12-team playoff introduced; universal DH adopted

## Python Quick-Start
```python
import pandas as pd
df = pd.read_csv('data/nl_historical_data.csv')
franc = pd.read_csv('data/franchise_summary.csv')
champs = pd.read_csv('nl_champions.csv')
wins = pd.read_csv('nl_team_wins.csv')
errors = pd.read_csv('data/era_analysis.csv')
highlights = pd.read_csv('data/nl_key_performance_highlights.csv')
print(f"Seasons: {df['season'].min()}–{df['season'].max()}")
print(f"Franchises: {franc['franchise'].nunique()}")
print(franc[["franchise", "win_pct", "ws_titles"]].sort_values("win_pct", ascending=False))
```