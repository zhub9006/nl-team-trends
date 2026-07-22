# Contributing to NL Team Trends

## How to Contribute

### Reporting Issues
- Use GitHub Issues for bug reports, feature requests, or discussion
- Tag issues appropriately: `research`, `data`, `visualization`, `enhancement`

### Adding Data
1. When adding new data files, update `DATA_INDEX.md` with column definitions
2. Follow existing CSV conventions (header row, snake_case columns)
3. Cross-reference data with at least 2 sources before committing
4. Cite sources in `source_references.md` if adding new ones

### Creating Visualizations
1. Add visualization scripts to the `notebooks/` directory as `.ipynb` files
2. Update `visualizations/README.md` with references to new scripts
3. Include a markdown cell at the top of each notebook explaining the visualization

### Submitting Pull Requests
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Commit with a descriptive message
5. Push to your branch: `git push origin feature/your-feature-name`
6. Open a Pull Request against the `main` branch

## Data Entry Standards

- Always use UTF-8 encoding for CSV files
- Use snake_case for column names
- Use `N/A` for missing data
- Use semicolons to separate multiple values in a single cell (e.g., pennant_years)
- Keep win percentages as decimals with 3 places (e.g., 0.535)

## Source Attribution

Primary sources for this project:
- Baseball-Reference.com
- Baseball Almanac
- Wikipedia
- SABR Lahman Database
- MLB.com

Please cite these sources when using project data.
