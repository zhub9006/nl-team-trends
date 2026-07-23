#!/usr/bin/env python3
"""NL Team Trends — Historical Performance Data Analysis Script

This script loads the NL historical performance data files and generates
summary statistics and basic visualizations.

Usage:
    python scripts/analyze_nl_data.py
"""

import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('husl')


def load_all_data():
    """Load all NL data files and return a dictionary of DataFrames."""
    data = {
        'all_time_records': pd.read_csv('data/nl_all_time_records.csv'),
        'pennant_winners': pd.read_csv('data/nl_pennant_winners.csv'),
        'historical_performance': pd.read_csv('data/nl_historical_performance.csv'),
        'notable_records': pd.read_csv('data/nl_notable_records.csv'),
        'recent_standings': pd.read_csv('data/nl_recent_standings.csv'),
        'recent_championships': pd.read_csv('data/nl_recent_championships.csv'),
        'team_vs_team': pd.read_csv('data/nl_team_vs_team_summary.csv'),
        'championship_trends': pd.read_csv('data/nl_championship_trends.csv'),
    }

    with open('data/nl_season_by_year.json') as f:
        data['season_by_year'] = json.load(f)

    with open('data/nl_team_era_performance.json') as f:
        data['era_performance'] = json.load(f)

    with open('data/research_data_supplement.json') as f:
        data['research_supplement'] = json.load(f)

    return data


def print_summary_stats(data):
    """Print key summary statistics."""
    records = data['all_time_records']
    pennants = data['pennant_winners']

    print("=" * 60)
    print("NL TEAM TRENDS — DATA SUMMARY")
    print("=" * 60)
    print(f"\nTotal NL franchises (historical): {len(records)}")
    print(f"Total pennant years: {len(pennants)}")
    print(f"Date range: {pennants['year'].min()} – {pennants['year'].max()}")

    print("\n--- WS Title Leaders ---")
    print(records.nlargest(5, 'ws_titles')[['team', 'ws_titles', 'wins', 'win_pct']].to_string(index=False))

    print("\n--- Highest Winning Percentage (1500+ games) ---")
    high_wp = records[records['wins'] >= 10000].nlargest(3, 'win_pct')[['team', 'win_pct', 'wins']]  
    print(high_wp.to_string(index=False))

    print("\n--- Most Games Played ---")
    print(records.nlargest(3, 'games')[['team', 'games', 'wins']].to_string(index=False))

    print("\n--- Era Win Percentage Rankings ---")
    era = data['era_performance']
    for era_key, era_data in era['eras'].items():
        print(f"  {era_data['name']}: Dominant team = {era_data['dominant_team']}")

    print("\n--- H2H Rivalry Extremes ---")
    h2h = data['team_vs_team']
    most_lopsided = h2h.nlargest(3, 't1_win_pct')
    most_competitive = h2h.nsmallest(3, abs=lambda x: abs(0.5 - x))

    print("  Most one-sided rivalries:")
    for _, row in most_lopsided.iterrows():
        print(f"    {row['team_1']} vs {row['team_2']}: {row['t1_win_pct']:.3f} ({row['t1_wins']}-{row['t2_wins']})")
    print("  Most competitive rivalries:")
    competitive_h2h = h2h.iloc[(h2h['t1_win_pct'] - 0.5).abs().argsort().head(3)]
    for _, row in competitive_h2h.iterrows():
        print(f"    {row['team_1']} vs {row['team_2']}: {row['t1_win_pct']:.3f}")

    print("\n" + "=" * 60)


def generate_basic_charts(data):
    """Generate basic Matplotlib charts."""
    records = data['all_time_records'].sort_values('ws_titles', ascending=True)

    # Chart 1: WS Titles by Team
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ['#b30000' if ws >= 5 else '#1a73e8' if ws >= 2 else '#ccc' for ws in records['ws_titles']]
    ax.barh(records['team'], records['ws_titles'], color=colors)
    ax.set_xlabel('World Series Titles')
    ax.set_title('NL Teams by World Series Titles (1876–2025)')
    ax.axvline(x=0, color='gray', linewidth=0.5)
    for i, (v, t) in enumerate(zip(records['ws_titles'], records['team'])):
        if v > 0:
            ax.text(v + 0.1, i, str(v), va='center', fontsize=9)
    plt.tight_layout()
    plt.savefig('charts/ws_titles_by_team.png', dpi=150, bbox_inches='tight')
    print("  Saved charts/ws_titles_by_team.png")
    plt.close()

    # Chart 2: Winning Percentage by Team
    records_wp = records.sort_values('win_pct', ascending=True)
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(records_wp['team'], records_wp['win_pct'], color='steelblue')
    ax.set_xlabel('All-Time Win Percentage')
    ax.set_title('NL Teams by All-Time Winning Percentage (1500+ games)')
    ax.axvline(x=0.500, color='red', linestyle='--', alpha=0.7, label='.500 baseline')
    ax.legend()
    plt.tight_layout()
    plt.savefig('charts/win_pct_by_team.png', dpi=150, bbox_inches='tight')
    print("  Saved charts/win_pct_by_team.png")
    plt.close()

    # Chart 3: Championship Era Heatmap Data
    pennants = data['pennant_winners']
    era_map = {
        **{y: '1876-1900' for y in range(1876, 1901)},
        **{y: '1901-1920' for y in range(1901, 1921)},
        **{y: '1921-1940' for y in range(1921, 1941)},
        **{y: '1941-1960' for y in range(1941, 1961)},
        **{y: '1961-1980' for y in range(1961, 1981)},
        **{y: '1981-2000' for y in range(1981, 2001)},
        **{y: '2001-2025' for y in range(2001, 2026)},
    }
    pennants['era'] = pennants['year'].map(era_map)

    print(f"\n  Pennant count by era:")
    era_counts = pennants.groupby('era')['NL_champion'].count()
    for era, count in era_counts.items():
        print(f"    {era}: {count} pennants")


def main():
    print("Loading NL historical performance data...")
    data = load_all_data()

    print_summary_stats(data)
    print("\nGenerating basic charts...")
    generate_basic_charts(data)

    print("\nAnalysis complete! Run individual Jupyter notebooks for deeper analysis.")


if __name__ == '__main__':
    main()
