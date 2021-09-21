#Importation        -------
import pygame
import Difficulties
import DrawSnake

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
Snake = [[1,0]]
direction = right


running = True
waze = Difficulties.difficulties("easy")


#init des ligne et colonne
for i in range(20):
    for y in range(20):
        pygame.draw.rect(screen,GREY,(border,border,mazeSize,mazeSize))
for i in range(21):
    pygame.draw.lines(screen,GREYY,False,[(border + (35*i), border),(border + (35*i), border + mazeSize)], 3)
    pygame.draw.lines(screen,GREYY,False,[(border , border+ (35*i)),(border+ mazeSize, border  + (35*i))], 3)

    
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

    if(direction == right):#on tourne a droite
        for i in range(len(Snake)):
            if(i==0):
                DrawSnake.drawErase(screen,border + 5 + 35 * Snake[i][0], border + 5 + 35 * Snake[i][1])
                Snake[i][0]+= 1
                DrawSnake.drawSnakeHead(screen,border + 5 + 35 * Snake[i][0],border + 5 + 35 * Snake[i][1],right)
            if(i>0):
                DrawSnake.drawErase(screen,border+5 + 35*Snake[i][0],border+5 + 35*Snake[i][1])
                Snake[i] = Snake[0]
                Snake[i][0] -= 1
                DrawSnake.drawSnakeCorpse(screen,border+5 + 35 * Snake[i][0],border + 5 + 35 * Snake[i][1])
    elif(direction == left):#on tourne a gauche
        for i in range(len(Snake)):
            if(i==0):
                DrawSnake.drawErase(screen,border + 5 + 35 * Snake[i][0], border + 5 + 35 * Snake[i][1])
                Snake[i][0]-= 1
                DrawSnake.drawSnakeHead(screen,border + 5 + 35 * Snake[i][0],border + 5 + 35 * Snake[i][1],left)
            if(i>0):
                DrawSnake.drawErase(screen,border+5 + 35*Snake[i][0],border+5 + 35*Snake[i][1])
                Snake[i] = Snake[0]
                Snake[i][0] += 1
                DrawSnake.drawSnakeCorpse(screen,border+5 + 35 * Snake[i][0],border + 5 + 35 * Snake[i][1])
    elif(direction == up):#on tourne en haut
        for i in range(len(Snake)):
            if(i==0):
                DrawSnake.drawErase(screen,border + 5 + 35 * Snake[i][0], border + 5 + 35 * Snake[i][1])
                Snake[i][1]-= 1
                DrawSnake.drawSnakeHead(screen,border + 5 + 35 * Snake[i][0],border + 5 + 35 * Snake[i][1],up)
            if(i>0):
                DrawSnake.drawErase(screen,border+5 + 35*Snake[i][0],border+5 + 35*Snake[i][1])
                Snake[i] = Snake[0]
                Snake[i][1] += 1
                DrawSnake.drawSnakeCorpse(screen,border+5 + 35 * Snake[i][0],border + 5 + 35 * Snake[i][1])
    elif(direction == dn):#on tourne en bas
        for i in range(len(Snake)):
            if(i==0):
                DrawSnake.drawErase(screen,border + 5 + 35 * Snake[i][0], border + 5 + 35 * Snake[i][1])
                Snake[i][1] += 1
                DrawSnake.drawSnakeHead(screen,border + 5 + 35 * Snake[i][0],border + 5 + 35 * Snake[i][1],dn)
            if(i>0):
                DrawSnake.drawErase(screen,border+5 + 35*Snake[i][0],border+5 + 35*Snake[i][1])
                Snake[i] = Snake[0]
                Snake[i][1] -= 1
                DrawSnake.drawSnakeCorpse(screen,border+5 + 35 * Snake[i][0],border + 5 + 35 * Snake[i][1])


        #if evenement.type == pygame.KEYDOWN:

        



pygame.quit()#on quitte le programme

