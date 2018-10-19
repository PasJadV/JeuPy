import sys, pygame
from pygame.locals import *


pygame.init()

largeur = 800
hauteur = 600
fenetre = pygame.display.set_mode((largeur, hauteur))

# un commentaire utile

imagePerso = pygame.image.load("perso2.png").convert_alpha()

imageFond = pygame.image.load("Fond2.jpg").convert()
imageFond2 = pygame.image.load("pacman.jpg").convert()
imageFond3 = pygame.image.load("fond.jpg").convert()
imageFond4 = pygame.image.load("mario.jpg").convert()

imageballe = pygame.image.load("balle2.png").convert_alpha()
imageballeS= pygame.image.load("balle3.png").convert_alpha()

font = pygame.font.Font(None, 34)
imageText = font.render("<Escape> pour quitter", True, (255, 255, 255))

font2 = pygame.font.Font(None, 20)
imageText2 = font2.render("<Space> pour mettre en pause", True, (255, 255, 255))

score_font = pygame.font.Font(None, 22)


framerate = pygame.time.Clock()

def meilleurScore():
	bestscore_font = pygame.font.Font(None, 22)
	Bestscore = bestscore_font.render(("Meilleur score: "+ str(bestscore)), True, (255, 255, 255))
	fenetre.blit(Bestscore, (380,10))

def Pauser2():
	font4 = pygame.font.Font(None, 42)
	pauser2 = font4.render("Jeu en Pause", True, (0, 0, 0))
	rect_pauser2 = pauser2.get_rect()
	rect_pauser2.x = 200
	rect_pauser2.y = 200
	fenetre.blit(pauser2, rect_pauser2)


def Pauser() :
	print("Pascale")

	i=1

	print(i)
	font3 = pygame.font.Font(None, 32)
	pauser = font3.render("Appuyez sur <Espace> pour continuer", True, (0, 0, 0))
	rect_pauser = pauser.get_rect()
	rect_pauser.x = 120
	rect_pauser.y = 250
	fenetre.blit(pauser, rect_pauser)

def joue() :
	font2=pygame.font.Font(None, 42)
	joue = font2.render(("GAMEOVER"), True, (0,0,0))
	rect_joue=joue.get_rect()
	rect_joue.x =200
	rect_joue.y= 150
	fenetre.blit(joue, rect_joue)

def playagain() :
	font1=pygame.font.Font(None, 30)
	playagain = font1.render(("Press <Enter> to play again"), True, (0,0,0))
	rect_playagain = playagain.get_rect()
	rect_playagain.x = 180
	rect_playagain.y = 200
	fenetre.blit(playagain, rect_playagain)

def gameover() :
	joue()
	playagain()
	pygame.display.flip()
	while playagain_or_quit()== None:
		framerate.tick()
	corps()

def playagain_or_quit() :

	toucher = pygame.key.get_pressed()
	if toucher [K_RETURN]:
		return corps()
	if toucher [K_ESCAPE]:
		quit()

	for event in pygame.event.get() :
		if event.type == QUIT and event.key == [K_ESCAPE] :
			pygame.quit()
			quit()

		if event.type == [K_RETURN]:
			return corps()
		else:
			return None



