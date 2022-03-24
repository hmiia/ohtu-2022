class Player:
    def __init__(self, name, nationality, assits, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assits = assits
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
        self.val = self.goals + self.assits
    
    def __str__(self):
        return f" {self.name:20} {self.team} {str(self.goals):2} + {str(self.assits):2} = {str(self.val)}"
