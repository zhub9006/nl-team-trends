#!/usr/bin/env python3
"""NL Team Trends - Sample Visualization Scripts

This script demonstrates how to generate charts from the NL historical performance data.
Run with: python nl_viz.py
"""

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ============================================================
# Chart 1: All-Time NL Franchise Wins & Losses (Horizontal Bar)
# ============================================================
def chart_franchise_wins():
    records = pd.read_csv('../data/nl_all_time_franchise_records.csv')
    records_sorted = records.sort_values('wins', ascending=True)

    fig, ax = plt.subplots(figsize=(14, 9))
    # Color by team
    card_colors = {
        'St. Louis Cardinals': '#C41E3A',
        'Los Angeles Dodgers': '#005A9C',
        'San Francisco Giants': '#FD5A1E',
        'Chicago Cubs': '#0E3386',
        'Atlanta Braves': '#CE1141',
        'Cincinnati Reds': '#C6011F',
        'Pittsburgh Pirates': '#FFC72C',
        'New York Mets': '#002D72',
        'Philadelphia Phillies': '#E81828',
        'Milwaukee Brewers': '#122153',
        'Arizona Diamondbacks': '#A71930',
        'Washington Nationals': '#AB0003',
        'Miami Marlins': '#00A3E0',
        'Colorado Rockies': '#33006F',
        'San Diego Padres': '#2F241E',
    }
    colors = [card_colors.get(t, '#888888') for t in records_sorted['team']]

    ax.barh(records_sorted['team'], records_sorted['wins'], color=colors, edgecolor='white', label='Wins')
    ax.barh(records_sorted['team'], records_sorted['losses'], left=records_sorted['wins'], color='#cccccc', alpha=0.4, edgecolor='white', label='Losses')
    ax.set_xlabel('Total Games', fontsize=12)
    ax.set_title('All-Time NL Regular-Season Franchise Wins & Losses (through 2025)', fontsize=14, fontweight='bold')
    ax.legend(loc='lower right')
    plt.tight_layout()
    plt.savefig('nl_franchise_wins_losses.png', dpi=150)
    plt.close()
    print('✓ Saved nl_franchise_wins_losses.png')


# ============================================================
# Chart 2: Win Rate Distribution by Era
# ============================================================
def chart_era_dist():
    perf = pd.read_csv('../data/nl_historical_performance.csv')
    fig, ax = plt.subplots(figsize=(14, 7))
    eras = perf['era'].unique()
    era_data = {e: perf[perf['era'] == e]['nl_win_pct'] for e in eras if str(e) != 'nan'}
    box_data = list(era_data.values())
    labels = [e.replace('_', ' ').title() for e in era_data.keys()]

    # Custom colors for eras
    era_colors = sns.color_palette('Set2', len(era_data))
    bp = ax.boxplot(box_data, labels=labels, patch_artist=True)
    for patch, color in zip(bp['boxes'], era_colors):
        patch.set_facecolor(color)

    ax.set_ylabel('Championship Win Percentage', fontsize=12)
    ax.set_title('NL Championship Win % Distribution by Era', fontsize=14, fontweight='bold')
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    plt.savefig('nl_era_win_pct_boxplot.png', dpi=150)
    plt.close()
    print('✓ Saved nl_era_win_pct_boxplot.png')


# ============================================================
# Chart 3: H2H Rivalry Horizontal Bar
# ============================================================
def chart_h2h():
    h2h = pd.read_csv('../data/nl_team_vs_team_summary.csv')
    # Compute total and sort
    h2h['total'] = h2h['t1_wins'] + h2h['t2_wins']
    h2h_sorted = h2h.sort_values('t1_win_pct', ascending=True)

    fig, ax = plt.subplots(figsize=(12, 10))
    # Plot the t1 win pct - so if t1 is dominant, it skews right
    y_labels = [f"{r['team_1']} vs {r['team_2']}" for _, r in h2h_sorted.iterrows()]
    x_vals = h2h_sorted['t1_win_pct']
    colors = ['#C41E3A' if v > 0.65 else '#005A9C' if v < 0.45 else '#888888' for v in x_vals]

    ax.barh(y_labels, x_vals, color=colors, edgecolor='white')
    ax.axvline(x=0.5, color='black', linestyle='--', alpha=0.5, label='Even (50%)')
    ax.set_xlabel('Team 1 Win Percentage', fontsize=12)
    ax.set_title('NL H2H Rivalry Win % (Team 1 %)', fontsize=14, fontweight='bold')
    ax.legend()
    plt.tight_layout()
    plt.savefig('nl_h2h_rivalry_pct.png', dpi=150)
    plt.close()
    print('✓ Saved nl_h2h_rivalry_pct.png')


