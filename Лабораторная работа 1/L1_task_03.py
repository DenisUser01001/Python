list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
total_players = len(list_players)
amount_of_teams = 2
index_first_player_of_team_02 = total_players // amount_of_teams
team_01 = list_players[:index_first_player_of_team_02]
team_02 = list_players[index_first_player_of_team_02:]
print(team_01)
print(team_02)
