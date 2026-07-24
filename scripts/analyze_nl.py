#!/usr/bin/env python3
"""
nl-team-trends: NL Performance Analysis Script

Performs basic analysis on the NL historical performance data.

Usage:
    python scripts/analyze_nl.py

Requirements:
    pip install -r requirements.txt
"""

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
CHARTS_DIR = REPO_ROOT / "charts"


def load_data():
    """Load key NL data files."""
    records = pd.read_csv(DATA_DIR / "nl_all_time_records.csv")
    h2h = pd.read_csv(DATA_DIR / "nl_h2h_matrix_full.csv")
    pennants = pd.read_csv(DATA_DIR / "nl_season_by_year_full.csv")
    trends = pd.read_csv(DATA_DIR / "nl_recent_trends_2000_2024.csv")
    eras = pd.read_csv(DATA_DIR / "nl_era_win_pct_comparison.csv")
    return records, h2h, pennants, trends, eras


def plot_win_loss_parity():
    """Create a wins vs losses scatter plot for all NL franchises."""
    records, _, _, _, _ = load_data()
    
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_facecolor('#f8f9fa')
    fig.patch.set_facecolor('white')
    
    sizes = records['games'] / 100
    colors = ['#005A9C' if row['ws_titles'] >= 5 else '#FD4D00' if row['ws_titles'] >= 2 else '#888888'
              for _, row in records.iterrows()]
    
    for _, row in records.iterrows():
        ax.scatter(row['losses'], row['wins'], s=sizes, c=colors,
                  alpha=0.8, edgecolors='white', linewidth=0.5, zorder=5)
        ax.annotate(row['team'], (row['losses'], row['wins']),
                   fontsize=7, ha='left', va='bottom', xytext=(5, 3),
                   textcoords='offset points')
    
    # Perfectly even line
    max_val = max(records['wins'].max(), records['losses'].max()) + 1000
    ax.plot([0, max_val], [0, max_val], '--', color='#cccccc', linewidth=1, zorder=1)
    
    ax.set_xlabel('Total Losses (through 2025)', fontsize=11)
    ax.set_ylabel('Total Wins (through 2025)', fontsize=11)
    ax.set_title('NL Franchises: Wins vs Losses (All-Time)', fontsize=13, fontweight='bold')
    ax.legend(['Even .500 line'], loc='upper left', fontsize=8)
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=0)
    plt.tight_layout()
    
    ensure_charts_dir()
    plt.savefig(CHARTS_DIR / 'win_loss_parity.png', dpi=150, bbox_inches='tight')
    print(f"Saved: charts/win_loss_parity.png")
    plt.close()


def plot_era_comparison():
    """Create an era comparison bar chart."""
    _, _, _, _, eras = load_data()
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_facecolor('#f8f9fa')
    fig.patch.set_facecolor('white')
    
    # Parse win_pct_range to get midpoint
    def parse_midpoint(rng):
        if pd.isna(rng):
            return 0.5
        parts = str(rng).split('-')
        if len(parts) == 2:
            try:
                return (float(parts[0]) + float(parts[1])) / 2
            except:
                return 0.5
        try:
            return float(rng)
        except:
            return 0.5
    
    eras['mid_pct'] = eras['win_pct_range'].apply(parse_midpoint)
    
    colors = ['#005A9C', '#FD4D00', '#1A5632', '#8B0000', '#2C3E50',
              '#6B3FA0', '#C8102E', '#004687', '#BA0C2F']
    bars = ax.barh(eras['era'], eras['mid_pct'], color=colors, edgecolor='white', height=0.7)
    
    for i, (bar, row) in enumerate(zip(bars, eras.itertuples())):
        ax.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2,
               f"{row.dominant_team} ({row.pennant_count} pennants)",
               va='center', fontsize=8)
    
    ax.set_xlabel('Midpoint Win Percentage', fontsize=11)
    ax.set_title('NL Era Comparison: Midpoint Win % by Historical Period', fontsize=13, fontweight='bold')
    ax.set_xlim(left=0.3, right=0.85)
    ax.axvline(x=0.5, color='red', linestyle='--', alpha=0.5, label='Even .500')
    plt.tight_layout()
    
    ensure_charts_dir()
    plt.savefig(CHARTS_DIR / 'era_comparison.png', dpi=150, bbox_inches='tight')
    print(f"Saved: charts/era_comparison.png")
    plt.close()


def ensure_charts_dir():
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)


def main():
    print("=" * 60)
    print("NL Team Trends - Analysis Script")
    print("=" * 60)
    
    print("\nGenerating visualizations...")
    plot_win_loss_parity()
    plot_era_comparison()
    
    print("\nAnalysis complete!")


if __name__ == "__main__":
    main()