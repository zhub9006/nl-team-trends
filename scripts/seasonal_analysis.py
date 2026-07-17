import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

DATA_DIR = Path("../data")
CHARTS_DIR = Path("../charts")

def load_seasonal_standings():
    return pd.read_csv(DATA_DIR / "nl_seasonal_standings.csv")

def load_divisional_titles():
    return pd.read_csv(DATA_DIR / "nl_divisional_titles.csv")

def analyze_era_win_rates():
    """Analyze winning percentage by era (154G vs 162G vs 60G)."""
    df = load_seasonal_standings()
    
    # Era classification
    def classify_era(year):
        if year <= 1961:
            return "154G Era"
        elif year == 2020:
            return "60G (COVID)"
        else:
            return "162G Era"
    
    df["Era"] = df["Year"].apply(classify_era)
    
    # Calculate average overall win% by era
    era_winrates = df.groupby("Era")["Overall_WPct"].agg(["mean", "std", "count"])
    print("\n=== Win% by Era ===")
    print(era_winrates)
    
    return df, era_winrates

def analyze_division_dominance():
    """Analyze which division has been most dominant."""
    df = load_divisional_titles()
    
    div_counts = df["Division"].value_counts()
    print("\n=== Division Titles by Division ===")
    print(div_counts)
    
    # Visualize
    plt.figure(figsize=(10, 6))
    div_counts.plot(kind="bar", color=["firebrick", "steelblue", "mediumgreen"])
    plt.title("Division Title Counts by Division (1876-2025)")
    plt.xlabel("Division")
    plt.ylabel("Title Count")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "division_title_counts.png", dpi=150)
    plt.close()
    
    return div_counts

def analyze_championship_droughts():
    """Analyze championship droughts across NL franchises."""
    all_time = pd.read_csv(DATA_DIR / "nl_all_time_records.csv")
    
    # Sort by WS titles (descending), then by last WS title year
    drought_data = []
    for _, row in all_time.iterrows():
        team = row["Team"]
        ws_titles = row["WS_Titles"]
        first_season = row["First_Season"]
        # Drought = years since last WS (approximate from data)
        drought_data.append({
            "Team": team,
            "WS_Titles": ws_titles,
            "First_Season": first_season
        })
    
    drought_df = pd.DataFrame(drought_data)
    
    # Visualize droughts
    plt.figure(figsize=(14, 8))
    colors = ["gold" if ws > 0 else "lightcoral" for ws in drought_df["WS_Titles"]]
    plt.barh(drought_df["Team"], drought_df["WS_Titles"], color=colors)
    plt.title("NL Franchise World Series Titles")
    plt.xlabel("World Series Titles Won")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "ws_titles_drought.png", dpi=150)
    plt.close()
    
    print("\n=== Championship Drought Analysis ===")
    print(drought_df.sort_values("WS_Titles", ascending=False).to_string(index=False))
    
    return drought_df

def analyze_expansion_impact():
    """Analyze how expansion teams have performed relative to original franchises."""
    all_time = pd.read_csv(DATA_DIR / "nl_all_time_records.csv")
    
    expansion_teams = ["Miami Marlins", "Colorado Rockies", "Arizona Diamondbacks", 
                       "San Diego Padres", "Milwaukee Brewers", "Washington Nationals",
                       "New York Mets"]
    
    original_teams = all_time[~all_time["Team"].isin(expansion_teams)]
    expansion = all_time[all_time["Team"].isin(expansion_teams)]
    
    print("\n=== Expansion Team Win% ===")
    print(expansion[["Team", "WinPct", "WS_Titles"]].sort_values("WinPct", ascending=False).to_string(index=False))
    
    print("\n=== Original 8+ Era Win% ===")
    print(original_teams[["Team", "WinPct", "WS_Titles"]].sort_values("WinPct", ascending=False).head(10).to_string(index=False))
    
    # Visualize
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    axes[0].barh(expansion["Team"], expansion["WinPct"], color="orange", alpha=0.8)
    axes[0].set_title("Expansion Team Win%")
    axes[0].set_xlabel("Winning Percentage")
    axes[0].invert_yaxis()
    
    axes[1].barh(original_teams.head(10)["Team"], original_teams.head(10)["WinPct"], color="steelblue", alpha=0.8)
    axes[1].set_title("Top 10 Original NL Franchise Win%")
    axes[1].set_xlabel("Winning Percentage")
    axes[1].invert_yaxis()
    
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "expansion_impact.png", dpi=150)
    plt.close()
    
    return expansion, original_teams

def analyze_pennant_wins_by_decade():
    """Analyze pennant winners by decade."""
    pennant = pd.read_csv(DATA_DIR / "nl_pennant_winners.csv")
    
    pennant["Decade"] = (pennant["Year"] // 10) * 10
    decade_counts = pennant["Team"].value_counts()
    
    # Top pennant winners by decade
    plt.figure(figsize=(14, 8))
    top_teams = pennant["Team"].value_counts().head(10)
    top_teams.plot(kind="bar", color="purple", alpha=0.8)
    plt.title("Most NL Pennant Winners by Franchise (All-Time)")
    plt.xlabel("Team")
    plt.ylabel("Pennant Titles")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "pennant_winners_alltime.png", dpi=150)
    plt.close()
    
    print("\n=== Top Pennant Winners ===")
    print(top_teams)
    
    return decade_counts

if __name__ == "__main__":
    print("NL Seasonal Trend Analysis")
    print("=" * 50)
    
    df, era_wr = analyze_era_win_rates()
    div_counts = analyze_division_dominance()
    drought_df = analyze_championship_droughts()
    expansion, original = analyze_expansion_impact()
    decade_counts = analyze_pennant_wins_by_decade()
    
    print("\n=== Analysis Complete ===")
    print(f"Charts saved to {CHARTS_DIR}/")
