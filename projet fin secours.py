import pygame
from pygame.locals import *
from random import randint
import time


pygame.init()


pygame.mixer.init()
pygame.mixer.music.load("musiques/gj.mp3")
pygame.mixer.music.set_volume(0.15)
crivivefr = pygame.mixer.Sound("musiques/crivivefr.wav")
cst = pygame.mixer.Sound("musiques/cst.wav")
lec = pygame.mixer.Sound("musiques/lec.wav")
applaudissements = pygame.mixer.Sound("musiques/applaudissements.wav")
pygame.mixer.music.play(loops=-1)
joue = 1
s =0

sons = [crivivefr,cst,lec]

pers_case_x = 0
pers_case_y = 0
pers_x = 0
pers_y = 0
position = (pers_x,pers_y)

statut = 1

rouge = (250,50,50)
bleu = (50,50,250)
vert = (50,250,50)

screen = pygame.display.set_mode((1280,640), RESIZABLE)
screen.fill(bleu)

gj = pygame.image.load("images/Gilets Jaune.png").convert_alpha()


pygame.display.set_icon(pygame.image.load("images/Gilets Jaune.png"))
pygame.display.set_caption("A yellow vest have to escape !!")
pygame.display.flip()

loose = pygame.image.load("images/macron content.jpg")
win = pygame.image.load("images/gilet jaune content.jpg")

pygame.key.set_repeat(400, 30)


niveaux = ["niveau.txt","niveau 2.txt","niveau 3.txt","niveau 4.txt"]
lvl = 0

tele_x = []
tele_y = []


with open("niveau.txt", "r") as texte:
			agencement_lvl = []
			for ligne in texte:
				ligne_lvl = []
				for sprite in ligne:
					if sprite != '\n':
						ligne_lvl.append(sprite)
				agencement_lvl.append(ligne_lvl)
def afficheur(screen):
        
        mur = pygame.image.load("images/mur.png").convert()
        sol = pygame.image.load("images/pavés.jpg").convert()
        depart = pygame.image.load("images/depart.png").convert()
        arrivee = pygame.image.load("images/Arrivée.png").convert_alpha()
        passage = pygame.image.load("images/trappe.jpg").convert()
	
        num_ligne = 0
        for ligne in agencement_lvl:
                num_case = 0
                for sprite in ligne:
                        x = num_case * 64
                        y = num_ligne * 64
                        if sprite == '1':		   
                                screen.blit(mur, (x,y))
                        elif sprite == '3':		   
                                screen.blit(depart, (x,y))
                        elif sprite == '2':
                                screen.blit(sol, (x,y))
                                screen.blit(arrivee, (x,y))
                        elif sprite == '0':
                                screen.blit(sol,(x,y))
                        elif sprite == '4' :
                                screen.blit(mur,(x,y))
                        elif sprite == '5':
                                screen.blit(passage, (x,y))
                                tele_x.append(num_case)
                                tele_y.append(num_ligne)
                        elif sprite == '6':
                                screen.blit(depart, (x,y))
                                crs_gd_case[0] = num_case
                                crs_gd_case[1] = num_ligne
                                
                                crs_gd_x = crs_gd_case[0] * 64
                                crs_gd_y = crs_gd_case[1] * 64
                        elif sprite == '7':
                                screen.blit(depart, (x,y))
                                crs_hb_case[0] = num_case
                                crs_hb_case[1] = num_ligne
                                
                                crs_hb_x = crs_hb_case[0] * 64
                                crs_hb_y = crs_hb_case[1] * 64

                                
                               
                                
                        num_case += 1
                num_ligne += 1




