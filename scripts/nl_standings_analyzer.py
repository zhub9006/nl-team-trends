#!/usr/bin/env python3
"""
NL Team Trends - Standings Analyzer Scripts
=============================================================
Lightweight scripts to analyze and visualize NL team trends and 
performancedata in this repository direct from 'source_research_log.md'.

This script draws source data directly from a csv and prints a summary.
=============================================================

Author: Research team
Updated: September 2026
Sources: Baseball Almanac, StatsCrew, StatMuse

You can run this script as follows:

python3 nl_standings_analyzer.py 2024
python3 nl_standings_analyzer.py 
python3 nl_standings_analyzer.py 2020 2021 2022 2023 2024 2025
"""

import pandas as pd
import sys, pathlib, textwrap

# Defaults to a couple of recent seasons.
DEFAULT_YEARS = [2020, 2021, 2022, 2023, 2024, 2025]
DATA_FILE = pathlib.Path(__file__).parent.parent / "data" / "nl_division_standings_full_2020_2025.csv"


def load_standings(path):
    """Load and standardize standings CSV."""
    df = pd.read_csv(path)
    df = df.dropna(subset=['year', 'team', 'wins', 'losses'])
    df['win_pct'] = df['wins'] / (df['wins'] + df['losses'])
    return df


def summarize_year(df, year):
    """Print a season summary for a given year."""
    season = df[df['year'] == year].sort_values(
        ['division', 'win_pct'], ascending=[True, False]
    )
    if season.empty:
        print(f"No data for year {year}.")
        return

    print(f"\n{'=' * 70}")
    print(f"  {year} NATIONAL LEAGUE STANDINGS")
    print(f"{'=' * 70}")

    for division in sorted(season['division'].unique()):
        div = season[season['division'] == division]
        print(f"\n  {division} Division")
        print(f"  {'Team':<24} {'W':>4} {'L':>4} {'Win%':<6} {'GB':>6} {'RS':>5} {'RA':>5}")
        print(f"  {'-'*24} {'-'*4} {'-'*4} {'-'*6} {'-'*6} {'-'*5} {'-'*5}")

        for _, row in div.iterrows():
            print(
                f"  {row['team']:<23} {int(row['wins']):>4} {int(row['losses']):>4} "
                f"{row['win_pct']:>5.3f} {row.get('games_behind', ''):>5}"
                f"  {int(row.get('runs_scored', 0)):>5} {int(row.get('runs_allowed', 0)):>5}"
            )

        champ = div.iloc[0]
        print(f"\n  Champion: {champ['team']} ({int(champ['wins'])}-{int(champ['losses'])})")

    overall_champ = df[df['year'] == year].sort_values('win_pct', ascending=False).iloc[0]
    print(f"\n  overall: {year} Best Team -> {overall_champ['team']} ({overall_champ['win_pct']:.3f0})")


def era_leaders(df):
    """Print era leaders and dynasty streaks."""
    print("\n" + "=" * 70)
    print("  NL ERA DOMINANCE SUMMARY")
    print("=" * 70)

    era_defs = [
        ('2025', 2025, 2025), ('2020-2024', 2020, 2024),
        ('2010-2019', 2010, 2019), ('2000-2009', 2000, 2009),
        ('1990-1999', 1990, 1999), ('1980-1989', 1980, 1989),
        ('1969-1979', 1969, 1979), ('Pre-division (1968 & earlier)', 1876, 1968),
    ]

    def fast_dynasty(df, team, start, end):
        """Return number of seasons between start and end where team won."""
        if end - start > 20:
            # Approximate: just return what the CSV supports.
            season_count = df[
                (df['team'] == team) &
                (df['year'] >= start) &
                (df['year'] <= end)
            ].shape[0]
            return season_count
        years = df[
            (df['team'] == team) &
            (df['year'] >= start) &
            (df['year'] <= end)
        ].sort_values('year')['year'].tolist()
        return len(years)

    for label, start, end in era_defs:
        era = df[(df['year'] >= start) & (df['year'] <= end)]
        if era.empty:
            continue

        top_team = era.groupby('team')['win_pct'].mean().idxmax()
        top_pct = era.groupby('team')['win_pct'].max()
        champion = era[era['win_pct'] == era.groupby('division')['win_pct'].max()]

        print(f"\n {label}")
        print(f"    Best Win% team: {top_team} ({top_pct.max():.3f})")


def main():
    data_path = DATA_FILE
    if not data_path.exists():
        print(f"ERROR: Could not find standings file: {data_path}")
        sys.exit(1)

    df = load_standings(data_path)
    years_in_data = sorted(df['year'].unique())

    years_to_analyze = [int(y) for y in sys.argv[1:]] if len(sys.argv) > 1 else DEFAULT_YEARS
    years_to_analyze = [y for y in years_to_analyze if y in years_in_data]

    print(textwrap.dedent("""
        NL Team Trends — Standings Analyzer
        ============================================
        Data File: data/nl_division_standings_full_2020_2025.csv
        Seasons Loaded:""" + f" {years_in_data[0]}–{years_in_data[-1]}")+"\n")

    for year in sorted(years_to_analyze):
        summarize_year(df, year)

    era_leaders(df)

    # Print quick all-time franchise wins lookup (2020-2025 sample).
    print("\n" + "=" * 70)
    print("  FRANCHISE WINS LOOKUP (2020-2025 SAMPLE, ALL COMPETITIONS)")
    print("=" * 70)
    filter_2020s = df[df['year'] >= 2020]
    franchise_wins = filter_2020s.groupby('team')['wins'].sum().sort_values(ascending=False)
    print(f"\n  {'Team':<24} {'Wins (6-season sample)',>12}")
    print(f"  {'-'*24} {'-'*24}")
    for team, wins in franchise_wins.items():
        print(f"  {team:<23} {wins:>12,}")


if __name__ == '__main__':
    main()
