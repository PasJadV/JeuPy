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
fenetre = pygame.display.set_mode((largeur, hauteur), RESIZABLE)
#---------------------------Medias divers------------------------
imageFond = pygame.image.load("galaxy.jpg").convert()
#imageFond2 = pygame.image.load("galaxy.jpg").convert()
imgameov = pygame.image.load("Game.jpg").convert()
imgvaisseau= pygame.image.load("faucon.png").convert_alpha()
imgprojectil= pygame.image.load("Projectile.png").convert_alpha()
imgaccueil= pygame.image.load("accueil.jpg").convert_alpha()


tab_tirenn=[]
img_tirenn= pygame.image.load("tirenn.png").convert_alpha()
tab_ast=[]
imgastro = pygame.image.load("astro.png").convert_alpha()
tab_enn=[]
imgenn = pygame.image.load("Spaceship_tut.png").convert_alpha()
son = pygame.mixer.Sound("space walk.ogg")
songameover=pygame.mixer.Sound("game-over-2.wav")
sontir=pygame.mixer.Sound("iceball.wav")

imagevie1 = pygame.image.load("coeur1.png").convert_alpha()
imagevie2 = pygame.image.load("coeur2.png").convert_alpha()
imagevie3 = pygame.image.load("coeur3.png").convert_alpha()
imagevie4 = pygame.image.load("coeur4.png").convert_alpha()
vrect = imagevie4.get_rect()
vrect.x = 400
vrect.y = 10

coin = []
imagecoin = pygame.image.load("coin1.png").convert_alpha()
star = []
imgstar = pygame.image.load("sss.png").convert_alpha()


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
#lol=continuer

def Pauser2():
    font4 = pygame.font.Font(None, 42)
    pauser2 = font4.render("Jeu en Pause", True, (0, 0, 0))
    rect_pauser2 = pauser2.get_rect()
    rect_pauser2.x = 200
    rect_pauser2.y = 200
    fenetre.blit(pauser2, rect_pauser2)
    pygame.mixer.pause()


def Pauser() :
    font3 = pygame.font.Font(None, 32)
    pauser = font3.render("Appuyez sur <Entrer> pour continuer", True, (0, 0, 0))
    rect_pauser = pauser.get_rect()
    rect_pauser.x = 120
    rect_pauser.y = 250
    fenetre.blit(pauser, rect_pauser)


def joue() :
    font2=pygame.font.Font('police/plasdrpe.ttf', 70)
    joue = font2.render(("GAMEOVER"), True, (255,255,255))
    fenetre.fill((0,0,0))
    rect_joue=joue.get_rect()
    rect_joue.x =150
    rect_joue.y= 150
    fenetre.blit(joue, rect_joue)
    son.stop()
    songameover.play()



