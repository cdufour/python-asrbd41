# dictionaryStudent.py
# from précise le fichier source (sans préciser .py)
# import permet d'indiquer la ou les fonctions à importer
from utils import listAverage

student1 = {'firstname':'Yassine', 'lastname':'El Khazraji', 'country':'Maroc', 'notes':[4,20,13]}
student2 = {'firstname':'Samba', 'lastname':'Lek', 'country':'Guinée', 'notes':[19,19,19]}
student3 = {'firstname':'Zak', 'lastname':'Abdel François', 'country':'France', 'notes':[5,3,20]}
students = [student1, student2, student3]

# print(students[2]['lastname']) # output: Abdel François
for student in students:
    # print(student['country'])
    average = round(listAverage(student['notes']), 2) # round limite la partie décimale à une longueur de 2
    print(student['firstname'] + ' a obtenu la moyenne de: ' + str(average))
