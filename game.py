#Le fichier qui s'occupe de la classe du jeu
#J'ai mis # pour les fonctions à faire en priorité et ## pour les fonctions secondaire
import pygame
global name
name = "RocketMan" #la variable du nom du jeu
from poto import *

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
        self.vaisseauposition = [150,0]
        self.vitesse = [0,0]
        self.acceleration = [0,0]
        self.nombrepoto = 16 #Defini le nombre de potos total à l'écran
        self.proportion = 0.7  #Défini la vitesse supplementaire à donner au vaisseau à chaque poussée
        self.score = 0  #Initialisation du score du jour à 0
        self.gravite = 0.002

        self.potos = [Poto]*self.nombrepoto
        for k in range(self.nombrepoto):
            self.potos[k] = Poto()

    def loadmap(self):
        #Charge la map du jeu
        print("loading map")
        self.fond = pygame.image.load("textures/fond.png").convert()
        self.vaisseautexture = pygame.image.load("textures/fusée.png").convert_alpha()
        self.vaisseautexture = pygame.transform.scale(self.vaisseautexture, (40,40))

        for k in range(self.nombrepoto): #Placement des potos initiaux
            self.potos[k].x = 800 + 50*k
    def events(self):
        self.action = "r"
        #Capte les évènements claviers
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                #la touche avancer a été appuyer
                self.action = "z"
                print("haut")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                #la touche avancer a été appuyer
                self.action = "s"
                print("bas")
           # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                #la touche avancer a été appuyer
                #self.action = "d"
                #print("droite")
           # elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                #la touche avancer a été appuyer
            #    self.action = "q"
             #   print("gauche")
            if event.type == pygame.QUIT:
                #quitte le jeu
                self.play = False
                print("Aurevoir")
    def calc(self):
    # Calcule les positions et les colisions


        #Commande pour faire varier la vitesse
        if self.action == "z" :
            self.vitesse[1]-= self.proportion
        elif self.action == "s" :
            self.vitesse[1]+= self.proportion
        elif self.action == "d" :
            self.vitesse[0]+= self.proportion
        elif self.action == "q" :
            self.vitesse[0]-= self.proportion

        #Prise en compte de la gravité s'il on ne touche pas le sol
        if self.vaisseauposition[1] < 559 :
            self.vitesse[1] += self.gravite
        #Influence de la vitesse sur le changement de position
        self.vaisseauposition[0] += self.vitesse[0]
        self.vaisseauposition[1] += self.vitesse[1]


        #Cas des collisions avec les bords de la map
        #collisions cotés
        if self.vaisseauposition[0] > 800:
            self.vaisseauposition[0] = 0
        if self.vaisseauposition[0] < 0:
            self.vaisseauposition[0] = 800
        #collisions bas haut
        if self.vaisseauposition[1] > 560 :
            self.vaisseauposition[1]= 560
            self.vitesse[1] = -0.5*self.vitesse[1]
        if self.vaisseauposition[1] < 0 :
            self.vaisseauposition[1] = 0
            self.vitesse[1] = 0
        for k in range(self.nombrepoto):
            self.potos[k].calc()
             #Collision Vaisseau potos
            if abs(self.vaisseauposition[0]-self.potos[k].x) < 10 and self.potos[k].etat :
                if self.potos[k].y > self.vaisseauposition[1] : #Si on est en dessous du poto
                    self.score += 1
                else :
                    self.score = 0
                print(self.score)
                self.potos[k].etat = False
        #Collision Vaisseau potos




    def write(self):
        #Affiche à l'écran les différents objets ayant changer de positions
        self.window.blit(self.fond, (0,0))
        self.window.blit(self.vaisseautexture, (self.vaisseauposition[0], self.vaisseauposition[1]))
        for k in range(self.nombrepoto):
            self.window.blit(self.potos[k].texture, (self.potos[k].x, self.potos[k].y))



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
