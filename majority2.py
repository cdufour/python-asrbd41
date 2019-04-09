# majority2.py
age = input('Quel est ton age: ')

if age.isnumeric():
    if int(age) < 70:
        if int(age) > 17:
            print("Tu peux passer le permis")
        else:
            if int(age) >= 16:
                print("Conduite accompagnée possible")
            else:
                print("Tu dois attendre...")
    else:
        print("Tu es danger pour la jeune génération")
else:
    print('Saisir une valeur numérique svp')
