# Sources & Methodology

## Research Sources

### Primary Sources (Authoritative Baseball Data)

| Source | Coverage | URL | Reliability |
|--------|----------|-----|-------------|
| Baseball Reference | NL standings, team stats 1876–present | https://www.baseball-reference.com/leagues/NL/ | ★★★★★ |
| Retrosheet | Play-by-play and box scores 1898–present | https://www.retrosheet.org/ | ★★★★★ |
| Lahman Database (SABR) | Complete MLB stats 1871–present | https://sabr.org/lahman-database/ | ★★★★★ |
| Baseball Almanac | Team-vs-team H2H records 1876–present | https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml | ★★★★ |
| FBref.com | Advanced NL season statistics | https://fbref.com/en/comps/34/history/ | ★★★★★ |
| MLB.com | Official NL news and standings | https://www.mlb.com/national-league | ★★★★ |
| Baseball Data Hub | All MLB seasons browsable | https://baseballdatabank.github.io/ | ★★★★ |
| StatsCrew | Historical standings | https://www.statscrew.com/baseball/l-NL | ★★★★ |
| Linger & Look | Year-by-year NL standings | https://www.lingerandlook.com/Names/BaseballStandings.php | ★★★★ |
| GitHub - chadwickbureau/baseballdatabank | Open-source complete baseball dataset | https://github.com/chadwickbureau/baseballdatabank | ★★★★★ |

### Secondary Sources

| Source | Coverage | URL |
|--------|----------|-----|
| Wikipedia — NL Pennant Winners | Championship history | https://en.wikipedia.org/wiki/List_of_National_League_pennant_winners |
| Wikipedia — World Series Champions | Championship history | https://en.wikipedia.org/wiki/List_of_World_Series_champions |
| Baseball Hall of Fame | Franchise milestones | https://baseballhall.org/ |
| Sporting Life | English NL tables | https://www.sportinglife.com/ |
| FBref.com | English NL season history | https://fbref.com/en/comps/34/history/ |

## Research Methodology

1. **Data Collection:** Season-by-season NL standings were cross-referenced across Baseball Reference, Retrosheet, and Baseballdatabank (GitHub) for accuracy
2. **Franchise Tracking:** Modern team names are used as the canonical identifier; historical franchise relocations are noted (e.g., Braves: Boston → Milwaukee → Atlanta; Dodgers: Brooklyn → Los Angeles; Giants: New York → San Francisco)
3. **Era Classification:** Seasons are tagged by era based on significant league structural changes (division format, expansion, rule changes)
4. **Championship Data:** NL pennant winners and World Series champions verified against Wikipedia and Baseball Reference
5. **H2H Records:** Team-vs-team all-time win-loss data compiled from Baseball Almanac
6. **Validation:** Triple-checked against at least two independent sources for all key statistics

## Key Sources Used in This Project

### For This Project's Research
- **Baseball Reference NL Standings** — Primary source for year-by-year standings and franchise stats
- **Retrosheet.org** — Box score and play-by-play verification
- **SABR Lahman Database** — Complete historical statistics backbone
- **Baseball Almanac** — All-time NL team-vs-team H2H referenced for franchise matchups
- **Existing Research (GitHub)** — `zhub9006/nl-team-trends-research` and `zhub9006/nl-team-trends-v2` provided foundational data and analytical frameworks

## Source URLs Detail

- NL Standings (all years): https://www.baseball-reference.com/leagues/NL/index.shtml
- NL Team-vs-Team H2H: https://www.baseball-almanac.com/teams/teamvsteam-nl.shtml
- Year-by-Year History: https://www.baseball-almanac.com/yearmenu.shtml
- Lahman DB Download: https://sabr.org/lahman-database/
- Retrosheet: https://www.retrosheet.org/
- NL Pennant Winners (Wiki): https://en.wikipedia.org/wiki/List_of_National_League_pennant_winners
- All-Time MLB Win-Loss Records (Wiki): https://en.wikipedia.org/wiki/List_of_all-time_Major_League_Baseball_win%E2%80%93loss_records
- Baseball Data Hub (All Seasons): https://baseballdatabank.github.io/
- MLB Historical Stats Visual: https://baseballsavant.mlb.com/visuals/historical-stats
- OpenIntro ml_teams dataset: https://www.openintro.org/data/index.php?data=mlb_teams
- MLB Win-Loss Visualizer: https://inkandthunder.github.io/win-loss-visualizer/
- NL Team Trends Research: https://github.com/zhub9006/nl-team-trends-research
- NL Team Trends V2: https://github.com/zhub9006/nl-team-trends-v2

## Data Notes

- Win percentages may vary slightly between sources due to different counting methods for ties/canceled games
- Pre-1900 era records use era-appropriate schedules (60–154 games)
- The 1994 season was canceled entirely — no NL champion that year
- The 2020 season was shortened to 60 games due to COVID-19
- From 2022 onward: 12-team playoff format and universal DH adopted in the NL
- Milwaukee Brewers moved from AL to NL in 1998
- Montreal Expos became Washington Nationals in 2005
- Houston Colt .45s/Astros moved from NL to AL in 2013