from playsound import playsound
import pygame 
from pygame.locals import *

pygame.init()

largeur = 800
hauteur = 600
fenetre = pygame.display.set_mode((largeur, hauteur))

imageFond = pygame.image.load("Fond2.jpg").convert()
rectFond = imageFond.get_rect()

playsound('/Users/Pascale/Desktop/A_rendre/Jeu_python_VALLOT/son.mp3')

fenetre.blit(imageFond, rectFond)
