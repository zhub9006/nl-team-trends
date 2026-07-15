"""
NL Team Trends - Starter Analysis Script
Loads historical NL data and generates key statistics and charts.
"""

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# Load all-time franchise records
df = pd.read_csv("data/nl_all_time_records.csv")
df_sorted = df.sort_values('win_pct', ascending=False)
print("NL Franchise Win% Ranking:")
print(df_sorted[['franchise', 'games', 'wins', 'losses', 'win_pct', 'ws_titles']].to_string(index=False))

# Generate Win% bar chart
fig, ax = plt.subplots(figsize=(12, 8))
df_plot = df.sort_values('win_pct', ascending=True)
colors = {'East': '#e74c3c', 'Central': '#3498db', 'West': '#2ecc71'}
bar_colors = [colors[d] for d in df_plot['division']]
ax.barh(df_plot['franchise'], df_plot['win_pct'], color=bar_colors, edgecolor='black', linewidth=0.5)
ax.set_xlabel('Winning Percentage')
ax.set_title('NL All-Time Franchise Winning Percentage (1876-2025)')
ax.axvline(x=df['win_pct'].mean(), color='gray', linestyle='--', label=f"Avg: {df['win_pct'].mean():.3f}")
plt.tight_layout()
os.makedirs('visualizations/figures', exist_ok=True)
plt.savefig('visualizations/figures/win_pct_by_franchise.png', dpi=150)
print('Saved: visualizations/figures/win_pct_by_franchise.png')
plt.close()
print('Analysis complete!')
