# NL Team Trends - Visualization Roadmap & Tool Stack

## Project Status
This research repository compiles historical NL team data. All data sources verified July 2026. 15 CSV data files are included in /data/. This roadmap lists planned visualizations for future implementation.

## Visualizations (To-Do / Planned)

### 1. Win-Loss Trend Lines Per Franchise (1876-2026)
- **Type**: Line chart (multi-line; one per franchise with modern 15-team overlay)
- **X-axis**: Season (rolling 5-year average win% for clarity)
- **Y-axis**: Rolling win percentage
- **Tool**: Matplotlib / Seaborn / Plotly
- **Insight**: Identify dynasty cycles, drought periods, franchise trajectories
- **Data Source**: `nl_historical_performance.csv` + `nl_all_time_records.csv`

### 2. Pennant/Championship Heatmap by Era and Team
- **Type**: Heatmap (rows=teams, columns=eras or decades 1870s-2020s)
- **Color scale**: Pennant count or championships per team-era
- **Tool**: Seaborn / Plotly
- **Insight**: Spot dominant dynasties and competitive balance shifts across 150 years
- **Data Source**: `nl_championship_trends.csv`

### 3. Head-to-Head Matchup Matrix Heatmap
- **Type**: Square heatmap (15x15 for current NL teams, full 15×15 W-L matrix)
- **Values**: Win% in head-to-head matchups using Baseball Almanac team-vs-team data
- **Tool**: Plotly (interactive hover labels)
- **Insight**: See inter-division rivalries and historical advantages; Dodgers 278W-122L vs Cubs dominates
- **Data Source**: Baseball Almanac NL team-vs-team matrix (1876-2026)

### 4. Championship Drought Duration by Franchise
- **Type**: Horizontal bar chart
- **Metric**: Years since last championship per franchise, sorted
- **Tool**: Matplotlib / Plotly
- **Insight**: Highlight historic droughts (Cubs 108yr; Phillies 48yr since 1980; Brewers 0 championships)
- **Data Source**: `nl_all_time_records.csv` WS_Titles column

### 5. Win% Distribution by Decade (Box/Violin Plot)
- **Type**: Violin/box plot (decades on x-axis; Win% on y-axis)
- **X-axis**: Decade (1880s, 90s, 00s, ..., 2020s); normalize 162-game schedules
- **Y-axis**: Win% (162-game adjusted) with 16+ game threshold
- **Tool**: Seaborn
- **Insight**: Show competitive balance changes over time; 1910s dead-ball vs. 2020s parity
- **Data Source**: `nl_historical_performance.csv`

### 6. All-Time Franchise Records Comparison (Top 15 NL Teams)
- **Type**: Clustered bar chart or radar chart
- **Metrics**: WS_Titles, Pennants, Win%, Games Played, divisions titles
- **Tool**: Plotly (interactive)
- **Insight**: Side-by-side multi-metric comparison of all 15 current NL franchises
- **Data Source**: `nl_all_time_records.csv`

### 7. Interactive Dashboard (Streamlit)
- **Type**: Streamlit web application
- **Features**: Team selector dropdown; time range slider (1876-2026); rolling averages toggle; download raw data button; franchise timeline view
- **Tool**: Streamlit + Plotly + Pandas
- **Status**: Future (~8-12hr dev time)
- **Data Source**: All CSV files in data/

## Recommended Tool Stack
| Tool | Purpose | Install Command |
|------|---------|----------------|
| Python 3.10+ | Core language | `python --version` |
| Pandas | Data manipulation | `pip install pandas` |
| Matplotlib | Static charts | `pip install matplotlib` |
| Seaborn | Statistical charts | `pip install seaborn` |
| Plotly | Interactive web charts | `pip install plotly` |
| Streamlit | Web dashboard app | `pip install streamlit` |
| Jupyter | Interactive exploration | `pip install jupyter` |

## Data Source Priority for Visualizations
1. `data/nl_all_time_records.csv` - All-time franchise totals (15 rows)
2. `data/nl_championship_trends.csv` - Era-level championship trends
3. `data/nl_historical_performance.csv` - Year-by-year NL data (150+ rows)
4. `data/nl_notable_records.csv` - Record categories with values
5. `data/nl_notable_seasons.csv` - Historic individual season data
6. `source_references.md` - Detailed source attribution for each data point

## Repository Structure
```
nl-team-trends/
├── README.md                         ← Research overview & key findings
├── DATA_PLACEHOLDER.md               ← Data file index & conventions
├── source_references.md              ← Updated source attribution (2026)
├── requirements.txt                  ← Python dependencies
├── data/
│   ├── nl_historical_performance.csv      ← Year-by-year NL champion data (1876-2025)
│   ├── nl_all_time_records.csv            ← All-time franchise records (15 NL teams)
│   ├── nl_notable_records.csv             ← Key single-season & franchise records
│   ├── nl_championship_trends.csv         ← Championship highlights by era
│   └── nl_notable_seasons.csv             ← Notable seasons with key statistics
├── docs/
│   └── data_notes.md                   ← Methodology & caveats
├── visualizations/
│   └── README.md                     ← This file: visualization roadmap
├── notebooks/                        ← Jupyter notebooks for analysis
├── scripts/                        ← Data collection & processing scripts
└── visualizations/                  ← Charts & dashboard outputs
```