"""
NL Team Trends - Visualization Suite
====================================
Generates charts and plots from the historical NL performance datasets.

Usage:
    python visualizations/visualize.py --season 2024
    python visualizations/visualize.py --all-time
    python visualizations/visualize.py --default

Data sources (under data/):
    - nl-franchise-records.csv
    - season-standings.csv
    - world-series-nl-champions.csv
    - nl-head-to-head-matrix.csv
    - nl-division-champions.csv
    - nl-eras-overview.csv

Author: zhub9006
Updated: September 2026
"""

import argparse
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

DATA_DIR = Path(__file__).parent.parent / "data"
OUT_DIR = Path(__file__).parent / "output"
OUT_DIR.mkdir(exist_ok=True)
sns.set_theme(style="whitegrid")


def load_csv(filename: str) -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / filename)


def plot_season_standings(year: int):
    df = load_csv("season-standings.csv")
    subset = df[df["year"] == year].sort_values("wins", ascending=True)
    if subset.empty:
        print(f"No data for year {year}. Available: {sorted(df['year'].unique())}")
        return
    fig, ax = plt.subplots(figsize=(11, 0.5 * len(subset)))
    ax.barh(subset["team"], subset["wins"], color="#1F77B4")
    ax.set_xlabel("Regular Season Wins")
    ax.set_title(f"NL Team Standings - {year}")
    ax.set_xlim(0, subset["wins"].max() + 10)
    for b in ax.patches:
        ax.annotate(f'{int(b.get_width())}', (b.get_width(), b.get_y()+b.get_height()/2),
                    xytext=(3,0), textcoords="offset points", ha="left", va="center", fontsize=9)
    ax.invert_yaxis()
    outfile = OUT_DIR / f"nl_standings_{year}.png"
    fig.tight_layout(); fig.savefig(outfile, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {outfile}")


def plot_franchise_win_pct():
    df = load_csv("nl-franchise-records.csv").sort_values("win_pct", ascending=True)
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.barh(df["franchise_name"], df["win_pct"].astype(float), color=plt.cm.viridis(np.linspace(0.1,0.9,len(df))))
    ax.set_xlabel("All-Time Win Percentage")
    ax.set_title("NL Franchise All-Time Win % (1876-2025)")
    ax.axvline(0.5, color="red", linestyle="--", alpha=0.5)
    for b in ax.patches:
        ax.annotate(f'{b.get_width():.3f}', (b.get_width(), b.get_y()+b.get_height()/2),
                    xytext=(3,0), textcoords="offset points", ha="left", va="center", fontsize=9)
    outfile = OUT_DIR / "nl_franchise_winpct.png"
    fig.tight_layout(); fig.savefig(outfile, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {outfile}")


def plot_franchise_ws_titles():
    df = load_csv("nl-franchise-records.csv").sort_values("ws_titles", ascending=True)
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.barh(df["franchise_name"], df["ws_titles"].astype(int), color="#1F77B4")
    ax.set_xlabel("World Series Titles")
    ax.set_title("NL Franchise World Series Titles (All-Time)")
    for b in ax.patches:
        if b.get_width() > 0:
            ax.annotate(f'{int(b.get_width())}', (b.get_width(), b.get_y()+b.get_height()/2),
                        xytext=(3,0), textcoords="offset points", ha="left", va="center", fontsize=9)
    outfile = OUT_DIR / "nl_franchise_ws_titles.png"
    fig.tight_layout(); fig.savefig(outfile, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {outfile}")


def plot_world_series_outcomes():
    df = load_csv("world-series-nl-champions.csv")
    valid = df[df["ws_result"].str.contains("Won|Lost", case=False, na=False)].copy()
    valid["decade"] = (valid["year"].astype(int)//10)*10
    nl_won = valid[valid["ws_result"].str.contains("Won", case=False)]["decade"].value_counts().sort_index()
    nl_lost = valid[valid["ws_result"].str.contains("Lost", case=False)]["decade"].value_counts().sort_index()
    decades = sorted(set(nl_won.index)|set(nl_lost.index))
    wv = [nl_won.get(d,0) for d in decades]
    lv = [nl_lost.get(d,0) for d in decades]
    fig, ax = plt.subplots(figsize=(14,5))
    x = np.arange(len(decades))
    ax.bar(x-0.175, wv, 0.35, color="#A8322D", label="NL Won WS")
    ax.bar(x+0.175, lv, 0.35, color="#325A8D", label="NL Lost WS")
    ax.set_xticks(x)
    ax.set_xticklabels([f"{d}s" for d in decades])
    ax.set_xlabel("Decade"); ax.set_ylabel("World Series Count")
    ax.set_title("NL World Series Outcomes by Decade (1903-2025)")
    ax.legend()
    for i,v in enumerate(wv):
        if v>0: ax.annotate(str(v),(i-0.175,v),ha="center",va="bottom")
    for i,v in enumerate(lv):
        if v>0: ax.annotate(str(v),(i+0.175,v),ha="center",va="bottom")
    outfile = OUT_DIR / "nl_ws_outcomes_by_decade.png"
    fig.tight_layout(); fig.savefig(outfile, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {outfile}")


def plot_division_champions():
    df = load_csv("nl-division-champions.csv")
    dm = pd.crosstab(df["champion"], df["division"])
    fig, ax = plt.subplots(figsize=(12,12))
    sns.heatmap(dm, annot=True, fmt="d", cmap="YlGn", ax=ax, linewidths=0.5)
    ax.set_title("NL Division Champions (1969-2025)")
    ax.set_xlabel("Division"); ax.set_ylabel("Franchise")
    plt.xticks(rotation=45, ha="right"); plt.yticks(rotation=0)
    outfile = OUT_DIR / "nl_division_champions_heatmap.png"
    fig.tight_layout(); fig.savefig(outfile, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {outfile}")


def run_all():
    print("="*60)
    print("NL Team Trends - Full Visualization Suite")
    print("="*60)
    plot_franchise_win_pct()
    plot_franchise_ws_titles()
    plot_world_series_outcomes()
    plot_division_champions()
    for yr in [1876,1941,1954,1961,1969,1975,1987,1989,1998,2001,2015,2020,2024,2025]:
        plot_season_standings(yr)
    print("="*60)
    print(f"All plots in: {OUT_DIR}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--season", type=int, help="Year for season standings")
    p.add_argument("--all-time", action="store_true", help="All franchise plots")
    p.add_argument("--default", action="store_true", help="Run everything")
    a = p.parse_args()
    if a.season:
        plot_season_standings(a.season)
    elif a.all_time:
        plot_franchise_win_pct(); plot_franchise_ws_titles()
    elif a.default:
        run_all()
    else:
        p.print_help()
