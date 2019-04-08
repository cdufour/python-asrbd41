# sumInput.py
'''
Ecrire un programme qui demande un chiffre
à l'utilisateur tant que l'utilisateur ne saisit
une valeur différente de 0
En sortie de boucle, afficher la somme des
valeurs précédemment saisies
Exemple:
5
6
0
=> 11
'''
sum = 0 # somme
while True:
    nb = input('Entre un chiffre (tape 0 pour sortir du programme):')
    if int(nb) == 0: # l'utilisateur a saisi 0
        break # sortie de boucle
    else:
        sum += int(nb) # on écrase la variable sum
        # en lui ajoutant la valeur saisie
print('Somme des valeurs saisies: ' + str(sum))
