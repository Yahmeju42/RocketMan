#Le fichier qui s'occupe de la classe du jeu
#J'ai mis # pour les fonctions à faire en priorité et ## pour les fonctions secondaire
global name
name = "RocketMan"
print("hello world", name)

class Game():
    #la classe qui contient toute le fonctions et variables du jeu
    def __init__(self):
        print("init game")
        #self.window

    #def loadmap(self):    Charge la map du jeu
    #def events(self):     Capte les évènements claviers
    #def calc(self):       Calcule les positions et les colisions
    #def write(self):      Affiche à l'écran les différents objets ayant changer de positions
    ##def win(self):        Le joueur a gagné
    ##def lose(self):       Le joueur a perdu

    #def loop       La boucle de jeu qui lance events, calc et write en boucle et qui se charge de la synchronisation
