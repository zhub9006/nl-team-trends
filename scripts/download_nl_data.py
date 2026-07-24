#!/usr/bin/env python3
"""
nl-team-trends: Data Download Script
Downloads the Lahman Baseball Database and relevant CSV datasets for NL historical analysis.

Usage:
    python scripts/download_nl_data.py

Requirements:
    pip install -r requirements.txt
"""

import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
SCRIPTS_DIR = REPO_ROOT / "scripts"


def ensure_directory(path: Path):
    """Create directory if it doesn't exist."""
    path.mkdir(parents=True, exist_ok=True)


def download_lahman_db():
    """Download the latest Lahman Baseball Database from SABR/chadwickbureau."""
    print("Downloading Lahman Baseball Database...")
    url = "https://github.com/chadwickbureau/baseballdatabank/archive/refs/heads/master.zip"
    tmp_zip = REPO_ROOT / "lahman_temp.zip"
    
    import requests
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    tmp_zip.write_bytes(resp.content)
    
    # Extract
    import zipfile
    extract_dir = REPO_ROOT / "lahman_raw"
    ensure_directory(extract_dir)
    with zipfile.ZipFile(tmp_zip, 'r') as z:
        z.extractall(extract_dir)
    
    # Copy relevant CSV files to data/ directory
    lahman_data = extract_dir / "baseballdatabank-master"
    csv_files = [
        "Teams.csv",
        "TeamsFranchises.csv", 
        "Seasons.csv",
        "AllstarFull.csv",
        "Managers.csv",
        "ParkFactors.csv",
    ]
    
    for csv_file in csv_files:
        src = lahman_data / csv_file
        if src.exists():
            import shutil
            dest = DATA_DIR / csv_file.lower()
            shutil.copy2(src, dest)
            print(f"  Copied {csv_file} -> {dest}")
    
    # Cleanup
    tmp_zip.unlink()
    print("Lahman Database download complete!")


def verify_data_files():
    """Check that expected data files exist in the data/ directory."""
    expected = [
        "nl_all_time_records.csv",
        "nl_season_by_year_full.csv",
        "nl_era_win_pct_comparison.csv",
        "nl_h2h_matrix_full.csv",
        "nl_h2h_summary_by_team.csv",
    ]
    print("\nVerifying data files:")
    for f in expected:
        path = DATA_DIR / f
        if path.exists():
            size = path.stat().st_size
            print(f"  ✓ {f} ({size:,} bytes)")
        else:
            print(f"  ✗ {f} (missing)")


def main():
    print("=" * 60)
    print("NL Team Trends - Data Download Script")
    print("=" * 60)
    
    ensure_directory(DATA_DIR)
    
    # Download Lahman DB
    download_lahman_db()
    
    # Verify existing files
    verify_data_files()
    
    print("\nDone! Data ready for analysis.")


if __name__ == "__main__":
    main()