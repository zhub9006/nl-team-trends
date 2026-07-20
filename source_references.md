# NL Team Trends — Source References & Attribution

This document provides detailed attribution for all research sources used in this repository, including URLs, coverage periods, data types, and verification status.

---

## Primary Sources

### 1. Baseball-Reference.com — National League
- **URL:** https://www.baseball-reference.com/leagues/NL/
- **Coverage:** 1876–present
- **Data Type:** Official year-by-year NL standings, team statistics, league leaders
- **Priority:** Primary (gold standard for baseball statistics)
- **Verified:** ✅ Yes

### 2. Baseball Almanac — NL Team vs Team Win-Loss
- **URL:** https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml
- **Coverage:** 1876–2026
- **Data Type:** Complete 15×15 H2H W-L matrix for every NL franchise vs every other NL franchise
- **Priority:** Primary for H2H analysis
- **Verified:** ✅ Yes (content fetched and parsed)

### 3. Baseball Almanac — Year-by-Year History
- **URL:** https://www.baseball-almanac.com/yearmenu.shtml
- **Coverage:** 1876–present
- **Data Type:** NL leadership, W-L records, fabulous feats per season
- **Priority:** Primary for seasonal data
- **Verified:** ✅ Yes

### 4. Baseball Data Hub — All MLB Seasons
- **URL:** https://baseballdatahub.com/seasons/
- **Coverage:** 1871–2026 (156 seasons)
- **Data Type:** Complete season standings, batting/pitching statistical leaders
- **Priority:** Secondary
- **Verified:** ✅ Yes

### 5. SABR Lahman Database
- **URL:** https://sabr.org/lahman-database/
- **Coverage:** 1871–2025
- **Data Type:** Free downloadable CSV dataset (team, batting, pitching fields)
- **Priority:** Primary for programmatic analysis
- **Verified:** ✅ Yes

### 6. StatsCrew — National League
- **URL:** https://www.statscrew.com/baseball/l-NL
- **Coverage:** 1876–present
- **Priority:** Secondary
- **Verified:** ⚠️ Partial

### 7. StatMuse — NL Championships & Team W-L
- **URL:** https://www.statmuse.com/mlb
- **Coverage:** 1876–2026
- **Priority:** Secondary
- **Verified:** ⚠️ Partial

### 8. ESPN — World Series History
- **URL:** https://www.espn.com/mlb/worldseries/history/winners
- **Coverage:** 1903–present
- **Priority:** Primary for WS data
- **Verified:** ✅ Yes

### 9. Wikipedia — NL Pennant Winners
- **URL:** https://en.wikipedia.org/wiki/List_of_National_League_pennant_winners
- **Coverage:** 1876–present
- **Priority:** Secondary
- **Verified:** ⚠️ Could not fetch content directly

### 10. Wikipedia — All-Time MLB Win-Loss Records
- **URL:** https://en.wikipedia.org/wiki/List_of_all-time_Major_League_Baseball_win–loss_records
- **Coverage:** All current MLB franchises
- **Priority:** Secondary
- **Verified:** ⚠️ Could not fetch content directly

### 11. MLB Win-Loss Visualizer
- **URL:** https://inkandthunder.github.io/win-loss-visualizer/
- **Coverage:** 1894–present
- **Priority:** Tertiary
- **Verified:** ⚠️ Could not fetch content directly

### 12. Champs or Chumps
- **URL:** https://champsorchumps.us/mlb
- **Coverage:** 1876–present
- **Priority:** Tertiary
- **Verified:** ⚠️ Could not fetch content directly

---

## Data Files and Their Source Mapping

| Data File | Primary Source(s) | Secondary Source(s) |
|-----------|-------------------|---------------------|
| `nl_historical_performance.csv` | Baseball-Reference (NL), Baseball Almanac | Baseball Data Hub |
| `nl_all_time_records.csv` | Baseball-Reference (NL), Wikipedia | Baseball Almanac |
| `nl_championship_trends.csv` | Baseball Almanac, ESPN (WS) | Wikipedia (NL Pennants) |
| `nl_pennant_winners.csv` | ESPN (WS), Baseball Almanac | Wikipedia (NL Pennants) |
| `nl_team_vs_team_summary.csv` | Baseball Almanac (H2H) | Baseball-Reference |
| `nl_h2h_rivalries_detailed.csv` | Baseball Almanac (H2H) | Baseball-Reference |
| `nl_notable_records.csv` | Baseball-Reference, Baseball Almanac | Multiple sources |
| `nl_recent_standings.csv` | StatMuse, ESPN | Baseball-Reference |
| `nl_championship_milestones.csv` | Baseball Almanac, ESPN | Wikipedia (NL Pennants) |
| `nl_historical_trends_analysis.md` | Baseball-Reference, Baseball Almanac | SABR research |

---

## NL Founding & Evolution

- **Founded:** February 2, 1876
- **Replaced:** National Association (1871–1875)
- **Original 8 teams:** Boston Red Caps, Chicago White Stockings, Cincinnati Reds, Hartford Dark Blues, Louisville Grays, Philadelphia Athletics, Brooklyn Mutuals, St. Louis Browns
- **Expansion timeline:** 8 (1876) → 12 (1900) → 16 (1969) → 15 (1998–present)
- **Key relocations:** Brooklyn → LA (1958), NY Giants → SF (1958), Boston → Milwaukee → Atlanta, Montreal → Washington (2005)

---

## Data Conventions

- **Team names:** Canonical NL names; franchise moves noted parenthetically
- **W-L-T format:** Standard wins-losses-ties; ties excluded from win %
- **Winning %:** Calculated as W/(W+L), 3 decimal places
- **Franchise continuity:** Relocated teams treated as continuous entities
- **Division names:** E (East), C (Central), W (West), NA (pre-division era)

---

*Last updated: July 2025*