import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import os

DATA_DIR = Path("../data")
CHARTS_DIR = Path("../charts")
os.makedirs(CHARTS_DIR, exist_ok=True)

# ---- Data Loaders ----

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

def load_historical_performance():
    return pd.read_csv(DATA_DIR / "nl_historical_performance.csv")

def load_seasonal_standings():
    return pd.read_csv(DATA_DIR / "nl_seasonal_standings.csv")

def load_divisional_titles():
    return pd.read_csv(DATA_DIR / "nl_divisional_titles.csv")

def load_wild_card_winners():
    return pd.read_csv(DATA_DIR / "nl_wild_card_winners.csv")

# ---- Chart Generators ----

def generate_all_charts():
    sns.set_style("whitegrid")
    plt.rcParams['figure.figsize'] = (14, 7)

    # 1. Pennant Winners by Franchise
    pennant_winner = load_pennant_winners()
    counts = pennant_winner["Team"].value_counts()
    plt.figure(figsize=(12, 6))
    counts.plot(kind="bar", color="steelblue")
    plt.title("NL Pennant Winners by Franchise (1876-2025)")
    plt.xlabel("Team")
    plt.ylabel("Pennant Titles")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "pennant_winners_by_franchise.png", dpi=150)
    plt.close()

    # 2. 162-Game Win% Comparison (Top 10 teams)
    all_time = load_all_time_records()
    top10 = all_time.sort_values("WinPct", ascending=False).head(10)
    plt.figure(figsize=(12, 6))
    plt.barh(top10["Team"], top10["WinPct"], color="coral")
    plt.title("Top 10 NL Franchises by All-Time Winning Percentage (162G Era)")
    plt.xlabel("Winning Percentage")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "win_pct_by_franchise.png", dpi=150)
    plt.close()

    # 3. Championship Drought Timeline
    all_time_sorted = all_time.sort_values("WS_Titles", ascending=False)
    team_labels = []
    drought_years = []
    for _, row in all_time_sorted.iterrows():
        team = row["Team"]
        ws = row["WS_Titles"]
        if ws > 0 and pd.notna(ws) and ws > 0:
            # Approximate drought (simplified: years since last title)
            # This is a placeholder; actual data should be computed
            drought = "(see chart)"
            team_labels.append(team)
            drought_years.append(ws)
    
    plt.figure(figsize=(14, 8))
    plt.barh(all_time_sorted["Team"], all_time_sorted["WS_Titles"], color="mediumpurple")
    plt.title("NL Franchises by World Series Titles")
    plt.xlabel("World Series Titles")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "ws_titles_by_franchise.png", dpi=150)
    plt.close()

    # 4. H2H W-L Heatmap (key matchups)
    h2h = load_team_h2h()
    # Create a simplified 5-team matchup for visualization
    key_matchups = h2h.head(10)
    plt.figure(figsize=(10, 6))
    print("Key H2H matchups loaded:", len(key_matchups))
    plt.title("Key H2H W-L Matchups (Selected from 15×15 Matrix)")
    plt.axis('off')
    table_data = []
    for _, row in key_matchups.iterrows():
        t1_wins = row["Team_1_Wins"]
        t2_wins = row["Team_2_Wins"]
        total = t1_wins + t2_wins
        t1_pct = t1_wins/total if total > 0 else 0
        table_data.append([row["Team_1"], row["Team_2"], f"{t1_wins}-{t2_wins}", f"{t1_pct:.3f}"])
    
    plt.table(cellText=table_data, colLabels=["Team 1", "Team 2", "W-L", "Win%"],
              cellLoc="center", loc="center")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "h2h_summary_table.png", dpi=150, bbox_inches="tight")
    plt.close()

    # 5. NL West Dominance (Dodgers 8 straight)
    recent = load_recent_standings()
    plt.figure(figsize=(12, 6))
    years = recent["Year"].tolist()
    west_champs = recent["NL_West_W"].tolist()
    plt.bar(years, west_champs, color="royalblue", label="NL West Wins")
    plt.title("NL West Dominance (2018-2025): 8 Straight Titles")
    plt.xlabel("Year")
    plt.ylabel("Wins")
    plt.legend()
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "nl_west_dominance.png", dpi=150)
    plt.close()

    # 6. Era-Based Championship Trends
    trends = load_championship_trends()
    if len(trends) > 0:
        plt.figure(figsize=(14, 8))
        eras = trends["Key_Franchise"].tolist()
        milestones = trends["Milestone"].tolist()
        plt.barh(range(len(eras)), [5]*len(eras), color="mediumseagreen", alpha=0.7)
        plt.yticks(range(len(eras)), [f"{y}: {m}" for y, m in zip(
            trends["Year"].tolist(), trends["Milestone"].tolist()[:len(eras)])])
        plt.title("NL Championship Milestones by Era")
        plt.xlabel("Frequency / Significance")
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.savefig(CHARTS_DIR / "championship_era_trends.png", dpi=150)
        plt.close()

    # 7. Recent Season Win% Comparison
    if len(recent) > 0:
        plt.figure(figsize=(12, 6))
        plt.plot(recent["Year"], recent["NL_East_W"], 'o-', label="NL East", color="firebrick")
        plt.plot(recent["Year"], recent["NL_Central_W"], 's-', label="NL Central", color="steelblue")
        plt.plot(recent["Year"], recent["NL_West_W"], '^-', label="NL West", color="mediumgreen")
        plt.title("NL Division Win Counts (2020-2025)")
        plt.xlabel("Year")
        plt.ylabel("Wins")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(CHARTS_DIR / "division_win_counts_recent.png", dpi=150)
        plt.close()

    print(f"Charts generated in {CHARTS_DIR}/")

if __name__ == "__main__":
    generate_all_charts()