def playagain() :
    font1=pygame.font.Font('police/plasdrpe.ttf', 30)
    playagain = font1.render(("Appuyer sur R pour rejouer"), True, (255,255,255))
    play2 = font1.render((" ou escape pour quitter"), True, (255,255,255))
    rect_playagain = playagain.get_rect()
    rect_playagain.x = largeur/6
    rect_playagain.y = hauteur/2
    rectplay2 = playagain.get_rect()
    rectplay2.x = largeur/8+largeur/10
    rectplay2.y = hauteur/2+hauteur/8
    fenetre.blit(playagain, rect_playagain)
    fenetre.blit(play2, rectplay2)



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

    #rectFond2 = imageFond2.get_rect()
    #rectFond2.x = -320
    #rectFond2.y = -hauteur

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

    coin = []
    rectcoin = imagecoin.get_rect()
    star = []
    rectstar = imgstar.get_rect()


    angle=0
    temps=0
    score=0
    ten=0
    vie=4
    dernier_tir=0
    joueson=0
    vitessevaisseau=10
    continuer=0

    while continuer==0:
        rectacc = imgaccueil.get_rect()
        rectacc.x = -650
        rectacc.y = -300
        font4 = pygame.font.Font(None, 52)
        menu = font4.render("<Space> pour commencer le jeu", True, (0, 0, 0))
        rectmenu = menu.get_rect()
        rectmenu.x = 10
        rectmenu.y = 50

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_SPACE:
                         continuer=1
        fenetre.blit(imgaccueil, rectacc)
        fenetre.blit(menu, rectmenu)
        for event in pygame.event.get() :
                if event.type == QUIT:
                    sys.exit
                    quit()
        touche = pygame.key.get_pressed()
        if touche [pygame.K_ESCAPE] :
            quit()
        pygame.display.flip()
    while continuer==1:
        framerate.tick(30)
        print(vie)
        son.play()
        songameover.stop()

        #vitesse fond
        #rectFond.y += 3
        #rectFond2.y += 3

        #Déplacement fond
        #if rectFond.y >= hauteur:
        #    rectFond.y = -hauteur
        #if rectFond2.y >= hauteur:
        #    rectFond2.y = -hauteur

        if joueson==0:
            pygame.mixer.unpause()

        #print(temps)
        tab_enn2 = []
        tab_ast2 = []
        coin_net = []
        tab_tir2=[]

        temps+=1
        #vague d'astéroide
        if temps%5 ==0 and temps < 200:
            rectast = imgastro.get_rect()
            rectast.x = randrange(0,largeur-rectast.w)
            rectast.y = 0
            tab_ast.append(rectast)
        #vague ennemis
        if temps%25 ==0 and temps > 200:
            rectenn = imgenn.get_rect()
            rectenn.x = randrange(0,largeur-rectenn.w)
            rectenn.y = 0
            tab_enn.append(rectenn)

        #bonus vie
        if temps%100==0 and temps>300 and vie!=4:
            rectcoin = imagecoin.get_rect()
            rectcoin.x = randrange(0,largeur-rectcoin.w)
            rectcoin.y = randrange(hauteur/2, hauteur-rectcoin.h)
            coin.append(rectcoin)
        #bonus vitesse
        if temps%400==0 and  temps>350:
            rectstar= imgstar.get_rect()
            rectstar.x = randrange(0,largeur-rectcoin.w)
            rectstar.y= 0
            star.append(rectstar)
        #essai pour un niveau 2
        #if score>3:
            #if temps%2 ==0 and temps > 200:
                #rectenn = imgenn.get_rect()
                #rectenn.x = randrange(0,largeur-rectenn.w)
                #rectenn.y = 0
                #tab_enn.append(rectenn)

        #tir ennemis
        if temps%20 == 0 and temps > 250:
            recttirenn = img_tirenn.get_rect()
            recttirenn.centerx=rectenn.centerx
            recttirenn.y=rectenn.bottom
            tab_tirenn.append(recttirenn)

        #vitesse tirs vaisseau ennemi
        for tirenn in tab_tirenn:
            tirenn.y+=15

        #vitesse vaisseau ennemi
        for enn in tab_enn:
            enn.y +=6
            #time = 0
            #time +=1
            #enn.x =  math.cos (math.pi / 24 * time) + rectenn.x
            #enn.y +=20*math.sin(2*angle)

        for enn in tab_enn:
            if enn.y < hauteur:
                tab_enn2.append(enn)
        tab_enn=tab_enn2

        for enn in tab_enn:
            for tir in tab_tir:
                if enn.colliderect(tir):
                    enn.y = hauteur
                    tir.y = 0
                    score = score+1

        for ast in tab_ast:
            ast.y += 5
        for starr in star:
            starr.y+=5

        for r in tab_ast:
            if r.y < hauteur:
                tab_ast2.append(r)
        tab_ast = tab_ast2

        for c in coin:
            if c.y < hauteur-c.h:
                coin_net.append(c)
        coin = coin_net

        for r in tab_ast:
            for tir in tab_tir:
                if r.colliderect(tir):
                    r.y = hauteur
                    tir.y = 0
        for r in tab_ast:
            if r.colliderect(rectv):
                vie=vie-1
                r.y = hauteur

        #collision entre les tirs ennemis et le vaisseau
        for recttirenn in tab_tirenn:
            if recttirenn.colliderect(rectv):
                vie=vie-1
                vitessevaisseau=10
                recttirenn.y = hauteur


