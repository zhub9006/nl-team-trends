#!/usr/bin/env python3
"""
NL Team Trends - Quick Analysis Script
Loads NL historical data and generates summary statistics.
"""

import pandas as pd
import os

def load_csv(filename):
    """Load a CSV file from the data directory, skipping comment lines."""
    path = os.path.join('data', filename)
    if not os.path.exists(path):
        print(f"Warning: {path} not found. Skipping.")
        return None
    df = pd.read_csv(path, comment='#', skipinitialspace=True)
    print(f"Loaded {filename}: {len(df)} rows")
    return df

def main():
    print("=" * 60)
    print("NL Team Trends - Historical Performance Analysis")
    print("=" * 60)
    
    # Load all-time records
    print("\n--- All-Time NL Franchise Records ---")
    records = load_csv('nl_all_time_records.csv')
    if records is not None:
        print(f"\nTotal NL franchises: {len(records)}")
        print(f"Most all-time wins: {records.loc[records['Wins'].idxmax(), ['Team', 'Wins']].values}")
        print(f"Best win percentage: {records.loc[records['WinPct'].idxmax(), ['Team', 'WinPct']].values}")
        print(f"Most pennants: {records.loc[records['Pennants'].idxmax(), ['Team', 'Pennants']].values}")
        print(f"Most WS titles: {records.loc[records['WS_Won'].idxmax(), ['Team', 'WS_Won']].values}")
        print("\nTop 5 by Win%:")
        top5 = records.nlargest(5, 'WinPct')[['Team', 'WinPct', 'Games_Played', 'Wins', 'Losses']]
        print(top5.to_string(index=False))
    
    # Load championship trends
    print("\n--- Championship Trends by Era ---")
    trends = load_csv('nl_championship_trends.csv')
    if trends is not None:
        print(f"\nEras tracked: {len(trends)}")
        for _, row in trends.iterrows():
            print(f"  {row['Era']}: {row['Start_Year']}-{row['End_Year']} ({row['Num_Seasons']} seasons)")
            print(f"    Dominant: {row['Dominant_Franchise']}")
            print(f"    Theme: {row['Key_Trend']}")
    
    # Load notable records
    print("\n--- Key Notable Records ---")
    records_df = load_csv('nl_notable_records.csv')
    if records_df is not None:
        print(f"\nRecords tracked: {len(records_df)}")
        for _, row in records_df.head(8).iterrows():
            print(f"  {row['Category']}: {row['Record']} — {row['Team_Year']} ({row.get('Details', '')})")

if __name__ == '__main__':
    main()