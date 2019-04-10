from utils import listAverage
html = '''
<!DOCTYPE html>
<html>
    <head></head>
    <body>
        <h1 style="color:red">[firstname] [lastname]</h1>
        <img src="flags/[country].png">
        <p>Moyenne: [average]</p>
        <script>
        alert('Javascript est là !')
        </script>
    </body>
</html>
'''
# source de  données
student1 = {'firstname':'Yassine', 'lastname':'El Khazraji', 'country':'Maroc', 'notes':[4,20,13]}
student2 = {'firstname':'Samba', 'lastname':'Lek', 'country':'Guinée', 'notes':[19,19,0]}
student3 = {'firstname':'Zak', 'lastname':'Abdel Francis', 'country':'France', 'notes':[5,3,20]}
student4 = {'firstname':'Antonio', 'lastname':'Vivaldi', 'country':'Italie', 'notes':[16,12]}
students = [student1, student2, student3, student4]

for student in students:
    # on génère un fichier à chaque passage
    filename = 'webpage_' + student['firstname'].lower() + '.html'
    f = open('./webpages/' + filename, 'w') # crée le fichier

    # remplacements
    htmlChanged = html.replace('[firstname]', student['firstname'])
    htmlChanged = htmlChanged.replace('[lastname]', student['lastname'])
    # calcul de la moyenne, arrondi, conversion en str
    average = str(round(listAverage(student['notes']), 2))
    htmlChanged = htmlChanged.replace('[average]', average)
    htmlChanged = htmlChanged.replace('[country]', student['country'].lower())

    f.write(htmlChanged) # écrit dans le fichier
    f.close()