continuer = True
menu = True
jeu = True
while continuer :
        
        accueil = pygame.image.load("images/accueil.jpg").convert()
        accueil_lvl1 = pygame.image.load("images/accueil_lvl1.jpg").convert()
        accueil_lvl2 = pygame.image.load("images/accueil_lvl2.jpg").convert()
        accueil_lvl3 = pygame.image.load("images/accueil_lvl3.jpg").convert()
        accueil_lvl4 = pygame.image.load("images/accueil_lvl4.jpg").convert()
        accueil_lvl5 = pygame.image.load("images/accueil_lvl5.jpg").convert()
        
        accueil1 = pygame.image.load("images/accueil1.jpg").convert()
        accueil1_lvl1 = pygame.image.load("images/accueil1_lvl1.jpg").convert()
        accueil1_lvl2 = pygame.image.load("images/accueil1_lvl2.jpg").convert()
        accueil1_lvl3 = pygame.image.load("images/accueil1_lvl3.jpg").convert()
        accueil1_lvl4 = pygame.image.load("images/accueil1_lvl4.jpg").convert()
        accueil1_lvl5 = pygame.image.load("images/accueil1_lvl5.jpg").convert()
        
        menus = [accueil, accueil_lvl1, accueil_lvl2, accueil_lvl3, accueil_lvl4, accueil_lvl5]
        menus1 = [accueil1,accueil1_lvl1,accueil1_lvl2,accueil1_lvl3,accueil1_lvl4, accueil1_lvl5]
        m = 0
        niv = 0
        screen.blit(accueil,(0,0))

        pygame.display.flip()

        menu = True
        jeu = True
        while menu :
                pygame.time.Clock().tick(30)
                
                
                
                for event in pygame.event.get() :
                        if event.type == MOUSEBUTTONDOWN:
                                if event.button == 1:

                                        
                                        if event.pos[1] > 490 and event.pos[1] < 560 :
                                                if event.pos[0] > 80 and event.pos[0] < 140 :
                                                        m = 1
                                                        niv = m
                                                        lvl = 0
                                                elif event.pos[0] > 186 and event.pos[0] < 245:
                                                        m = 2
                                                        niv = m
                                                        lvl = 1
                                                elif event.pos[0] > 295 and event.pos[0] < 355:
                                                        m = 3
                                                        niv = m
                                                        lvl = 2
                                                elif event.pos[0] > 404 and event.pos[0] < 460:
                                                        m = 4
                                                        niv = m
                                                        lvl = 3
                                                elif event.pos[0] > 505 and event.pos[0] < 567:
                                                        m = 5
                                                        niv = m
                                                        lvl = 4
                                                else :
                                                        m = 0
                                                        niv = m

                                                screen.blit(menus[m],(0,0))
                                                pygame.display.flip()

                                        if event.pos[0] > 700 and event.pos[0] < 1260 and event.pos[1] > 425 and event.pos[1] < 630:
                                                if event.button == 1:
                                                        menu = False
                                                        jeu = True
                                                        commencer = 1


                        if event.type == MOUSEMOTION :
                                if event.pos[0] > 700 and event.pos[0] < 1260 and event.pos[1] > 425 and event.pos[1] < 630:
                                        screen.blit(menus1[niv],(0,0))
                                        pygame.display.flip()
        
                                if event.pos[1] > 490 and event.pos[1] < 560 :
                                        if event.pos[0] > 80 and event.pos[0] < 140 :
                                                m = 1
                                                screen.blit(menus[m],(0,0))
                                                pygame.display.flip()
                                        elif event.pos[0] > 186 and event.pos[0] < 245:
                                                m = 2
                                                screen.blit(menus[m],(0,0))
                                                pygame.display.flip()
                                        elif event.pos[0] > 295 and event.pos[0] < 355:
                                                m = 3
                                                screen.blit(menus[m],(0,0))
                                                pygame.display.flip()
                                        elif event.pos[0] > 404 and event.pos[0] < 460:
                                                m = 4
                                                screen.blit(menus[m],(0,0))
                                                pygame.display.flip()
                                        elif event.pos[0] > 505 and event.pos[0] < 567:
                                                m = 5
                                                screen.blit(menus[m],(0,0))
                                                pygame.display.flip()
                                else :
                                        m = niv
                                        screen.blit(menus[m],(0,0))
                                        pygame.display.flip()
                        if event.type == QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                                continuer = False
                                menu = False
                                jeu = False
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                        menu = False
                                        jeu = True
                                        commencer = 1

                    
        while jeu :
                pygame.time.Clock().tick(30)
                if commencer == 1 :
                        temps = time.time()
                        with open(niveaux[lvl], "r") as texte:
                                agencement_lvl = []
                                for ligne in texte:
                                        ligne_lvl = []
                                        for sprite in ligne:
                                                if sprite != '\n':
                                                        ligne_lvl.append(sprite)
                                        agencement_lvl.append(ligne_lvl)
                        commencer = 0
                        
                for event in pygame.event.get() :
                        
                        if event.type == pygame.KEYDOWN:
                                
                                s = randint (0,2)
                                son = sons[s]
                                
                                if joue == 0:
                                        pygame.mixer.music.play()
                                        joue = 1

                                if statut == 0 :
                                        sons[s].fadeout(300)
                                        statut = 1
                                        pygame.mixer.music.unpause()
                                if statut == 2 :
                                        menu = True
                                        jeu = False
                                

                                        commencer = 0
                                        pers_case_x = 0
                                        pers_case_y = 0
                                        pers_x = 0
                                        pers_y = 0

                                        sons[s].fadeout(300)
                                        pygame.mixer.music.unpause()
                                        statut = 1
                                        
                                        
                                if event.key == pygame.K_a:
                                        jeu = False
                                        continuer = False


                                elif event.key == K_RIGHT:
                                        if pers_case_x < 19:
                                                if niveaux[lvl] == "niveau 4.txt" :
                                                        if agencement_lvl[pers_case_y][pers_case_x+1] == "5":
                                                                
                                                                if pers_case_y == tele_y[0] and pers_case_x+1 == tele_x[0]:
                                                                        pers_case_y = tele_y[1]
                                                                        pers_case_x = tele_x[1]
                                                                        pers_y = tele_y[1]*64
                                                                        pers_x = tele_x[1]*64
                                                                        
                                                                else:
                                                                        pers_case_y = tele_y[0]
                                                                        pers_case_x = tele_x[0]
                                                                        pers_y = tele_y[0]*64
                                                                        pers_x = tele_x[0]*64

                                                                        
                                                if agencement_lvl[pers_case_y][pers_case_x+1] != "1":
                                                        pers_case_x += 1
                                                        pers_x = pers_case_x * 64
                                                        
                                                elif agencement_lvl[pers_case_y][pers_case_x+1] == "1":
                                                        statut = 0
                                                        pygame.mixer.music.fadeout(300)
                                                        pygame.mixer.music.pause()
                                                        son.play()
        

                                                        
                                elif event.key == K_LEFT:
                                        if pers_case_x > 0:
                                                if niveaux[lvl] == "niveau 4.txt":
                                                        if agencement_lvl[pers_case_y][pers_case_x-1] == "5":
                                                                if pers_case_y == tele_y[0] and pers_case_x-1 == tele_x[0]:
                                                                        pers_case_y = tele_y[1]
                                                                        pers_case_x = tele_x[1]
                                                                        pers_y = tele_y[1]*64
                                                                        pers_x = tele_x[1]*64
                                                                else:
                                                                        pers_case_y = tele_y[0]
                                                                        pers_case_x = tele_x[0]
                                                                        pers_y = tele_y[0]*64
                                                                        pers_x = tele_x[0]*64
                                                if agencement_lvl[pers_case_y][pers_case_x-1] != "1":
                                                        pers_case_x -= 1
                                                        pers_x = pers_case_x * 64
                                                        
                                                elif agencement_lvl[pers_case_y][pers_case_x-1] == "1" :
                                                        statut = 0
                                                        pygame.mixer.music.fadeout(300)
                                                        pygame.mixer.music.pause()
                                                        son.play()
                                                            
                                elif event.key == K_UP:
                                        if pers_case_y > 0:
                                                if niveaux[lvl] == "niveau 4.txt":
                                                        if agencement_lvl[pers_case_y-1][pers_case_x] == "5":
                                                                if pers_case_y-1 == tele_y[0] and pers_case_x == tele_x[0]:
                                                                        pers_case_y = tele_y[1]
                                                                        pers_case_x = tele_x[1]
                                                                        pers_y = tele_y[1]*64
                                                                        pers_x = tele_x[1]*64
                                                                else:
                                                                        pers_case_y = tele_y[0]
                                                                        pers_case_x = tele_x[0]
                                                                        pers_y = tele_y[0]*64
                                                                        pers_x = tele_x[0]*64
                                                if agencement_lvl[pers_case_y-1][pers_case_x] != "1":
                                                        pers_case_y -= 1
                                                        pers_y = pers_case_y * 64
                                                        
                                                elif agencement_lvl[pers_case_y-1][pers_case_x] == "1":
                                                        statut = 0
                                                        pygame.mixer.music.fadeout(300)
                                                        pygame.mixer.music.pause()
                                                        son.play()
                                elif event.key == K_DOWN:
                                        if pers_case_y < 9:
                                                if niveaux[lvl] == "niveau 4.txt":
                                                        if agencement_lvl[pers_case_y+1][pers_case_x] == "5":
                                                                if pers_case_y+1 == tele_y[0] and pers_case_x == tele_x[0]:
                                                                        pers_case_y = tele_y[1]
                                                                        pers_case_x = tele_x[1]
                                                                        pers_y = tele_y[1]*64
                                                                        pers_x = tele_x[1]*64
                                                                else:
                                                                        pers_case_y = tele_y[0]
                                                                        pers_case_x = tele_x[0]
                                                                        pers_y = tele_y[0]*64
                                                                        pers_x = tele_x[0]*64
                                                if agencement_lvl[pers_case_y+1][pers_case_x] != "1":
                                                        pers_case_y += 1
                                                        pers_y = pers_case_y * 64
                                                        
                                                elif agencement_lvl[pers_case_y+1][pers_case_x] == "1" :
                                                        statut = 0
                                                        pygame.mixer.music.fadeout(300)
                                                        pygame.mixer.music.pause()
                                                        son.play()
                        
       
                if agencement_lvl[pers_case_y][pers_case_x]== "2":
                        statut = 2
                        pers_case_x = 0
                        pers_case_y = 0
                        pers_x = 0
                        pers_y = 0
                        pygame.mixer.music.fadeout(300)
                        pygame.mixer.music.pause()
                        applaudissements.play()
                afficheur(screen)
                
                screen.blit(gj,(pers_x,pers_y))
                if agencement_lvl[pers_case_y][pers_case_x] == "4":
                
                        afficheur(screen)
                
                if statut == 0:

                        commencer = 0
                        
                        pers_case_x = 0
                        pers_case_y = 0
                        pers_x = 0
                        pers_y = 0
                        
                        screen.blit(loose,(0,0))
                        
                        
                        
                        
                        joue = 0
                        
                        
                        
                elif statut == 2:
                        commencer = 0
                        screen.blit(win,(0,0))
                        
                        
                pygame.display.flip()
pygame.quit()
   
        
