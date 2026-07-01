#!/usr/bin/env python3
"""NL Team Trends - Comprehensive Analysis and Visualization Generator."""

import os, sys
try:
    import pandas as pd
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import seaborn as sns
except ImportError as e:
    print(f"Missing dependency: {e}")
    sys.exit(1)

sns.set_style("whitegrid")
plt.rcParams.update({"figure.figsize": (14, 8), "figure.dpi": 150,
                     "font.size": 11, "axes.titlesize": 15, "axes.labelsize": 12})

DATA_DIR = "data"
PLOT_DIR = "plots"
os.makedirs(PLOT_DIR, exist_ok=True)

TEAM_COLORS = {
    "Atlanta Braves": "#ce1141", "Chicago Cubs": "#0e3386",
    "Cincinnati Reds": "#c6011f", "Colorado Rockies": "#300075",
    "Los Angeles Dodgers": "#005a9c", "Milwaukee Brewers": "#0a2342",
    "New York Mets": "#002244", "Philadelphia Phillies": "#e03a3e",
    "Pittsburgh Pirates": "#ffc72c", "San Diego Padres": "#27251d",
    "San Francisco Giants": "#fd5a1e", "St. Louis Cardinals": "#c41e3a",
    "Washington Nationals": "#ffcc01", "Arizona Diamondbacks": "#a71930",
    "Miami Marlins": "#00933c",
}


def load():
    hist = pd.read_csv(f"{DATA_DIR}/nl_historical_data_complete.csv")
    fr   = pd.read_csv(f"{DATA_DIR}/franchise_summary.csv")
    era  = pd.read_csv(f"{DATA_DIR}/era_analysis.csv")
    rc   = pd.read_csv("nl_champions.csv")
    try:
        comp = pd.read_csv(f"{DATA_DIR}/nl_performance_compiled.csv")
    except FileNotFoundError:
        comp = None
    return hist, fr, era, rc, comp


hist, fr, era, rc, comp = load()
print(f"Loaded: {len(hist)} historical, {len(fr)} franchises, "
      f"{len(era)} eras, {len(rc)} championship years")
if comp is not None:
    print(f"  + {len(comp)} compiled rows")


def chart_franchise_winpct():
    fig, ax = plt.subplots(figsize=(14, 8))
    sf = fr.sort_values("win_pct", ascending=True)
    y = range(len(sf))
    ax.barh(y, sf["win_pct"] * 100,
            color=[TEAM_COLORS.get(n, "#888") for n in sf["modern_name"]],
            height=0.7, edgecolor="white")
    for i, (_, r) in enumerate(sf.iterrows()):
        ax.text(r["win_pct"] * 100 + 0.3, i,
                f'{r["win_pct"]:.3f}  ({int(r["ws_titles"])} WS)',
                va="center", fontsize=9, fontweight="bold")
    ax.set_yticks(y)
    ax.set_yticklabels(sf["modern_name"], fontsize=10)
    ax.set_xlabel("All-Time Win Percentage (%)")
    ax.set_title("NL Franchise All-Time Win% - Ranked with WS Titles", fontsize=16, fontweight="bold")
    ax.set_xlim(40, 62)
    fig.tight_layout()
    fig.savefig(f"{PLOT_DIR}/chart1_alltime_winpct.png", dpi=150)
    plt.close()
    print("  OK Chart 1: Franchise Win%")


def chart_era_trends():
    era_order = ["Pre-Modern", "Dead Ball", "Live Ball",
                 "Post-War", "Expansion", "Divisional", "Modern"]
    ew = hist.groupby(["era", "modern_name"]).agg(w=("wins", "sum"),
                                                   l=("losses", "sum")).reset_index()
    ew["pct"] = ew["w"] / (ew["w"] + ew["l"])
    ew["eo"] = ew["era"].map({e: i for i, e in enumerate(era_order)})
    ew = ew.sort_values(["modern_name", "eo"])
    fig, ax = plt.subplots(figsize=(14, 8))
    for team in ew["modern_name"].unique():
        d = ew[ew["modern_name"] == team]
        if len(d) > 1:
            ax.plot(d["eo"], d["pct"] * 100, marker="o", label=team,
                    color=TEAM_COLORS.get(team, "#888"), linewidth=2, markersize=5)
    ax.set_xticks(range(len(era_order)))
    ax.set_xticklabels(era_order, rotation=30, ha="right")
    ax.set_ylabel("Win Percentage (%)")
    ax.set_title("NL Franchise Win% Trajectory by Era (1876-2025)", fontsize=16, fontweight="bold")
    ax.legend(loc="lower left", fontsize=7, ncol=2, framealpha=0.9)
    ax.set_ylim(30, 72)
    fig.tight_layout()
    fig.savefig(f"{PLOT_DIR}/chart2_era_trends.png", dpi=150)
    plt.close()
    print("  OK Chart 2: Era Win% Trends")


