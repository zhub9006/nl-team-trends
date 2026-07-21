# NL Team Trends — Scripts Directory

This directory contains Python scripts for extracting, processing, and analyzing
National League team performance data.

## Scripts

| Script | Description |
|--------|-------------|
| `get_nl_data.py` | Download Lahman DB and extract NL team-season data to CSV |
| `analyze_trends.py` | Era-based trend analysis and comparison metrics |
| `build_visualizations.py` | Generate charts from the data CSVs |

## Usage

```bash
# Install dependencies
pip install -r ../requirements.txt

# Extract NL data from Lahman database
python scripts/get_nl_data.py
```

## Data Pipeline

1. Download Lahman Baseball Database (CSV format)
2. Extract NL team-season records → `data/nl_lahman_raw.csv`
3. Aggregate by franchise → `data/nl_all_time_records.csv`
4. Compare across eras → `data/nl_championship_trends.csv`

## Requirements

- Python 3.9+
- pandas >= 1.5.0
- matplotlib >= 3.5.0
- seaborn >= 0.12.0
- plotly >= 5.10.0
