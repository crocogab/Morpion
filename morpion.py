import os

grille = [["-","-","-"],
          ["-","-","-"],
          ["-","-","-"]]

jeu = True

poss = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]

# defs

def show_grid():
    """ affiche la grille actuelle """
    print(f"{grille[0]}\n{grille[1]}\n{grille[2]}")

def num_to_pos(num):
    """ transforme le num de case donné en positions """
    return poss[num-1]



def tour_croix(pos): # aurelien
    """" fait jouer les croix """
    if grille[pos[0]][pos[1]] == "-":
        grille[pos[0]][pos[1]] = "X"
        clear()
        show_grid()
        return
    else:
        print("cette case est déjà occupée !")
        tour_croix(num_to_pos(int(input("CROIX : dans quelle case veux-tu jouer ?\n"))))

def tour_ronds(pos): # aurelien
    """" fait jouer les ronds """
    if grille[pos[0]][pos[1]] == "-":
        grille[pos[0]][pos[1]] = "O"
        clear()
        show_grid()
        return
    else:
        print("cette case est déjà occupée !")
        tour_ronds(num_to_pos(int(input("RONDS : dans quelle case veux-tu jouer ?\n"))))



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

clear = lambda: os.system('cls')


# début du jeu # aurelien

clear()
print("les cases sont numérotées de 1 à 9, de haut en bas et des gauche à droite :")
print("|1|2|3| \n|4|5|6| \n|7|8|9| \n")


show_grid()
while jeu :

    # tour des croix 
    tour_croix(num_to_pos(int(input("CROIX : dans quelle case veux-tu jouer ?\n"))))
    #print(len(grille[0]),)
    check_win()

    # tour des ronds
    tour_ronds(num_to_pos(int(input("RONDS : dans quelle case veux-tu jouer ?\n"))))
    #print(len(grille))
    check_win()