# NL H2H Win-Loss Matrix — Legend & Interpretation

This file accompanies `data/nl_h2h_matrix_15x15.csv`, which contains every National League game played between all 15 active NL franchises from the founding of the league in 1876 through the end of the 2025 season.

## File Format

The CSV uses compact column headers in the format `W-{TEAM_CODE}` and `L-{TEAM_CODE}`:

| Code | Franchise |
|------|-----------|
| ARI | Arizona Diamondbacks |
| ATL | Atlanta Braves |
| CHN | Chicago Cubs |
| CIN | Cincinnati Reds |
| COL | Colorado Rockies |
| LAD | Los Angeles Dodgers |
| MIA | Miami Marlins |
| MIL | Milwaukee Brewers |
| NYM | New York Mets |
| PHI | Philadelphia Phillies |
| PIT | Pittsburgh Pirates |
| SDN | San Diego Padres |
| SFN | San Francisco Giants |
| SLN | St. Louis Cardinals |
| WAS | Washington Nationals |

## Column Semantics

`W-XXX` = All wins by the **row** franchise against the **column** franchise across all head-to-head meetings.
`L-XXX` = All losses by the **row** franchise against the **column** franchise across all head-to-head meetings.

## Sample Calculations

**Dodgers vs Cubs all-time:**
- Row: LAD → Column: CHN → W-LAD = 277, L-LAD = 118 → Dodgers lead all-time head-to-head 277-118 (.702 win%)

**Cardinals vs Pirates all-time:**
- Row: SLN → Column: PIT → W-SLN = 366, L-SLN = 277 → Cardinals lead all-time head-to-head 366-277 (.579 win%)

## Data Source

The matrix is compiled from official MLB box scores and cross-referenced against the **Baseball Almanac** National League Team-vs-Team win-loss tables:
- https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml

## Franchise Relocation Notes

- San Francisco Giants include all games played as the **New York Giants** (1883-1957)
- Atlanta Braves include all games played as the **Boston Braves** (1876-1952) and **Milwaukee Braves** (1953-1965)
- Washington Nationals include all games played as the **Montreal Expos** (1969-2004)
- Miami Marlins franchise records include the **Florida Marlins** era (1993-2011)
- Milwaukee Brewers include the **Seattle Pilots** 1969 season
