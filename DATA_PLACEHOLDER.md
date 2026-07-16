# Data Files Index - nl-team-trends
# Guide to all data files in the data/ directory

## Data Directory

### 1. nl_historical_performance.csv
Description: Year-by-year NL champion, 2nd place, W-L records, and World Series results from 1876 to 2025.
Columns: Year, NL_Champion, Champion_Wins, Champion_Losses, Champion_WPct, Second_Place, Second_Wins, Second_Losses, Second_WPct, WS_Champion, WS_Result, Era
Size: ~150 rows (1876-2025)
Use: Primary time series for Win% trend charts and pennant winner analysis.

### 2. nl_all_time_records.csv
Description: All-time franchise win-loss totals, championship counts (division titles, pennants, WS), and era data for every NL team (including relocated franchises).
Columns: Franchise, NL_Team_Names, First_Season, Last_Season, Games_Played, All-Time_Wins, All_Time_Losses, Win_Pct, Division_Titles, Wild_Cards, NL_Pennants, WS_Titles, Current_Division, Notable_Era, Championship_Focus
Use: All-time franchise leaderboards and era comparisons.

### 3. nl_notable_records.csv
Description: Key single-season and franchise records with context and historical notes.
Columns: Category, Record, Team, Year, Statistic, Value, Notes
Use: Highlight-reel stats for visualizations and fact panels.

### 4. nl_championship_trends.csv
Description: Era-based championship trend data mapping NL dominant teams, pennant counts, and World Series winners per decade.
Columns: Era, Start_Year, End_Year, NL_Championships, League_Champs, Top_Winning_Pct, Top_WPct_Team, Braves_Streak, Other_Notable_Teams, WS_Champions_in_Era, notes
Use: Heatmaps and era trend visualizations showing how dominance shifted across the 150-year span.

### 5. nl_notable_seasons.csv
Description: Significant seasons with key statistics, categories, and historical context.
Columns: Year, Team, Key_Statistic, Value, Category, Context
Use: Timeline-style visualizations and milestone annotations.

## Supported Files

- README.md - Repository overview, research sources found, key historical data points, and structure
- source_references.md - Detailed source list, key data points, and data file reference
- requirements.txt - Python dependencies for analysis (pandas, matplotlib, seaborn, plotly, streamlit, etc.)

## Repository Structure

nl-team-trends/
  README.md - Overview & research findings
  source_references.md - Source list & data conventions
  DATA_PLACEHOLDER.md - File index & usage guide
  requirements.txt - Python dependencies
  .gitignore
  LICENSE (MIT)
  data/
    nl_historical_performance.csv
    nl_all_time_records.csv
    nl_notable_records.csv
    nl_championship_trends.csv
    nl_notable_seasons.csv
  docs/
    research_notes.md - Detailed research findings & methodology
  notebooks/ - Jupyter notebooks for analysis
  scripts/ - Data processing scripts
  visualizations/ - Generated charts & dashboards

## Suggested Analysis Pipeline

1. Load nl_historical_performance.csv -> plot Win% trends per era
2. Join with nl_all_time_records.csv -> compare franchises across centuries
3. Use nl_championship_trends.csv -> era heatmap visualizations
4. Merge nl_notable_records.csv and nl_notable_seasons.csv -> oriented milestone timelines
5. Cross-reference with SABR Lahman CSV data for richer player-level stats

## Data Cleaning Notes

- 1994 & 1981: Data reflects a season with no NL pennant (1994) or a split-season champion (1981)
- Prefix teams like Chicago WSS, Brooklyn Bridegrooms, and Providence Grays may appear in early-season data before team-name standardization
- 2020 season data uses a compressed 60-game schedule; WinPcts are not directly comparable to 162-game seasons
- 2025 data final through season end