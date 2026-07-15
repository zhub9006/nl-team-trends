#!/usr/bin/env python3
"""
NL Team Trends — Quick Analysis Scripts
Run from the `notebooks/` directory or from the repo root.
"""

import pandas as pd
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

def load_csv(filename):
    path = os.path.join(DATA_DIR, filename)
    return pd.read_csv(path)

def main():
    print("="*70)
    print("NL Team Trends — Quick Data Overview")
    print("="*70)
    
    # 1. All-time records
    print("\n【1】All-Time NL Franchise Records (from nl_all_time_records.csv)")
    print("-"*70)
    records = load_csv('nl_all_time_records.csv')
    print(f"Total franchises tracked: {len(records)}")
    print(f"Most wins: {records.loc[records['Wins'].idxmax(), 'Franchise']} ({records['Wins'].max():,})")
    print(f"Highest Win%: {records.loc[records['Win_Pct'].idxmax(), 'Franchise']} ({records['Win_Pct'].max():.3f})")
    print(f"Most pennants: {records.loc[records['Pennants'].idxmax(), 'Franchise']} ({records['Pennants'].max()})")
    print(f"Most WS titles: {records.loc[records['WS_Titles'].idxmax(), 'Franchise']} ({records['WS_Titles'].max()})")
    print()
    
    # 2. Championship trends
    print("【2】NL Championship History (from nl_championship_trends.csv)")
    print("-"*70)
    ct = load_csv('nl_championship_trends.csv')
    ws_winners = ct.dropna(subset=['WS_Result'])
    print(f"Total championship highlights: {len(ct)}")
    print(f"World Series winners listed: {len(ws_winners)}")
    print("\nMost Recent WS Winners:")
    for _, row in ws_winners.tail(10).iterrows():
        print(f"  {int(row['Year'])} {row['Franquise']} ({row['Record']}) — {row.get('Notable_Event','')}")
    print()
    
    # 3. Notable Records
    print("【3】Notable NL Records (from nl_notable_records.csv)")
    print("-"*70)
    nr = load_csv('nl_notable_records.csv')
    print(f"Total records catalogued: {len(nr)}")
    print("\nKey Single-Season Records:")
    single_season = nr[nr['Record_Category'].str.contains('Best|Record', case=False)]
    for _, row in single_season.iterrows():
        print(f"  {row['Record_Category']}: {row['Team']} ({row['Value']})")
    print()
    
    print("="*70)
    print("All data loaded from ./data/ directory successfully!")
    print("="*70)

if __name__ == '__main__':
    main()
