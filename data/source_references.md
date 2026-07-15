# NL Team Trends — Source References

## Primary Data Sources

| Source | URL | Coverage | Notes |
|--------|-----|----------|-------|
| Baseball-Reference (NL) | https://www.baseball-reference.com/leagues/NL/ | 1876–present | Year-by-year NL standings & team stats |
| Baseball Almanac | https://www.baseball-almanac.com/ | 1876–present | NL team-vs-team W-L matrices |
| SABR Lahman Database | https://sabr.org/lahman-database/ | 1871–2025 | Full historical team/batting/pitching stats (CSV) |
| Baseball Data Hub | https://baseballdatahub.com/seasons/ | 1871–2026 | Complete season standings archive |
| StatsCrew (NL) | https://www.statscrew.com/baseball/l-NL | 1876–present | NL rosters, standings & leaders |
| StatMuse | https://www.statmuse.com/mlb/ask/most-national-league-titles | 1876–2026 | NL championship leaders & franchise stats |
| OpenIntro MLB Dataset | https://www.openintro.org/data/index.php?data=mlb_teams | Multi-year | ML-ready MLB team data |
| Wikipedia (NL Pennants) | https://en.wikipedia.org/wiki/List_of_National_League_pennant_winners | 1876–present | Complete pennant winner list with WS results |
| ESPN (World Series) | https://www.espn.com/mlb/worldseries/history/winners | 1903–present | World Series champions by year |

## Data Conventions & Caveats

1. **Win%** = Wins / Games Played
2. **Pennants** = League championship awards (pre-Wild Card era); championship titles (1969+)
3. **WS Titles** = World Series championships won as an NL team
4. **All data** through end of 2025 MLB season
5. **Pre-1961 seasons** used 154-game schedule; 1961+ uses 162-game schedule
6. **Shortened seasons** (e.g., 1918: 140 games due to WWI; 1981: split season; 2020: 60 games) are noted as special cases
7. **Tied games** in early NL (pre-1920s) were replayed, so win% is calculated from non-tied games or based on standard W-L record
8. **Division alignment**: 2 divisions (E/W) in 1969; 3 divisions in 1994 with Wild Card; Brewers moved from AL to NL Central in 1998
9. **Interleague play** began in 1997; full schedule in 2023
10. **Team names** reflect the primary name for each era; mergers/relocations noted in the detailed CSV notes column

## Data File Reference

| File | Description | Rows |
|------|-------------|------|
| `data/nl_all_time_records.csv` | All-time franchise win-loss totals by team | 15 teams |
| `data/nl_historical_performance.csv` | Championship-season highlights with era labels | ~56 rows |
| `data/nl_historical_performance_detailed.csv` | Year-by-year NL champion + 2nd place + WS results 1876-2025 | ~150 rows |
| `data/nl_pennant_winners_recent.csv` | NL pennant winners and WS results 1995-2025 | 31 rows |
| `data/nl_championship_trends.csv` | Era-based championship trends and innovations | 8 eras |
| `data/nl_notable_records.csv` | Key single-season and franchise records | 16 records |

## Research Notes

- NL has 15 current franchises; 14 of those have NL history; Brewers joined NL in 1998
- 8 original NL franchises (1876): Chicago, Boston, Providence, Cincinnati, Louisville, Mutual NY, Athletic PA, Hartford
- Tied games were replayed; early NL had many tied games (pre-1920s)
- Most pennants: Dodgers (26), Giants (23), Cardinals (19), Braves (17+18), Cubs (17)
- Most WS titles: Cardinals (11), Giants (8 as SF/NY), Dodgers (8 as LA/NY)
- The 1906 Cubs hold the all-time major league record for winning percentage (.763)
- Cubs' 108-year WS drought (1908-2016) is the longest in North American pro sports history
- Braves' 14 consecutive division titles (1991-2005) is the longest run in any major American pro sport
