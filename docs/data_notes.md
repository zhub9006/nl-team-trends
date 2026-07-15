# Data Notes: Methodology, Conventions & Caveats

## How This Repository Was Populated

### Research Process
1. **Initial Search**: Searched multiple baseball databases for NL team histories, all-time records, and championship data
2. **Source Verification**: Cross-referenced findings across 10+ authoritative sources to ensure accuracy
3. **Data Compilation**: Extracted tabular data from HTML tables, stat listings, and year-by-year records
4. **CSV Generation**: Structured data into CSV format for programmatic analysis and visualization
5. **Validation**: Checked key figures against independent sources to confirm consistency

### Data Sources Consulted
| Source | URL | Used For |
|--------|-----|----------|
| Baseball Almanac | baseball-almanac.com/teams/teamvsteam-nl.shtml | NL team-vs-team W-L matrices, franchise histories |
| Baseball Reference | baseball-reference.com/leagues/NL/ | Year-by-year standings and leaders |
| StatMuse | statmuse.com/mlb | All-time franchise W-L records, championship data |
| Baseball Data Hub | baseballdatahub.com/seasons/ | Season-by-season standings archive |
| Linger and Look | lingerandlook.com/Names/BaseballStandings.php | Year-by-year standings with managers (1901+) |
| Wikipedia | wikipedia.org | All-time MLB W-L records overview |

## Key Conventions Used Throughout

### Win-Loss Records
- Format: `Wins-Losses` (e.g., `93-69`)
- Win percentage: `Wins/Games` rounded to 3 decimal places (e.g., `.574`)
- Pre-1961 seasons used 154-game schedule; 1961+ uses 162-game schedule
- Shortened seasons flagged (1892, 1981 split seasons; 1994 cancelled; 2020 60 games)

### Franchise Naming
- Each team listed by current name but includes historical name(s) in parentheses
- Example: `"San Francisco Giants (NY Giants)"`
- Milwaukee Brewers explicitly noted as AL→NL switch (1998)
- Washington Nationals noted as former Montreal Expos (2005 relocation)
- Houston Astros noted as NL team since 2013 (previously AL)

### Era Labels
| Era | Years | Key Characteristics |
|-----|-------|-------------------|
| Pre-Modern | 1876-1902 | 8-team league; no World Series |
| Dead Ball | 1903-1919 | Record-setting wins; no DH |
| Live Ball | 1920-1945 | Power transition; franchise migration begins |
| Integration | 1946-1969 | Jackie Robinson 1947; expansion; 154→162 games |
| Expansion | 1970-1989 | 12-14 teams; divisions; LCS |
| Modern | 1990-present | 14-15 teams; Wild Card; interleague; full interleague |

### Pennant vs. Championship
- **Pennant** = League championship (pre-Wild Card era) or division/league title
- **WS Title** = Won the World Series as a National League team
- **WS Loss** = Won league championship but lost World Series
- Some seasons have no pennant (1994 strike) or no WS (pre-1903)

## Known Limitations & Caveats

### 1. Franchise Continuity
- The SF Giants franchise includes all-time New York Giants stats (1903-1957)
- The LA Dodgers franchise includes all-time Brooklyn/LA stats (1890-1957)
- The Atlanta Braves franchise includes Boston (1876-1952) and Milwaukee (1953-1965)
- These prior-city totals inflate win totals significantly

### 2. Schedule Variations
- 1876-1891: Approx. 70-140 game seasons
- 1892-1960: 154-game seasons
- 1961-2019: 162-game seasons
- 1981: Split season (102 games in 2 halves)
- 1994: Season cancelled by strike (no stats counted)
- 2020: 60-game season (21 games behind closed doors)
- 2025: 162-game season (standard)

### 3. Pre-War/Post-War Comparison
- Comparing win percentages across eras is misleading due to expansion, schedule changes, and talent distribution
- The "Dead Ball" and "Live Ball" eras had fundamentally different scoring environments
- 1968 "Year of the Pitcher" led to the mound being lowered in 1969
- The juiced ball controversy (1990s-2000s) inflated run scoring
- 2019 saw an MLB-record 6,776 home runs across both leagues

### 4. Interleague Data
- Interleague play began in 1997
- Full interleague schedule since 2023
- Team-vs-Team W-L matrices from Baseball Almanac include interleague games
- Pre-1997, all W-L is exclusively intraleague

### 5. Statistical Inflation
- All-time win totals should NOT be directly compared without normalizing for era
- 11,663 wins by SF Giants includes 77 seasons in New York
- Win% is more meaningful for cross-era comparisons
- Per-game win% adjusts for schedule length differences

## Data Validation Methods
- Cross-referenced all-time franchise totals across StatMuse, Baseball Almanac, and Baseball Reference
- Verified championship years against multiple sources
- Checked head-to-head W-L matrices against Baseball Almanac's comprehensive dataset
- Confirmed era labels and timeline milestones with SABR and Baseball Data Hub
- All numbers flagged with source attribution for transparency

## Controversial/Disputed Data Points
- 1904: No World Series played (John McGraw refused to compete)
- 1994: Season voided — no pennant or WS awarded
- Split-season 1892 and 1981: Championship determined in second-half/playoff
- Houston Astros' 2013 move to AL Central (not NL) — excluded from NL historical data

## Future Data Enhancements
- Add year-by-year standings for all 15 NL teams (1876-2025)
- Include batting/pitching leaders for each season
- Add head-to-head matchup breakdowns (team-vs-team CSV)
- Include playoff/postseason results for each year
- Add manager data and front office changes
- Integrate salary data when available
- Cross-reference with SABR era sequences

## Contact & Contribution
- Data sources are cited in `source_references.md`
- Contributions welcome: additional data, visualizations, analysis notebooks
- Please preserve existing conventions when adding data
- For discrepancies, document source and note in comments