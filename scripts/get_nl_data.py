"""NL Team Trends — Data Extraction Script

Downloads and prepares NL team performance data from the Lahman Baseball Database
for analysis and visualization.

Usage:
    python scripts/get_nl_data.py

Requirements:
    pip install -r requirements.txt
"""

import pandas as pd
import os
import sys

# --------------------------------------------------------------
# Configuration
# --------------------------------------------------------------
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
LAHMAN_URL = (
    "https://github.com/chadwickbureau/baseballdatabank/archive/refs/heads/master.zip"
)

# Teams to include (modern NL names)
NL_TEAMS = [
    "ARI", "ATL", "CHC", "CIN", "COL", "LAD", "MIA",
    "MIL", "NYM", "PHI", "PIT", "SDN", "SFN", "SLN", "WAS",
]


def download_lahman():
    """Download and extract the Lahman Baseball Database."""
    import zipfile
    import tempfile
    
    tmp_dir = tempfile.mkdtemp()
    zip_path = os.path.join(tmp_dir, "baseballdatabank.zip")
    
    print(f"Downloading Lahman Database from {LAHMAN_URL}...")
    import urllib.request
    urllib.request.urlretrieve(LAHMAN_URL, zip_path)
    
    print("Extracting...")
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(tmp_dir)
    
    base = os.path.join(tmp_dir, "baseballdatabank-master")
    print(f"Extracted to {base}")
    return base


def load_csv(base_dir, filename):
    """Load a CSV from the Lahman database directory."""
    path = os.path.join(base_dir, filename)
    if os.path.exists(path):
        return pd.read_csv(path, dtype=str)
    print(f"Warning: {path} not found")
    return None


def extract_nl_teams(lahman_dir):
    """Extract NL team-level data from the Lahman database."""
    # Team IDs for NL franchises (mapped to modern names)
    team_id_map = {
        "ari": "ARI", "atl": "ATL", "chn": "CHC", "cin": "CIN",
        "col": "COL", "lad": "LAD", "mia": "MIA", "mil": "MIL",
        "nyn": "NYM", "phi": "PHI", "pit": "PIT", "sdn": "SDN",
        "sfn": "SFN", "sln": "SLN", "wsn": "WAS",
    }
    
    # Load Teams and TeamStandings
    teams_df = load_csv(lahman_dir, "Teams.csv")
    if teams_df is None:
        return None
    
    # Convert numeric columns
    for col in ["W", "L", "G", "RS", "RA", "Rank"]:
        teams_df[col] = pd.to_numeric(teams_df[col], errors="coerce")
    
    # Filter to NL teams
    nl = teams_df[teams_df["lgID"] == "NL"].copy()
    nl["modern_team"] = nl["teamIDBR"].map(team_id_map)
    
    # Calculate win percentage
    nl["win_pct"] = nl["W"] / (nl["W"] + nl["L"])
    
    print(f"Extracted {len(nl)} NL team-seasons from {nl['yearID'].min()} to {nl['yearID'].max()}")
    return nl


def main():
    """Main pipeline: download Lahman DB, extract NL data, save to CSV."""
    lahman_dir = download_lahman()
    nl = extract_nl_teams(lahman_dir)
    
    if nl is not None:
        output_path = os.path.join(DATA_DIR, "nl_lahman_raw.csv")
        nl.to_csv(output_path, index=False)
        print(f"Saved NL team-season data to {output_path}")
        print(f"Columns: {list(nl.columns)}")
        print(f"Shape: {nl.shape}")
    
    # Also pull TeamSpell简短的 franchise continuity info
    teams_info = load_csv(lahman_dir, "Teams.csv")
    if teams_info is not None:
        # Get franchise list
        franchises = teams_info[teams_info["lgID"] == "NL"]["franchID"].unique()
        print(f"\nNL franchises in Lahman DB: {sorted(franchises)}")


if __name__ == "__main__":
    main()
