# sumList.py
notes = [2, 18, 13, 7, 14]
# Calculer et afficher la somme
sum = 0
for note in notes:
    sum += note
print('Somme des notes: ' + str(sum))

# Calculer et afficher la moyenne
average = sum / len(notes)
print('Moyenne des notes: ' + str(average))
