# scripts/ — Data Loading & Analysis Utilities

This directory contains Python scripts to load, explore, and visualize the NL team performance data stored in `../data/`.

## Files

| File | Purpose |
|------|---------|
| `data_loader.py` | Loads all CSV files from `../data/`, prints summary stats, filters by team/era, and generates quick charts |

## Usage

```bash
# From the repo root
pip install -r requirements.txt

# Load all data and print summary statistics
python scripts/data_loader.py

# Filter for a specific team
python scripts/data_loader.py --team Dodgers

# Generate quick matplotlib charts (saved to ./charts/)
python scripts/data_loader.py --chart

# Combine options
python scripts/data_loader.py --team Cardinals --chart
```

## Output

- Console summary of all data files loaded
- Team-specific filtering results
- Visualizations saved to `./charts/` (PNG)

Requirements: pandas, matplotlib (both play nicely with seaborn / plotly from `requirements.txt`)
