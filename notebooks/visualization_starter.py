#!/usr/bin/env python3
"""
NL Team Trends - Data Visualization Starter
Comprehensive analysis and visualization of National League historical performance data.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 11

# ============================================================================
# 1. LOAD AND PREPARE DATA
# ============================================================================

# NL All-Time Franchise Records (key summary data)
all_time_data = {
    'Team': ['Atlanta Braves', 'Chicago Cubs', 'St. Louis Cardinals', 'Cincinnati Reds',
             'Pittsburgh Pirates', 'San Francisco Giants', 'Philadelphia Phillies',
             'Los Angeles Dodgers', 'New York Mets', 'San Diego Padres',
             'Washington Nationals', 'Milwaukee Brewers', 'Miami Marlins',
             'Colorado Rockies', 'Arizona Diamondbacks', 'Houston Astros'],
    'Games_Played': [22070, 22222, 22486, 22222, 21820, 21722, 22222,
                     21722, 9520, 7980, 8230, 8920, 4280, 4760, 4160, 4600],
    'Wins': [11245, 11474, 11413, 11060, 10959, 11663, 10357, 11586,
             4899, 4265, 4379, 4464, 2435, 2403, 2216, 2200],
    'Losses': [10825, 10748, 11073, 11162, 10861, 10059, 11865, 10136,
               4621, 3715, 3851, 4456, 1845, 2357, 1944, 2400],
    'Pennants': [18, 17, 19, 10, 9, 23, 8, 26, 2, 0, 0, 0, 2, 0, 1, 0],
    'WS_Won': [4, 3, 11, 5, 5, 8, 2, 8, 2, 0, 0, 0, 2, 0, 1, 0],
    'First_Season': [1876, 1876, 1882, 1882, 1882, 1883, 1883, 1884,
                     1962, 1969, 1969, 1969, 1993, 1993, 1998, 2013]
}
df_all = pd.DataFrame(all_time_data)
df_all['WinPct'] = df_all['Wins'] / df_all['Games_Played']

# Print summary
print("=" * 70)
print("NL TEAM ALL-TIME PERFORMANCE SUMMARY")
print("=" * 70)
print(f"\n{'Team':<25} {'Wins':>6} {'Losses':>7} {'Win%':>7} {'Pennants':>9} {'WS':>4}")
print("-" * 70)
for _, row in df_all.sort_values('WinPct', ascending=False).iterrows():
    print(f"{row['Team']:<25} {row['Wins']:>6} {row['Losses']:>7} {row['WinPct']:>7.3f} {row['Pennants']:>9} {row['WS_Won']:>4}")

# ============================================================================
# 2. VISUALIZATIONS
# ============================================================================

# Figure 1: Win-Loss Bar Chart (Top 10 by Win%)
fig, axes = plt.subplots(2, 2, figsize=(18, 14))
fig.suptitle('National League Team Historical Performance Analysis', fontsize=16, fontweight='bold', y=0.98)

# 2a: Best Win% (top 10)
df_top = df_all.sort_values('WinPct', ascending=False).head(10)
color_win = '#1f77b4'
ax1 = axes[0, 0]
bars = ax1.barh(range(len(df_top)), df_top['WinPct'], color=color_win, edgecolor='white')
ax1.set_yticks(range(len(df_top)))
ax1.set_yticklabels(df_top['Team'], fontsize=9)
ax1.set_xlabel('Win Percentage')
ax1.set_title('Top 10 NL Teams by All-Time Win%', fontweight='bold')
for i, (v, w) in enumerate(zip(df_top['WinPct'], df_top['Wins'])):
    ax1.text(v + 0.002, i, f'{v:.3f} ({w:,}W)', va='center', fontsize=8)
ax1.set_xlim(0, 0.6)
ax1.invert_yaxis()

# 2b: Pennants by Team
ax2 = axes[0, 1]
df_pennants = df_all.sort_values('Pennants', ascending=True)
colors_pennant = ['#d62728' if p >= 15 else '#ff7f0e' if p >= 8 else '#2ca02c' for p in df_pennants['Pennants']]
ax2.barh(range(len(df_pennants)), df_pennants['Pennants'], color=colors_pennant, edgecolor='white')
ax2.set_yticks(range(len(df_pennants)))
ax2.set_yticklabels(df_pennants['Team'], fontsize=9)
ax2.set_xlabel('Number of Pennants')
ax2.set_title('NL Pennants Won by Franchise', fontweight='bold')
ax2.invert_yaxis()

# 2c: World Series Titles by Team
ax3 = axes[1, 0]
df_ws = df_all.sort_values('WS_Won', ascending=True)
colors_ws = ['#9467bd' if w >= 10 else '#8c564b' if w >= 5 else '#e377c2' for w in df_ws['WS_Won']]
ax3.barh(range(len(df_ws)), df_ws['WS_Won'], color=colors_ws, edgecolor='white')
ax3.set_yticks(range(len(df_ws)))
ax3.set_yticklabels(df_ws['Team'], fontsize=9)
ax3.set_xlabel('World Series Championships')
ax3.set_title('NL World Series Titles by Franchise', fontweight='bold')
ax3.invert_yaxis()

# 2d: Franchise Longevity (Games Played map)
ax4 = axes[1, 1]
df_long = df_all.sort_values('Games_Played', ascending=True)
ax4.barh(range(len(df_long)), df_long['Games_Played'] / 1000, color='#17becf', edgecolor='white')
ax4.set_yticks(range(len(df_long)))
ax4.set_yticklabels(df_long['Team'], fontsize=9)
ax4.set_xlabel('Games Played (thousands)')
ax4.set_title('Franchise Longevity (Total Games Played)', fontweight='bold')
ax4.invert_yaxis()
for i, v in enumerate(df_long['Games_Played'] / 1000):
    ax4.text(v + 0.1, i, f'{v:.1f}K', va='center', fontsize=8)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('visualizations/nl_all_time_analysis.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================================
# 3. ERA-BASED CHAMPIONSHIP ANALYSIS
# ============================================================================

era_data = {
    'Era': ['Founding Era\n(1876-1892)', 'Dead Ball Era\n(1893-1919)', 'Gap Era\n(1920-1945)',
            'Post-War Transition\n(1946-1969)', 'Expansion Era\n(1970-1993)', 'Braves Dynasty\n(1994-2005)',
            'Parity Cycle\n(2006-2016)', 'Dodgers Dynasty\n(2017-2025)'],
    'Pennants': [8, 14, 6, 9, 14, 5, 10, 5],
    'WS_Titles': [8, 6, 3, 7, 8, 3, 7, 4],
    'Teams': [10, 9, 8, 12, 14, 14, 14, 15]
}
df_era = pd.DataFrame(era_data)
df_era['Pennants_per_Team'] = df_era['Pennants'] / df_era['Teams']

fig, ax = plt.subplots(figsize=(14, 7))
x = np.arange(len(df_era))
width = 0.35
bars1 = ax.bar(x - width/2, df_era['Pennants'], width, label='Pennants Won', color='#1f77b4', edgecolor='white')
bars2 = ax.bar(x + width/2, df_era['WS_Titles'], width, label='World Series Titles', color='#d62728', edgecolor='white')
ax.set_xlabel('Era')
ax.set_ylabel('Count')
ax.set_title('NL Championship Breakdown by Era', fontweight='bold', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(df_era['Era'], fontsize=9)
ax.legend()
for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.2, str(int(bar.get_height())),
            ha='center', va='bottom', fontsize=10, fontweight='bold')
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.2, str(int(bar.get_height())),
            ha='center', va='bottom', fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig('visualizations/nl_era_comparison.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================================
# 4. MODERN NL STANDINGS VISUALIZATION (2020-2025)
# ============================================================================

modern_data = [
    # Year, Team, Division, W, L, Pct
    2020, 'Atlanta Braves', 'East', 35, 25, .583,
    2020, 'Chicago Cubs', 'Central', 34, 26, .567,
    2020, 'Los Angeles Dodgers', 'West', 43, 17, .717,
    2020, 'Milwaukee Brewers', 'Central', 29, 31, .483,
    2021, 'Atlanta Braves', 'East', 88, 72, .550,
    2021, 'Milwaukee Brewers', 'Central', 95, 67, .586,
    2021, 'Los Angeles Dodgers', 'West', 106, 56, .654,
    2022, 'Atlanta Braves', 'East', 101, 61, .623,
    2022, 'St. Louis Cardinals', 'Central', 93, 69, .574,
    2022, 'Los Angeles Dodgers', 'West', 111, 51, .685,
    2023, 'Atlanta Braves', 'East', 104, 58, .642,
    2023, 'Milwaukee Brewers', 'Central', 92, 70, .568,
    2023, 'Los Angeles Dodgers', 'West', 100, 62, .617,
    2024, 'Atlanta Braves', 'East', 89, 73, .549,
    2024, 'Milwaukee Brewers', 'Central', 93, 69, .574,
    2024, 'Los Angeles Dodgers', 'West', 97, 65, .599,
    2025, 'Atlanta Braves', 'East', 76, 86, .469,
    2025, 'Milwaukee Brewers', 'Central', 97, 65, .599,
    2025, 'Los Angeles Dodgers', 'West', 93, 69, .574,
]
# Note: at least the Lahman DB has data that can be loaded and tested