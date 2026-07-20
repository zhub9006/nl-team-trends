# Data Notes — nl-team-trends

## Methodology

### Data Sources
All primary data sourced from:
- **StatMuse NL Championships & All-Time %**: 12-row NL franchise grid with complete W/L/G statistics
- **Baseball Almanac H2H (NL)**: Complete 15x15 team-vs-team win/loss matrix 1876-2026
- **SABR Lahman Database**: Commission-level team stats, batting/pitching (free CSV download)
- **Baseball-Reference NL Index**: Official year-by-year standings
- **Baseball Data Hub**: Season-by-season standings archive

### Franchise Continuity
All records treat relocated franchises as continuous entities:
- LA Dodgers = Brooklyn (1884-1957) + LA (1958-present)
- SF Giants = NY Giants (1883-1957) + SF (1958-present)
- Washington Nationals = Montreal Expos (1969-2004) + Washington DC (2005-present)
- Atlanta Braves = Boston Red Stockings (1871-1952) + Milwaukee Braves (1953-1965) + Atlanta Braves (1966-present)

### Win% Calculation
- Win% = Wins / (Wins + Losses) — ties excluded as rare post-1920
- Pre-WS era pennants: Counted as pennants won but WS_Result = None
- 1904 NY Giants: No WS (owner refused); NOT counted as WS championship

### Schedule Eras
| Era | Games | Period |
|-----|-------|--------|
| Early NL | 60-112 | 1876-1884 |
| Growth | 126-154 | 1885-1908 |
| 154-Game Standard | 154 | 1909-1961 |
| 162-Game Modern | 162 | 1962-2019, 2021+ |
| COVID Shortened | 60 | 2020 |

### Key Conventions
- Pre-1903: Only NL championship exists; no World Series
- 1994 strike: No pennant or WS awarded
- Split seasons: 1892 (first half / second half) and 1981 (first half / second half)
- Milwaukee Brewers moved from AL→NL Central in 1998
- Interleague play began in 1997

### Colorado Rockies Special Note
Rockies competitive but 0 WS titles:
- 1995: First NL pennant in franchise's 2nd year
- 2007: Won NLCS (lost to Boston)
- 2017-2018: Back-to-back 100+ win seasons
- Best win% among active NL zero-title teams (.505)

### Notable NL Cinderella Stories
1. **1914 Boston Braves** — Last place July 4, won WS by Sept 1: first major upset
2. **1969 NY Mets** — 100 WS wins; expansion team that won the whole thing
3. **1986 NY Mets** — 108-54 regular season + famous October back-to-back
4. **2001 Arizona Diamondbacks** — 2nd-year franchise winning WS
5. **2019 Washington Nationals** — Breaking the November drought

### Missing Data / Gaps
- No WS data before 1903
- Some pre-season counting differences in older records
- H2H full 15×15 matrix at Baseball Almanac NL H2H pages

## Recommended Data Analysis Workflow
```python
import pandas as pd
all_time = pd.read_csv('data/nl_all_time_records.csv')
seasonal = pd.read_csv('data/nl_historical_performance.csv')
records = all_time.sort_values('WS_Titles', ascending=False)
print(records.head())
```

## Contributing Guidelines
- Add new seasons to nl_historical_performance.csv using Baseball Almanac
- Expand H2H data using the full 15×15 matrix
- Document methodology changes in docs/data_notes.md
- Maintain cross-reference in source_references.md for new data sources