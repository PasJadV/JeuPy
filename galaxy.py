import sys, pygame
from pygame.locals import *

pygame.init()

largeur = 640
hauteur = 640
fenetre = pygame.display.set_mode((largeur, hauteur))

imageFond = pygame.image.load("galaxy.jpg").convert()
imgvaisseau= pygame.image.load("faucon.png").convert_alpha()
imgprojectil= pygame.image.load("balle.gif").convert_alpha()

rectFond = imageFond.get_rect()
rectFond.x = -320
rectFond.y = 0

rectv = imgvaisseau.get_rect()
rectv.x = 295
rectv.y = 555

rectprojectil= imgprojectil.get_rect()
rectprojectil.x= rectv.x+(rectv.w/2)-(rectprojectil.w/2)
rectprojectil.y= rectv.y-20

framerate= pygame.time.Clock()
continuer=1

while continuer:
    framerate.tick(30)
    touched = pygame.key.get_pressed()
    if touched [pygame.K_LEFT] and rectv.x>0:
        rectv.x-=10
        rectprojectil.x= rectv.x+(rectv.w/2)-(rectprojectil.w/2)
    if touched [pygame.K_RIGHT] and rectv.x<590:
        rectv.x+=10
        rectprojectil.x= rectv.x+(rectv.w/2)-(rectprojectil.w/2)
    if touched [pygame.K_UP] and rectv.y>hauteur/2:
        rectv.y-=10
        rectprojectil.y= rectv.y-20
    if touched [pygame.K_DOWN] and rectv.y<575:
        rectv.y+=10
        rectprojectil.y= rectv.y-20

    fenetre.blit(imageFond, rectFond)
    fenetre.blit(imgvaisseau, rectv)

    if touched [pygame.K_SPACE]:
        fenetre.blit(imgprojectil, rectprojectil)

    if touched [pygame.K_ESCAPE] :
       		 	continuer=0
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer=0
    pygame.display.flip()

pygame.quit()
