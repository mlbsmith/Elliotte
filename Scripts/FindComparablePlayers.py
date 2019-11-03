from GetComparables import *
from GetDataService import *


player_struct = {'last_name': ['Smith'], 'first_name': ['Mitchell'], 'Age': [23], 'Pos': 'C', 'GP': [98], 'G': [30],
                 'A': [63],
                 'Sh': [300],
                 'TOI': [1080]}
player = pd.DataFrame(player_struct)

GDS = GetDataService()
players = GDS.get_all_players()

GC = GetComparables(players)

comparables = GC.get_player_comparables(player)

print(comparables)

