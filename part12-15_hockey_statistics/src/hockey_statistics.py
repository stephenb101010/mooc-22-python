import json

class Player:
    def __init__(self, name:str, nationality:str, assists:int, goals:int, penalties:int, team:str, games:str):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
    
    def __str__(self):
        return f"{self.name:21}{self.team:3}{self.goals:4} + {self.assists:2} = {(self.goals+self.assists):3}"

class HockeyApplication:    
    def __init__(self):
        self.players = []
    
    def help(self):
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")
    
    def read_file(self, file_name: str):
        with open(file_name) as file:
            data = file.read()
        return json.loads(data)

    def add_players(self, all_players: list):
        for player in all_players:
            p = Player(player["name"], player["nationality"], player["assists"], player["goals"], player["penalties"], player["team"], player["games"])
            self.players.append(p)

    def search_player(self):
        name = input("name: ")
        for player in self.players:
            if player.name == name:
                print(player)
    
    def list_teams(self):
        teams = map(lambda player: player.team, self.players)
        teams = set(list(teams))
        for team in sorted(teams):
            print(team)

    def list_countries(self):
        countries = map(lambda player: player.nationality, self.players)
        countries = set(list(countries))
        for country in sorted(countries):
            print(country)

    def __points_scored(self, player: Player):
        return [(player.goals + player.assists), player.goals]

    def list_players_in_team(self):
        team = input("team: ")
        team_players = filter(lambda player: player.team == team, self.players)
        team_players = sorted(team_players, key=self.__points_scored, reverse=True)
        for player in team_players:
            print(player)

    def list_players_in_country(self):
        country = input("country: ")
        country_players = filter(lambda player: player.nationality == country, self.players)
        country_players = sorted(country_players, key=self.__points_scored, reverse=True)
        for player in country_players:
            print(player)

    def list_players_most_points(self):
        max_num_of_players = int(input("how many: "))
        points_players = sorted(self.players, key=self.__points_scored, reverse=True)
        count = 1
        for player in points_players:
            if count <= max_num_of_players:
                print(player)
                count += 1

    def __goals_scored(self, player: Player):
        return [player.goals, (player.games)*-1]

    def list_players_most_goals(self):
        max_num_of_players = int(input("how many: "))
        points_players = sorted(self.players, key=self.__goals_scored, reverse=True)
        count = 1
        for player in points_players:
            if count <= max_num_of_players:
                print(player)
                count += 1

    def execute(self):
        if True:
            file_name = input("file name: ")
        else:
            file_name = "partial.json"
        all_players = self.read_file(file_name)
        print(f"read the data of {len(all_players)} players")
        self.add_players(all_players)
        self.help()
        while True:
            print()
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.search_player()
            if command == "2":
                self.list_teams()
            elif command == "3":
                self.list_countries()
            if command == "4":
                self.list_players_in_team()
            elif command == "5":
                self.list_players_in_country()
            if command == "6":
                self.list_players_most_points()
            elif command == "7":
                self.list_players_most_goals()

app = HockeyApplication()
app.execute()

'''
import json

class Statistics:
    def __init__(self, players: list):
        self.__players = players

    def by_points(self,  p):
        return  p['goals'] + p['assists']

    def by_goals(self,  p):
        # if the numbe of goals is equal, less played games is better
        return (p['goals'], -p['games'])

    def player_data(self, name: str):
        for player in self.__players:
            if player['name'] == name:
                return player
        return None

    def countries(self):
        return sorted(list(set(p['nationality'] for p in self.__players )))

    def teams(self):
        return sorted(list(set(p['team'] for p in self.__players )))

    def players_in_team(self, team: str):
        players = [ p for p in self.__players if p['team'] == team]
        return sorted(players, key=self.by_points, reverse=True)

    def players_from_country(self, country: str):
        players = [ p for p in self.__players if p['nationality'] == country]
        return sorted(players, key=self.by_points, reverse=True)

    def most_points(self, countryra):
        players = sorted(self.__players, key=self.by_points, reverse=True)
        return players[0: countryra]

    def most_goals(self, countryra):
        players = sorted(self.__players, key=self.by_goals, reverse=True)
        return players[0: countryra]

class Application:
    def __init__(self):
        self.__statistics = None

    def instructions(self):
        instructions = """
commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals"""
        print(instructions)
    def f(self, p: dict):
        """
            helper method, which creates a string out of players formatted for output
        """
        points = p['goals'] + p['assists']
        return f"{p['name']:20} {p['team']}  {p['goals']:2} + {p['assists']:2} = {points:3}"

    def read_file(self):
        file_name = input("file: ")
        with open(file_name) as file:
            data = file.read()
        players = json.loads(data)
        print(f"read the data of {len(players)} players")
        self.__statistics = Statistics(players)

    def get_playes(self):
        name = input("name: ")
        player = self.__statistics.player_data(name)
        if player:
            print(self.f(player))

    def get_teams(self):
        for team in self.__statistics.teams():
            print(team)

    def get_countries(self):
        for country in self.__statistics.countries():
            print(country)

    def players_in_team(self):
        team = input("team: ")
        for player in self.__statistics.players_in_team(team):
            print(self.f(player)) 

    def players_from_country(self):
        country = input("country: ")
        for player in self.__statistics.players_from_country(country):
            print(self.f(player)) 

    def most_points(self):
        number = int(input("how many: "))
        for player in self.__statistics.most_points(number):
            print(self.f(player)) 

    def most_goals(self):
        number = int(input("how many: "))
        for player in self.__statistics.most_goals(number):
            print(self.f(player)) 

    def execute(self):
        self.read_file()
        self.instructions()
        while True:
            print()
            command = input("command: ")
            if command == "0":
                return
            elif command == "1":
                self.get_playes()
            elif command == "2":
                self.get_teams()
            elif command == "3":
                self.get_countries()
            elif command == "4":
                self.players_in_team()
            elif command == "5":
                self.players_from_country()
            elif command == "6":
                self.most_points()
            elif command == "7":
                self.most_goals()

Application().execute()
'''