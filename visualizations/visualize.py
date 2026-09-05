usage: visualize.py [options]

NL Team Trends — Visualization Suite
Generates charts and plots from the historical NL performance datasets.

Arguments:
  --season YEAR    Plot season standings for a specific year (e.g. 2024)
  --all-time       Generate all franchise-level plots
  --default        Run all visualization modules sequentially

Data sources (under data/):
  nl-franchise-records.csv
  season-standings.csv
  world-series-nl-champions.csv
  nl-head-to-head-matrix.csv
  nl-division-champions.csv
  nl-eras-overview.csv

Examples:
  python visualizations/visualize.py --season 1969
  python visualizations/visualize.py --season 2024
  python visualizations/visualize.py --all-time
