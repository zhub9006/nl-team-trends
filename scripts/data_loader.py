import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import os

DATA_DIR = Path("../data")
CHARTS_DIR = Path("../charts")
os.makedirs(CHARTS_DIR, exist_ok=True)


def load_pennant_winners():
    return pd.read_csv(DATA_DIR / "nl_pennant_winners.csv")


def load_all_time_records():
    return pd.read_csv(DATA_DIR / "nl_all_time_records.csv")


def load_championship_trends():
    return pd.read_csv(DATA_DIR / "nl_championship_trends.csv")


def load_notable_records():
    return pd.read_csv(DATA_DIR / "nl_notable_records.csv")


def load_recent_standings():
    return pd.read_csv(DATA_DIR / "nl_recent_standings.csv")


def load_team_h2h():
    return pd.read_csv(DATA_DIR / "nl_team_vs_team_summary.csv")


def generate_all_charts():
    sns.set_style("whitegrid")

    # Pennant Winners by Franchise
    pennant_winner = load_pennant_winners()
    counts = pennant_winner["Team"].value_counts()
    plt.figure(figsize=(12, 6))
    counts.plot(kind="bar", color="steelblue")
    plt.title("NL Pennant Winners by Franchise (1876-1968)")
    plt.xlabel("Team")
    plt.ylabel("Pennant Titles")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "pennant_winners_by_franchise.png", dpi=150)
    plt.close()

    # Franchise Win % Bar Chart
    all_time = load_all_time_records()
    all_time_sorted = all_time.sort_values("WinPct", ascending=True)
    plt.figure(figsize=(12, 8))
    plt.barh(all_time_sorted["Team"], all_time_sorted["WinPct"], color="steelblue")
    plt.xlabel("Winning Percentage")
    plt.title("NL Franchise All-Time Winning Percentage")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "win_pct_by_franchise.png", dpi=150)
    plt.close()

    # Recent Standings Heatmap
    recent = load_recent_standings()
    numeric_cols = recent.select_dtypes(include="number").columns
    plt.figure(figsize=(10, 6))
    sns.heatmap(recent.set_index("Year")[numeric_cols], annot=True, cmap="RdYlGn", fmt="d")
    plt.title("NL Recent Division Standings (2020-2025)")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "recent_standings_heatmap.png", dpi=150)
    plt.close()


def main():
    print("NL Team Trends — Data Loader & Analysis")
    print("=" * 50)
    pennant_winner = load_pennant_winners()
    print(f"Pennant Winners: {len(pennant_winner)} records")
    all_time = load_all_time_records()
    print(f"All-Time Records: {len(all_time)} teams")
    print("\nGenerating charts...")
    generate_all_charts()
    print("Analysis complete!")


if __name__ == "__main__":
    main()