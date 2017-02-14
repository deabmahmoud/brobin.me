TEAMS = {
    'MIN': 30,
    'NYR': 3,
    'WSH': 15,
    'BOS': 6,
    'DET': 17,
    'NYI': 2,
    'FLA': 13,
    'COL': 21,
    'NSH': 18,
    'NJD': 1,
    'LAK': 26,
    'DAL': 25,
    'CGY': 20,
    'TOR': 10,
    'CAR': 12,
    'WPG': 52,
    'TBL': 14,
    'PIT': 5,
    'VAN': 23,
    'STL': 19,
    'CHI': 16,
    'MTL': 8,
    'PHI': 4,
    'ANA': 24,
    'CBJ': 29,
    'BUF': 7,
    'EDM': 22,
    'SJS': 28,
    'ARI': 53,
    'OTT': 9,
}

NHL_TEAMS = {team: team for team in TEAMS.keys()}
NHL_TEAMS['TB'] = 'TBL'
NHL_TEAMS['LA'] = 'LAK'
NHL_TEAMS['SJ'] = 'SJS'
NHL_TEAMS['NJ'] = 'NJD'
NHL_TEAMS = [(key, team) for key, team in NHL_TEAMS.items()]
NHL_TEAMS.sort(key=lambda x: x[0])
