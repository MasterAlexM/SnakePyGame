#Importation
import pygame
import Difficulties

#Initialisaiton des couleurs
WHITE  = pygame.Color(255, 255, 255)
GREY   = pygame.Color(160,160,160)
GREYY  = pygame.Color(100,100,100)
BLUE   = pygame.Color(0,0,255)

#Initialisation de l'écran de jeu
pygame.init()
screenSize = 800
screen  = pygame.display.set_mode((screenSize,screenSize))#init display a 800x800
pygame.display.set_caption('Snake')
screen.fill(WHITE)
border = 50
mazeSize = screenSize-border*2
pygame.draw.rect(screen,GREY,(border,border,mazeSize,mazeSize))

#Initialisation des principales variables du Snake
up      = 0
right   = 1
dn      = 2
left    = 3
Snake = [[1,0]]
direction = right


running = True
waze = Difficulties.difficulties("easy")

#Création de la grille de jeu
for i in range(20):
    for y in range(20):
        pygame.draw.rect(screen,GREY,(border,border,mazeSize,mazeSize))
for i in range(21):
    pygame.draw.lines(screen,GREYY,False,[(border + (35*i), border),(border + (35*i), border + mazeSize)], 3)
    pygame.draw.lines(screen,GREYY,False,[(border , border+ (35*i)),(border+ mazeSize, border  + (35*i))], 3)

    
pygame.display.update()
keys = []
while running:
    #Délai du jeu pour l'affichage
    pygame.time.delay(300)
    #Lecture des évènements
    for event in pygame.event.get():
        #Exit
        if event.type == pygame.QUIT:#Exit
            running = False
        #Si une touche est appuyé
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            #Flèche de gauche
            if keys[pygame.K_LEFT]:
                direction = left
            #Flèche de droite
            elif keys[pygame.K_RIGHT]:
                direction = right
            #Flèche du haut
            elif keys[pygame.K_UP]:
                direction = up
            #Flèche du bas
            elif keys[pygame.K_DOWN]:
                direction = dn

    #On tourne a droite
    if(direction == right):
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
    #On tourne a gauche
    elif(direction == left):
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
    #On tourne en haut
    elif(direction == up):
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
    #On tourne en bas
    elif(direction == dn):
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
