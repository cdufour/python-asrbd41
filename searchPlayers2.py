# searchPlayers2
players = ['Choupo','Messi','Verratti', 'Messi', 'Choupo', 'Ronaldo', 'Messi']
# searchedPlayer = 'Messi'
searchedPlayer = input("Searched player's name:")
nbFound = 0

for player in players:
    if player == searchedPlayer:
        nbFound += 1

print(searchedPlayer + ' found ' + str(nbFound) + ' times')
