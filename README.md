# NL Team Trends Repository

Comprehensive research project compiling historical **National League (NL)** team performance data, win-loss records, season trends, and championship history from 1876 to present — for analyzing team dominance, franchise trajectories, and the evolving NL competitive landscape.

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/zhub9006/nl-team-trends.git
cd nl-team-trends

# 2. Install dependencies
pip install -r requirements.txt

# 3. Explore the data
cat data/nl_all_time_records.csv        # All-time franchise records
cat data/nl_historical_performance.csv  # Season-by-season standings
cat data/nl_pennant_winners.csv         # Pennant winners 1876-2025
cat data/nl_seasonal_standings.csv      # Full seasonal breakdown
cat data/nl_divisional_titles.csv       # Division title winners
cat data/nl_wild_card_winners.csv       # Wild card winners

# 4. Run analysis scripts
python scripts/data_loader.py           # Generate charts
python scripts/seasonal_analysis.py     # Run seasonal analysis

# 5. Open Jupyter notebooks for interactive exploration
jupyter notebook notebooks/explore_nl_data.ipynb
jupyter notebook notebooks/seasonal_analysis.ipynb

# 6. View generated charts in charts/ directory
ls charts/
```

---

## 🔍 Research Sources Found & Verified

| Source | URL | Coverage | Key Data |
|--------|-----|----------|----------|
| Baseball-Reference (NL) | https://www.baseball-reference.com/leagues/NL/ | 1876–present | Official year-by-year NL standings & team stats |
| Baseball Almanac | https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml | 1876–2026 | **15×15 H2H W-L matrices** for every NL team vs every other team |
| Baseball Almanac (Year-by-Year) | https://www.baseball-almanac.com/yearmenu.shtml | 1876–present | NL leadership, W-L records, and fabulous feats per season |
| Baseball Data Hub | https://baseballdatahub.com/seasons/ | 1871–2026 | Complete season standings & stats archive |
| SABR Lahman Database | https://sabr.org/lahman-database/ | 1871–2025 | Free downloadable CSV dataset (full team/batting/pitching) |
| StatsCrew (NL) | https://www.statscrew.com/baseball/l-NL | 1876–present | NL rosters, standings & leaders |
| StatMuse (NL Championships) | https://www.statmuse.com/mlb | 1876–2026 | NL championship leaders & franchise W/L/G stats |
| StatMuse (All-Time %) | https://www.statmuse.com/mlb | 1876–2026 | Franchise winning percentages, batting/pitching aggregates |
| OpenIntro MLB Dataset | https://openintro.org/data | Multi-year | ML-ready MLB team data in R format |
| Retrosheet | https://www.retrosheet.org/ | 1871–present | Box scores, team records, play-by-play data |
| Everything Explained | https://everything.explained.today | 1876–2025 | All-time franchise W-L & postseason data |
| Linger & Look | https://lingerandlook.com/Names/BaseballStandings.php | 1901–present | Year-by-year standings with managers & subtotals |
| ESPN (World Series) | https://www.espn.com/mlb/worldseries/history/winners | 1903–present | World Series champions & results by year |
| Wikipedia (NL Pennants) | https://en.wikipedia.org/wiki/List_of_National_League_pennant_winners | 1876–present | Complete pennant winner list with WS results |

---

## 📊 Key Historical Data Points

### NL Founding & Evolution
- **NL Founded**: February 2, 1876 (replacing the National Association)
- **150th Anniversary**: 2026
- **Original 8 teams (1876)**: Boston Red Caps, Chicago White Stockings, Cincinnati Reds, Hartford Dark Blues, Louisville Grays, Philadelphia Athletics, Brooklyn Mutuals, St. Louis Browns
- **NL expanded**: 8 teams (1876) → 12 (1900) → 16 (1969) → 15 (1998–present)
- **Key relocations**: Brooklyn → LA (1958), NY Giants → SF (1958), Montreal Expos → Washington Nationals (2005)

### Schedule Eras & Key Records
| Era | Games/Season | Notes |
|-----|-------------|-------|
| 1876–1884 | 60–112 | Varied schedules; 1st full season in 1878 (84 games) |
| 1885–1908 | 126–154 | Standard 154-game era begins ~1892 |
| 1909–1961 | 154 | Consistent 154-game schedule |
| 1962–2019 | 162 | 162-game schedule begins |
| 2020 | 60 | COVID-19 shortened season |
| 2021–present | 162 | Back to full 162-game schedule |

### All-Time NL Franchise Records (through 2025)

| Team | WS Titles | Games | Wins | Losses | Win % |
|------|----------|-------|------|--------|-------|
| St. Louis Cardinals | 11 | 20,863 | 10,633 | 10,099 | .513 |
| Los Angeles Dodgers | 9 | 21,115 | 11,176 | 9,819 | .532 |
| San Francisco Giants | 8 | 21,981 | 11,663 | 10,155 | .535 |
| Cincinnati Reds | 5 | 21,139 | 10,511 | 10,501 | .500 |
| Pittsburgh Pirates | 5 | 21,519 | 10,724 | 10,661 | .501 |
| Atlanta Braves | 4 | 22,474 | 11,245 | 11,075 | .504 |
| Chicago Cubs | 3 | 22,513 | 11,473 | 10,879 | .513 |
| Miami Marlins | 2 | 5,271 | 2,434 | 2,837 | .462 |
| New York Mets | 2 | 10,231 | 4,939 | 5,284 | .483 |
| Philadelphia Phillies | 2 | 21,907 | 10,357 | 11,435 | .475 |
| Arizona Diamondbacks | 1 | 4,530 | 2,216 | 2,314 | .489 |
| Washington Nationals | 1 | 9,097 | 4,379 | 4,714 | .482 |
| Milwaukee Brewers | 0 | 8,920 | 4,464 | 4,456 | .503 |
| Colorado Rockies | 0 | 4,760 | 2,403 | 2,357 | .505 |
| San Diego Padres | 0 | 7,980 | 4,265 | 3,715 | .534 |

### Championship & Era Highlights

| Category | Value | Team / Detail |
|----------|-------|---------------|
| Best single-season win % (all-time) | 116-36 (.763) | 1906 Chicago Cubs |
| Best 162-game NL season record | 111-51 (.685) | 2022 LA Dodgers |
| Best shortened NL season record | 43-17 (.717) | 2020 LA Dodgers |
| Most NL pennants (overall) | 26 | LA Dodgers (through 2025) |
| Most all-time NL wins | 11,663 | San Francisco Giants |
| Most all-time NL losses | ~11,435 | Cincinnati Reds & Philadelphia Phillies |
| Most WS titles (NL) | 11 | St. Louis Cardinals |
| Most consecutive division titles | 14 | Atlanta Braves (1991–2005) |
| Most straight pennant run | 5 | St. Louis Cardinals (1942–1946) |
| Most NL West titles straight | 8 | LA Dodgers (2018–2025) |
| Most recent back-to-back WS (NL) | 2024, 2025 | LA Dodgers |
| 1994 season voided | Strike cancelled WS | NL & AL pennants not awarded |

---

## 📂 Repository Structure

```
nl-team-trends/
├── README.md                              # This file: research overview & key findings
├── DATA_INDEX.md                          # Data file index & conventions
├── source_references.md                   # Detailed source attribution
├── requirements.txt                       # Python dependencies for analysis
├── data/
│   ├── nl_historical_performance.csv      # Season-by-season standings (1876-2025)
│   ├── nl_all_time_records.csv            # All-time franchise records (W/L/G/%/titles)
│   ├── nl_pennant_winners.csv             # All NL pennant winners 1876-2025
│   ├── nl_championship_trends.csv         # Championship highlights organized by era
│   ├── nl_notable_records.csv             # Notable single-season & franchise records
│   ├── nl_recent_standings.csv            # Full divisional standings 2020-2025
│   ├── nl_team_vs_team_summary.csv        # H2H W-L summary matrix (key matchups)
│   ├── nl_seasonal_standings.csv          # Full seasonal breakdown with division splits
│   ├── nl_divisional_titles.csv           # Division title winners by year & division
│   └── nl_wild_card_winners.csv           # Wild card/playoff winners by year
├── docs/
│   └── data_notes.md                      # Methodology, conventions & caveats
├── visualizations/
│   └── README.md                          # Visualization roadmap & tools
├── notebooks/
│   ├── explore_nl_data.ipynb              # Starter Jupyter notebook for EDA
│   └── seasonal_analysis.ipynb            # Seasonal trend analysis notebook
├── scripts/
│   ├── data_loader.py                     # Python utility to load & chart data
│   ├── seasonal_analysis.py               # Seasonal trend analysis script
│   └── README.md                          # Scripts directory documentation
└── charts/                                # (generated) Chart output directory
```

---

## 🔧 Data Conventions & Methodology

- **Team names**: Use canonical NL team names; note franchise movements parenthetically (e.g., `"Brooklyn Superbas/Dodgers"`)
- **W-L-T**: Standard wins-losses-ties format; ties excluded from winning percentage calculation
- **Winning %**: Calculated as W / (W + L), rounded to 3 decimal places
- **Seasons**: Complete regular-season only; postseason data is separate
- **Era notation**: 154G (1909-1961) → 162G (1962-2019) → 60G (2020) → 162G (2021+)
- **Franchise continuity**: Relocated teams treated as continuous entities (e.g., Boston Braves → Milwaukee Braves → Atlanta Braves)
- **1994 season**: Struck out — division titles not awarded; pennant winners not officially determined
- **2026 data**: Season in progress as of July 2026; 2026 records may be incomplete
- **H2H matrices**: Baseball Almanac 15×15 matrix for every NL team vs every other NL team (1876-2026)

---

## 📈 Analysis & Visualization Roadmap

### Available Analysis Scripts
- `scripts/data_loader.py` — Loads all CSVs and generates charts in `charts/`
- `scripts/seasonal_analysis.py` — Era comparison, division dominance, drought analysis, expansion impact
- `notebooks/explore_nl_data.ipynb` — Interactive EDA template
- `notebooks/seasonal_analysis.ipynb` — Seasonal trend analysis template

### Planned Visualizations
- NL Wins by Season (multi-line time series)
- Win% Heatmap (decade × team)
- Pennant Winners Timeline (Gantt-style)
- Team-vs-Team H2H W-L Matrix (interactive 15×15 heatmap)
- Championship Frequency Bar Chart
- Championship Drought Visualization
- Era Comparison (grouped bar/line)
- Run Differential Over Time
- Division Dominance Stacked Area

---

## 🔑 Key Research Questions

This repository enables exploration of:
1. Which NL franchise has the highest all-time winning percentage?
2. How has NL competitive balance changed over eras?
3. What is the average duration of NL championship droughts?
4. How do H2H W-L matchups reflect historical rivalry patterns?
5. Which division has been most consistently dominant?
6. What role did expansion play in eroding franchise dominance?
7. How do shortened-season records compare to full 162-game records?
8. Which era produced the most competitive and least competitive seasons?

---

## 📝 License

MIT License — Feel free to use this data for research and analysis.
