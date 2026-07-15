# NL Team Trends — Data Notes

## Methodology & Conventions

### Schedule Eras
- **Founding Era (1876–1892)**: 8 teams; 70-132 games per season; no divisions
- **Dead Ball Era (1893–1919)**: 12-16 teams; 154-game schedule (1892+)
- **Power Era (1920–1949)**: 16 teams; 154-game schedule
- **Relocation Era (1950–1969)**: 16-20 teams; 154/162-game schedule
- **Expansion Era (1970–1989)**: 12 teams; 162-game schedule; no divisions until 1969
- **Dynasty Era (1990–2005)**: 14-16 teams; 3 divisions + Wild Card (1994+)
- **Resurgence Era (2006–2016)**: 15 teams; 4-division format
- **Dodgers Dynasty (2017–present)**: 15 teams; full interleague play

### Win% Calculation
- Win% = Wins / Games Played (not winning percentage in the traditional baseball sense)
- Pre-1961 seasons reflect shorter schedules, so raw win counts are not directly comparable to modern seasons
- Win% normalizes across eras for fair comparison

### Franchise Name/Location Changes
| Original Name | Current Name | Year Changed |
|--------------|-------------|-------------|
| Chicago White Stockings | Chicago Cubs | 1900/1907 |
| Boston Beaneaters | Boston Doves | 1907 |
| Boston Doves | Boston Rustlers | 1911 |
| Boston Rustlers | Boston Braves | 1912 |
| Boston Braves | Milwaukee Braves | 1953 |
| Milwaukee Braves | Atlanta Braves | 1966 |
| Brooklyn Dodgers | Los Angeles Dodgers | 1958 |
| New York Giants | San Francisco Giants | 1958 |
| Montreal Expos | Washington Nationals | 2005 |

### Important Caveats
1. **Not all franchises are continuous** — Some teams (e.g., Boston Braves→Milwaukee→Atlanta) involve relocations
2. **Uneven schedule lengths** across eras mean raw win totals favor modern teams
3. **Pre-1969** data has no division structure — single league standings only
4. **2020 season** was shortened to 60 games due to COVID-19
5. **Wild Card era** (1994+) means "pennant" is no longer the sole path to WS
6. **Milwaukee Brewers** switched from AL to NL Central in 1998

### Data Sources
See `source_references.md` for full list of research sources.

### Visualization Plans
- Win % trend lines (smoothed) per franchise across eras
- Pennant heatmap: team × year, color-coded by division/wild card
- WS title timeline with drought durations highlighted
- Inter-team matchup matrices (Head-to-Head W-L)
- Interactive dashboard: Streamlit + Plotly
