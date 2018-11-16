import sys, pygame, math
from random import randrange
from pygame.locals import *

#----------------------definition des options--------------------
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
imgprojectil= pygame.image.load("Projectile.png").convert_alpha()

tab_ast=[]
imgastro = pygame.image.load("astro.png").convert_alpha()
tab_enn=[]
imgenn = pygame.image.load("enn.png").convert_alpha()

font = pygame.font.Font(None, 20)
imageText = font.render("<Escape> pour quitter", True, (255, 255, 255))
rectText = imageText.get_rect()
rectText.x = 10
rectText.y = 10
font2 = pygame.font.Font(None, 20)
imageText2 = font2.render("<Entrer> pour mettre en pause", True, (255, 255, 255))
rectText2 = imageText2.get_rect()
rectText2.x = 10
rectText2.y = 30
font3 = pygame.font.Font(None, 20)
imageText3 = font3.render("<Space> pour envoyer des projectiles", True, (255, 255, 255))
rectText3 = imageText2.get_rect()
rectText3.x = 10
rectText3.y = 50
score_font = pygame.font.Font(None, 22)


framerate= pygame.time.Clock()

def Pauser2():
	font4 = pygame.font.Font(None, 42)
	pauser2 = font4.render("Jeu en Pause", True, (0, 0, 0))
	rect_pauser2 = pauser2.get_rect()
	rect_pauser2.x = 200
	rect_pauser2.y = 200
	fenetre.blit(pauser2, rect_pauser2)

def Pauser() :
	font3 = pygame.font.Font(None, 32)
	pauser = font3.render("Appuyez sur <Entrer> pour continuer", True, (0, 0, 0))
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
	playagain = font1.render(("Appuyer sur R pour rejouer"), True, (255,255,255))
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
	if toucher [K_r]:
		return corps()
	if toucher [K_ESCAPE]:
		quit()

	for event in pygame.event.get() :
		if event.type == QUIT and event.key == [K_ESCAPE] :
			pygame.quit()
			quit()

#--------------------------Corps du jeu--------------------------
def corps():

	rectFond = imageFond.get_rect()
	rectFond.x = -320
	rectFond.y = 0


	tab_ast = []
	rectast = imgastro.get_rect()
	tab_enn = []
	rectenn = imgenn.get_rect()

	rectv = imgvaisseau.get_rect()
	rectv.x = largeur/2 - rectv.w
	rectv.y = hauteur - hauteur/4
	tab_tir=[]
	tab_tir2=[]
	rectprojectil= imgprojectil.get_rect()
	vitesse = 7
	framerate= pygame.time.Clock()

	continuer=1
	angle=0
	temps=0
	score=0

	while continuer:
		framerate.tick(30)
		print(temps)

		temps+=1
		#vague d'astéroide
		if temps%5 ==0 and temps < 200:
			rectast = imgastro.get_rect()
			rectast.x = randrange(0,largeur-rectast.w)
			rectast.y = 0
			tab_ast.append(rectast)

		if temps%5 ==0 and temps > 250:
			rectenn = imgenn.get_rect()
			rectenn.x = randrange(0,largeur-rectenn.w)
		#	rectenn.x = largeur/2
			rectenn.y = hauteur/4
			tab_enn.append(rectenn)

		for enn in tab_enn:
			time = 0
			time +=1
			enn.x =  math.cos (math.pi / 24 * time) + rectenn.x
			enn.y = temps
			#if rectenn.x>0:

			#if rectenn.x<largeur-rectenn.w:

			#if rectenn.y>0:

			#if enn.y>hauteur/2:
			#	enn.y -=

		for ast in tab_ast:
			ast.y += 5

		nettoyage=[]
		for r in tab_ast:
			if rectast.y < hauteur:
				nettoyage.append(r)
		tab_ast=nettoyage


		touched = pygame.key.get_pressed()
		if touched [pygame.K_LEFT] and rectv.x>0:
			rectv.x-=10
		if touched [pygame.K_RIGHT] and rectv.x<largeur-rectv.w:
			rectv.x+=10
		if touched [pygame.K_UP] and rectv.y>hauteur/2:
			rectv.y-=10
		if touched [pygame.K_DOWN] and rectv.y<hauteur-rectv.h:
			rectv.y+=10
		if touched [pygame.K_ESCAPE] :
			continuer=0

		if touched [pygame.K_SPACE]:
			rectprojectil= imgprojectil.get_rect()
			rectprojectil.x= rectv.x+(rectv.w/2)-(rectprojectil.w/2)
			rectprojectil.y= rectv.y-2
			tab_tir.append(rectprojectil)
		#for a in tab_tir:
		#	if a.x>=0 and a.x<=(largeur-rectprojectil.w) and a.y>=0 and a.y<=(hauteur-rectprojectil.h):
		#		tab_tir2.append(a)
		#tab_tir=[]
		#tab_tir=tab_tir2

		for tir in tab_tir:
			tir.y -= vitesse

		nettoyage=[]
		for r in tab_tir:
			if rectprojectil.y > 0:
				nettoyage.append(r)
		tab_tir=nettoyage

		scoretext = score_font.render(("score: "+ str(score)), True, (255, 255, 255))

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

		if pygame.Rect.colliderect(rectv, rectenn) :
			continuer = 0
			gameover()
		if pygame.Rect.colliderect(rectprojectil, rectenn) :
		 	score +=1

		fenetre.blit(imageFond, rectFond)
		fenetre.blit(imgvaisseau, rectv)
		fenetre.blit(imageText, rectText)
		fenetre.blit(imageText2, rectText2)
		fenetre.blit(imageText3, rectText3)
		fenetre.blit(scoretext, (520,10)) 

		for ast in tab_ast:
			fenetre.blit(imgastro, ast)
		for enn in tab_enn:
			fenetre.blit(imgenn, enn)
		for t in tab_tir:
			fenetre.blit(imgprojectil, t)

		pygame.display.flip()

#----------------------------execution du programme----------------
corps()
pygame.quit()
