# dictionary.py
dico = {}
# print(type(dico)) output: <class 'dict'>

# team1 = ['FC Juventus', 1904]
team1 = {'name':'FC Juventus', 'created':1904, 'coach':'Allegri'}
# print(team1['name']) output: FC Juventus

print(team1)
team1['created'] = 1897 # mise à jour
print(team1)
team1['stadium'] = 'Allianz Arena' # ajout d'une clé/valeur, méthode 1
print(team1)
team1.update({'scudetti':36}) # ajout d'une clé/valeur, méthode 2
print(team1)
del team1['stadium'] # suppresion d'une clé/valeur
print(team1)

# itération sur les clés du dico
for k in team1.keys():
    print(k)

# itération sur les valeurs du dico
for v in team1.values():
    print(v)

if 'created' in team1.keys():
    print('la clé created existe')

if 'FC Juventus' in team1.values():
    print('la valeur FC Juventus existe')

if not 'AS Roma' in team1.values(): # not: opérateur de négation
    print('AS Roma inexistante')
