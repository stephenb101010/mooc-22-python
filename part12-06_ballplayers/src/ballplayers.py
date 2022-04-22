class BallPlayer:
    def __init__(self, nimi: str, number: int, goals: int, passes: int, minutes: int):
        self.nimi = nimi
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(nimi={self.nimi}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')

def most_goals(players: list):
    player = max(players, key=lambda item: item.goals)
    return player.nimi

def most_points(players: list):
    player = max(players, key= lambda item: item.goals + item.passes)
    return (player.nimi, player.number)

def least_minutes(players: list):
    return min(players, key= lambda item: item.minutes)