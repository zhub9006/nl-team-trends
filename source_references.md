# NL Team Trends - Source References & Methodology (Updated)

## Primary Data Sources

| Source | URL | Coverage | Key Data Used |
|--------|-----|----------|---------------|
| Baseball-Reference (NL) | https://www.baseball-reference.com/leagues/NL/ | 1876–present | Official year-by-year NL standings & team stats |
| Baseball Almanac (Year-by-Year) | https://www.baseball-almanac.com/yearmenu.shtml | 1876–2026 | NL leadership, W-L records, fabulous feats per season |
| Baseball Almanac (H2H) | https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml | 1876–2026 | 15×15 H2H W-L matrices for all NL team vs NL team matchups |
| Baseball Data Hub | https://baseballdatahub.com/seasons/ | 1871–2026 | Complete season standings & stats archive |
| SABR Lahman Database | https://sabr.org/lahman-database/ | 1871–2025 | Free downloadable CSV dataset (full team/batting/pitching) |
| StatsCrew (NL) | https://www.statscrew.com/baseball/l-NL | 1876–present | NL rosters, standings & leaders |
| StatMuse (NL Championships) | https://www.statmuse.com/mlb | 1876–2026 | NL championship leaders & franchise W/L/G stats |
| Retrosheet | https://www.retrosheet.org/ | 1871–present | Box scores, team records, play-by-play data |
| Everything Explained | https://everything.explained.today | 1876–2025 | All-time franchise W-L & postseason data |
| Linger & Look | https://lingerandlook.com/Names/BaseballStandings.php | 1901–present | Year-by-year standings with managers & subtotals |
| ESPN (World Series) | https://www.espn.com/mlb/worldseries/history/winners | 1903–present | WS champions & results by year |
| Wikipedia (NL Pennants) | https://en.wikipedia.org/wiki/List_of_National_League_pennant_winners | 1876–present | Complete pennant winner list with WS results |
| Champs or Chumps | https://champsorchumps.us/mlb | 1876–present | Win% rankings, droughts, streaks, postseason records |
| MLB Win-Loss Visualizer | https://inkandthunder.github.io/win-loss-visualizer/ | 1894–present | Interactive YoY W-L visualization for all MLB teams |
| BetIQ / TeamRankings | https://betiq.teamrankings.com/mlb/betting-trends/win-loss-records/ | 1876–present | Every team's S/U W-L record with MOV and run-line data |
| MLB.com (Best Records) | https://www.mlb.com/news/best-regular-season-record-for-every-mlb-team | All years | Best single-season records by team |
| Surprise Sports Champions | https://surprisesports.com/baseball/mlb-champions-list/ | 1903–2025 | Complete WS champions list & era analysis |
| OpenIntro MLB Dataset | https://openintro.org/data/index.php?data=mlb_teams | Multi-year | ML-ready MLB team data (batting, pitching, fielding stats) |
| Kaggle (Lahman DB) | https://www.kaggle.com/datasets/dalyas/lahman-baseball-database | 1871–present | Lahman DB on Kaggle with CSV downloads |
| BaseballHQ CSV Center | https://www.baseballhq.com/articles/tools/csv-download-center | Various | Historical data CSV downloads |

## Data Methodology & Caveats

1. **Franchise continuity**: Relocations (Brooklyn→LA, NY Giants→SF, Montreal→Washington) INCLUDE all historical data. Chicago Cubs count includes Chicago White Stockings days (1876).
2. **H2H data**: Baseball Almanac includes 15×15 H2H W-L matrices for all 15 NL teams vs all 15 NL teams (225 unique matchups). Full matrix available in `data/nl_h2h_matrix_full.csv`.
3. **Schedule eras**: Variable schedule lengths (60-154 games pre-1962, 162 from 1962-present, 60 in 2020 COVID season). Win percentages provided for cross-era comparison.
4. **Interleague play**: Beginning in 1997 and permanent since 2023. H2H data is NL-only; interleague results tracked separately.
5. **Championship verification**: All results verified against ESPN World Series data and Baseball-Almanac records.

## Recommended Citation

If using this data for research, please cite:
- Baseball Reference NL franchise records: https://www.baseball-reference.com/leagues/NL/
- SABR Lahman Database: https://sabr.org/lahman-database/
- Baseball Almanac H2H: https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml
- Retrosheet: https://www.retrosheet.org/

## Automated Data Downloads

The Lahman Baseball Database (full season-by-season data) can be downloaded programmatically:
```bash
python scripts/download_nl_data.py
```

This script fetches the latest Lahman DB from the Chadwick Bureau GitHub repository and copies relevant CSV files to the `data/` directory.