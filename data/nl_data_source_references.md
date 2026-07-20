# NL Team Trends Data — Source References & Methodology

## Research Completed: July 2026

All data sources verified and cross-referenced as of July 2026. Data includes NL franchise records, head-to-head teams, championship data, and season-by-season performance metrics.

## Primary Sources (Verified July 2026)

| Source | URL | Data Found | Key Value |
|--------|-----|------------|-----------|
| Baseball Almanac (H2H) | https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml | NL H2H W-L matrices 1876-2026 | 15x15 matrix with franchise-vs-franchise totals |
| Baseball Almanac (Year-by-Year) | https://www.baseball-almanac.com/yearmenu.shtml | NL leadership by year | Pennant winners + fabulous feats by season |
| StatMuse NL Championships | https://www.statmuse.com/mlb | NL 12-team franchise grid | WS titles, W/L/G percent by franchise |
| StatMuse All-Time %s | https://www.statmuse.com/mlb | 30-team totals | W/L/G for all active MLB franchises |
| SABR Lahman Database | https://sabr.org/lahman-database/ | Complete team stats 1871-2025 | Free CSV downloads of all team/batting:pitching data |
| Baseball-Reference (NL) | https://www.baseball-reference.com/leagues/NL/ | NL standings index 1876+ | Official year-by-year NL team stats |
| Baseball Data Hub | https://baseballdatahub.com/seasons/ | Season-by-season archive | 1871-2026 full standings & stats |
| Retrosheet | https://www.retrosheet.org/ | Historical game data | Box scores, team records, play-by-play from 1871 |
| OpenIntro MLB Dataset | https://openintro.org/data | R-format ML datasets | Subset of Lahman data for ML/statistical use |
| Everything Explained | https://everything.explained.today | All-time W-L by franchise | 30-team table with W/L/Win%/G totals |
| Linger & Look | https://lingerandlook.com/~names/baseballstandings.php | Year-by-year standings | 1901-present with managers + subtotals |
| ESPN WS History | https://www.espn.com/mlb/worldseries/history/winners | WS champion results | 1903-present with year, winner, score, Series record |
| Grokipedia (MLB W-L Records) | https://grokipedia.com/page/List_of_all-time_Major_League_Baseball_win%E2%80%93loss_records | All-time franchise records | Expanding to 143-season franchise totals |
| SportsGearDaily (Best MLB Record) | https://sportsgeardaily.com/rules/who-has-the-best-record-in-the-major-league-baseball | Franchise win rankings | Top 5 by total wins + winpct through 2024 |
| Wikipedia (NL Pennants) | https://en.wikipedia.org/wiki/List_of_National_League_pennant_winners | Complete pennant winners | 1876-present; champtionship & WS results |
| Champs or Chumps | https://champsorchumps.us/mlb | Win% rankings & droughts | Win% history, droughts, streaks, postseason records |
| Data Hub (re:full annual) | https://www.baseballdatahub.com/ | Complete season standings 1871-2026 | Pulls from Retrosheet + Sports Reference aggregates |

## Data Conventions

- **Win%** = Wins / (Wins + Losses) — ties excluded as rare post-1920
- **Pre-1961** = 154+ games per season; 1962+ = 162 games
- **2020** = 60 games (COVID season) — not comparable to standard seasons
- **Split seasons in 1892 & 1981** handled with half-designators
- **Milwaukee Brewers** moved from AL→NL Central in 1998 (AL stats excluded from NL totals)
- **Washington Nationals** = Montreal Expos 1969-2004 + Washington 2005+ total
- **LA Dodgers** = Brooklyn Adventurers 1884-1957 + LA Dodgers 1958+ total
- **SF Giants** = New York Giants 1883-1957 + SF Giants 1958+ total
- **Atlanta Braves** = Boston Red Stockings 1871-1952 + Milwaukee Braves 1953-1965 + Atlanta Braves 1966+ total

## Methodology Notes

1. Franchise continuity: All records treated as continuous entities regardless of relocations
2. Pre-W data: 1903 = first World Series; 1876-1902 = NL pennant winners only (no WS)
3. NL pennants: Counted per league championship once per season (including split season designations)
4. 1994 strike: Season voided; no NL championship awarded
5. H2H data: Aggregated from Baseball Almanac 1876-2026 for all NL team vs NL team matchups
6. Longest streaks by winning%: Cardinals (11 WS), Dodgers (26 pennants), Braves (14 div titles)