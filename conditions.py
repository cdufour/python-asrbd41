# conditions.py
isStrong = True
nbStudents = 2
nbStudentsMax = 16

if isStrong == True:
    print('Il est fort')

# Afficher "Le groupe est au complet"
# si la variable nbStudents est supérieure à 15
if nbStudents > 15:
    print("Le groupe est au complet")
else:
    # print("Il manque du monde")
    nbMissing = nbStudentsMax - nbStudents
    if nbMissing > 8:
        print("Il manque " + str(nbMissing) + " personnes")
        print('Cours annulé')
    else:
        print("Il manque " + str(nbMissing) + " personnes")
        print("Cours maintenu")







print('Fin du script')
