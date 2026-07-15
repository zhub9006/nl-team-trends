#!/usr/bin/env python3
"""
NL Team Trends - Analysis & Visualization Script
==================================================
Generates charts and analysis from the historical National League datasets
in the data/ directory.

Dependencies:
    pip install pandas matplotlib seaborn plotly

Usage:
    python scripts/analyze_nl.py          # Run all analyses
    python scripts/analyze_nl.py --era     # Era comparison chart
    python scripts/analyze_nl.py --trend   # Win-loss trend per franchise
    python scripts/analyze_nl.py --h2h     # Head-to-head heatmap
    python scripts/analyze_nl.py --drought # Championship drought chart
"""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import numpy as np

# ── Paths ────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUT_DIR = os.path.join(BASE_DIR, "visualizations", "output")

os.makedirs(OUT_DIR, exist_ok=True)

# ── Style ────────────────────────────────────────────────────────────────────
sns.set_style("whitegrid")
plt.rcParams.update({
    "figure.dpi": 150,
    "savefig.dpi": 150,
    "font.family": "sans-serif",
    "font.size": 10,
})

NL_TEAMS = [
    "San Francisco Giants", "Los Angeles Dodgers", "St. Louis Cardinals",
    "Chicago Cubs", "Cincinnati Reds", "Atlanta Braves", "Pittsburgh Pirates",
    "Philadelphia Phillies", "New York Mets", "Washington Nationals",
    "San Diego Padres", "Milwaukee Brewers", "Miami Marlins",
    "Colorado Rockies", "Arizona Diamondbacks",
]

NL_COLORS = sns.color_palette("husl", len(NL_TEAMS))
TEAM_COLORS = dict(zip(NL_TEAMS, NL_COLORS))


def load_all_time() -> pd.DataFrame:
    """Load all-time franchise records."""
    path = os.path.join(DATA_DIR, "nl_all_time_records.csv")
    df = pd.read_csv(path)
    df = df.sort_values("win_pct", ascending=True)
    return df


def load_championship_trends() -> pd.DataFrame:
    """Load championship trends by era."""
    path = os.path.join(DATA_DIR, "nl_championship_trends.csv")
    df = pd.read_csv(path)
    return df


def load_recent_standings() -> pd.DataFrame:
    """Load recent standings (2020-2025)."""
    path = os.path.join(DATA_DIR, "nl_recent_standings.csv")
    df = pd.read_csv(path)
    return df


def load_pennant_winners() -> pd.DataFrame:
    """Load pennant winners (1995-2025)."""
    path = os.path.join(DATA_DIR, "nl_pennant_winners_recent.csv")
    df = pd.read_csv(path)
    return df


def load_notable_records() -> pd.DataFrame:
    """Load notable records."""
    path = os.path.join(DATA_DIR, "nl_notable_records.csv")
    df = pd.read_csv(path)
    return df


def chart_all_time_bar_chart():
    """Horizontal bar chart of franchise win percentages."""
    df = load_all_time()
    fig, ax = plt.subplots(figsize=(10, 7))
    bars = ax.barh(
        df["franchise"],
        df["win_pct"],
        color=[TEAM_COLORS.get(t, "steelblue") for t in df["franchise"]],
        edgecolor="white",
    )
    ax.set_xlabel("All-Time Win Percentage")
    ax.set_title("NL All-Time Franchise Win Percentage (through 2025)", fontsize=14, fontweight="bold")
    ax.xaxis.set_major_formatter(mticker.PercentFormatter(xmax=1, decimals=3))
    for bar, w, l in zip(bars, df["win_pct"], df["wins"]):
        ax.text(
            bar.get_width() + 0.002,
            bar.get_y() + bar.get_height() / 2,
            f'{w:.3f}  ({int(l):,}W)',
            va="center",
            fontsize=8,
        )
    plt.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "all_time_win_pct_bar.png"), bbox_inches="tight")
    plt.close(fig)
    print(f"  ✓ Saved: all_time_win_pct_bar.png")


def chart_era_comparison():
    """Era comparison bar chart of competitive balance."""
    df = load_championship_trends()
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Pennants by era
    ax1 = axes[0]
    df.plot.bar(x="era", y="most_p醛ants" if "most_p醛ants" in df.columns else "most_pEnts", ax=ax1, color="steelblue")
    ax1.set_title("Most Pennants in Era", fontweight="bold")
    ax1.set_ylabel("Pennant Count")
    ax1.set_xlabel("")
    ax1.tick_params(axis="x", rotation=30)

    # WS Titles by era
    ax2 = axes[1]
    ws_col = [c for c in df.columns if "ws" in c.lower() or "tit" in c.lower()][0]
    df.plot.bar(x="era", y=ws_col, ax=ax2, color="crimson")
    ax2.set_title("Most WS Titles in Era", fontweight="bold")
    ax2.set_ylabel("Title Count")
    ax2.set_xlabel("")
    ax2.tick_params(axis="x", rotation=30)

    plt.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "era_comparison.png"), bbox_inches="tight")
    plt.close(fig)
    print(f"  ✓ Saved: era_comparison.png")


