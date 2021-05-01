import os
import random

file = open("C:/Users/croco/Desktop/Cours/NSI/Morpion/data.txt", "a")

#gab
grille = [["-","-","-"],
          ["-","-","-"],
          ["-","-","-"]]

jeu = True

#gab
poss = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]

# defs
#gab
def show_grid():
    """ affiche la grille actuelle """
    print(f"{grille[0]}\n{grille[1]}\n{grille[2]}")
#gab
def num_to_pos(num):
    """ transforme le num de case donné en positions """
    return poss[num-1]



def tour_croix(pos): # aurelien
    """" fait jouer les croix """
    if grille[pos[0]][pos[1]] == "-":
        grille[pos[0]][pos[1]] = "X"
        clear()
        
        return
    else:
        tour_croix(num_to_pos(random.randrange(9)))

def tour_ronds(pos): # aurelien
    """" fait jouer les ronds """
    if grille[pos[0]][pos[1]] == "-":
        grille[pos[0]][pos[1]] = "O"
        clear()
        
        return
    else:
        
        tour_ronds(num_to_pos(random.randrange(9)))



def check_win(): # aurelien
    """ vérifie si un joueur a gagné """
    for a in range(0,3):
        if grille[a][0] == grille[a][1] and grille[a][0] == grille[a][2] and grille[a][0] !="-" :
            
            file.write((str(grille)+"\n"))
            quit()
        elif grille[0][a] == grille[1][a] and grille[0][a] == grille[2][a] and grille[0][a] !="-" :
            
            file.write((str(grille) +"\n")) 
            quit()
    if (grille[0][0] == grille[1][1] and grille[0][0] == grille[2][2] and grille[0][0] !="-") or (grille[0][2] == grille[1][1] and grille[0][2] == grille[2][0] and grille[0][2] !="-"):
            
            file.write((str(grille)+"\n"))
            quit()
    
    # print(grille[0].count('X')+grille[0].count('O')+grille[1].count('X')+grille[1].count('O')+grille[2].count('X')+grille[2].count('O')) Test
    if grille[0].count('X')+grille[0].count('O')+grille[1].count('X')+grille[1].count('O')+grille[2].count('X')+grille[2].count('O') ==9:
        
        file.write(str(grille)+"\n")
        quit()
    




clear = lambda: os.system('cls')


# début du jeu # aurelien

clear()


#gab

while jeu :

    # tour des croix / Gab
    tour_ronds(num_to_pos(random.randrange(9)))
    
        
    check_win()

    # tour des ronds / Gab
    tour_croix(num_to_pos(random.randrange(9)))
    
            
    check_win()