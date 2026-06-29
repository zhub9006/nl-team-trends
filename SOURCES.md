# Sources & Methodology

## Research Sources

### Primary Sources

| Source | Coverage | URL | Reliability |
|--------|----------|-----|-------------|
| Baseball Reference | NL standings, team stats 1876–present | https://www.baseball-reference.com/leagues/NL/ | ★★★★★ |
| Retrosheet | Box scores and play-by-play 1898–present | https://www.retrosheet.org/ | ★★★★★ |
| Lahman Database (SABR) | Complete MLB stats 1871–present | https://sabr.org/lahman-database/ | ★★★★★ |
| Baseball Almanac | Team-vs-team H2H records 1876–present | https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml | ★★★★ |
| FBref.com | Advanced NL season statistics | https://fbref.com/en/comps/34/history/ | ★★★★★ |
| MLB.com | Official NL news and standings | https://www.mlb.com/national-league | ★★★★ |

### Secondary Sources

- **Baseball Data Hub** — All MLB seasons browsable
- **StatsCrew** — Historical standings
- **Linger & Look** — Year-by-year NL standings
- **Wikipedia** — NL pennant winners, franchise histories
- **Baseball Hall of Fame** — Franchise milestones
- **Sporting Life** — English National League tables
- **FBref.com** — English NL season history

## Key Research Findings

### Competitive Balance by Era (MLB NL)
1. **Low (1876–1920):** Few teams, dynasties lasted years
2. **Moderate (1920–1968):** Cardinals, Giants, Dodgers forged rivalries
3. **High (1969–2005):** Expansion + Wild Card increased parity
4. **Lower (2006–present):** Dodgers supremacy; more equitable remaining field

### Dominant Franchises Summary
- **Cardinals** — 11 WS titles, most successful NL franchise historically
- **Giants** — 8 WS titles across NY/SF eras; 2010–2014 dynasty
- **Dodgers** — 7 WS titles, 25+ pennants; most pennants in franchise history
- **Braves** — 4 WS titles; 14 consecutive division titles (1991–2005)
- **Reds** — Big Red Machine (.610 Win%); 5 titles in concentrated era
- **Mets** — Most productive expansion franchise; perennial contender

### Champion Win% Range (1960–2025)
- **Highest:** .717 (2020 Dodgers, shortened season)
- **Lowest:** .516 (2006 Cardinals), .519 (2023 D-backs)
- **Trend:** WC era sees lower Win% champions due to broader playoff field

### Franchise H2H (Sample)
| Matchup | Win Ratio | Leader |
|---------|-----------|--------|
| Cardinals vs Cubs | ~41-49 | Cubs |
| Giants vs Dodgers | ~56-43 | Giants (incl. NY) |
| Mets vs all NL | 1034-885 | Mets |
| Dodgers vs all NL | 2781-2071 | Dodgers |

## Data Validation

- Cross-reference franchise totals with Baseball Reference and Retrosheet
- For head-to-head data: use Baseball Almanac
- Flag discrepancies > 0.5% win differential between sources in GitHub Issues
- Era classifications based on major structural changes (expansion, strike, format changes)

## How to Contribute

1. Pull from primary sources (Baseball Reference, Retrosheet, Lahman)
2. Add new seasons to `nl_team_wins.csv` and `nl_champions.csv` annually
3. Update era classifications if structural changes occur
4. Open issues for data discrepancies found across sources