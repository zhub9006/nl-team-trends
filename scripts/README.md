# Analysis Scripts

Miscellaneous Python scripts for data processing, scraping, and utility functions.

## Scripts

| Script | Description |
|--------|-------------|
| `fetch_lahman_db.py` | Download and unpack the SABR Lahman Database CSV files |
| `aggregate_nl_records.py` | Aggregate franchise-level records from the Lahman database |
| `generate_h2h_matrix.py` | Process Baseball Almanac H2H data into the rivalry CSV format |
| `update_standings.py` | Scrape and update NL standings from Baseball-Reference or StatMuse |

## Usage

```bash
python scripts/fetch_lahman_db.py
python scripts/aggregate_nl_records.py
python scripts/aggregate_nl_records.py --help
```

## Dependencies

See `requirements.txt` for full Python dependency list.