def chart_recent_standings():
    """Recent standings comparison (2020-2025)."""
    df = load_recent_standings()
    fig, ax = plt.subplots(figsize=(12, 6))
    years = df["Year"].tolist()
    x = np.arange(len(years))
    width = 0.2

    for i, col in enumerate(["East_Champion", "Central_Champion", "West_Champion"]):
        teams = df[col].tolist()
        labels = [f"{t}" for t in teams]
        bars = ax.bar(x + i * width, [1]*len(years), width, label=col.replace("_Champion", ""), alpha=0.7)
        for bar, team in zip(bars, labels):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_y() + 0.02, team,
                    ha="center", va="bottom", fontsize=7, rotation=45)

    ax.set_xticks(x + width)
    ax.set_xticklabels(years)
    ax.set_ylim(0, 1.15)
    ax.set_ylabel("")
    ax.set_title("NL Division Champions by Year (2020–2025)", fontweight="bold")
    ax.legend(loc="upper right")
    ax.yaxis.set_visible(False)

    plt.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "recent_division_champions.png"), bbox_inches="tight")
    plt.close(fig)
    print(f"  ✓ Saved: recent_division_champions.png")


def chart_pennant_winners_timeline():
    """Pennant winners timeline (1995-2025)."""
    df = load_pennant_winners()
    fig, ax = plt.subplots(figsize=(14, 6))
    teams = df["team"].tolist()
    years = df["year"].tolist()
    y_positions = list(range(len(teams)))

    # Assign y-position by team
    unique_teams = list(dict.fromkeys(teams))
    team_y = {t: i for i, t in enumerate(unique_teams)}
    ys = [team_y[t] for t in teams]

    colors = [TEAM_COLORS.get(t, "steelblue") for t in teams]
    ax.scatter(years, ys, c=colors, s=100, zorder=5, edgecolors="white", linewidth=0.5)

    # Connect same team's appearances
    for team in unique_teams:
        mask = [i for i, t in enumerate(teams) if t == team]
        if len(mask) > 1:
            xs = [years[i] for i in mask]
            ys_line = [ys[i] for i in mask]
            ax.plot(xs, ys_line, "-", color="gray", alpha=0.4, linewidth=1)

    ax.set_yticks(list(range(len(unique_teams))))
    ax.set_yticklabels(unique_teams, fontsize=8)
    ax.set_xlabel("Year")
    ax.set_title("NL Pennant Winners Timeline (1995–2025)", fontweight="bold", fontsize=14)
    ax.set_xlim(1993, 2027)
    plt.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "pennant_winners_timeline.png"), bbox_inches="tight")
    plt.close(fig)
    print(f"  ✓ Saved: pennant_winners_timeline.png")


def chart_notable_records():
    """Bar chart of notable records."""
    df = load_notable_records()
    # Filter to numeric records only
    numeric_records = []
    labels = []
    values = []
    for _, row in df.iterrows():
        rec = row["record"]
        val = row["value"]
        # Try to extract numeric value
        if "(" in val:
            num_str = val.split("(")[1].split(")")[0]
            try:
                num_val = float(num_str.split("-")[0]) if "-" in num_str else float(num_str.strip())
            except (ValueError, IndexError):
                continue
        else:
            try:
                num_val = float(val.strip())
            except ValueError:
                continue
        labels.append(rec)
        values.append(num_val)

    if not values:
        print("  ⚠ No numeric records to chart")
        return

    fig, ax = plt.subplots(figsize=(12, 6))
    colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(values)))
    ax.barh(labels[::-1], values[::-1], color=colors[::-1], edgecolor="white")
    ax.set_xlabel("Value")
    ax.set_title("NL Notable Records", fontweight="bold", fontsize=14)
    plt.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "notable_records.png"), bbox_inches="tight")
    plt.close(fig)
    print(f"  ✓ Saved: notable_records.png")


def chart_championship_droughts():
    """Championship drought duration chart."""
    # Drafted data from the README - championship droughts
    teams = [
        "Chicago Cubs", "Cleveland Guardians", "San Diego Padres",
        "Milwaukee Brewers", "Texas Rangers (AL)", "Tampa Bay Rays (AL)",
        "Houston Astros (AL)", "Washington Nationals", "Arizona Diamondbacks",
        "Florida Marlins",
    ]
    droughts = [108, 71, 30, 29, 28, 16, 6, 16, 0, 0]  # Approximate years since last WS
    colors_list = ["#e74c3c" if d > 50 else "#f39c12" if d > 20 else "#2ecc71" for d in droughts]

    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(teams, droughts, color=colors_list, edgecolor="white")
    for bar, d in zip(bars, droughts):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5, f"{d} yr",
                ha="center", fontsize=9, fontweight="bold")
    ax.set_ylabel("Years Since Last World Series Title")
    ax.set_title("NL Championship Droughts (as of 2025)", fontweight="bold", fontsize=14)
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "championship_droughts.png"), bbox_inches="tight")
    plt.close(fig)
    print(f"  ✓ Saved: championship_droughts.png")


def main():
    print("=" * 60)
    print("  NL Team Trends – Analysis & Visualization Script")
    print("=" * 60)

    if not os.path.exists(DATA_DIR):
        print(f"  ✗ Data directory not found: {DATA_DIR}")
        print("  Please run from the repository root.")
        sys.exit(1)

    analyses = {
        "all_time": chart_all_time_bar_chart,
        "era": chart_era_comparison,
        "recent": chart_recent_standings,
        "pennant": chart_pennant_winners_timeline,
        "records": chart_notable_records,
        "drought": chart_championship_droughts,
    }

    if len(sys.argv) == 1:
        # Run all
        for name, func in analyses.items():
            print(f"\n  Running: {name}...")
            func()
    else:
        for arg in sys.argv[1:]:
            arg = arg.lstrip("--")
            if arg in analyses:
                print(f"\n  Running: {arg}...")
                analyses[arg]()
            else:
                print(f"  ⚠ Unknown analysis: {arg}")
                print(f"  Available: {', '.join(analyses.keys())}")

    print(f"\n{'=' * 60}")
    print(f"  All outputs saved to: {OUT_DIR}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()