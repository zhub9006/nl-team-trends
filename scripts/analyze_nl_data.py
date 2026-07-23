#!/usr/bin/env python3
"""NL Team Trends — Historical Performance Data Analysis Script

This script loads the NL historical performance data files and generates
summary statistics for analysis and visualization.

Usage:
    python scripts/analyze_nl_data.py
"""

import pandas as pd
import json
import os

def load_all_data():
    """Load all NL data files and return a dictionary of DataFrames."""
    data = {}

    csv_files = [
        'data/nl_all_time_records.csv',
        'data/nl_pennant_winners.csv',
        'data/nl_historical_performance.csv',
        'data/nl_notable_records.csv',
        'data/nl_recent_standings.csv',
        'data/nl_recent_championships.csv',
        'data/nl_team_vs_team_summary.csv',
        'data/nl_championship_trends.csv',
        'data/nl_historical_performance_full.csv',
    ]

    for f in csv_files:
        if os.path.exists(f):
            data[os.path.basename(f).replace('.csv', '')] = pd.read_csv(f)
            print(f"Loaded {f}: {len(data[os.path.basename(f).replace('.csv', '')])} rows")

    json_files = [
        'data/nl_season_by_year.json',
        'data/nl_team_era_performance.json',
        'data/research_data_supplement.json',
    ]

    for f in json_files:
        if os.path.exists(f):
            with open(f) as fh:
                data[os.path.basename(f).replace('.json', '')] = json.load(fh)
            print(f"Loaded {f}: JSON data")

    return data


def print_summary_stats(data):
    """Print key summary statistics from the loaded data."""
    records = data.get('nl_all_time_records')
    pennants = data.get('nl_pennant_winners')

    if records is not None:
        print("\n" + "=" * 60)
        print("NL TEAM TRENDS — DATA SUMMARY")
        print("=" * 60)
        print(f"\nTotal NL franchises: {len(records)}")
        if pennants is not None:
            print(f"Total pennant years tracked: {len(pennants)}")
            print(f"Date range: {pennants['year'].min()} - {pennants['year'].max()}")

        print("\n--- Top 5 NL Teams by WS Titles ---")
        top5 = records.nlargest(5, 'ws_titles')[['team', 'ws_titles', 'wins', 'win_pct']]
        print(top5.to_string(index=False))

        print("\n--- Top 5 NL Teams by Winning Percentage (1500+ games) ---")
        high_wp = records[records['wins'] >= 10000].nlargest(5, 'win_pct')[['team', 'win_pct', 'wins']]
        print(high_wp.to_string(index=False))

        print("\n--- Most Games Played in NL History ---")
        print(records.nlargest(3, 'games')[['team', 'games', 'wins']].to_string(index=False))

    if 'nl_team_era_performance' in data:
        print("\n--- Dominant Team by Era ---")
        for era_key, era_data in data['nl_team_era_performance']['eras'].items():
            print(f"  {era_data['name']}: {era_data['dominant_team']} ({era_data['start_year']}-{era_data['end_year']})")

    if 'nl_team_vs_team' in data:
        h2h = data['nl_team_vs_team']
        print("\n--- Most One-Sided H2H Rivalries (top 5) ---")
        most_lopsided = h2h.nlargest(5, 't1_win_pct')
        for _, row in most_lopsided.iterrows():
            print(f"  {row['team_1']} vs {row['team_2']}: {row['t1_win_pct']:.3f} ({row['t1_wins']}-{row['t2_wins']})")

    print("\n" + "=" * 60)


def main():
    print("NL Team Trends — Historical Performance Data Analysis")
    print("=" * 60)
    print("Loading data files...\n")

    data = load_all_data()

    if not data:
        print("ERROR: No data files found!")
        print("Please ensure data files are in the data/ directory.")
        return

    print_summary_stats(data)

    print("\nAnalysis complete. Use Jupyter notebooks in notebooks/ for deeper analysis.")
    print("Available notebooks:")
    print("  01_eda_nl_standings.ipynb")
    print("  02_championship_trends.ipynb")
    print("  03_h2h_rivalries.ipynb")
    print("  04_win_percentage_trends.ipynb")
    print("  05_dynamic_dashboards.ipynb")


if __name__ == '__main__':
    main()