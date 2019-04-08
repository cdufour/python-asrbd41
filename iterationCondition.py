# iterationCondition.py
correctPassword = "abc123"
password = ''
nbAttempts = 0

while password != correctPassword:
    nbAttempts += 1
    if nbAttempts == 3:
        print("Attention: 3 essais effectués")
    print("Essai n° " + str(nbAttempts))
    password = input('Saisir un mot de passe:')


print('Accès autorisé')
