import random

class Poto() :
    def __init__(self):
        self.taille = random.randint(150,600)
        self.pos = 800

    def calc(self):
        self.pos -= 1
