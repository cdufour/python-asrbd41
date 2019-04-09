# strings.py

message = 'Ciao tutti'
# print(len(message))
# print(message[0])

# for letter in message:
    # print(letter)

password = input('Mot de passe: ')
if len(password) >= 3 and len(password) <= 6:
    print('ok')
else:
    print('la longueur du mdp doit être comprise entre 3 et 6')
