"""
NL Team Trends - Data Loader
Utility to load and explore the NL team trend datasets.
"""
import pandas as pd
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

def load_all_time_records():
    return pd.read_csv(os.path.join(DATA_DIR, 'nl_all_time_records.csv'))

def load_historical_performance():
    return pd.read_csv(os.path.join(DATA_DIR, 'nl_historical_performance.csv'))

def load_pennant_winners():
    return pd.read_csv(os.path.join(DATA_DIR, 'nl_pennant_winners.csv'))

def load_championship_trends():
    return pd.read_csv(os.path.join(DATA_DIR, 'nl_championship_trends.csv'))

def load_notable_records():
    return pd.read_csv(os.path.join(DATA_DIR, 'nl_notable_records.csv'))

def load_h2h_rivalries():
    return pd.read_csv(os.path.join(DATA_DIR, 'nl_h2h_rivalries_detailed.csv'))

if __name__ == '__main__':
    print('=' * 60)
    print('NL Team Trends - Data Explorer')
    print('=' * 60)
    records = load_all_time_records()
    print(f'\nAll-time NL franchise records: {len(records)} teams')
    print(records.sort_values('WS_Titles', ascending=False).head())