# Scripts Directory Documentation

This directory contains Python scripts for data loading, analysis, and visualization generation for the NL Team Trends project.

## Files

| File | Description |
|------|-------------|
| `data_loader.py` | Utility to load and explore CSV data files from `data/` |

## Usage

Run scripts from the repo root:
```bash
python scripts/data_loader.py
```

## Adding New Scripts

When adding new scripts, follow these conventions:
1. Name files descriptively: `viz_championship_trends.py`, `analyze_h2h.py`, etc.
2. Import from `data_loader` for CSV loading
3. Save any generated images to `charts/`
4. Add dependencies to `../requirements.txt`

## Requirements

See [requirements.txt](../requirements.txt) for all Python dependencies.