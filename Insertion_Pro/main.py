#Exerice 1
#Etape 1
#Nous souhaitons avoir une interface sous forme de grille NxN (6x6 par exemple). Dans chaque case, nous devons pouvoir afficher un caractère (comme A par exemple).
#Pour commencer nous allons faire une fonction qui permet d'afficher des matrices NxN (6x6 par exemple). Dans chaque case, nous devons pouvoir afficher un caractère (comme A par exemple).
import random


def print_matrix(matrix):
    for row in matrix:
        print(" | ".join(row))

print_matrix([["|", "|", "|", "|"], ["|", "1", "|", "|"], ["|", "|", "|", "|"], ["|", "|", "|", "|"]])

#Etape 2
#Génération aléatoire de la grille Nous souhaitons afficher la grille avec K objets (K<N)

def generate_grid(N, K):
    #grid = []
    #for i in range(N):
     #   row = []
       # for j in range(N):
        #    row.append("|")
        #grid.append(row)
    grid = [["0" for i in range(N)] for j in range(N)]
    for i in range(K):
        while True:
            x = random.randint(0, N-1)
            y = random.randint(0, N-1)
            if grid[x][y] == "0":
                grid[x][y] = "A"
                break
    return grid

#print_matrix(generate_grid(6, 5))

#Etape 3
#Algo à chercher (algo de peuplement)
#Nous souhaitons pouvoir tester un algo qui doit trouver tous les K objets et placer à côté (à droite ou à gauche) un nouvel objet de tel sorte que chaque objet est un et unique voisin. Il faut retourner le tableau en remplacant les 0 par des A quand c'est un voisin et il ne faut pas que 2 A aient des voisins en commun
#Algo de peuplement
def find_neighbors(grid):
    pose = False
    positions = []
    position_false = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "A":
                if j != len(grid[i]) - 1 and grid[i][j + 1] == "A":
                    pose = False;
                    position_false.append((j+1))
                    position_false.append((j-1))
                    position_false.append((j))
                elif j != 0 and grid[i][j - 1] == "A":
                    pose = False;
                    position_false.append((j + 1))
                    position_false.append((j-1))
                    position_false.append((j))
                if j != len(grid[i])-1 and grid[i][j+1] == "0":
                    if j != len(grid[i])-2 and grid[i][j+2] == "A":
                        pose = False
                        position_false.append(j+1)
                        position_false.append(j+3)
                        position_false.append(j-1)
                    elif j+1 not in position_false:
                        positions.append((i,j+1))
                        position_false.append(j+2)
                        position_false.append(j-1)
                        position_false.append(j+1)
                        pose = True
                elif j != 0 and grid[i][j-1] == "0":
                    if j != 1 and grid[i][j-2] == "A":
                        pose = False
                        position_false.append(j-1)
                        position_false.append(j-3)
                        position_false.append(j+1)
                    elif j-1 not in position_false:
                        positions.append((i,j-1))
                        position_false.append(j-2)
                        position_false.append(j+1)
                        position_false.append(j-1)
                        pose = True
        position_false = []
        if pose :
            for i in range(len(positions)):
                grid[positions[i][0]][positions[i][1]] = "B"
            positions = []
            pose = False
    return grid



#grid = generate_grid(6, 4)
#print_matrix(grid)
#print("------------------------------")
#print_matrix(find_neighbors(grid))

#Etape 4
#Modifier la fonction de l’Etape 2 pour ajouter des casses bloquées (P < N/2).


def generate_grid(N, K, P):
    grid = [["0" for i in range(N)] for j in range(N)]
    for i in range(K):
        while True:
            x = random.randint(0, N-1)
            y = random.randint(0, N-1)
            if grid[x][y] == "0":
                grid[x][y] = "A"
                break
    for i in range(P):
        while True:
            x = random.randint(0, N-1)
            y = random.randint(0, N-1)
            if grid[x][y] == "0":
                grid[x][y] = "P"
                break
    return grid

