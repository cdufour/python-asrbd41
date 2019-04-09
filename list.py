# list.py
# players = list()
players = ["Dybala", "Chiellini", "Ronaldo"]
print(type(players)) # output: <class 'list'>

print(players[0]) # output: Dybala

players.append('Pjanic')
print(players)
players[3] = 'Pianic'
print(players)

# players.remove("Chiellini") # suppression par valeur
del players[1] # suppression par index
print(players)

print(len(players))
