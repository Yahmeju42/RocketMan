#Le fichier qui s'occupe de la classe du jeu
#J'ai mis # pour les fonctions à faire en priorité et ## pour les fonctions secondaire
import pygame
global name
name = "RocketMan" #la variable du nom du jeu

class Game():
    #la classe qui contient toute le fonctions et variables du jeu
    def __init__(self):
        #merci d'initialiser toute les variables ici
        self.play = True
        print("init game")
        self.window = pygame.display.set_mode((800, 600)) #défini la fenêtre et sa taille
        pygame.display.set_caption(name) #défini le nom de la fenêtre
        icon = pygame.image.load("textures/icon.png").convert() #charge l'icon de la fenêtre
        pygame.display.set_icon(icon) #défini l'icon de la fenêtre


    #def loadmap(self):    Charge la map du jeu
    def events(self):
        #Capte les évènements claviers
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #quitte le jeu
                self.play = False
    #def calc(self):       Calcule les positions et les colisions
    #def write(self):      Affiche à l'écran les différents objets ayant changer de positions
    ##def win(self):        Le joueur a gagné
    ##def lose(self):       Le joueur a perdu

    def loop(self):
        #La boucle de jeu qui lance events, calc et write en boucle et qui se charge de la synchronisation
        print("lancement de la boucle du jeu")
        while(self.play == True):
            print("jeu")
            self.events()
