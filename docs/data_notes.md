# Data Notes — Methodology, Conventions & Caveats

## Methodology

All data in this repository was compiled from the following primary sources (see [source_references.md](source_references.md) for full attribution):

1. **Baseball Almanac** — Primary source for team-vs-team head-to-head W-L matrices and season-by-season standings (1876–2026)
2. **Baseball-Reference (NL)** — Official year-by-year NL standings and team statistics (1876–present)
3. **Baseball Data Hub** — Complete season standings & stats archive (1871–2026)
4. **SABR Lahman Database** — Free downloadable CSV dataset with full team/batting/pitching data (1871–2025)
5. **ESPN / MLB.com** — World Series results and postseason data
6. **Wikipedia** — NL pennant winners and franchise history verification

### Data Collection & Cleaning

- Franchise continuity: Relocated teams are treated as continuous entities (e.g., Brooklyn → LA Dodgers, NY Giants → SF Giants, Montreal → Washington Nationals). This means all historical wins for the Brooklyn franchise are credited to the LA Dodgers.
- Schedule length: Winning percentages are calculated as W / (W + L), excluding ties. Pre-1962 seasons had varying game counts (60–154 games).
- Ties: Before the introduction of the tiebreaker game in 2009, ties were counted separately. Data in these CSVs uses standard W-L format and does not include ties in the win % calculation.
- 1994: The strike-shortened season is included. No pennant was awarded, and the World Series was cancelled.
- 2020: The COVID-19 shortened season (60 games) is included with both regular-season and postseason data.

### Conventions

| Convention | Format |
|----------|--------|
| Team names | Canonical NL names; franchise movements parenthetically |
| W-L format | Wins-Losses (e.g., 98-55) |
| Win % | W/(W+L), 3 decimal places |
| Seasons | Regular-season only (postseason is separate) |
| Era tags | Dead-Ball (pre-1920), Live-Ball (1920-1941), Bracket Era (1946-1972), Divisional (1969+), Modern (2000+) |
| Source priority | Baseball Almanac H2H > Baseball Reference standings > ESPN/MLB.com WS > Wikipedia verification |

### Caveats

- **Pre-1900 data**: Early NL records are less standardized. Era-specific records (e.g., best winning pct in the 1880s) may differ from modern recalculations.
- **1989 Cubs record**: The 1989 NL East champion Cubs finished 92-70; some sources list a different record due to the rain-shortened season.
- **2025 season data**: 2025 data is simulated/projected based on mid-season trends. Verify with Baseball-Reference when the season concludes.
- **1994 gap**: No pennant was awarded in 1994; the strike voided all regular-season and postseason records.
- **Interleague data**: Team-vs-team matrices include only NL-vs-NL matchups. Interleague records are noted separately where applicable.

### Questions / Corrections

If you find any data inconsistencies or errors, please open an issue or pull request. Especially appreciated:
- Corrections to early NL (1876-1900) records
- Updates to 2025 season data when finalized
- Additional H2H matchup data for any era