def corps() :

	rectText = imageText.get_rect()
	rectText.x = 10
	rectText.y = 10

	rectText2 = imageText2.get_rect()
	rectText2.x = 10
	rectText2.y = 40

	rectPerso = imagePerso.get_rect()
	rectPerso.x = 60
	rectPerso.y = 60

	mesBalles=[]
	deltax =  []
	deltay =  []

	## Balle qui change le fond
	rectballes = imageballeS.get_rect()
	rectballes.x = 250
	rectballes.y = 300

	## Toutes les autres balles
	rectballe = imageballe.get_rect()
	rectballe.x = 50
	rectballe.y = 300

	mesBalles.append(rectballe)
	deltax.append(5)
	deltay.append(2)


	rectFond = imageFond.get_rect()
	rectFond2 = imageFond2.get_rect()
	rectFond3 = imageFond3.get_rect()
	rectFond4 = imageFond4.get_rect()
	i=0

	pasPerso=2
	pasx=5
	pasy=1

	continuer=1
	score=0
	test=0
	bestscore=0

	ajout = False

	while continuer:

		framerate.tick(30)
		i=i+1

		if score%5 == 0 :
			if ajout :

				rectballe = imageballe.get_rect()
				rectballe.x = 250
				rectballe.y = 300
				mesBalles.append(rectballe)
				deltax.append(4)
				deltay.append(-3)
				ajout = False

		if score%5 == 1 :
			ajout = True

		## Deplacement des balles


		for i in range(len(mesBalles)) :
			mesBalles[i].x = mesBalles[i].x + deltax[i]
			mesBalles[i].y = mesBalles[i].y + deltay[i]

			if mesBalles[i].x>=(largeur-mesBalles[i].w) or mesBalles[i].x<0:
				deltax[i] = - deltax[i]
				score+=1

			if mesBalles[i].y>=(hauteur-mesBalles[i].h) or mesBalles[i].y<0:
				deltay[i] = - deltay[i]
				score+=1

		rectballes.y =rectballes.y + pasy
		rectballes.x =rectballes.x + pasx

		if rectballes.x>=(largeur-rectballes.w) :
			pasx = - pasx
			score+=1
			test=0

		if rectballes.x<0:
			pasx = - pasx
			score+=1
			test=1

		if rectballes.y<0 :
			pasy = - pasy
			score+=1
			test=2

		if rectballes.y > (hauteur-rectballes.h):
			pasy = - pasy
			score+=1
			test=3

		scoretext = score_font.render(("score: "+ str(score)), True, (255, 255, 255))



		for event in pygame.event.get() :
			if event.type == QUIT :
				sys.exit
				quit()
			if event.type == KEYUP :
			   if event.key == K_SPACE :
			   	pause=True

				while pause:
					framerate.tick()
					for event in pygame.event.get() :
						if event.type == QUIT :
							quit()

						if event.type == KEYUP :

						   if event.key == K_SPACE :
							pause = False
						   if event.key == K_ESCAPE :
						   	quit()
					Pauser2()
					Pauser()
					pygame.display.flip()



		touches = pygame.key.get_pressed()

		if touches [K_ESCAPE] :
			continuer=0

		if touches [K_DOWN] :
			rectPerso.y = rectPerso.y + pasPerso

		if touches [K_UP] :
			rectPerso.y = rectPerso.y - pasPerso

		if touches [K_LEFT] :
			rectPerso.x = rectPerso.x - pasPerso

		if touches [K_RIGHT] :
			rectPerso.x = rectPerso.x + pasPerso

		if rectPerso.x<0 :
			rectPerso.x = rectPerso.x - rectPerso.x

		if rectPerso.x > largeur - (rectPerso.w) :
			rectPerso.x = largeur - (rectPerso.w)

		if rectPerso.y<0 :
			rectPerso.y = rectPerso.y - rectPerso.y

		if rectPerso.y > hauteur - (rectPerso.h) :
			rectPerso.y = hauteur - (rectPerso.h)

		if pygame.Rect.colliderect(rectballes, rectPerso) :
			continuer = 0
			gameover()

		for b in mesBalles :
			if pygame.Rect.colliderect(b, rectPerso) :
				continuer = 0
				gameover()

		if test==1:
			fenetre.blit(imageFond2, rectFond2)

		elif test==2:
			fenetre.blit(imageFond3, rectFond3)

		elif test==3:
			fenetre.blit(imageFond4, rectFond4)
		else:
			fenetre.blit(imageFond, rectFond)

		fenetre.blit(imagePerso, rectPerso)

		fenetre.blit(imageText, rectText)

		fenetre.blit(imageText2, rectText2)

		fenetre.blit(imageballeS, rectballes)

		for b in mesBalles :
			fenetre.blit(imageballe, b)



		fenetre.blit(scoretext, (520,10))



		pygame.display.flip()


	meilleurScore()


	touched = pygame.key.get_pressed()
	if touched [K_ESCAPE] :
		continuer=0
	for event in pygame.event.get():
		if event.type == [K_RETURN]:
			return corps()

		if event.type == QUIT:
			continuer=0

	pygame.display.flip()

corps()
pygame.quit()
