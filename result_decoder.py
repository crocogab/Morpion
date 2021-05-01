import os

file = open("C:/Users/croco/Desktop/Cours/NSI/Morpion/data.txt", "r")
file2 = open("C:/Users/croco/Desktop/Cours/NSI/Morpion/data_result.txt", "w")





def check_win(liste): # aurelien
    """ vérifie si un joueur a gagné """
    n=0
    # for a in range(0,3):
    #     if liste[a]== liste[a+3] and liste[a+3] == liste[a+6] and liste[a] !="-" :
    #         print(f"Victoire : {liste[a]} !")
    #         file2.write(liste[a]+'\n')
    #         n=1
        
            
            
    #     elif liste[a] == liste[a+3] and liste[a] == liste[a+6] and liste[a] !="-" :
    #         print(f"Victoire : {liste[0]} !")
    #         file2.write(liste[0]+'\n')
    #         n=1
            
    # if (liste[0] == liste[4] and liste[0] == liste[8] and liste[0] !="-") or (liste[2] == liste[4] and liste[2] == liste[6] and liste[2] !="-"):
    #         print(f"Victoire : {liste[4]} !")
    #         file2.write(liste[4]+'\n')
    #         n=1
    if liste[0]==liste[1]==liste[2] and n==0:
        print(f"Victoire : {liste[1]} !")
        file2.write(liste[1]+'\n')
        n=1
    if liste[3]==liste[4]==liste[5] and n==0:
        print(f"Victoire : {liste[3]} !")
        file2.write(liste[3]+'\n')
        n=1
    if liste[6]==liste[7]==liste[8] and n==0:
        print(f"Victoire : {liste[6]} !")
        file2.write(liste[6]+'\n')
        n=1
    if liste[0]==liste[3]==liste[6] and n==0:
        print(f"Victoire : {liste[0]} !")
        file2.write(liste[0]+'\n')
        n=1
    if liste[1]==liste[4]==liste[7] and n==0:
        print(f"Victoire : {liste[1]} !")
        file2.write(liste[1]+'\n')
        n=1
    if liste[3]==liste[4]==liste[5] and n==0:
        print(f"Victoire : {liste[3]} !")
        file2.write(liste[3]+'\n')
        n=1
    if liste[2]==liste[5]==liste[8] and n==0:
        print(f"Victoire : {liste[2]} !")
        file2.write(liste[2]+'\n')
        n=1
    if liste[0]==liste[4]==liste[8] and n==0:
        print(f"Victoire : {liste[0]} !")
        file2.write(liste[0]+'\n')
        n=1
    if liste[2]==liste[4]==liste[6] and n==0:
        print(f"Victoire : {liste[2]} !")
        file2.write(liste[2]+'\n')
        n=1
    # print(liste[0].count('X')+liste[0].count('O')+liste[1].count('X')+liste[1].count('O')+liste[2].count('X')+liste[2].count('O')) Test
    if  n==0:
        print(f"Match nul !\n")
        file2.write("="+'\n')

        
for i in file:
    print(i)
    
    i=i.replace('[', '')
    i=i.replace(']', '')
    i=i.replace("'", '')
    i=i.replace(',', '')
    arr=list(i)
    arr.remove('\n')
    for i in arr:
        if i==' ':
            arr.remove(i)
    print(arr,type(arr))
    check_win(arr)