def chart_era_heatmap():
    pivot = hist.groupby(["era", "modern_name"]).agg(w=("wins", "sum"),
                                                       l=("losses", "sum")).reset_index()
    pivot["pct"] = pivot["w"] / (pivot["w"] + pivot["l"])
    pivot = pivot.pivot_table(index="modern_name", columns="era", values="pct") * 100
    fig, ax = plt.subplots(figsize=(12, 9))
    sns.heatmap(pivot, annot=True, fmt=".1f", cmap="RdYlGn",
                vmin=40, vmax=75, center=55, linewidths=0.5, ax=ax,
                cbar_kws={"label": "Win %"})
    ax.set_title("NL Team Win% by Era - Heatmap", fontsize=16, fontweight="bold")
    ax.set_ylabel("Franchise")
    ax.set_xlabel("Baseball Era")
    fig.tight_layout()
    fig.savefig(f"{PLOT_DIR}/chart3_era_heatmap.png", dpi=150)
    plt.close()
    print("  OK Chart 3: Era Heatmap")


def chart_championship_droughts():
    ref_year = 2025
    sf = fr.sort_values("last_championship", ascending=True).copy()
    def calc_drought(r):
        lc = r["last_championship"]
        if pd.notna(lc) and lc != "-":
            return ref_year - int(lc)
        return ref_year - int(r["first_season"])
    sf["drought"] = sf.apply(calc_drought, axis=1).astype(int)
    sf = sf.sort_values("drought", ascending=True)
    colors = ["#d62728" if d > 20 else "#ff7f0e" if d > 10 else "#2ca02c" for d in sf["drought"]]
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.barh(range(len(sf)), sf["drought"], color=colors, height=0.7)
    ax.set_yticks(range(len(sf)))
    ax.set_yticklabels(sf["modern_name"], fontsize=10)
    ax.set_xlabel("Years Since Last World Series Title")
    ax.set_title(f"NL Championship Drought Tracker ({ref_year})", fontsize=16, fontweight="bold")
    for i, (_, r) in enumerate(sf.iterrows()):
        ws = int(r["ws_titles"]) if pd.notna(r["ws_titles"]) else 0
        ax.text(r["drought"] + 0.5, i, f'{r["drought"]}y ({ws} WS)',
                va="center", fontsize=9)
    ax.set_xlim(0, sf["drought"].max() * 1.2)
    fig.tight_layout()
    fig.savefig(f"{PLOT_DIR}/chart4_championship_droughts.png", dpi=150)
    plt.close()
    print("  OK Chart 4: Championship Droughts")


def chart_pennant_timeline():
    rc2 = rc.dropna(subset=["Year"]).copy()
    rc2["Year"] = pd.to_numeric(rc2["Year"], errors="coerce").astype(int)
    fig, ax = plt.subplots(figsize=(18, 8))
    teams = sorted(rc2["Champion"].unique())
    y_positions = {t: i for i, t in enumerate(teams)}
    for _, row in rc2.iterrows():
        team = row["Champion"]
        y = y_positions[team]
        color = TEAM_COLORS.get(team, "#888")
        ax.plot(row["Year"], y, "o", color=color, markersize=12,
                markeredgecolor="white", markeredgewidth=1, zorder=5)
        ax.vlines(row["Year"], y - 0.4, y + 0.4, color=color, linewidth=2)
    ax.set_yticks(range(len(teams)))
    ax.set_yticklabels(teams, fontsize=10)
    ax.set_xlabel("Season")
    ax.set_title("NL Championship Winners Timeline - 1960 to 2025", fontsize=16, fontweight="bold")
    ax.set_xlim(1959, 2026)
    fig.tight_layout()
    fig.savefig(f"{PLOT_DIR}/chart5_pennant_timeline.png", dpi=150)
    plt.close()
    print("  OK Chart 5: Pennant Timeline")