# ============================================================
# Chart 4: Recent NL Standings Heatmap
# ============================================================
def chart_recent_standings_heatmap():
    recent = pd.read_csv('../data/nl_recent_standings.csv')
    # Pivot: year vs team
    # Filter to division winners only
    dw = recent[recent['division_finish'] == '1st'][['year', 'team', 'win_pct']].pivot(index='team', columns='year', values='win_pct')

    fig, ax = plt.subplots(figsize=(10, 7))
    sns.heatmap(dw, annot=True, fmt='.2f', cmap='RdYlGn', center=0.55, linewidths=1, ax=ax)
    ax.set_title('NL Division Winners - Win % Heatmap (2018-2026)', fontsize=13, fontweight='bold')
    ax.set_ylabel('Division Winner Team')
    plt.tight_layout()
    plt.savefig('nl_win_pct_heatmap.png', dpi=150)
    plt.close()
    print('✓ Saved nl_win_pct_heatmap.png')


# ============================================================
# Chart 5: WS Championship Timeline
# ============================================================
def chart_ws_timeline():
    champs = pd.read_csv('../data/nl_recent_championships.csv')
    # For the WS champions (NL champs who won WS)
    ws_winners = champs[champs['ws_champion'].str.contains('Dodgers|Cardinals|Braves|Mets|Cubs|Rangers|Rays|Giants', case=False, na=False)]
    
    fig, ax = plt.subplots(figsize=(14, 8))
    color_map = {
        'St. Louis Cardinals': '#C41E3A', 'Los Angeles Dodgers': '#005A9C',
        'Atlanta Braves': '#CE1141', 'Chicago Cubs': '#0E3386',
        'New York Mets': '#002D72', 'San Francisco Giants': '#FD5A1E',
    }
    for _, row in ws_winners.iterrows():
        is_nl = 'Dodgers' in str(row['ws_champion']) or 'Cardinals' in str(row['ws_champion']) or 'Braves' in str(row['ws_champion']) or 'Mets' in str(row['ws_champion']) or 'Cubs' in str(row['ws_champion']) or 'Giants' in str(row['ws_champion'])
        label = str(row['ws_champion'])
        color = color_map.get(label, '#888888') if is_nl else '#cccccc'
        marker = 'D' if is_nl else 's'
        ax.scatter(row['year'], row['nl_win_pct'], color=color, marker=marker, s=100, zorder=5)
        # only annotation of NL champs
        ax.annotate(f"{row['nl_champion']} ({row['ws_champion'].split(' (')[0] if '(' in str(row['ws_champion']) else row['ws_champion']})",
                    (row['year'], row['nl_win_pct']), fontsize=7, rotation=45, ha='right')
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('NL Champion Win %', fontsize=12)
    ax.set_title('NL Champion Season Win % vs Year (▲ = NL champion won WS; ◆ = AL champion broke NL run)', fontsize=13, fontweight='bold')
    ax.axhline(y=0.5, color='gray', linestyle=':', alpha=0.5)
    plt.tight_layout()
    plt.savefig('nl_ws_timeline.png', dpi=150)
    plt.close()
    print('✓ Saved nl_ws_timeline.png')


# ============================================================
# Run all charts
# ============================================================
if __name__ == '__main__':
    print('Generating NL Team Trends visualizations...')
    chart_franchise_wins()
    chart_era_dist()
    chart_h2h()
    chart_recent_standings_heatmap()
    chart_ws_timeline()
    print('\nAll charts generated successfully!')
    print('Output files are in the visualizations/ directory.')
