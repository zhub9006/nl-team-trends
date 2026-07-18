# NL Team Trends — Data Loader

Utility module for loading and exploring NL team trend data.

## Quick Start
```python
from data_loader import load_nl_records
import pandas as pd

# Load all-time records
df = load_nl_records('data/nl_all_time_records.csv')

# Sort by winning percentage
top_teams = df.sort_values('WinPct', ascending=False)
print(top_teams[['Team', 'WinPct', 'WSChampionships']])
```

## Functions
- `load_nl_records(path)` - Load NL franchise records CSV
- `load_pennant_winners(path)` - Load NL pennant winners CSV
- `load_historical(path)` - Load historical season-by-season standings
- `load_h2h_matrix(path)` - Load team-vs-team H2H W-L summary
- `load_championship_trends(path)` - Load championship trends by era
- `load_notable_records(path)` - Load notable records CSV
- `load_recent_standings(path)` - Load recent divisional standings

## Example: Championship Drought Analysis
```python
import pandas as pd

records = pd.read_csv('data/nl_all_time_records.csv')
# Calculate years since last WS title
print(records[['Team', 'LastWSTitle']].sort_values('LastWSTitle'))
```

## Dependencies
```bash
pip install -r requirements.txt
```