#thibault

import os
grille = [["-","-","-"],
          ["-","-","-"],
          ["-","-","-"]]
jeu = True
poss = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
clear = lambda: os.system('cls')

# defs # gab

def show_grid():
    """ affiche la grille actuelle """
    print(f"{grille[0]}\n{grille[1]}\n{grille[2]}")

def num_to_pos(num):
    """ transforme le num de case donné en positions """
    return poss[num-1]

 # aurelien

def tour_croix(pos):
    """" fait jouer les croix """
    if grille[pos[0]][pos[1]] == "-":
        grille[pos[0]][pos[1]] = "X"
        clear()
        show_grid()
        return
    else:
        print("cette case est déjà occupée !")
        tour_croix(num_to_pos(int(input("CROIX : dans quelle case veux-tu jouer ?\n"))))
          
# aurelien

def tour_ronds(pos):
    """" fait jouer les ronds """
    if grille[pos[0]][pos[1]] == "-":
        grille[pos[0]][pos[1]] = "O"
        clear()
        show_grid()
        return
    else:
        print("cette case est déjà occupée !")
        tour_ronds(num_to_pos(int(input("RONDS : dans quelle case veux-tu jouer ?\n"))))

# aurelien

def check_win():
    """ vérifie si un joueur a gagné """
    for a in range(0,3):
        if grille[a][0] == grille[a][1] and grille[a][0] == grille[a][2] and grille[a][0] !="-" :
            print(f"C'est gagné sur la ligne {a+1} pour {grille[a][0]} !\n")
            quit()
        elif grille[0][a] == grille[1][a] and grille[0][a] == grille[2][a] and grille[0][a] !="-" :
            print(f"C'est gagné sur la colonne {a+1} pour {grille[0][a]} !\n")
            quit()
    if (grille[0][0] == grille[1][1] and grille[0][0] == grille[2][2] and grille[0][0] !="-") or (grille[0][2] == grille[1][1] and grille[0][2] == grille[2][0] and grille[0][2] !="-"):
            print(f"C'est gagné sur la diagonale pour {grille[1][1]} !\n")
            quit()
    
    # print(grille[0].count('X')+grille[0].count('O')+grille[1].count('X')+grille[1].count('O')+grille[2].count('X')+grille[2].count('O')) Test
    if grille[0].count('X')+grille[0].count('O')+grille[1].count('X')+grille[1].count('O')+grille[2].count('X')+grille[2].count('O') ==9:
        print(f"Match nul !\n")
        quit()

# début du jeu # thibault

clear()
print(" __  __  ____  _____  _____ _____ ____  _   _ \n|  \/  |/ __ \|  __ \|  __ \_   _/ __ \| \ | |\n| \  / | |  | | |__) | |__) || || |  | |  \| |\n| |\/| | |  | |  _  /|  ___/ | || |  | | . ` |\n| |  | | |__| | | \ \| |    _| || |__| | |\  |\n|_|  |_|\____/|_|  \_\_|   |_____\____/|_| \_|\n")
print("Alignez 3 symboles identiques et c'est gagné !")
print("les cases sont numérotées de 1 à 9, de haut en bas et des gauche à droite :")
print("|1|2|3| \n|4|5|6| \n|7|8|9| \n")


show_grid()#gab
while jeu :

    # tour des croix / Gab
    tour_croix(num_to_pos(int(input("CROIX : dans quelle case veux-tu jouer ?\n"))))
    
            
    check_win()

    # tour des ronds / Gab
    tour_ronds(num_to_pos(int(input("RONDS : dans quelle case veux-tu jouer ?\n"))))
    
            
    check_win()
