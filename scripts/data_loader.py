#!/usr/bin/env python3
"""
NL Team Trends — Data Loader & Explorer
=========================================
Utility script to load the CSV data files in data/ and perform
basic exploratory analysis on National League team performance.

Dependencies: pandas, matplotlib, seaborn, plotly
Install: pip install -r requirements.txt

Usage:
    python scripts/data_loader.py               # Load & print summary stats
    python scripts/data_loader.py --chart        # Generate quick charts
    python scripts/data_loader.py --team LAD     # Filter by team
    python scripts/data_loader.py --era 2010s    # Filter by era
"""

import argparse
import os
import sys

try:
    import pandas as pd
except ImportError:
    print("Error: pandas is required. Run: pip install pandas")
    sys.exit(1)

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

FILES = {
    "historical_performance": "nl_historical_performance.csv",
    "all_time_records": "nl_all_time_records.csv",
    "pennant_winners": "nl_pennant_winners.csv",
    "championship_trends": "nl_championship_trends.csv",
    "notable_records": "nl_notable_records.csv",
    "notable_seasons": "nl_notable_seasons.csv",
    "recent_standings": "nl_recent_standings.csv",
    "team_vs_team": "nl_team_vs_team_summary.csv",
}


def load_all():
    """Load all CSV files into a dict of DataFrames."""
    dataframes = {}
    for key, filename in FILES.items():
        path = os.path.join(DATA_DIR, filename)
        if os.path.exists(path):
            dataframes[key] = pd.read_csv(path)
            print(f"✓ Loaded {filename} → {len(dataframes[key])} rows")
        else:
            print(f"✗ Missing {filename}")
    return dataframes


def summary_stats(dataframes):
    """Print summary statistics for key data files."""
    print("\n" + "=" * 60)
    print("NL TEAM TRENDS — DATA SUMMARY")
    print("=" * 60)

    if "historical_performance" in dataframes:
        df = dataframes["historical_performance"]
        print(f"\n📊 Historical Performance: {len(df)} seasons (1876–present)")
        print(f"   NL Champs: {df['NL_Champion'].nunique()} distinct teams")
        print(f"   Eras:    {df['Era'].unique()}")
        print(f"   Best W%: {df['Champion_WPct'].max():.3f} (Champion)")

    if "all_time_records" in dataframes:
        df = dataframes["all_time_records"]
        print(f"\n🏆 All-Time Records: {len(df)} NL franchises")
        print(f"   Most WS Titles: {df.loc[df['WS_Titles'].idxmax(), 'Franchise']} ({df['WS_Titles'].max()})")
        print(f"   Most Wins:      {df.loc[df['Total_Wins'].idxmax(), 'Franchise']} ({df['Total_Wins'].max()})")
        print(f"   Highest Win%:   {df.loc[df['Win_Pct'].idxmax(), 'Franchise']} ({df['Win_Pct'].max():.3f})")

    if "recent_standings" in dataframes:
        df = dataframes["recent_standings"]
        print(f"\n📅 Recent Standings: {df['year'].nunique()} seasons (2020–2025)")
        print(f"   Teams tracked: {df['team'].nunique()}")
        print(f"   WS Champions:  {df[df['ws_result'] == 'Won Champions']['team'].nunique()}")


def filter_by_team(dataframes, team_name):
    """Filter recent standings and historical data for a specific team."""
    if "recent_standings" in dataframes:
        df = dataframes["recent_standings"]
        team_df = df[df["team"].str.contains(team_name, case=False, na=False)]
        if not team_df.empty:
            print(f"\n🔍 Recent standings for '{team_name}':")
            print(team_df.to_string(index=False))
        else:
            print(f"No recent standings found for '{team_name}'")

    if "all_time_records" in dataframes:
        df = dataframes["all_time_records"]
        team_df = df[df["Franchise"].str.contains(team_name, case=False, na=False)]
        if not team_df.empty:
            print(f"\n🏆 All-time record for '{team_name}':")
            for _, row in team_df.iterrows():
                print(f"   WS: {row['WS_Titles']} | W: {row['Total_Wins']} | L: {row['Total_Losses']} | Win%: {row['Win_Pct']:.3f}")


def quick_charts(dataframes):
    """Generate simple matplotlib charts from the data files."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not installed. Run: pip install matplotlib")
        return

    os.makedirs("charts", exist_ok=True)

    # Chart 1: All-time franchise wins (top 15 NL)
    if "all_time_records" in dataframes:
        df = dataframes["all_time_records"].sort_values("Total_Wins", ascending=True)
        fig, ax = plt.subplots(figsize=(10, 6))
        colors = ["#005A9C" if w > 10000 else "#FD5A1E" for w in df["Total_Wins"]]
        ax.barh(df["Franchise"], df["Total_Wins"], color=colors)
        ax.set_xlabel("Total Wins")
        ax.set_title("All-Time NL Franchise Wins (1876–2026)")
        plt.tight_layout()
        path = "charts/all_time_wins.png"
        plt.savefig(path, dpi=150)
        print(f"  Chart saved: {path}")
        plt.close()

    # Chart 2: Championship droughts
    if "all_time_records" in dataframes:
        df = dataframes["all_time_records"]
        df["Championship_Drought"] = df["WS_Titles"].apply(
            lambda x: "Has Won WS" if x > 0 else "No WS Title"
        )
        fig, ax = plt.subplots(figsize=(10, 6))
        counts = df["Championship_Drought"].value_counts()
        ax.pie(counts, labels=counts.index, autopct="%1.0f%%",
               colors=["#FD5A1E", "#005A9C"])
        ax.set_title("NL Franchises With/Without World Series Titles")
        plt.tight_layout()
        path = "charts/ws_drought.png"
        plt.savefig(path, dpi=150)
        print(f"  Chart saved: {path}")
        plt.close()

    # Chart 3: Recent standings wins by year
    if "recent_standings" in dataframes:
        df = dataframes["recent_standings"]
        fig, ax = plt.subplots(figsize=(10, 6))
        for team in df["team"].unique():
            team_data = df[df["team"] == team]
            ax.plot(team_data["year"], team_data["wins"], marker="o", label=team, linewidth=1.5)
        ax.set_xlabel("Year")
        ax.set_ylabel("Wins")
        ax.set_title("NL Team Win Totals (2020–2025)")
        ax.legend(fontsize=8, loc="upper right")
        plt.tight_layout()
        path = "charts/recent_standings.png"
        plt.savefig(path, dpi=150)
        print(f"  Chart saved: {path}")
        plt.close()


def main():
    parser = argparse.ArgumentParser(
        description="NL Team Trends — Data Loader & Explorer"
    )
    parser.add_argument("--chart", action="store_true", help="Generate quick charts")
    parser.add_argument("--team", type=str, default=None, help="Filter by team name")
    parser.add_argument("--era", type=str, default=None, help="Filter by era (e.g., 2010s)")
    args = parser.parse_args()

    print("Loading NL Team Trends data...\n")
    dataframes = load_all()

    if not dataframes:
        print("No data files found. Are you in the repo root?")
        sys.exit(1)

    summary_stats(dataframes)

    if args.team:
        filter_by_team(dataframes, args.team)

    if args.chart:
        quick_charts(dataframes)

    print("\n✅ Done.")


if __name__ == "__main__":
    main()
