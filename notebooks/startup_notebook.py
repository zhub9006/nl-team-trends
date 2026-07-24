"""
NL Team Trends - Starter Notebook

This script can be run as a Jupyter notebook or a Python script.
It loads NL historical data and produces key summary statistics.

To run as a notebook:
    jupyter notebook notebooks/startup_notebook.py
To run as a script:
    python notebooks/startup_notebook.py
"""

import os
import pandas as pd
import json

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")


def load_csv(filename):
    path = os.path.join(DATA_DIR, filename)
    return pd.read_csv(path) if os.path.exists(path) else None


def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    return json.load(open(path)) if os.path.exists(path) else None


def main():
    print("=" * 65)
    print("NL Team Trends - Data Explorer")
    print("=" * 65)

    # 1. All-time records
    records = load_csv("nl_all_time_records.csv")
    if records is not None:
        print("\n--- All-Time NL Franchise Records (top 5 by WS titles) ---")
        print(records.sort_values("ws_titles", ascending=False)
              [["team", "ws_titles", "wins", "losses", "win_pct"]]
              .head().to_string(index=False))

    # 2. Pennant winners
    pennants = load_csv("nl_pennant_winners.csv")
    if pennants is not None:
        print("\n--- Pennant Winners by Franchise (top 5) ---")
        print(pennants["NL_champion"].value_counts().head().to_string())

    # 3. Era comparison
    era = load_csv("nl_era_win_pct_comparison.csv")
    if era is not None:
        print("\n--- Era Comparison ---")
        print(era[["era", "dominant_team", "pennant_count", "ws_titles"]]
              .to_string(index=False))

    # 4. Key records
    notable = load_csv("nl_notable_records.csv")
    if notable is not None:
        print("\n--- Notable Records ---")
        for _, row in notable.iterrows():
            print(f"  {row['category']}: {row['record_holder']} - {row['value']}" +
                  (f" ({row['year']})" if pd.notna(row.get("year")) else ""))

    # 5. Championship frequency
    season_json = load_json("nl_season_by_year.json")
    if season_json is not None:
        print("\n--- Championship Frequency by Franchise ---")
        for team, info in season_json.get("championship_frequency", {}).items():
            print(f"  {team}: {info['ws_titles']} WS titles, {info['pennants']} pennants")

    # 6. 23-year span trends
    trends = load_csv("nl_recent_trends_2000_2024.csv")
    if trends is not None:
        print("\n--- Best NL Teams by 23-Year Span (2000-2024) ---")
        print(trends[["team", "win_pct", "wins", "losses", "games"]]
              .sort_values("win_pct", ascending=False)
              .head(5).to_string(index=False))

    print("\n" + "=" * 65)
    print("Explore more in the data/ directory or run scripts/plot_nl_trends.py")
    print("=" * 65)


if __name__ == "__main__":
    main()
