#!/usr/bin/env python3
"""
NL Team Trends — Analysis Script

Load NL historical performance data and compute summary statistics,
era comparisons, and trend indicators. Designed to be run from the
repository root.

Usage:
    python scripts/analyze_nl_trends.py
"""

import json
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def load_all_time_records() -> pd.DataFrame:
    """Load all-time NL franchise records."""
    return pd.read_csv(DATA_DIR / "nl_all_time_records.csv")


def load_pennant_winners() -> pd.DataFrame:
    """Load NL pennant winners 1876–2025."""
    return pd.read_csv(DATA_DIR / "nl_pennant_winners.csv")


def load_historical_performance() -> pd.DataFrame:
    """Load key historical performance seasons."""
    return pd.read_csv(DATA_DIR / "nl_historical_performance.csv")


def load_team_vs_team_summary() -> pd.DataFrame:
    """Load H2H rivalry summary data."""
    return pd.read_csv(DATA_DIR / "nl_team_vs_team_summary.csv")


def load_recent_trends() -> pd.DataFrame:
    """Load 23-year span trend data (StatMuse, 2000–2024)."""
    return pd.read_csv(DATA_DIR / "nl_recent_trends_2000_2024.csv")


def load_season_by_year() -> dict:
    """Load season-by-year JSON data."""
    with open(DATA_DIR / "nl_season_by_year.json") as f:
        return json.load(f)


def print_summary(df: pd.DataFrame) -> None:
    """Print summary statistics from all-time records."""
    print("=" * 60)
    print("NL ALL-TIME FRANCHISE RECORDS SUMMARY")
    print("=" * 60)
    print(f"Total franchises: {len(df)}")
    print(f"Most wins: {df['wins'].max()} ({df.loc[df['wins'].idxmax(), 'team']})")
    print(f"Highest win %: {df['win_pct'].max():.3f} ({df.loc[df['win_pct'].idxmax(), 'team']})")
    print(f"Most WS titles: {df['ws_titles'].max()} ({df.loc[df['ws_titles'].idxmax(), 'team']})")
    print()


def print_era_comparison(df: pd.DataFrame) -> None:
    """Print pennant-winning team by decade."""
    print("=" * 60)
    print("NL PENNANT WINNERS BY DECADE")
    print("=" * 60)
    df["decade"] = (df["year"] // 10) * 10
    counts = df.groupby("decade")["NL_champion"].value_counts()
    for (decade, team), count in counts.items():
        print(f"  {decade}s — {team}: {count} pennant(s)")
    print()


def print_top_rivalries(df: pd.DataFrame) -> None:
    """Print the most one-sided H2H rivalries."""
    print("=" * 60)
    print("MOST ONE-SIDED H2H RIVALRIES")
    print("=" * 60)
    df["total"] = df["t1_wins"] + df["t2_wins"]
    df["dominance"] = (df["t1_wins"] / df["total"] * 100).round(1)
    for _, row in df.nlargest(5, "dominance").iterrows():
        print(f"  {row['team_1']} vs {row['team_2']}: {row['dominance']:.1f}% ({row['t1_wins']}-{row['t2_wins']})")
    print()


def main() -> None:
    """Run all analysis routines."""
    print("\n🔍 NL Team Trends — Analysis Output 🔍\n")

    print_summary(load_all_time_records())
    print_era_comparison(load_pennant_winners())
    print_top_rivalries(load_team_vs_team_summary())

    trends = load_recent_trends()
    print("=" * 60)
    print("BEST NL TEAMS BY 23-YEAR SPAN (StatMuse, 2000–2024)")
    print("=" * 60)
    for _, row in trends.sort_values("win_pct", ascending=False).iterrows():
        print(f"  {row['team']:20s}  {row['record']:12s}  {row['win_pct']:.3f}")
    print()

    data = load_season_by_year()
    print("=" * 60)
    print("SAMPLE HISTORICAL SEASONS")
    print("=" * 60)
    for year, info in data.get("sample_seasons", {}).items():
        print(f"  {year}: {info['champion']} ({info['record']}) — {info['notes']}")
    print()

    print("✅ Analysis complete.")


if __name__ == "__main__":
    main()