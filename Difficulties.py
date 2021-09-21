import pygame

easy = []
medium = []
hard = []

#Fonction de sélection de difficulté et initialisation du niveau
def difficulties(difficulty):
    if(difficulty == "easy"):
        for i in range(5):
            easy.append([])
            for y in range(5):
                easy[i].append(0)
        return easy


        #medium.append = []
        #print(medium)
        #hard = []

difficulties(1)
print(easy)
