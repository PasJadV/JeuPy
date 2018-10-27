import sys, pygame
from pygame.locals import *

pygame.init()
icone = pygame.image.load("ico.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("Gwalaxy")
largeur = 640
hauteur = 640
fenetre = pygame.display.set_mode((largeur, hauteur))
#---------------------------Medias divers------------------------
imageFond = pygame.image.load("galaxy.jpg").convert()
imgvaisseau= pygame.image.load("faucon.png").convert_alpha()
imgprojectil= pygame.image.load("balle.gif").convert_alpha()
font = pygame.font.Font(None, 34)
imageText = font.render("<Escape> pour quitter", True, (255, 255, 255))

font2 = pygame.font.Font(None, 25)
imageText2 = font2.render("<Entrer> pour mettre en pause", True, (255, 255, 255))

font3 = pygame.font.Font(None, 20)
imageText3 = font3.render("<Space> pour envoyer des projectiles", True, (255, 255, 255))

#----------------------definition des options--------------------
def Pauser2():
	font4 = pygame.font.Font(None, 42)
	pauser2 = font4.render("Jeu en Pause", True, (0, 0, 0))
	rect_pauser2 = pauser2.get_rect()
	rect_pauser2.x = 200
	rect_pauser2.y = 200
	fenetre.blit(pauser2, rect_pauser2)


def Pauser() :
	font3 = pygame.font.Font(None, 32)
	pauser = font3.render("Appuyez sur <Espace> pour continuer", True, (0, 0, 0))
	rect_pauser = pauser.get_rect()
	rect_pauser.x = 120
	rect_pauser.y = 250
	fenetre.blit(pauser, rect_pauser)

#--------------------------Corps du jeu--------------------------
def corps():
    rectText = imageText.get_rect()
    rectText.x = 10
    rectText.y = 10

    rectText2 = imageText2.get_rect()
    rectText2.x = 10
    rectText2.y = 40

    rectText3 = imageText2.get_rect()
    rectText3.x = 10
    rectText3.y = 70

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

        for event in pygame.event.get() :
            if event.type == QUIT:
                sys.exit
                quit()
            if event.type == KEYUP :
                if event.key == K_RETURN :
                    pause=True
                    while pause:
                        framerate.tick()
                        for event in pygame.event.get() :
                            if event.type == QUIT :
                                quit()
                            if event.type == KEYUP :
                                if event.key == K_RETURN :
                                    pause = False
                                if event.key == K_ESCAPE :
                                    quit()
                        Pauser2()
                        Pauser()
                        pygame.display.flip()

        fenetre.blit(imageFond, rectFond)
        fenetre.blit(imgvaisseau, rectv)
        fenetre.blit(imageText, rectText)
        fenetre.blit(imageText2, rectText2)
        fenetre.blit(imageText3, rectText3)

        if touched [pygame.K_SPACE]:
            fenetre.blit(imgprojectil, rectprojectil)
        pygame.display.flip()

        touched = pygame.key.get_pressed()
        if touched [pygame.K_ESCAPE] :
           		 	continuer=0
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer=0
        pygame.display.flip()
#----------------------------execution du programme----------------
corps()
pygame.quit()
