def get_score():
    scores_team = []
    for i in range(6):
        game_score = list(map(int, input().split('-')))
        scores_team.append(game_score)
    return scores_team


def result_of_spain(scores):
    spain_games = [scores[0][::-1], scores[3], scores[4]]
    spain = {'name': 'Spain', 'wins': 0, 'loses': 0, 'draws': 0, 'goal_difference': 0, 'points': 0}
    football_scored = 0
    goals = 0
    for result in spain_games:
        goals += result[0]
        football_scored += result[1]
        if result[0] > result[1]:
            spain['wins'] += 1
            spain['points'] += 3
        elif result[0] < result[1]:
            spain['loses'] += 1
        else:
            spain['draws'] += 1
            spain['points'] += 1
    goal_difference = goals - football_scored
    spain['goal_difference'] = goal_difference
    return spain
    # return f'Spain  wins:{spain["wins"]}, loses:{spain["loses"]} , draws:{spain["draws"]} ,' \
    # f' goal difference:{spain["goal_difference"]} , points:{spain["points"]}'
    # return spain


def result_of_iran(scores):
    spain_games = [scores[0], scores[1], scores[2]]
    iran = {'name': 'Iran', 'wins': 0, 'loses': 0, 'draws': 0, 'goal_difference': 0, 'points': 0}
    goals = 0
    football_scored = 0
    for result in spain_games:
        goals += result[0]
        football_scored += result[1]
        if result[0] > result[1]:
            iran['wins'] += 1
            iran['points'] += 3
        elif result[0] < result[1]:
            iran['loses'] += 1
        else:
            iran['draws'] += 1
            iran['points'] += 1
    goal_difference = goals - football_scored
    iran['goal_difference'] = goal_difference
    return iran


def result_of_portugal(scores):
    spain_games = [scores[1][::-1], scores[3][::-1], scores[5]]
    portugal = {'name': 'Portugal', 'wins': 0, 'loses': 0, 'draws': 0, 'goal_difference': 0, 'points': 0}
    goals = 0
    football_scored = 0
    for result in spain_games:
        goals += result[0]
        football_scored += result[1]
        if result[0] > result[1]:
            portugal['wins'] += 1
            portugal['points'] += 3
        elif result[0] < result[1]:
            portugal['loses'] += 1
        else:
            portugal['draws'] += 1
            portugal['points'] += 1
    goal_difference = goals - football_scored
    portugal['goal_difference'] = goal_difference
    return portugal


def result_of_morocco(scores):
    spain_games = [scores[2][::-1], scores[4][::-1], scores[5][::-1]]
    morocco = {'name': 'Morocco', 'wins': 0, 'loses': 0, 'draws': 0, 'goal_difference': 0, 'points': 0}
    goals = 0
    football_scored = 0
    for result in spain_games:
        goals += result[0]
        football_scored += result[1]
        if result[0] > result[1]:
            morocco['wins'] += 1
            morocco['points'] += 3
        elif result[0] < result[1]:
            morocco['loses'] += 1
        else:
            morocco['draws'] += 1
            morocco['points'] += 1
    goal_difference = goals - football_scored
    morocco['goal_difference'] = goal_difference
    return morocco


def show_result(spain, iran, portugal, morocco):
    teams = [spain, iran, portugal, morocco]
    sorted_teams = sorted(teams, key=lambda x: x['name'])
    sorted_teams = sorted(sorted_teams, key=lambda x: (x['points'], x['wins']), reverse=True)
    for team in sorted_teams:
        print(f'{team["name"]}  wins:{team["wins"]} , loses:{team["loses"]} , draws:{team["draws"]} ,' \
               f' goal difference:{team["goal_difference"]} , points:{team["points"]}')


team_score = get_score()
spain_team = result_of_spain(team_score)
iran_team = result_of_iran(team_score)
portugal_team = result_of_portugal(team_score)
morocco_team = result_of_morocco(team_score)
show_result(spain_team, iran_team, portugal_team, morocco_team)


