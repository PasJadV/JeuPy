#-*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import pygame.image
import time
def titre() :
    ## Initialisation de la fenetre et crÃ©ation
    pygame.init()

    #Personnalisation du jeu
    icone = pygame.image.load("17.png")
    pygame.display.set_icon(icone)
    pygame.display.set_caption("PHANTOM Defense")

    #Initialisation de la musique
    pygame.mixer.music.load("mus/titre2.wav")
    #Lecture de la musique
    pygame.mixer.music.play()

    #creation de la fenetre

    largeur = 640
    hauteur = 480
    fenetre=pygame.display.set_mode((largeur,hauteur))

    ## Lecture des differentes images.
    # lecture de l'image du fond
    imageFond = pygame.image.load("title/titre3.png").convert()
    rectFond = imageFond.get_rect()

    play = pygame.image.load("title/jouer2.png").convert_alpha()
    rectplay = play.get_rect()
    rectplay.x = 450
    rectplay.y = 280

    quitt = pygame.image.load("title/quit2.png").convert_alpha()
    rectquit = quitt.get_rect()
    rectquit.x = 450
    rectquit.y = 320


    # servira a regler l'horloge du jeu
    framerate = pygame.time.Clock()
    continuer=1
    jeu=0
    while continuer == 1 or jeu == 0 :

        # fixons le nombre max de frames / secondes
        framerate.tick(20)

        

    

        # Affichage du fond
        fenetre.blit(imageFond, rectFond)
        fenetre.blit(play, rectplay)
        fenetre.blit(quitt, rectquit)


        # On vide la pile d'evenements et on verifie certains evenements
        for event in pygame.event.get():   # parcours de la liste des evenements recus
            if event.type == QUIT:     #Si un de ces evenements est de type QUIT
                continuer = 0	   # On arrete la boucle


        if event.type == MOUSEMOTION and (event.pos[0] >= rectplay.x and event.pos[0] <= 570 and event.pos[1] >=rectplay.y and event.pos[1] <=310) :
            play = pygame.image.load("title/jouer1.png").convert_alpha()
        else:
            play = pygame.image.load("title/jouer2.png").convert_alpha()

        if event.type == MOUSEMOTION and (event.pos[0] >= rectquit.x and event.pos[0] <= 570 and event.pos[1] >=rectquit.y and event.pos[1] <=340) :
            quitt = pygame.image.load("title/quit1.png").convert_alpha()
        else:
            quitt = pygame.image.load("title/quit2.png").convert_alpha()        
    
        if event.type == MOUSEBUTTONDOWN and (event.pos[0] >= rectplay.x and event.pos[0] <= 570 and event.pos[1] >=rectplay.y and event.pos[1] <=310) :
            jeu = 1

        if event.type == MOUSEBUTTONDOWN and (event.pos[0] >= rectquit.x and event.pos[0] <= 570 and event.pos[1] >=rectquit.y and event.pos[1] <=340) :
            continuer = 0

        # raffraichissement
        pygame.display.flip()

        if continuer == 0 :
            # fin du programme principal...
            pygame.quit()
        if jeu == 1 :
            return jeu ;

def gameover() :
    ## Initialisation de la fenetre et crÃ©ation
    pygame.init()

    #Personnalisation du jeu
    icone = pygame.image.load("17.png")
    pygame.display.set_icon(icone)
    pygame.display.set_caption("PHANTOM Defense")

    #Initialisation de la musique
    pygame.mixer.music.load("GAME OVER/lose.mp3")
    

    #creation de la fenetre

    largeur = 640
    hauteur = 480
    fenetre=pygame.display.set_mode((largeur,hauteur))

    ## Lecture des differentes images.
    # lecture de l'image du fond


    fin= pygame.image.load("GAME OVER/fond2.png").convert()
    rectfin = fin.get_rect()

    over = {}
    over[1]=pygame.image.load("GAME OVER/1.png").convert()
    over[2]=pygame.image.load("GAME OVER/2.png").convert()
    over[3]=pygame.image.load("GAME OVER/3.png").convert()
    over[4]=pygame.image.load("GAME OVER/4.png").convert()
    over[5]=pygame.image.load("GAME OVER/5.png").convert()
    over[6]=pygame.image.load("GAME OVER/6.png").convert()
    over[7]=pygame.image.load("GAME OVER/7.png").convert()
    over[8]=pygame.image.load("GAME OVER/8.png").convert()
    over[9]=pygame.image.load("GAME OVER/11.png").convert()
    over[10]=pygame.image.load("GAME OVER/11.png").convert()
    over[11]=pygame.image.load("GAME OVER/11.png").convert()
    over[12]=pygame.image.load("GAME OVER/10.png").convert()
    over[13]=pygame.image.load("GAME OVER/11.png").convert()
    over[14]=pygame.image.load("GAME OVER/10.png").convert()
    over[15]=pygame.image.load("GAME OVER/11.png").convert()
    over[16]=pygame.image.load("GAME OVER/10.png").convert()
    over[17]=pygame.image.load("GAME OVER/11.png").convert()
    over[18]=pygame.image.load("GAME OVER/10.png").convert()
    over[19]=pygame.image.load("GAME OVER/11.png").convert()
    over[20]=pygame.image.load("GAME OVER/10.png").convert()
    over[21]=pygame.image.load("GAME OVER/11.png").convert()
    over[22]=pygame.image.load("GAME OVER/10.png").convert()
    over[23]=pygame.image.load("GAME OVER/11.png").convert()
    over[24]=pygame.image.load("GAME OVER/10.png").convert()
    over[25]=pygame.image.load("GAME OVER/11.png").convert()
    i=1

    tru = {}
    tru[1]=pygame.image.load("GAME OVER/12.png").convert()
    tru[2]=pygame.image.load("GAME OVER/12.png").convert()
    tru[3]=pygame.image.load("GAME OVER/12.png").convert()
    tru[4]=pygame.image.load("GAME OVER/13.png").convert()
    tru[5]=pygame.image.load("GAME OVER/13.png").convert()
    j=1
    

    # servira a regler l'horloge du jeu
    framerate = pygame.time.Clock()
    tmp = time.time()
    continuer=1
    again=0
    game=0

    #Lecture de la musique
    pygame.mixer.music.play()
    
    while continuer == 1 :
        tmp2 = time.time()

        # fixons le nombre max de frames / secondes
        framerate.tick(20)

        if (tmp2-tmp)>0 and (tmp2-tmp)<3 :
            fenetre.blit(fin,rectfin)
            
        if (tmp2-tmp)>=3 :
            again=1

        if again==1 :
            fenetre.blit(over[i],(0,0))
            if i<25 :
                i += 1
                
        if i==25 :
            fenetre.blit(tru[j],(210,400))
            j += 1
            if j>5 :
                j=1

        # On vide la pile d'evenements et on verifie certains evenements
        for event in pygame.event.get():   # parcours de la liste des evenements recus
            if event.type == QUIT:     #Si un de ces evenements est de type QUIT
                continuer = 0	   # On arrete la boucle
            if event.type == MOUSEBUTTONDOWN  :
                game = 1

        
        # raffraichissement
        pygame.display.flip()

        if continuer == 0 :
            # fin du programme principal...
            pygame.quit()
        if game == 1 :
            return game ;