#collision entre vaisseau ennemis et le vaisseau
        for rectenn in tab_enn:
            if rectenn.colliderect(rectv):
                vie=vie-1
                rectenn.y = hauteur
                vitessevaisseau=10
#collision entre le vaisseau et la piece
        for c in coin:
            if rectv.colliderect(c):
                vie=vie+1
                c.y= hauteur
        #collision entre le vaisseau et l'etoile
        for v in star:
            if rectv.colliderect(v):
                vitessevaisseau=20
                v.y= hauteur


            for r in tab_tir:
                for tir in tab_tirenn:
                    if r.colliderect(tir):
                        tir.y = hauteur
                        r.y = 0

        touched = pygame.key.get_pressed()
        if touched [pygame.K_LEFT] and rectv.x>0:
            rectv.x-=vitessevaisseau
        if touched [pygame.K_RIGHT] and rectv.x<largeur-rectv.w:
            rectv.x+=vitessevaisseau
        if touched [pygame.K_UP] and rectv.y>hauteur/2:
            rectv.y-=vitessevaisseau
        if touched [pygame.K_DOWN] and rectv.y<hauteur-rectv.h:
            rectv.y+=vitessevaisseau
        if touched [pygame.K_ESCAPE] :
            continuer=0
        #tir ennemis
        if touched [pygame.K_SPACE] and pygame.time.get_ticks() - dernier_tir >= 200:

            dernier_tir=pygame.time.get_ticks()
            rectprojectil= imgprojectil.get_rect()
            rectprojectil.x= rectv.x+(rectv.w/2)-(rectprojectil.w/2)
            rectprojectil.y= rectv.y-2
            tab_tir.append(rectprojectil)

        #for a in tab_tir:
        #    if a.x>=0 and a.x<=(largeur-rectprojectil.w) and a.y>=0 and a.y<=(hauteur-rectprojectil.h):
        #        tab_tir2.append(a)
        #tab_tir=[]
        #tab_tir=tab_tir2
        for tir in tab_tir:
            tir.y -= vitesse

        for r in tab_tir:
            if r.y > 0 and r.y<hauteur:
                tab_tir2.append(r)
        tab_tir=tab_tir2
        #print("nb_tir=", str(len(tab_ast)))
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
        #for t in tab_enn:
        #    if t.colliderect(rectv) :
        #        continuer = 0
        #        gameover()

        fenetre.blit(imageFond, rectFond)
        #fenetre.blit(imageFond2, rectFond2)
        fenetre.blit(imgvaisseau, rectv)
        fenetre.blit(imageText, rectText)
        fenetre.blit(imageText2, rectText2)
        fenetre.blit(imageText3, rectText3)
        if vie == 1 :
            fenetre.blit(imagevie1,vrect)
        if vie == 2 :
            fenetre.blit(imagevie2,vrect)
        if vie == 3 :
            fenetre.blit(imagevie3,vrect)
        if vie == 4 :
            fenetre.blit(imagevie4,vrect)

        fenetre.blit(scoretext, (520,10))

        for ast in tab_ast:
            fenetre.blit(imgastro, ast)
        for enn in tab_enn:
            fenetre.blit(imgenn, enn)
        for t in tab_tir:
            fenetre.blit(imgprojectil, t)
        for tiree in tab_tirenn:
            fenetre.blit(img_tirenn, tiree)
        for c in coin:
            fenetre.blit(imagecoin, c)
        for ve in star:
            fenetre.blit(imgstar, ve)
        if pygame.Rect.colliderect(rectv, rectenn) :
            vie = vie - 1
        if vie==0 :
            print("vie =", vie)
            continuer = 0
            gameover()
        pygame.display.flip()

#----------------------------execution du programme----------------
corps()
pygame.quit()
