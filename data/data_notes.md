# Data Notes for NL Team Trends Repository
# ==========================================
#
# This document describes the data collection methodology,
# sources used, known limitations, and planned updates.
#
# ## Data Sources
#
# 1. Baseball Almanac (baseball-almanac.com)
#    - NL team-vs-team win-loss matrices, 1876-2026
#    - Team-vs-team H2H data with franchise moves included
#
# 2. Baseball Data Hub (baseballdatahub.com)
#    - Year-by-year NL standings for selected key seasons
#    - Full batting/pitching leaders per season
#    - Playoff bracket results
#
# 3. Lahman Baseball Database (sabr.org/lahman-database/)
#    - Complete historical team stats (1871-2025)
#    - Season-level standings, batting, pitching, fielding
#    - Negro Leagues data included (licensed from Seamheads)
#    - Available in SQL, Access, and CSV formats
#
# 4. OpenIntro mlb_teams dataset
#    - Curated subset of Lahman data (R package)
#    - 2784 rows x 41 variables covering all seasons
#    - Includes team-level win/loss, runs, ERA, etc.
#
# 5. Baseball Reference (baseball-reference.com)
#    - NL index with year-by-year standings
#    - All-time franchise records
#
# 6. Retrosheet (retrosheet.org)
#    - Complete game-by-game records
#    - CSV downloads for programmatic access
#
# ## Known Limitations
#
# - Data for seasons 1871-1875 (National Association) are
#   not included as they predate the NL founding (1876)
# - Team names have changed over the decades; franchise
#   continuity is maintained where possible
# - Negro League NL data (1920-1948) added in 2025
#   Lahman release but presented with caveats
# -罚球赛和平局在早期赛季很常见，可能影响
#   看似奇怪的胜率和排名
# - Interleague play (post-1997) is excluded from
#   team-vs-team matrices (NL-only focus)
# - Colorado Rockies and San Diego Padres franchise
#   histories are shorter (1993 and 1969 respectively)
#
# ## Data File Descriptions
#
# nl_key_seasons.csv:
#   - Selected NL seasons spanning 1876-2025
#   - Full standings for each team in that season
#   - Columns: year, team, wins, losses, win_pct,
#     games_behind, division, team_founded, notes
#   - Covers: founding year, best record, pennant years,
#     WS winners, milestone seasons
#
# nl_pennant_winners.csv:
#   - Every NL pennant winner 1876-2025
#   - Columns: year, team, league, record, win_pct,
#     games_behind, pennant_winner, ws_winner, notes
#
# nl_team_records.csv:
#   - All-time aggregate franchise records
#   - Columns: team, franchise_start, seasons_played,
#     total_wins, total_losses, win_pct, pennants,
#     pennant_pct, ws_titles, ws_pct, last_pennant,
#     last_ws, notes
#   - Based on NL-only seasons; AL history excluded
#
# nl_team_vs_team.csv:
#   - Head-to-head matrices for all NL franchises
#   - Columns: team1, team2, games_played,
#     wins_team1, losses_team1, win_pct_team1, notes
#   - NL-only; interleague games excluded
#
# ## Planned Updates
#
# - Add complete NL standings for every season
# - Add season-by-season visualization scripts
# - Add statistical analysis (run differential,
#   Pythagorean expectation, etc.)
# - Expand team-vs-team matrix to include
#   full H2H game logs by decade
# - Add divisional realignment timeline
# - Compare NL vs. AL performance trends
# - Add Elo ratings or strength-of-schedule metrics