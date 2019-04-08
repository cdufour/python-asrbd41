# iterationCondition.py
correctPassword = "abc123"
password = ''
nbAttempts = 0
maxAttempts = 3
 
while nbAttempts < maxAttempts:
    password = input('Saisir votre mot de passe:')
    nbAttempts += 1
    if password == correctPassword:
        print('Mot de passe correct')
        break # on force la sortie de boucle
    else:
        print('Mot de passe incorrect')
