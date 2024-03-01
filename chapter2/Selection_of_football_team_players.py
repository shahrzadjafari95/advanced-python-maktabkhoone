import random


class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        return self.name


class Football_player(Person):  # this class inherit of Person class and override init with enter team name
    def __init__(self, name, team):
        super().__init__(name)
        self.team = team


# The get_user_name function first create empty list and then get 22 name from user with use input command and then
# create an object of Person class, so append name of user input to the players_name list. At the end return players_
# name list
def get_user_name():
    players_name = []
    for count in range(22):
        player_name = input('enter your name:')
        player_object = Person(player_name)
        players_name.append(player_object.show_name())
    return players_name


team_a = []
team_b = []

all_players = get_user_name()
random.shuffle(all_players)  # this method changes the original list(all_players)

for i in range(len(all_players)):  # for half the all_players list, create an object from Football_player class and
    # add to the team a and team b
    if i < len(all_players) // 2:
        player = Football_player(all_players[i], "Team A")
        team_a.append(player)
    else:
        player = Football_player(all_players[i], "Team B")
        team_b.append(player)

for player_game in team_a:  # show the name and team_name of each player in the team_a list
    print(player_game.name, "-", player_game.team)

for player_game in team_b:
    print(player_game.name, "-", player_game.team)
