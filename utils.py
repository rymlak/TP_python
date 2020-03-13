##################### LE JEU DE LA VIE ######################

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

#### Implemation sans numpy

### Question 4 : 
##Calcul du nombre de voisins vivants 

def calcul_nb_voisins(Z):
    forme = len(Z), len(Z[0])
    N = [[0, ] * (forme[0]) for i in range(forme[1])]
    for x in range(1, forme[0] - 1):
        for y in range(1, forme[1] - 1):
            N[x][y] = Z[x-1][y-1]+Z[x][y-1]+Z[x+1][y-1] \
                   + Z[x-1][y] + 0 +Z[x+1][y] \
                   + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
    return N    
    

 
##Fonction Iteration_jeu

def iteration_jeu(Z):
    """Simulation d'un jeu de la vie 
    
    Arguments : 
    Z : 2D liste de listes composée de 0 et 1 d'un jeu de la vie donnée
        
    Cette fonction applique les regles du jeu de la vie de 'Conway':
    Toute cellule morte ayant exactement 3 voisins vivants on lui affecte la valeur 1.
    Toute cellule vivante ayant 0, 1 ou 4 voisins vivants meurt à la génération suivante, on lui affecte 0.
    Sinon la cellule garde la meme valeur.
    
    LA fonction 'iteration_jeu' realise une simulation d'un tour du jeu pour une liste Z donnée.
    """
    
    forme = len(Z), len(Z[0])
    N = calcul_nb_voisins(Z)
    for x in range(1,forme[0]-1):
        for y in range(1,forme[1]-1):
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            elif Z[x][y] == 0 and N[x][y] == 3:
                Z[x][y] = 1
    return Z
    

### Question 5 :

def iterations_steps(Z):

    plt.subplots(figsize=(15,7))
    for i in range(10):
        ax = plt.subplot(2,5,i+1)
        plt.imshow(Z, extent=[0,len(Z[0]),0,len(Z)])
        plt.grid(True)  #trace la grille
        ax.set_xticks(range(0,len(Z[0]),1))
        plt.title('Itération' + str(i))
               
        Z = iteration_jeu(Z) 

    plt.show() 
    

### Question 8 :

def calcul_nb_voisins_np(Z):
    T = np.zeros_like(Z)
    for i in range(1, Z.shape[0]-1):
        for j in range(1, Z.shape[1]-1):
            T[i,j] += Z[i-1,j] + Z[i+1,j] + Z[i,j-1] + Z[i,j+1] + Z[i-1,j-1] +Z[i-1,j+1] + Z[i+1,j-1] + Z[i+1,j+1]
            
    return T


### Question 9 :


def iteration_jeu_np(Z):
    M = calcul_nb_voisins_np(Z)
    for i in range(1, Z.shape[0]-1):
        for j in range(1, Z.shape[1]-1):
            if (Z[i,j].any == 1) and (M.any != 2 and M.any != 3):
                Z[i,j] = 0
            elif Z[i,j].any == 0 and M.any == 3:
                Z[i,j] = 1        
    return Z
    

### Question 10 :

def jeu_np(Z_in, nb_iter):
    Z_after = np.array(Z_in)
    for i in range(nb_iter):
        Z_after = iteration_jeu(Z_in)
    
    return Z_after
    

### Question 13 :

def affiche(mat):
    
    
    plt.subplots(figsize=(15,9))
    
    for i in range(10):
        ax = plt.subplot(2,5,i+1)
        plt.imshow(mat, extent=[0,len(mat[0]),0,len(mat)])
        plt.title('Itération' + str(i))
        
        mat = iteration_jeu_np(mat)
        
    
    plt.show() 