grid = generate_grid(6, 4, 5)
print_matrix(grid)
print("------------------------------")
print_matrix(find_neighbors(grid))

#Exercice 2
#Dans une chaîne, détecter la plus longue chaîne de caractères composés de caractères distincts.
#Par exemple : “abcdemo” est la plus longue chaîne de caractères distincts de “abcdemoderneancien”

def longest_distinct_characters(word):
    list1 = []
    list2 = []
    for i in range(len(word)):
        if word[i] not in list2:
            list2.append(word[i])
        else:
            if len(list1) < len(list2):
                list1 = list2
            list2 = [word[i]]
    return "".join(list1)

print(longest_distinct_characters("abcdemoderneancien"))

#Exercice 3
#Concevoir un algorithme pour trouver tous les caractères communs à deux listes triées.
#Par exemple, pour les listes a, e, e, e et b, b, c, e, e, g, la sortie doit être de e, e.

def common_characters(list1, list2):
    array1 = []
    for letter in list1:
        if letter in list2:
            array1.append(letter)
            list2.remove(letter)
    return array1


print(common_characters(["a", "e", "e", "e"], ["b", "b", "c", "e", "e", "g"]))

#Exercice 4
#Diviser un tableau de nombre en deux de manière à ce que la différence entre les deux tableaux soit la plus petite possible.

def split_array(array):
    array1 = []
    array2 = []
    array.sort(reverse=True)
    for i in range(len(array)):
        if sum(array1) < sum(array2):
            array1.append(array[i])
        else:
            array2.append(array[i])
    return array1, array2

print(split_array([1,2,3,4,5,6,7,8,9,10,100]))

#Exercice 5
#Ecrire une fonction qui calcule la longueur moyenne des mots d’un texte. sentence1 = "Même les phrases avec des caractères de la langue française peuvent être utilisées."
#print(average_words_length(sentence1)) [Output] => 5.38
import string


def average_words_length(sentence):
    words = sentence.split()
    return round(sum([len(word) for word in words if word not in string.punctuation]) / len(words), 2)

sentence1 = "Même les phrases avec des caractères de la langue française peuvent être utilisées."
print(average_words_length(sentence1))

#Exercice 6
#Nous souhaitons inverser un entier (positif ou négatif), c’est-à-dire notre fonction prend en entrée un entier -6523 par exemple et retourne en sortie l’entier inversé -3256.
#Afficher les résultats de notre fonction pour 2020 et -9430
def reverse_int(number):
    if number < 0:
        return -int(str(number)[1:][::-1])
    return int(str(number)[::-1])
    #return int(str(number)[::-1])

print(reverse_int(2020))
print(reverse_int(-9430))

#Exercice 7
#Retrouver dans une liste d’entiers, tous les triplets pythagoriciens possibles qui y sont. Pour rappel, un triplet pythagoricien respecte le théorème suivant : a2 + b2 = c2. Prenons l’exemple suivant : nous avons la liste [0, 3, 6, 1, 2, 4, 5]. Notre fonction renvoie la liste des triplets possibles : [(3, 4, 5)] car 9 + 16 = 25.


def pythagoricien(liste):
    liste_pythagoricien = []
    for a in liste:
        for b in liste:
            for c in liste:
                if a**2 + b**2 == c**2:
                    liste_pythagoricien.append((a, b, c))
    return liste_pythagoricien

print(pythagoricien([3, 6, 1, 2, 4, 5]))

#Exercice 8
#Nous avons un mot et nous voulons savoir quel est le premier caractère unique de ce mot, c’est-à-dire la lettre qui ne se répète pas dans le mot et la première.

def first_unique_character(word):
    for letter in word:
        if word.lower().count(letter.lower()) == 1:
            return (letter, word.lower().index(letter.lower()))
    return None

print(first_unique_character('coronavirus'))
print(first_unique_character('Europe'))