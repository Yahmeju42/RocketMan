global name
name = "RocketMan"
import pygame #importe le module pygame
from game import *

pgwrk = pygame.init() #charges les modules de pygame (pgwrk est un tuple pour verifier si tout fonctionne)
print("pygamepgwrk = loaded", pgwrk[0], "eror", pgwrk[1], "\n")
if(pgwrk[1] != 0 and pgwrk != 6):
    print("ereur")
else:
    #lance le jeu
    print("lancement de", name)
    jeu = Game()
    jeu.loop()

print("fermeture de pygame")
pygame.quit()
