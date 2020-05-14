import random
import pygame

class Poto() :
    def __init__(self):
        self.y = random.randint(150,600) #Hauteur aleatoire du poto
        self.x = 800    #Définition de la coordonné x (le 800 n'est pas contraignant)
        self.etat = True #poto pas dépassé --> True , sinon False
        self.texture = pygame.image.load("textures/tuyeau.png").convert_alpha()
        self.texture = pygame.transform.scale(self.texture, (30,600))
    def calc(self):
        self.x -= 0.2 #Les potos reculent constamment
        if self.x < 0: #Reinitialisation du poto lorsqu'il passe à gauche de l'écran
            self.y = random.randint(150,600)
            self.x = 800
            self.etat = True #Le poto redevient valide
