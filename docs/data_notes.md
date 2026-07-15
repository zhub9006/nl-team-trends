# Data Notes & Methodology

## Overview

This document explains the conventions, methodologies, and caveats for all datasets in the `data/` directory.

## Key Conventions

| Convention | Description |
|------------|-------------|
| Win% | Wins / Games Played |
| Pennants | League championship awards (pre-Wild Card era, typically best record) |
| WS Titles | World Series championships won while representing the NL |
| All-time records | Through end of 2025 MLB season |
| Franchise continuity | Relocated teams (NY→LA Dodgers, NY→SF Giants, Montreal→Washington) are combined under current franchise name |

## Era Boundaries

Eras are delineated by major structural changes:

| Boundary | Change |
|----------|--------|
| 1876 | NL founding (8 original teams) |
| 1892 | First 154-game season; schedule standardization |
| 1903 | First World Series (NL vs AL) |
| 1961 | 162-game schedule adopted |
| 1969 | Divisions created (E/W); LCS introduced |
| 1994 | 3 divisions + Wild Card playoff format |
| 1997 | Interleague play begins |
| 2023 | Full interleague schedule (every team plays every other) |

## Historical Notes

- **Pre-1961 seasons**: 154-game schedule means win totals and percentages are not directly comparable with the modern 162-game era.
- **Shortened seasons**: 2020 was a 60-game season due to COVID-19. Records are noted as special cases.
- **Milwaukee Brewers**: Switched from AL to NL Central in 1998. NL data from 1998 onward includes them.
- **Washington Nationals**: Continental franchise began as Montreal Expos in 1969; relocated to DC in 2005.
- **Early NL (1876–1892)**: 8-team league with no divisions. Some box scores from this era are incomplete in certain sources.

## Data Gap Warnings

- **1876–1892**: Some early-season records have gaps; the Lahman Database is the most comprehensive source for this period.
- **Pre-1903**: No World Series existed; "pennants" = best regular-season record.
- **1994 strike**: Season was cut short; no pennant was awarded that year.

## Chart Intent

For visualizations, consider these transformations:
- Win% trends: Calculate rolling 5-year or 10-year averages for smoother trend lines.
- Head-to-head matrices: Normalize by total games played between each pair to get matchup percentages.
- Era comparison: Use 162-game adjusted win totals for any era comparison from 1961 onward.
