#Importation        -------
import pygame
import Difficulties

#Initialisation     -------
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
FPS = 60
WHITE = pygame.Color(255, 255, 255)
GREY = pygame.Color(160,160,160)
clock.tick(FPS)
 
screen.fill(WHITE)
pygame.draw.rect(screen,GREY,(50,50,700,700))
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        



pygame.quit()