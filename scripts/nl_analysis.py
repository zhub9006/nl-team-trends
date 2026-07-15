#!/usr/bin/env python3
"""
NL Team Trends — Starter Analysis Script
Loads NL historical data and generates basic visualizations.

Requirements: pandas, matplotlib, seaborn, plotly (optional)
Usage: python scripts/nl_analysis.py
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Use non-interactive backend for script execution
matplotlib.use('Agg')

# Ensure output directory exists
os.makedirs('visualizations', exist_ok=True)

# =============================================================================
# 1. Load all-time franchise records
# =============================================================================
print("Loading NL all-time records...")
all_time = pd.read_csv('data/nl_all_time_records.csv', comment='#')
print(f"Loaded {len(all_time)} teams")

# Sort by winning percentage
all_time_sorted = all_time.sort_values('WinPct', ascending=True)

# --- Plot 1: All-Time Win% Bar Chart ---
fig, ax = plt.subplots(figsize=(12, 7))
colors = ['#002d62' if i < 5 else '#041e42' for i in range(len(all_time_sorted))]
bars = ax.barh(all_time_sorted['Team'], all_time_sorted['WinPct'], color=colors)
ax.set_xlabel('Winning Percentage', fontsize=12)
ax.set_title('NL Franchise All-Time Winning Percentage (1876–2025)', fontsize=14, fontweight='bold')
ax.axvline(x=0.500, color='red', linestyle='--', alpha=0.5, label=' .500 (average)')
ax.legend()
plt.tight_layout()
plt.savefig('visualizations/fig1_alltime_win_pct.png', dpi=150, bbox_inches='tight')
print("Saved: visualizations/fig1_alltime_win_pct.png")

# --- Plot 2: Pennants vs WS Titles Bubble Chart ---
fig, ax = plt.subplots(figsize=(10, 8))
sizes = all_time['WS_Won'] * 200 + 200  # Scale bubble by WS titles
scatter = ax.scatter(all_time['Pennants'], all_time['WS_Won'], 
                      s=sizes, alpha=0.6, c=all_time['WinPct'], 
                      cmap='RdYlGn', edgecolors='black', linewidth=0.5)
for _, row in all_time.iterrows():
    ax.annotate(row['Team'].split('(')[0].strip()[:8], 
                (row['Pennants'], row['WS_Won']),
                fontsize=8, ha='center', va='bottom')
ax.set_xlabel('Pennants Won', fontsize=12)
ax.set_ylabel('World Series Titles', fontsize=12)
ax.set_title('Pennants vs. WS Titles (Bubble Size = WS Won; Color = Win%)', fontsize=13, fontweight='bold')
plt.colorbar(scatter, label='Winning %')
plt.tight_layout()
plt.savefig('visualizations/fig2_pennants_vs_ws.png', dpi=150, bbox_inches='tight')
print("Saved: visualizations/fig2_pennants_vs_ws.png")

# =============================================================================
# 2. Load season-by-season records
# =============================================================================
print("\nLoading season-by-season records...")
season = pd.read_csv('data/nl_season_records_all_teams.csv', comment='#')
# Clean WinPct column (it may be string type)
season['WinPct'] = pd.to_numeric(season['WinPct'], errors='coerce')
print(f"Loaded {len(season)} season records")

# --- Plot 3: Modern Era (162-game) Win% distribution ---
modern = season[season['Games'] >= 160].copy()
if len(modern) > 0:
    fig, ax = plt.subplots(figsize=(10, 6))
    for team in modern['Team'].unique():
        team_data = modern[modern['Team'] == team].sort_values('Year')
        ax.plot(team_data['Year'], team_data['WinPct'], marker='o', markersize=3, label=team, linewidth=1)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Win Percentage', fontsize=12)
    ax.set_title('NL Team Win% Trends — Modern Era (162-game schedule)', fontsize=14, fontweight='bold')
    ax.axhline(y=0.500, color='red', linestyle='--', alpha=0.3)
    ax.legend(fontsize=7, loc='upper left', ncol=2)
    plt.tight_layout()
    plt.savefig('visualizations/fig3_modern_win_trends.png', dpi=150, bbox_inches='tight')
    print("Saved: visualizations/fig3_modern_win_trends.png")

# --- Plot 4: Top 10 teams by average modern-era win% ---
if len(modern) > 0:
    avg_win = modern.groupby('Team')['WinPct'].mean().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10, 6))
    top10 = avg_win.head(10)
    colors = ['#003087' if w > 0.58 else '#c00000' for w in top10.values]
    bars = ax.barh(range(len(top10)), top10.values, color=colors)
    ax.set_yticks(range(len(top10)))
    ax.set_yticklabels(top10.index, fontsize=9)
    ax.set_xlabel('Average Win Percentage', fontsize=12)
    ax.set_title('Top 10 NL Franchises by Avg Win% (Modern Era)', fontsize=14, fontweight='bold')
    ax.axvline(x=0.500, color='red', linestyle='--', alpha=0.5, label=' .500')
    ax.legend()
    ax.invert_yaxis()
    plt.tight_layout()
    plt.savefig('visualizations/fig4_top10_avg_win.png', dpi=150, bbox_inches='tight')
    print("Saved: visualizations/fig4_top10_avg_win.png")

# =============================================================================
# 3. Load championship trends by era
# =============================================================================
print("\nLoading championship trends...")
trends = pd.read_csv('data/nl_championship_trends.csv', comment='#')
if len(trends) > 0:
    fig, ax = plt.subplots(figsize=(12, 6))
    for _, row in trends.iterrows():
        era_range = row['Era'].split('-')
        start_year = int(era_range[0])
        end_year = int(era_range[1].split(',')[0] if ',' in era_range[1] else era_range[1])
        ax.barh(row['Team'], end_year - start_year + 1, left=start_year, 
                alpha=0.7, label=row['Team'][:12])
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Era / Team', fontsize=12)
    ax.set_title('NL Era Dominance Visualization', fontsize=14, fontweight='bold')
    ax.legend(fontsize=8, loc='lower right')
    plt.tight_layout()
    plt.savefig('visualizations/fig5_era_dominance.png', dpi=150, bbox_inches='tight')
    print("Saved: visualizations/fig5_era_dominance.png")

print("\n✅ All visualizations saved to visualizations/ directory!")
print("\nNext steps:")
print("  - Explore data in data/ with pandas")
print("  - Add more charts to visualizations/")
print("  - Build interactive dashboard with Plotly/Streamlit")
print("  - Add Jupyter notebooks in notebooks/")