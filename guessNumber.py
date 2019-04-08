# guessNumber.py
'''
Le programme détermine un chiffre de manière aléatoire
entre 1 et 100 que l'utilisateur doit deviner

Tant que l'utilisateur n'a pas trouvé le bon chiffre
le programme lui demande de fournir un chiffre

Si le chiffre saisi est inférieur au chiffre à deviner
on affiche "c'est plus"
Si le chiffre est supérieur on affiche "c'est moins"

Quand le bon chiffre est trouvé, on affiche "Bravissimo,
tu as trouvé après n essais"
'''
import random
# produit un nombre aléatoire entre 1 et 100
secretNumber = random.randint(1,100)
tries = 0 # nombre de tentatives

while True:
    print('Devine mon chiffre secret (entre 1 et 100)')
    tries += 1 # incrémentation du nombre d'essais
    response = input() # saisie utilisateur
    if int(response) > secretNumber:
        print("c'est moins")
    elif int(response) < secretNumber:
        print("c'est plus")
    else: # égalité, le secret est trouvé, il faut sortir de la boucle
        print("Bravo ! Tu as trouvé le secret")
        print("Après " + str(tries) + " essai(s)")
        break # sortie de boucle
