#!/usr/bin/env python
"""
nl_viz.py — NL Team Trends Visualization Script

Run with: python nl_viz.py

Generates PNG charts saved to plots/ directory.
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (13, 7)

DATA = Path('data')
OUT = Path('plots')
OUT.mkdir(exist_ok=True)

# ── 1. Load Datasets ──────────────────────────────────────────────────
hist  = pd.read_csv(DATA / 'nl_historical_data_complete.csv')
hist['win_pct'] = hist['wins'] / (hist['wins'] + hist['losses'])

franchise = pd.read_csv(DATA / 'franchise_summary.csv')
era       = pd.read_csv(DATA / 'era_analysis.csv')

# ── 2. NL Franchise Win% Bar Chart ────────────────────────────────────
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

f = franchise.sort_values('win_pct', ascending=True)
colors = ['#e74c3c' if v >= .52 else '#95a5a6' for v in f['win_pct']]
ax1.barh(f['modern_name'], f['win_pct'], color=colors, edgecolor='white')
ax1.set_xlabel('All-Time NL Win %')
ax1.set_title('NL Franchise Win% (1876–Present)')
ax1.axvline(.500, ls='--', c='black', lw=.7)

era_s = era.sort_values('avg_win_pct')
ax2.barh(era_s['era'], era_s['avg_win_pct'], color=sns.color_palette('pastel'), edgecolor='white')
ax2.set_xlabel('Average Win%')
ax2.set_title('Era Win% Comparison')
ax2.axvline(.500, ls='--', c='black', lw=.7)

plt.tight_layout()
plt.savefig(OUT / 'franchise_winpct_era.png', dpi=200, bbox_inches='tight')
plt.close()
print("✓ franchise_winpct_era.png")

# ── 3. Roll-10 Win% Trend Lines ────────────────────────────────────────
TEAMS = ['St. Louis Cardinals', 'Los Angeles Dodgers', 'San Francisco Giants',
         'Atlanta Braves', 'Chicago Cubs', 'New York Mets',
         'Philadelphia Phillies', 'Pittsburgh Pirates', 'Cincinnati Reds']

fig, ax = plt.subplots(figsize=(14, 6))
for team in TEAMS:
    tdf = hist[hist['modern_name'] == team].sort_values('season')
    tdf['ma'] = tdf['win_pct'].rolling(10, min_periods=5).mean()
    ax.plot(tdf['season'], tdf['ma'], lw=2, label=team)

ax.set_title('NL Franchise Win% — 10-Year Rolling Average (1876-2025)')
ax.set_xlabel('Season')
ax.set_ylabel('Win%')
ax.axhline(.500, ls='-', c='black', lw=.5)
ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', fontsize=8)
plt.tight_layout()
plt.savefig(OUT / 'rolling_win_pct.png', dpi=200, bbox_inches='tight')
plt.close()
print("✓ rolling_win_pct.png")

# ── 4. Era Win% Heatmap ─────────────────────────────────────────────────
pivot = hist.groupby(['modern_name', 'era'])['win_pct'].mean().unstack(fill_value=0)
fig, ax = plt.subplots(figsize=(14, 7))
sns.heatmap(pivot, cmap='RdYlGn', center=.55, ax=ax, annot=True, fmt='.2f', linewidths=.5)
ax.set_title('Era Win% Heatmap — Franchise × NL Era')
plt.tight_layout()
plt.savefig(OUT / 'era_heatmap.png', dpi=200, bbox_inches='tight')
plt.close()
print("✓ era_heatmap.png")

# ── 5. Championship Drought Chart ──────────────────────────────────────
titles = {
    'St. Louis Cardinals'   : [1926,1931,1934,1942,1944,1946,1964,1967,1982,1985,1987,1996,2006,2011,2013,2025],
    'San Francisco Giants'  : [1905,1921,1922,2010,2012,2014],
    'Los Angeles Dodgers'   : [1955,1959,1963,1965,1966,1981,1988,1995,2020,2024],
    'Atlanta Braves'        : [1914,1957,1995,2021],
    'Cincinnati Reds'       : [1919,1940,1975,1976,1990],
    'Pittsburgh Pirates'    : [1909,1925,1960,1971,1979],
    'Chicago Cubs'          : [1907,1908,2016],
    'Philadelphia Phillies' : [1980,2008],
    'New York Mets'         : [1969,1986],
    'Florida Marlins'       : [1997,2003],
    'Arizona Diamondbacks'  : [2001],
    'Washington Nationals'  : [2019],
}

fig, ax = plt.subplots(figsize=(14, 7))
for i, (team, years) in enumerate(titles.items()):
    gaps = [years[j] - years[j-1] for j in range(1, len(years))]
    if gaps:
        ax.barh(i, gaps, left=years[:-1], height=.6,
                color=sns.color_palette('pastel')[i % 12])
        for j, gap in enumerate(gaps):
            ax.text(years[j] + gap/2, i, f'{gap}y', va='center', ha='center', fontsize=7)

ax.set_yticks(range(len(titles)))
ax.set_yticklabels(list(titles.keys()), fontsize=9)
ax.set_xlabel('Season')
ax.set_title('NL Championship Drought Tracker  (years between NL WS titles)')
plt.tight_layout()
plt.savefig(OUT / 'championship_droughts.png', dpi=200, bbox_inches='tight')
plt.close()
print("✓ championship_droughts.png")

print(f"\nAll 5 charts saved to {OUT}/")
