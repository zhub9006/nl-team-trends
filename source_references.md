# NL Team Trends — Source References & Research Attribution

Below is a comprehensive catalog of all research sources used to compile the historical National League performance data in this repository. Each source is verified, with coverage dates, key data types, and access information.

---

## Primary Data Sources

### 1. Baseball-Reference (NL)
- **URL**: https://www.baseball-reference.com/leagues/NL/index.shtml
- **Coverage**: 1876–present
- **Key Data**: Official year-by-year NL standings, team statistics, leaderboards
- **Verified By**: Long-standing authoritative baseball reference site; data cross-checked with Baseball Almanac
- **Used For**: Seasonal standings, franchise histories, player statistics

### 2. Baseball Almanac — Year-by-Year
- **URL**: https://www.baseball-almanac.com/yearmenu.shtml
- **Coverage**: 1876–present
- **Key Data**: NL leadership, W-L records, fabulous feats per season, all-time team records
- **Verified By**: Independent research by Baseball Almanac staff; data consistent with Baseball-Reference
- **Used For**: Championship events, season-by-season records, NL pennant winners

### 3. Baseball Almanac — Team vs Team H2H
- **URL**: https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml
- **Coverage**: 1876–2026
- **Key Data**: 15×15 H2H W-L matrices for every NL team vs every other team
- **Verified By**: Primary H2H data source; cross-checked with existing repo H2H files
- **Used For**: Rivalry analysis, detailed H2H matrices

### 4. Sports Reference (Baseball-Reference)
- **URL**: https://www.baseball-reference.com/
- **Coverage**: 1871–present
- **Key Data**: Complete MLB player, team, and league stats, awards, records
- **Verified By**: Industry-standard baseball statistics authority
- **Used For**: Supplementary statistics, franchise timelines

### 5. SABR Lahman Database
- **URL**: https://sabr.org/lahman-database/
- **Coverage**: 1871–present (including Negro Leagues)
- **Key Data**: Free downloadable CSV datasets — full team/batting/pitching/fielding
- **Verified By**: Created by SABR member Sean Lahman; used by researchers worldwide
- **Used For**: Programmatic analysis, advanced statistics, data science workflows
- **Note**: Recommended download at https://github.com/chadwickbureau/baseballdatabank

### 6. Baseball Data Hub
- **URL**: https://baseballdatahub.com/seasons/
- **Coverage**: 1871–2026
- **Key Data**: Complete season standings & stats archive, proprietary PIV metric
- **Verified By**: Authoritative archive with 150+ years of MLB history
- **Used For**: Season-by-season standings data

### 7. StatsCrew (NL)
- **URL**: https://www.statscrew.com/baseball/l-NL
- **Coverage**: 1876–present
- **Key Data**: NL rosters, standings, and leaders
- **Verified By**: Consistent with other sources
- **Used For**: Supplementary standings and roster data

### 8. StatMuse (NL Championships)
- **URL**: https://www.statmuse.com/mlb
- **Coverage**: 1876–2026
- **Key Data**: NL championship leaders, franchise W/L/G stats
- **Verified By**: Modern statistical platform with consistent data
- **Used For**: Championship records, franchise statistics

### 9. ESPN (World Series)
- **URL**: https://www.espn.com/mlb/worldseries/history/winners
- **Coverage**: 1903–present
- **Key Data**: World Series champions & results by year
- **Verified By**: Official MLB broadcast partner
- **Used For**: World Series results, champion verification

### 10. Wikipedia — NL Pennant Winners
- **URL**: https://en.wikipedia.org/wiki/List_of_National_League_pennant_winners
- **Coverage**: 1876–present
- **Key Data**: Complete pennant winner list with WS results
- **Verified By**: Community-maintained; cross-checked with Baseball Almanac
- **Used For**: Pennant winner verification, era context

### 11. Wikipedia — All-Time MLB Win-Loss Records
- **URL**: https://en.wikipedia.org/wiki/List_of_all-time_Major_League_Baseball_win-loss_records
- **Coverage**: All 30 current MLB teams through 2025 season
- **Key Data**: All-time franchise records ranked by win-loss percentage
- **Verified By**: Cross-checked with Baseball-Reference and Baseball Almanac
- **Used For**: All-time franchise rankings, franchise notes

### 12. MLB Win-Loss Visualizer
- **URL**: https://inkandthunder.github.io/win-loss-visualizer/
- **Coverage**: 1894–present
- **Key Data**: Interactive year-over-year W-L visualization tool
- **Verified By**: Open-source visualization tool; data consistent with other sources
- **Used For**: Visualizing win-loss trends over time

### 13. Champs or Chumps
- **URL**: https://champsorchumps.us/mlb
- **Coverage**: 1876–present
- **Key Data**: Win% rankings, droughts, streaks, postseason records
- **Verified By**: Comprehensive stat tracking site
- **Used For**: Drought analysis, streak tracking, win% rankings

---

## Data Collection Methodology

1. **Multiple Source Cross-Verification**: All key statistics are verified across at least two independent sources (typically Baseball-Reference + Baseball Almanac).

2. **Franchise Relocation Handling**: When a team relocates (e.g., Brooklyn → LA, NY Giants → SF), the data includes the franchise's complete history across all cities. This is consistent with Baseball Almanac's approach.

3. **H2H Data**: Head-to-head records are sourced from Baseball Almanac's comprehensive 15×15 matrix (1876–2026). Some rivalry data has been curated and summarized in `data/nl_h2h_rivalries_detailed.csv` with era-specific notes.

4. **Season Data**: Seasonal standings are compiled from Baseball-Reference and Baseball Almanac, covering 1876–2025 (with 2025 season complete through the regular season and postseason).

5. **Championship Data**: World Series results are verified against ESPN's official records and Baseball Almanac. Pennant winners are cross-checked with Wikipedia's NL pennant winners list.

---

## Data Accuracy & Limitations

- **Through 2025 Season**: All data files are current through the end of the 2025 MLB regular season and postseason (LA Dodgers won the 2025 World Series).
- **Pre-1900 Data**: Early season data (1876–1899) may have minor discrepancies between sources due to different counting methods for tied games and season lengths.
- **H2H Totals**: H2H records may not perfectly match across all sources due to differences in counting interleague games before 1997 (when interleague play began).
- **Franchise Counts**: All-time game/pennant/title counts include the franchise's time in all cities. Team names have been modernized for clarity.
- **Negro Leagues**: Not included in all-time records (consistent with MLB's official counting, which incorporated Negro Leagues stats in 2020).
- **Ties**: Pre-1920 seasons occasionally had tied games that were replayed; these are generally counted as both a win and a loss in some sources.

---

## Key Reference Books & Publications

- *Total Baseball* by John Thorn et al. — Definitive baseball encyclopedia
- *The Bill James Historical Baseball Abstract* — Historical analysis and context
- SABR Analytics Conference proceedings — Advanced analytical methods
- Baseball Prospectus — Modern statistical analysis

---

*Last Updated: July 2025*