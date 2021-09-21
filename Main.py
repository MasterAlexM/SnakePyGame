#Importation        -------
import pygame
import Difficulties

#init color         -------
WHITE   = pygame.Color(255, 255, 255)
GREY    = pygame.Color(160,160,160)
GREYY   = pygame.Color(100,100,100)
BLUE    = pygame.Color(0,0,255)
#Initialisation     -------
pygame.init()
screenSize = 800
screen  = pygame.display.set_mode((screenSize,screenSize))#init display a 800x800
pygame.display.set_caption('Snake')
screen.fill(WHITE)
border = 50
mazeSize = screenSize-border*2
pygame.draw.rect(screen,GREY,(border,border,mazeSize,mazeSize))

#init snakeBase & direction
up      = 0
right   = 1
dn      = 2
left    = 3
Snake = [[2,0],[1,0],[0,0]]
direction = right


running = True
waze = Difficulties.difficulties("easy")


for i in range(20):
    for y in range(20):
        pygame.draw.rect(screen,GREY,(border,border,mazeSize,mazeSize))
for i in range(21):
    pygame.draw.lines(screen,GREYY,False,[(border + (35*i), border),(border + (35*i), border + mazeSize)], 3)
    pygame.draw.lines(screen,GREYY,False,[(border , border+ (35*i)),(border+ mazeSize, border  + (35*i))], 3)

pygame.draw.rect(screen,BLUE,(border+5,border+5,25,25))
posKR = [0,0]
    
pygame.display.update()
keys = []
while running:
    pygame.time.delay(300)#Delay du jeu pour l'affichage
    for event in pygame.event.get():#lecture des evenement
        if event.type == pygame.QUIT:#Exit
            running = False
        if event.type == pygame.KEYDOWN:#si une touche est appuyer
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:#fleche de gauche
                direction = left
            elif keys[pygame.K_RIGHT]:#fleche de droite
                direction = right
            elif keys[pygame.K_UP]:#fleche de haut
                direction = up
            elif keys[pygame.K_DOWN]:#fleche de bas
                direction = dn

    if(direction == right):
        pygame.draw.rect(screen,GREY,(border+5 + 35*posKR[0],border+5 + 35*posKR[1],25,25))
        posKR[0]+= 1
        pygame.draw.rect(screen,BLUE,(border+5 + 35*posKR[0],border+5 + 35*posKR[1],25,25))
        pygame.display.update()
    elif(direction == left):
        pygame.draw.rect(screen,GREY,(border+5 + 35*posKR[0],border+5 + 35*posKR[1],25,25))
        posKR[0]-= 1
        pygame.draw.rect(screen,BLUE,(border+5 + 35*posKR[0],border+5 + 35*posKR[1],25,25))
        pygame.display.update()   
    elif(direction == up):
        pygame.draw.rect(screen,GREY,(border+5 + 35*posKR[0],border+5 + 35*posKR[1],25,25))
        posKR[1]-= 1
        pygame.draw.rect(screen,BLUE,(border+5 + 35*posKR[0],border+5 + 35*posKR[1],25,25))
        pygame.display.update()  
    elif(direction == dn):
        pygame.draw.rect(screen,GREY,(border+5 + 35*posKR[0],border+5 + 35*posKR[1],25,25))
        posKR[1]+= 1
        pygame.draw.rect(screen,BLUE,(border+5 + 35*posKR[0],border+5 + 35*posKR[1],25,25))
        pygame.display.update()


        #if evenement.type == pygame.KEYDOWN:

        



pygame.quit()

