import random
import pygame

class Poto() :
    def __init__(self):
        self.y = random.randint(150,600)
        self.x = 800
        self.texture = pygame.image.load("textures/tuyeau.png").convert_alpha()
        self.texture = pygame.transform.scale(self.texture, (30,600))
    def calc(self):
        self.x -= 0.2
        if self.x < 0:
            self.y = random.randint(150,600)
            self.x = 800