def chart_best_worst():
    if comp is None:
        print("  WARN: compiled data not available")
        return
    best = comp[comp["wins"] + comp["losses"] >= 154].nlargest(5, "win_pct")
    worst = comp[comp["wins"] + comp["losses"] >= 154].nsmallest(5, "win_pct")
    fig, axes = plt.subplots(1, 2, figsize=(18, 8))
    labels = [f"{r['modern_name']} ({r['season']})" for _, r in best.iterrows()]
    axes[0].barh(range(len(best)), best["win_pct"] * 100, color="green", height=0.6)
    axes[0].set_yticks(range(len(best)))
    axes[0].set_yticklabels(labels, fontsize=8)
    axes[0].set_xlabel("Win %")
    axes[0].set_title("Top 5 Best Win% Seasons (>=154 G)", fontsize=13, fontweight="bold", color="green")
    axes[0].grid(True, alpha=0.3)
    labels = [f"{r['modern_name']} ({r['season']})" for _, r in worst.iterrows()]
    axes[1].barh(range(len(worst)), worst["win_pct"] * 100, color="red", height=0.6)
    axes[1].set_yticks(range(len(worst)))
    axes[1].set_yticklabels(labels, fontsize=8)
    axes[1].set_xlabel("Win %")
    axes[1].set_title("Top 5 Worst Win% Seasons (>=154 G)", fontsize=13, fontweight="bold", color="red")
    axes[1].grid(True, alpha=0.3)
    fig.suptitle("NL Key Performance Extremes", fontsize=16, fontweight="bold", y=1.02)
    fig.tight_layout()
    fig.savefig(f"{PLOT_DIR}/chart6_best_worst_seasons.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("  OK Chart 6: Best/Worst Seasons")


def chart_era_dominance():
    if comp is None:
        print("  WARN: compiled data not available")
        return
    pennant_data = comp[comp["pennant"] == "Yes"].groupby(
        ["modern_name", "era"]).size().reset_index(name="pennants")
    pivot = pennant_data.pivot_table(index="modern_name", columns="era",
                                      values="pennants", fill_value=0)
    fig, ax = plt.subplots(figsize=(14, 9))
    sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlOrRd",
                linewidths=0.5, ax=ax, cbar_kws={"label": "Pennant Count"})
    ax.set_title("NL Pennant Dominance by Franchise and Era", fontsize=16, fontweight="bold")
    ax.set_ylabel("Franchise")
    ax.set_xlabel("Baseball Era")
    fig.tight_layout()
    fig.savefig(f"{PLOT_DIR}/chart7_era_pennant_heatmap.png", dpi=150)
    plt.close()
    print("  OK Chart 7: Era Dominance Heatmap")


def chart_championship_run_quality():
    if comp is None:
        print("  WARN: compiled data not available")
        return
    champions = comp[comp["ws_title"].isin(["Yes", "Indeed"])]
    fig, ax = plt.subplots(figsize=(12, 8))
    plotted = set()
    for _, row in champions.iterrows():
        team = row["modern_name"]
        if team in plotted:
            continue
        plotted.add(team)
        color = TEAM_COLORS.get(team, "#888")
        ax.scatter(row["wins"] + row["losses"], row["win_pct"] * 100,
                   s=150, color=color, edgecolors="white", linewidth=1.5,
                   zorder=5, label=team)
        ax.annotate(str(row["season"]),
                    (row["wins"] + row["losses"], row["win_pct"] * 100),
                    fontsize=7, xytext=(5, 5), textcoords="offset points")
    ax.set_xlabel("Total Games in Championship Season")
    ax.set_ylabel("Championship Season Win %")
    ax.set_title("NL Championship Run Quality - Win% vs Season Length", fontsize=16, fontweight="bold")
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=8, ncol=2, loc="lower right")
    fig.tight_layout()
    fig.savefig(f"{PLOT_DIR}/chart8_championship_run_quality.png", dpi=150)
    plt.close()
    print("  OK Chart 8: Championship Run Quality")


