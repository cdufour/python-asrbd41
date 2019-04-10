# poo.py
class Team:
    # 1/ propriétés
    name = ''
    stadium = ''
    coach = ''
    points = 0

    # 2/ méthodes

    # constructeur: méthode qui exécutée automatiquement
    # au moment de l'instanciation
    def __init__(self, name):
        self.name = name

    def win(self):
        self.points += 3
        # return 3

    def draw(self):
        self.points += 1

    def printPoints(self):
        print(self.name + ': ' + str(self.points) + ' points')

team1 = Team('PSG') # instanciation de la classe Team
# un objet est généré à partir de la classe
# il dispose de toutes les propriétés et de toutes
# les méthodes définies par la classe Team

# team1.name = 'PSG'
team1.printPoints()
team1.win()
team1.draw()
team1.printPoints()

team2 = Team('Chelsea')
team2.printPoints()
team2.draw()
team2.draw()
team2.printPoints()

team3 = Team()
