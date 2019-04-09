# searchPlayers

players = ['Choupo','Messi','Verratti', 'Messi', 'Choupo', 'Ronaldo', 'Messi']
# searchedPlayer = 'Messi'
searchedPlayer = input("Searched player's name:")
nbFound = 0
nbPlayers = len(players)

while nbPlayers > 0:
    nbPlayers -= 1
    # print(players[nbPlayers])
    if players[nbPlayers] == searchedPlayer:
        # print(searchedPlayer + ' trovato !')
        nbFound += 1

print(searchedPlayer + ' found ' + str(nbFound) + ' fois')
