#!/usr/bin/env python
"""
NL Team Trends - Starter Visualization Script
Generates example charts from the NL historical data files.

Usage:
    python scripts/viz_nl_trends.py

Requirements:
    pip install -r requirements.txt
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Style settings
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('husl')

# ========== 1. NL Winners by Era (Bar Chart) ==========

def plot_wins_by_era():
    """Plot NL championship winners by era."""
    from collections import Counter

    # Load penalty files
    try:
        pennants = pd.read_csv('data/nl_pennant_winners.csv')
    except FileNotFoundError:
        print("nl_pennant_winners.csv not found. Using alternative data...")
        return

    if pennants is not None and 'era' in pennants.columns:
        era_wins = pennants.groupby('era').size()
        fig, ax = plt.subplots(figsize=(14, 6))
        bars = ax.bar(era_wins.index, era_wins.values, color=sns.color_palette("Set2"))
        ax.set_title('NL Pennant Winners by Era (1876–2025)', fontsize=16, fontweight='bold')
        ax.set_xlabel('Era')
        ax.set_ylabel('Pennant Count')
        plt.xticks(rotation=45)
        for bar, val in zip(bars, era_wins.values):
            ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.1, str(val),
                    ha='center', fontweight='bold')
        plt.tight_layout()
        plt.savefig('visualizations/nl_pennants_by_era.png', dpi=150, bbox_inches='tight')
        print("Saved visualizations/nl_pennants_by_era.png")

# ========== 2. Franchise Win % Comparison (Horizontal Bar Chart) ==========

def plot_franchise_win_pcts():
    """Plot all-time franchise win percentages."""
    records = pd.read_csv('data/nl_all_time_records.csv')
    records_sorted = records.sort_values('win_pct', ascending=True)

    fig, ax = plt.subplots(figsize=(12, 8))
    colors = ['#c0392b' if ws > 8 else '#e67e22' if ws > 5 else '#3498db'
              for ws in records_sorted['ws_titles']]
    bars = ax.barh(records_sorted['team'], records_sorted['win_pct'], color=colors)

    # Annotate
    for bar, wins, ws in zip(bars, records_sorted['wins'], records_sorted['ws_titles']):
        label = f'{wins:,}W'
        if ws > 0:
            label += f' ({ws} WS)'
        ax.text(bar.get_width() + 0.002, bar.get_y() + bar.get_height()/2.,
                label, va='center', fontsize=8)

    ax.set_title('NL Franchise All-Time Win Percentages', fontsize=16, fontweight='bold')
    ax.set_xlabel('Win Percentage (W / (W+L))')
    ax.axvline(0.500, color='red', linestyle='--', linewidth=0.8, alpha=0.5)
    plt.tight_layout()
    plt.savefig('visualizations/franchise_win_pcts.png', dpi=150, bbox_inches='tight')
    print("Saved visualizations/franchise_win_pcts.png")

# ========== 3. H2H Rivalry Heatmap ==========

def plot_h2h_heatmap():
    """Create H2H rivalry heatmap."""
    h2h = pd.read_csv('data/nl_h2h_rivalries_detailed.csv')

    # Build pivot table: team1 vs team2 (just for the top rivalries)
    fig, ax = plt.subplots(figsize=(14, 10))

    # Sort by locality to highlight major rivalries
    h2h_sorted = h2h.sort_values('total_games', ascending=False)

    # Create a focused heatmap of top rivalries by t1_win_pct
    labels = [f"{r['team_1']} vs {r['team_2']}" for _, r in h2h_sorted.iterrows()]
    win_pcts = h2h_sorted['t1_win_pct'].values
    total_games = h2h_sorted['total_games'].values

    colors = ['#e74c3c' if wp > 0.58 else '#27ae60' if wp < 0.42 else '#95a5a6'
              for wp in win_pcts]

    y_pos = np.arange(len(labels))
    bars = ax.barh(y_pos, win_pcts, color=colors, edgecolor='white', linewidth=0.5)

    # Add game count labels
    for i, (wp, tg) in enumerate(zip(win_pcts, total_games)):
        ax.text(wp + 0.002, i, f'{tg:,} games', va='center', fontsize=7)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=8)
    ax.set_xlim(0, 1.05)
    ax.set_xlabel('Team 1 Win Percentage', fontsize=12)
    ax.set_title('NL Head-to-Head Rivalry Win Rankings (1876–2026)', fontsize=16, fontweight='bold')
    ax.axvline(0.500, color='gray', linestyle='--', linewidth=0.8)
    ax.invert_yaxis()

    plt.tight_layout()
    plt.savefig('visualizations/h2h_rivalries.png', dpi=150, bbox_inches='tight')
    print("Saved visualizations/h2h_rivalries.png")

# ========== 4. Box Plot of Win % Distribution by Era ==========

def plot_win_pct_boxplot():
    """Show spread of win % across NL seasons by era."""
    seasonal = pd.read_csv('data/nl_historical_performance.csv')

    # Get champion and runner-up IP column names based on what exists
    champ_wc = 'Champion_WPct' if 'Champion_WPct' in seasonal.columns else None

    if champ_wc is None:
        # Alternative: compute from raw columns
        print("Raw seasonal data: plotting available metrics")
        year_col = 'Year' if 'Year' in seasonal.columns else seasonal.columns[0]
        print(f"Columns: {list(seasonal.columns)}")
        return

    # Compute team win pct Where it existed
    fig, ax = plt.subplots(figsize=(14, 6))

    # Group by era and compute spread of champion WPct
    era_stats = seasonal.groupby('Era').agg(
        min_wpct=('Champion_WPct', 'min'),
        q1_wpct=('Champion_WPct', lambda x: x.quantile(0.25)),
        median_wpct=('Champion_WPct', 'median'),
        q3_wpct=('Champion_WPct', lambda x: x.quantile(0.75)),
        max_wpct=('Champion_WPct', 'max')
    )

    iqr = era_stats['q3_wpct'] - era_stats['q1_wpct']
    lower = era_stats['q1_wpct'] - 1.5 * iqr
    upper = era_stats['q3_wpct'] + 1.5 * iqr

    # Plot
    eras = sorted(seasonal['Era'].unique())
    data_for_box = [seasonal[seasonal['Era'] == era]['Champion_WPct'].dropna().values for era in eras]

    bp = ax.boxplot(data_for_box, labels=eras, patch_artist=True)
    for patch in bp['boxes']:
        patch.set_facecolor('#3498db')
        patch.set_alpha(0.6)

    ax.set_title('NL Champion Win % Distribution by Era', fontsize=16, fontweight='bold')
    ax.set_ylabel('Champion Win Percentage')
    ax.set_xlabel('Era')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('visualizations/winpct_by_era_boxplot.png', dpi=150, bbox_inches='tight')
    print("Saved visualizations/winpct_by_era_boxplot.png")

# ========== 5. NL Team Win Trends Over Time (Line Chart) ==========

def plot_win_trend_lines():
    """Plot year-by-year win % for key NL franchises."""
    seasonal = pd.read_csv('data/nl_historical_performance.csv')

    # Identify the years
    year_col = 'Year' if 'Year' in seasonal.columns else seasonal.columns[0]
    seasons = sorted(seasonal[year_col].unique())

    # Get teams with most prominence
    top_teams = ['St. Louis Cardinals', 'LA Dodgers', 'San Francisco Giants',
                 'Cincinnati Reds', 'Chicago Cubs', 'Atlanta Braves', 'Pittsburgh Pirates']

    fig, ax = plt.subplots(figsize=(18, 8))

    for team in top_teams:
        team_data = []
        for yr in seasons:
            yr_data = seasonal[seasonal[year_col] == yr]
            # Check each of the classifier columns with the team name present
            for col in ['NL_Champion', 'Second_Place']:
                if col in yr_data.columns:
                    match = yr_data[yr_data[col] == team]
                    if len(match) > 0:
                        wpct_col = 'Champion_WPct' if col == 'NL_Champion' else 'Second_WPct'
                        team_data.append((yr, match[wpct_col].values[0] if wpct_col in match.columns else None))
                        break

        if team_data:
            years = [d[0] for d in team_data]
            winpcts = [d[1] for d in team_data if d[1] is not None]
            valid_years = [y for d in team_data if d[1] is not None for y in [d[0]]]
            ax.plot(valid_years, winpcts, marker='o', markersize=2, linewidth=1.2, label=team)

    ax.set_title('NL Top Franchise Win % Trends (Champion/Runner-Up Seasons Only)', fontsize=16, fontweight='bold')
    ax.set_ylabel('Win Percentage')
    ax.set_xlabel('Year')
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)
    ax.axhline(0.500, color='gray', linestyle='--', linewidth=0.8)
    plt.tight_layout()
    plt.savefig('visualizations/franchise_win_trends.png', dpi=150, bbox_inches='tight')
    print("Saved visualizations/franchise_win_trends.png")


# ========== Main ==========

if __name__ == '__main__':
    import os
    os.makedirs('visualizations', exist_ok=True)

    print("Generating NL Team Trends visualizations...")
    print()

    print("1. Franchise Win % Comparison...")
    plot_franchise_win_pcts()

    print("2. H2H Rivalry Win Rankings...")
    plot_h2h_heatmap()

    print("3. Win % Boxplot by Era...")
    plot_win_pct_boxplot()

    print("4. Franchise Win Trend Lines...")
    plot_win_trend_lines()

    print()
    print("All visualizations generated in visualizations/ directory.")
    print("For additional visualizations (treemap, Gantt chart, etc.), see visualizations/README.md")
