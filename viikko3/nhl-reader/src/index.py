from operator import attrgetter
from player_reader import PlayerReader
from playerstats import PlayerStats

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")
    
    players.sort(key=attrgetter('val'))
    for player in reversed(players):
        print(player)
        
if __name__ == "__main__":
    main()
