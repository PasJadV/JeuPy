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
<<<<<<< Updated upstream
=======

tab_tirenn=[]
img_tirenn= pygame.image.load("tirenn.png").convert_alpha()
>>>>>>> Stashed changes
tab_ast=[]
imgastro = pygame.image.load("astro.png").convert_alpha()
tab_enn=[]
imgenn = pygame.image.load("ship.png").convert_alpha()


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
	tab_tirenn=[]
	recttirenn = img_tirenn.get_rect()




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
	ten=0
	l=imgenn.get_rect()

	while continuer:
		framerate.tick(30)
		#print(temps)
		tab_enn2 = []
		tab_ast2=[]
		temps+=1
		#vague d'astéroide
		if temps%10 ==0 and temps < 200:
			rectast = imgastro.get_rect()
			rectast.x = randrange(0,largeur-rectast.w)
			rectast.y = 0
			tab_ast.append(rectast)
		#vague ennemis
<<<<<<< Updated upstream
		if temps%50 ==0 and temps > 250:
=======
		if temps%30 ==0 and temps > 200:
>>>>>>> Stashed changes
			rectenn = imgenn.get_rect()
			rectenn.x = randrange(0,largeur-rectenn.w)
			rectenn.y = 0
			tab_enn.append(rectenn)
		#tir ennemis
<<<<<<< Updated upstream
		#if temps%30 ==0 and temps > 200:
=======
		if temps%30 ==0 and temps > 200:
			recttirenn = img_tirenn.get_rect()
			recttirenn.x=rectenn.x+33
			recttirenn.y=rectenn.h/2
			tab_tirenn.append(recttirenn)

		for tirenn in tab_tirenn:
			tirenn.y+=6

>>>>>>> Stashed changes
		for enn in tab_enn:
			#time = 0
			#time +=1
			#enn.x =  math.cos (math.pi / 24 * time) + rectenn.x
<<<<<<< Updated upstream
			#enn.y +=20*math.sin(2*angle)
			enn.y +=1
=======
			#enn.x=100*math.cos(angle)+largeur/2
			#enn.y=50*math.sin(angle)+largeur/2
			enn.y+=3
			#if rectenn.x>0:
>>>>>>> Stashed changes

		for enn in tab_enn:
			if enn.y < hauteur:
				tab_enn2.append(enn)

		tab_enn=tab_enn2

		for enn in tab_enn:
			for tir in tab_tir:
				if enn.colliderect(tir):
					enn.y = hauteur
					tir.y = hauteur


		for ast in tab_ast:
			ast.y += 5


		for r in tab_ast:
			if r.y < hauteur:
				tab_ast2.append(r)

		tab_ast = tab_ast2


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
		scoretext = score_font.render(("score: "+ str(score)), True, (255, 255, 255))

		for tir in tab_tir:
			tir.y -= vitesse

		tab_tir2 = []
		for r in tab_tir:
			if r.y > 0:
				tab_tir2.append(r)
		tab_tir=tab_tir2
		#print("nb_tir=", str(len(tab_ast)))



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
		#for t in tab_enn:
		#	if t.colliderect(rectv) :
		#		continuer = 0
		#		gameover()

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
		for tiree in tab_tirenn:
			fenetre.blit(img_tirenn, tiree)
		pygame.display.flip()

#----------------------------execution du programme----------------
corps()
pygame.quit()
