# favoritesColors.py
'''
1. Créer une liste de couleurs (au choix)
2. Afficher chacune des couleurs via une boucle for
3. Demander à l'utilisateur d'indiquer sa couleur
préférée
4. Rechercher la couleur saisie dans la liste
Si elle est trouvée => afficher "Tu as bon goût"
Sinon: "Couleur non trouvée"

'''
colors = ['vert','blanc','rouge'] #1
for color in colors: #2
    print(color)

#3
favoriteColor = input('Quelle est ta couleur favorite ?')

#4
foundColor = False
for color in colors:
    if favoriteColor == color:
        foundColor = True
        break # optimisation, inutile de continuer à boucler, on sort

if foundColor: # équivalent à: if foundColor == True:
    print("Tu as bon gout")
else:
    print("Couleur non trouvee")
