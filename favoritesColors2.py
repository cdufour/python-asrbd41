# favoritesColors2.py
colors = ['vert','blanc','rouge']
favoriteColor = input('Quelle est ta couleur favorite ?')

# Affichage des couleurs
for color in colors:
    print(color)

# l'opérateur in permet de rechercher une valeur
# dans une liste et renvoie True s'il la trouve
if favoriteColor in colors:
    print('Tu as bon gout')
else:
    print('Couleur non trouvee')