def chart_playoff_frequency():
    team_years = rc.groupby("Champion")["Year"].apply(list)
    appearances = {team: len(years) for team, years in team_years.items()}
    title_counts = rc["Champion"].value_counts().to_dict()
    sf = pd.DataFrame({
        "team": list(appearances.keys()),
        "titles": [title_counts.get(t, 0) for t in appearances.keys()],
        "playoff_appearances": list(appearances.values()),
    }).sort_values("titles", ascending=True)
    fig, ax = plt.subplots(figsize=(14, 8))
    y = range(len(sf))
    ax.barh(y, sf["playoff_appearances"],
            color=[TEAM_COLORS.get(n, "#888") for n in sf["team"]],
            height=0.7, alpha=0.8)
    for i, (_, r) in enumerate(sf.iterrows()):
        ax.text(r["playoff_appearances"] + 0.2, i,
                f'{int(r["playoff_appearances"])} pennants  ({int(r["titles"])} WS)',
                va="center", fontsize=9, fontweight="bold")
    ax.set_yticks(y)
    ax.set_yticklabels(sf["team"], fontsize=10)
    ax.set_xlabel("Pennant Titles (NLCS Appearances 1969-2025)")
    ax.set_title("NL Playoff Appearance Frequency", fontsize=16, fontweight="bold")
    ax.set_xlim(0, sf["playoff_appearances"].max() * 1.3)
    fig.tight_layout()
    fig.savefig(f"{PLOT_DIR}/chart9_playoff_frequency.png", dpi=150)
    plt.close()
    print("  OK Chart 9: Playoff Frequency")


def chart_era_comparison():
    if comp is None:
        print("  WARN: compiled data not available")
        return
    era_top = comp.groupby("era").apply(lambda g: g.nlargest(1, "win_pct")).reset_index(drop=True)
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.bar(range(len(era_top)), era_top["win_pct"] * 100,
           color=[TEAM_COLORS.get(t, "#888") for t in era_top["modern_name"]],
           edgecolor="white")
    ax.set_xticks(range(len(era_top)))
    ax.set_xticklabels(era_top["era"], rotation=30, ha="right")
    ax.set_ylabel("Win %")
    ax.set_title("NL Most Dominant Team by Era - Win% Comparison", fontsize=16, fontweight="bold")
    for i in range(len(era_top)):
        t = era_top["modern_name"].iloc[i]
        w = era_top["win_pct"].iloc[i]
        s = era_top["season"].iloc[i]
        wi = int(era_top["wins"].iloc[i])
        li = int(era_top["losses"].iloc[i])
        ax.text(i, w * 100 + 1.5, f"{t} ({s})\n{wi}-{li}",
                ha="center", fontsize=8, fontweight="bold")
    ax.set_ylim(0, 82)
    fig.tight_layout()
    fig.savefig(f"{PLOT_DIR}/chart10_era_comparison.png", dpi=150)
    plt.close()
    print("  OK Chart 10: Era Comparison")


def print_summary():
    print("\n" + "=" * 64)
    print("  NL TEAM TRENDS - STATISTICAL SUMMARY")
    print("=" * 64)
    print(f"\n  Coverage: {hist['season'].min()}-{hist['season'].max()} "
          f"({hist['season'].nunique()} seasons, {fr['franchise'].nunique()} franchises)")
    print(f"\n  Top 5 All-Time Win% Franchises:")
    for _, r in fr.sort_values("win_pct", ascending=False).head(5).iterrows():
        print(f"    {r['modern_name']:25s} {r['win_pct']:.3f}  "
              f"({int(r['ws_titles'])} WS, last: {r['last_championship']})")
    if comp is not None:
        print(f"\n  Best 3 Seasons (compiled data):")
        for _, r in comp.nlargest(3, "win_pct").iterrows():
            print(f"    {r['modern_name']} {r['season']}: "
                  f"{int(r['wins'])}-{int(r['losses'])} ({r['win_pct']:.3f})")
        champs = comp[comp["ws_title"].isin(["Yes", "Indeed"])].sort_values("season")
        print(f"\n  Championship Seasons ({len(champs)}):")
        for _, r in champs.iterrows():
            print(f"    {r['season']}  {r['modern_name']:25s}  "
                  f"{int(r['wins'])}-{int(r['losses'])} ({r['win_pct']:.3f})")
    print("\n" + "=" * 64)


if __name__ == "__main__":
    print("\n  NL Team Trends - Comprehensive Analysis and Visualization Generator")
    print("-" * 64 + "\n  Generating charts...\n")
    chart_franchise_winpct()
    chart_era_trends()
    chart_era_heatmap()
    chart_championship_droughts()
    chart_pennant_timeline()
    chart_best_worst()
    chart_era_dominance()
    chart_championship_run_quality()
    chart_playoff_frequency()
    chart_era_comparison()
    print_summary()
    print(f"\n  Charts saved to: {PLOT_DIR}/\n")