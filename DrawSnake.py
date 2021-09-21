#Importation
import pygame

#Initialisation des variables
screen = pygame.display.set_mode((800, 800))
RED = pygame.Color(240, 30, 40)
BLUE = pygame.Color(0, 160, 230)
GREEN = pygame.Color(30, 170, 70)
GREY = pygame.Color(160, 160, 160)

#Fonction créatrice de la tête du Snake
def drawSnakeHead(screen, x, y, orientation):

    #Dessine la tête du serpent en fonction de son orientation
    #Nord
    if(orientation == 0):
        pygame.draw.polygon(screen, RED, [(x, y+25), (x+12.5, y), (x+25, y+25)])
    #Est
    elif(orientation == 1):
        pygame.draw.polygon(screen, RED, [(x, y), (x+25, y+12.5), (x, y+25)])
    #Sud
    elif(orientation == 2):
        pygame.draw.polygon(screen, RED, [(x, y), (x+12.5, y+25), (x+25, y)])
    #Ouest
    elif(orientation == 3):
        pygame.draw.polygon(screen, RED, [(x, y+12.5), (x+25, y), (x+25, y+25)])
        
    #Raffraichis l'écran
    pygame.display.update()


#Fonction créatrice du corps du Snake
def drawSnakeCorpse(screen, x, y):
    
    #Dessine le corps du serpent
    pygame.draw.rect(screen, GREEN, [(x, y), (25, 25)])


#Fonction créatrice de la queue du Snake
#def drawSnakeTail(screen, x, y, orientation):


#Fonction créatrice de la cible
def drawTarget(screen, x, y):

    #Dessine la cible
    pygame.draw.circle(screen, BLUE, ((x+12.5,y+12.5)), 12.5)
    pygame.draw.circle(screen, RED, ((x+12.5,y+12.5)), 3)

    #Raffraichis l'écran
    pygame.display.update()


#Fonction destructrice du Snake
def drawErase(screen, x, y):
    pygame.draw.rect(screen, GREY, [(x-1, y-1), (27, 27)])

    #Raffraichis l'écran
    pygame.display.update()
