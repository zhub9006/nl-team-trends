# NL Team Trends — Data Methodology, Conventions & Caveats

This document describes the methodology used to compile the data in this repository, along with conventions and known caveats.

---

## Data Collection Methodology

### 1. Source Selection
- **Primary sources**: Baseball-Reference.com and Baseball Almanac are used as the two primary data sources for all statistics
- **Cross-verification**: Key statistics are verified across both sources independently
- **Tertiary sources**: Wikipedia and ESPN are used for supplementary verification

### 2. Data Freshness
- **Standard seasons**: All data is current through the end of the most recent completed regular season and postseason
- **All-time records**: Updated annually after the World Series concludes
- **Seasonal data**: Individual season records are updated as each season concludes

### 3. Franchise Counting
- **Franchise continuity**: When a franchise relocates, all years of that franchise's history are combined
- **Example**: The Chicago Cubs include years as the Chicago White Stockings (1876–1902), Chicago Orphans (1903–1906), etc.
- **Modern names**: Where possible, modern/franchise-identity team names are used for clarity

---

## Data Conventions

### Win-Loss Formatting
- All W-L records are shown as **Wins-Losses** (e.g., 116-36)
- Ties (pre-1920) are not displayed separately but are included in win/loss counts where they affect averages
- Win percentages are calculated as: Wins / (Wins + Losses), rounded to 3 decimal places

### Year Counting
- Regular season years are the "standard" calendar year (e.g., 2025 means the 2025 regular season)
- Split seasons (1981, 1918) are noted with appropriate flags

### Division Naming
- Divisions are labeled as: NL East, NL Central, NL West (standard modern naming)
- Pre-1969 teams are listed with "NA" (no division) or "Eastern"/"Western" (1876-1968 NL structure)
- The three-division format (East/Central/West) has been in place since 1994

### Franchise H2H Data
- **Inclusion of interleague games**: Since 1997, interleague games are included in H2H totals
- **Pre-1997**: Only intra-league games (NL vs NL) are included
- **Modern team names**: H2H data uses current franchise names and includes the opposing franchise history

### Championship Data
- **World Series**: Begins 1903 (no WS in 1904 as Giants declined / 1994 as strike cancelled)
- **Pennants**: Includes all NL pennant winners from 1876 to present
- **Tied games (pre-1920)**: Some seasons had postseason ties that are counted as NL pennant appearances with note "tie"

### Record Classifications
- **Franchise records**: All-time franchise W-L records including relocations
- **Single-season records**: Individual season W-L records
- **Streak records**: Consecutive title/dynasty records

---

## Known Caveats & Limitations

### Data Gaps
1. **1876 Season**: Only 6 teams (Hartford, Louisville, and Philadelphia Athletics folded after one year; Mutuals expelled)
2. **1892 Season**: Split-season format used; final standings adjusted for championship
3. **1981 Season**: Split-season format used due to players' strike
4. **2020 Season**: 60-game COVID-19 shortened season; West Division reduced to 5 intradision games

### Pre-1900 Data Accuracy
- Early season statistics may contain discrepancies between Baseball-Reference and Baseball Almanac due to:
  - Different counting of ties/replays
  - Varying season lengths (60–136 games)
  - Inconsistent official record-keeping
- The repository uses Baseball-Reference as the primary source for pre-1900 data

### H2H Data Caveats
1. **Interleague era (1997–present)**: H2H totals include both intra- and interleague games, which may not perfectly match pre-1997 H2H records that were intra-league only
2. **Cross-city rivals**: H2H records between cross-city rivals (Dodgers vs Angels, etc.) may be incomplete for AL-NL overlap periods
3. **Games vs. non-NL teams**: Only intra-NL World Series games are included in H2H records (e.g., Cubs vs White Sox in 1906 WS)

### Franchise Relocations
- When a franchise relocates, the relocation year is noted in era-specific H2H analysis
- The "Brooklyn/LA Dodgers" label is used when tracking the franchise through both 1876-1957 and 1958-present
- "Washington Nationals" includes the Montreal Expos (1969-2004), and franchise records span both identities

### Championship Counting
- The NL pennant count in `nl_all_time_records.csv` is consistent with Baseball Almanac's pennant winner list
- World Series titles are cross-verified with Baseball Almanac and ESPN
- Pre-NLWF (pre-1903) championship events may not align perfectly across sources

### Data Updates
- The NL has expanded to 15 teams (1998: Arizona Diamondbacks and Milwaukee Brewers moved from AL to NL; Houston Astros moved from NL Central to NL West)
- The 2020 shortened season (60 games) is flagged in relevant data files
- Division alignment has changed multiple times — current alignment since 1998 is used for modern data

### Missing Data
- Some early seasons may have incomplete box score data
- Pre-1920 records may not have complete game-by-game pitching/batting data
- Minor league data is not included in this repository

---

## Recommended Analysis Tools

### For Statistical Analysis
- **Pandas**: Core data manipulation and analysis
- **NumPy**: Numerical computing
- **SciPy**: Statistical analysis and hypothesis testing

### For Visualization
- **Matplotlib**: Static publication-quality figures
- **Seaborn**: Statistical visualization (heatmaps, violin plots, etc.)
- **Plotly**: Interactive plots and dashboards

### For Advanced Analytics
- **Statsmodels**: Regression analysis and time series
- **Scikit-learn**: Machine learning (predictive models)

### For Dashboard Creation
- **Streamlit**: Data apps for interactive exploration

---

*Last Updated: July 2025*