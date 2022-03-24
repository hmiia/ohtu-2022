from operator import attrgetter

class PlayerStats:
  def __init__(self,reader):
    self.reader = reader

  def top_scorers_by_nationality(self, nationality):
      # print(f"Players from {nationality} 2021-01-04 19:15:32.858661:")
      players = self.reader.get_players()
      return [player for player in players if player.nationality == nationality]

  

