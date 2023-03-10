#variables
def vars():
    global n
    n = int(input("table size:  ")) # Taille du tableau
    global tbl
    tbl = [" " for i in range(n)]  # Tableau de n places
    for i in range(n): # Chaque place dans tbl aura n places lui meme. Cela creé effectivement une liste de n^2 places
        tbl[i] = [" " for j in range(n)]
    global activePlayer
    activePlayer = "O"

# Fonction pour afficher le tableau
def printTable(p, k):
    lines = [""]*n # list de n places (lignes horizontaux sur le tableau)
    for i in k:
        for j in k:
            lines[i] += " " + p[i][j] if j == 0 else " | " + p[i][j]
    print(lines[0])
    for i in range(1,n):
        print("---"+"+---"*(n-1))
        print(lines[i])

def gui():
    #changement de jouer
    global activePlayer
    if activePlayer == "X":
        activePlayer = "O"
    elif activePlayer == "O":
        activePlayer = "X"

    # Choix de placement
    foul = True
    print("Player {0}, your turn.".format(activePlayer))
    print("Possible inputs are coordinates from 1 to {0} on both axes".format(n))
    while foul == True:
        play = (input(" ")).split()
        playX = int(play[0]) - 1
        playY = int(play[-1]) - 1
        if (tbl[playY][playX] == " ") and (playY <= (n-1)) and (playX <= (n-1)):
            tbl[playY][playX] = activePlayer
            foul = False
        else:
            print("Place taken! Please try again")
            print("")
    printTable(tbl, range(n))

def logic(t): # Logique pour qui gagne
    global win
    win = False
    
    # Lignes droites

    for i in range(n): # Lignes verticales
        if t[i].count(activePlayer) >= n:
            win = True

    for i in range(n): # Lignes horizontales
        temp = []
        for j in range(n):
            temp.append(t[j][i])
        if temp.count(activePlayer) >= n:
            win = True

    # Lignes diagonales

    temp2 = [] # Diagonal du gauche en haut a la droite en bas
    for i in range(n):
        temp2.append(t[i][i])
    if temp2.count(activePlayer) >= n:
        win = True

    temp3 = [] # Diagonal du gauche en bas a la droite en haut
    for i in range(n):
        temp3.append(t[i][(n-1)-i])
    if temp3.count(activePlayer) >= n:
        win = True

def end():
    print("Do you want to play again? y/n")
    temp = input(": ")
    if temp == "y":
        main()
    else:
        pass

# Processus principale avec tous les fonctions
def main():
    vars() #declaration des variables
    printTable(tbl, range(n)) # Premiere table vide
    for i in range(int(n**2)):
        gui()
        logic(tbl)
        if win == True:
            print("gameover")
            print(activePlayer + " won")
            break
    end()
    
main() # Fonction Pricipale