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
        self.vaisseauposition = [0,0]
        self.vitesse = [0,0]
        self.acceleration = [0,0]

    def loadmap(self):
        #Charge la map du jeu
        print("loading map")
        self.fond = pygame.image.load("textures/fond.png").convert()
        self.vaisseautexture = pygame.image.load("textures/fusée.png").convert_alpha()
        self.vaisseautexture = pygame.transform.scale(self.vaisseautexture, (40,40))
    def events(self):
        self.action = "r"
        #Capte les évènements claviers
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                #la touche avancer a été appuyer
                self.action = "z"
                self.play = True
                print("Z")
            if event.type == pygame.QUIT:
                #quitte le jeu
                self.play = False
                print("Aurevoir")

    def calc(self):
    # Calcule les positions et les colisions


        if self.action == "z" :
            self.vitesse[0]+=1

        self.vaisseauposition[0] += self.vitesse[0]

    def write(self):
        #Affiche à l'écran les différents objets ayant changer de positions
        self.window.blit(self.fond, (0,0))
        self.window.blit(self.vaisseautexture, (self.vaisseauposition[0], self.vaisseauposition[1]))


        pygame.display.flip()
    ##def win(self):        Le joueur a gagné
    ##def lose(self):       Le joueur a perdu

    def loop(self):

        #La boucle de jeu qui lance events, calc et write en boucle et qui se charge de la synchronisation
        self.loadmap()
        print("lancement de la boucle du jeu")
        while(self.play == True):
            #print("jeu")
            self.events()
            self.calc()
            self.write()
