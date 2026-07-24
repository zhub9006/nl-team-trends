"""
NL Team Trends - Starter Analysis Script

Loads NL historical performance data and generates foundational visualizations.
Run with: python scripts/plot_nl_trends.py
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")  # Non-interactive backend for script usage

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
CHARTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "charts")
os.makedirs(CHARTS_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Load data files
# ---------------------------------------------------------------------------
def load_data(filename):
    """Load a CSV from the data directory and return a DataFrame."""
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        print(f"Warning: {path} not found. Skipping.")
        return None
    return pd.read_csv(path)


def plot_pennant_timeline():
    """Generate a horizontal bar chart of NL pennant winners by franchise."""
    pennants = load_data("nl_pennant_winners.csv")
    if pennants is None:
        return

    # Count pennants per team
    counts = pennants["NL_champion"].value_counts()

    fig, ax = plt.subplots(figsize=(12, 8))
    colors = plt.cm.tab20(range(len(counts)))
    bars = ax.barh(counts.index, counts.values, color=colors, edgecolor="white")
    ax.set_xlabel("Number of NL Pennants", fontsize=12)
    ax.set_title("NL Pennant Winners by Franchise (1876–2025)", fontsize=14, fontweight="bold")
    ax.invert_yaxis()

    # Add count labels on bars
    for bar, val in zip(bars, counts.values):
        ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height() / 2,
                str(val), va="center", fontsize=10, fontweight="bold")

    plt.tight_layout()
    out_path = os.path.join(CHARTS_DIR, "pennant_timeline.png")
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    print(f"Saved pennant timeline chart to {out_path}")
    plt.close()


def plot_all_time_wins_vs_losses():
    """Generate a scatter plot of all-time wins vs losses for NL franchises."""
    records = load_data("nl_all_time_records.csv")
    if records is None:
        return

    fig, ax = plt.subplots(figsize=(10, 8))
    sizes = records["games"] / 50  # Scale bubble size

    for _, row in records.iterrows():
        ax.scatter(row["losses"], row["wins"], s=sizes[row.name], alpha=0.7,
                   edgecolors="black", linewidth=0.5)
        ax.annotate(row["team"], (row["losses"], row["wins"]), fontsize=7,
                    ha="left", va="bottom", xytext=(4, 4), textcoords="offset points")

    # Add 45-degree reference line
    max_val = records["wins"].max() * 1.05
    ax.plot([0, max_val], [0, max_val], "k--", alpha=0.3, label=".500 line")

    ax.set_xlabel("Total Losses", fontsize=12)
    ax.set_ylabel("Total Wins", fontsize=12)
    ax.set_title("NL Franchise All-Time Wins vs Losses (Bubble size = games played)", fontsize=13, fontweight="bold")
    ax.legend()
    ax.set_xlim(0, max_val)
    ax.set_ylim(0, max_val)
    ax.set_aspect("equal", adjustable="datalim")

    plt.tight_layout()
    out_path = os.path.join(CHARTS_DIR, "wins_vs_losses.png")
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    print(f"Saved wins vs losses chart to {out_path}")
    plt.close()


def plot_era_dominance():
    """Generate an era-by-era championship count heatmap."""
    era = load_data("nl_era_win_pct_comparison.csv")
    pennants = load_data("nl_pennant_winners.csv")
    if era is None or pennants is None:
        return

    # Build era bins for pennant winners
    def assign_era(year):
        if year <= 1900:
            return "1876-1900"
        elif year <= 1920:
            return "1901-1920"
        elif year <= 1940:
            return "1921-1940"
        elif year <= 1960:
            return "1941-1960"
        elif year <= 1980:
            return "1961-1980"
        elif year <= 2000:
            return "1981-2000"
        elif year <= 2015:
            return "2001-2015"
        else:
            return "2016-2025"

    pennants["era"] = pennants["year"].apply(assign_era)
    pennants = pennants[pennants["ws_result"] != "No WS played"]
    pennants = pennants[pennants["year"] >= 1903]  # WS started in 1903

    ct = pd.crosstab(pennants["era"], pennants["NL_champion"])
    ct = ct.reindex(["1876-1900", "1901-1920", "1921-1940", "1941-1960",
                      "1961-1980", "1981-2000", "2001-2015", "2016-2025"])

    fig, ax = plt.subplots(figsize=(14, 6))
    sns = __import__("seaborn")
    sns.heatmap(ct, cmap="YlOrRd", annot=True, fmt="d", linewidths=0.5, ax=ax)
    ax.set_title("NL Pennant Winners by Era & Team (1903–2025)", fontsize=13, fontweight="bold")
    ax.set_ylabel("Era")
    ax.set_xlabel("NL Champion")

    plt.tight_layout()
    out_path = os.path.join(CHARTS_DIR, "era_dominance_heatmap.png")
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    print(f"Saved era dominance heatmap to {out_path}")
    plt.close()


def plot_franchise_win_pct_bar():
    """Generate a horizontal bar chart of all-time NL franchise winning percentages."""
    records = load_data("nl_all_time_records.csv")
    if records is None:
        return

    records_sorted = records.sort_values("win_pct", ascending=True)

    fig, ax = plt.subplots(figsize=(10, 8))
    colors = ["#c0392b" if w < 0.500 else "#27ae60" if w > 0.530 else "#f39c12"
              for w in records_sorted["win_pct"]]
    bars = ax.barh(records_sorted["team"], records_sorted["win_pct"], color=colors, edgecolor="white")
    ax.set_xlabel("Winning Percentage", fontsize=12)
    ax.set_title("NL Franchise All-Time Winning Percentages (through 2025)", fontsize=13, fontweight="bold")
    ax.axvline(x=0.500, color="black", linestyle="--", alpha=0.5, label=".500")
    ax.legend()

    # Add labels
    for bar, val in zip(bars, records_sorted["win_pct"]):
        ax.text(bar.get_width() + 0.002, bar.get_y() + bar.get_height() / 2,
                f"{val:.3f}", va="center", fontsize=8, fontweight="bold")

    plt.tight_layout()
    out_path = os.path.join(CHARTS_DIR, "win_pct_by_team.png")
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    print(f"Saved win % chart to {out_path}")
    plt.close()


def main():
    """Run all analysis plots."""
    print("=" * 60)
    print("NL Team Trends - Starter Analysis")
    print("=" * 60)

    print("\n1. Generating pennant timeline chart...")
    plot_pennant_timeline()

    print("\n2. Generating wins vs losses scatter plot...")
    plot_all_time_wins_vs_losses()

    print("\n3. Generating era dominance heatmap...")
    plot_era_dominance()

    print("\n4. Generating franchise winning percentage chart...")
    plot_franchise_win_pct_bar()

    print("\n" + "=" * 60)
    print("All charts saved to charts/ directory.")
    print("=" * 60)


if __name__ == "__main__":
    main()