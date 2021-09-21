import random2

easy = []
medium = []
hard = []

#Fonction de sélection de difficulté et initialisation du niveau
def difficulties(difficulty):
    
    #Difficultée facile
    if(difficulty == "easy"):
        for i in range(20):
            easy.append([])
            for y in range(20):
                easy[i].append(0)
        return easy

    #Difficultée moyenne
    if(difficulty == "medium"):
        for i in range(20):
            medium.append([])
            for y in range(20):
                if (random2.randint(1,100) > 5):
                    medium[i].append(0)
                else:
                    medium[i].append(1)
        return medium

    #Difficultée difficile
    if(difficulty == "hard"):
        for i in range(20):
            hard.append([])
            for y in range(20):
                if (random2.randint(1,100) > 15):
                    hard[i].append(0)
                else:
                    hard[i].append(1)
        return hard
