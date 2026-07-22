# NL Team Trends — Data Notes & Methodology

## Overview

This document provides detailed methodology notes, data conventions, and caveats for the datasets in the `data/` directory.

## Data Collection Approach

### Primary Collection
- Manual extraction from authoritative baseball reference sources
- Cross-referencing across multiple sources for accuracy
- Integration of franchise movement data to ensure historical continuity

### Data Validation
- Win-loss totals cross-checked against Baseball-Reference and Lahman Database
- Championship data verified against MLB official records
- H2H data sourced from Baseball Almanac (updated daily during season)
- All-time records compared with Wikipedia — discrepancies noted

## Era Definitions

| Era | Years | Key Characteristics |
|-----|-------|---------------------|
| Founding Era | 1876–1891 | Original 8 teams; no divisions; varied schedules (60–140 games) |
| Merger Era | 1892–1902 | NL-AA merger to 12 teams; 154-game schedule standardizes |
| Transition Era | 1903–1919 | First World Series played; Dead Ball Era; 154-game schedule |
| Expansion Era | 1920–1968 | Franchise mobility; integration; 154-game schedule through 1961; 162-game from 1962 |
| Modern Era | 1969–present | Divisional split; 162-game schedule; free agency; labor disputes; 3-division (1994+) |

## Schedule Lengths by Era

- **1876–1877**: 60 games
- **1878–1882**: 84 games
- **1883**: 98 games
- **1884**: 112 games
- **1885–1891**: 126–136 games
- **1892–1900**: 132–154 games
- **1901–1919**: 154 games
- **1920–1961**: 154 games
- **1962–2019**: 162 games
- **2020**: 60 games (COVID-19)
- **2021–2025**: 162 games

## Franchise Movement History

| Original Franchise | Current Franchise | Year of Move |
|-------------------|-------------------|-------------|
| Boston Red Stockings | Atlanta Braves | 1966 (from Milwaukee) |
| Boston Beaneaters/Miners | — | Replaced by Braves lineage |
| Brooklyn Superbas/Doddgers | LA Dodgers | 1958 |
| New York Giants | SF Giants | 1958 |
| Baltimore Orioles | — | Original NA team; replaced by AL Orioles |
| Philadelphia Athletics | — | Moved to KC and Oakland (AL) |
| St. Louis Browns | — | Replaced by current Cardinals (different franchise) |
| Hartford Dark Blues | — | Folded 1877 |
| Louisville Grays | — | Folded 1877 |
| Cleveland Spiders | — | Folded 1899 |
| Washington Senators (NL) | — | Folded 1899 |
| Concordia/Louisville | — | Various folds and reforms |
| Boston Reds | — | Folded 1891 (AA) |
| Providence Grays | — | Folded 1885 |

## Data Caveats

1. **Pre-WS Champions**: Seasons before 1903 do not have a formal World Series. Some sources consider the NL pennant winner as champion; others note no formal championship was played.

2. **1885–1886 Series**: The 1885 and 1886 editions between the NL and AA champions are sometimes disputed in historical records. Our data reflects the most widely accepted results.

3. **1994 Strike**: The 1994 season was cut short by a players' strike on August 12. No playoffs or World Series were held. The abolition of the division series and LCS creates a data gap.

4. **Ties**: Ties in early baseball (1876–1890s) are sometimes not counted in win-loss records. Our data reflects best available sources.

5. **Interleague Play**: Starting in 1997, NL teams play AL teams. H2H totals in `nl_team_vs_team_summary.csv` include only NL-vs-NL games.

6. **franchise_origin notes**: The `franchise_origin` field shows the original franchise name(s) or notable transitions. For example, "B/cardinals" indicates the franchise started as the Boston Red Stockings, moved to St. Louis as the Browns, and became the Cardinals.

7. **Win Percentage Accuracy**: Win% is calculated as Wins / (Wins + Losses). In seasons with tied games, those games are excluded from the denominator.

8. **Recent Standings**: The `nl_recent_standings.csv` file is named for recent divisional standings (2014–2025). Some division winner data for 2017–2020 may be approximate.

## Visualization Recommendations

For building visualizations in the `visualizations/` directory, we recommend:

1. **Time series line charts**: Win% by team over time (group by era)
2. **Heatmaps**: NL team-vs-team H2H results matrix
3. **Bar charts**: All-time franchise win totals, WS titles by team
4. **Stacked area charts**: League win% by division over eras
5. **Chord diagrams**: Trade/player flow between NL teams (using Retrosheet data)
6. **Treemaps**: Franchise market value vs. on-field success (using financial data)
7. **Win probability graphs**: Season trajectories for championship teams

Tools: matplotlib, seaborn, plotly, altair, pandas
