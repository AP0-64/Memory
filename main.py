from random import randint
from time import sleep

def genere_liste_aleatoire(niveau):
    """ Génère une liste de longueur n avec des élements aléatoires """
    assert niveau > 0
    global lst_aleatoire
    lst_aleatoire = []
    for _ in range(niveau):
        lst_aleatoire.append(randint(10, 99))
    return lst_aleatoire

def saisie_liste(niveau):
    """ Génère une liste de longueur n en nous demandant les entiers voulus """
    assert niveau > 0
    lst_saisie = []
    for i in range(niveau):
        entier_saisie = int(input(f"Veuillez taper l'entier numéro {i+1} seulement : "))
        lst_saisie.append(entier_saisie)
    return lst_saisie

def mystere(lst, n):
    """ Renvoie le nombre de fois que le chiffre n est dans la liste """
    compteur = 0
    for elt in lst:
        if elt == n:
            compteur = compteur + 1
    return compteur

def compare_liste(lst1, lst2):
    """ Compare deux liste et renvoie le nombre d'erreur """
    assert len(lst1) == len(lst2)
    if lst1 == [] or lst2 == []:
        print("Tapez une liste non vide")
        return None
    nombre_de_difference = 0
    if lst1[0] != lst2[0]:
        nombre_de_difference = nombre_de_difference + 1
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            nombre_de_difference = nombre_de_difference + 1
    return nombre_de_difference

def affichage():
    print("\n" * 40)
    print("Bienvenu au jeu de mémoire.")
    print()
    print("Objectif : Le but du jeu est de tester ta mémoire et de voir jusqu'à quel niveau tu peux aller en reproduisant des séquences de nombres qui sera de plus en plus longue à travers les niveaux.")
    print()
    print("À chaque niveau, tu verras une séquence de nombres s'afficher à l'écran. Regarde bien cette séquence, car tu aura quelques secondes pour la mémoriser. Ensuite, tu devras taper une liste de nombres.")
    print()
    print("Si tu parviens à reproduire la séquence exactement comme elle était affichée, tu passes au niveau suivant, et tu gagnes ! Du moins, pour l'instant.")
    print()
    print("Si tu te trompes en tapant la liste de nombres, tu perdra.")
    print()
    print("L'objectif ultime est de voir jusqu'à quel niveau tu peux arriver en te rappelant et en tapant correctement ces séquences de nombres.")
    print()

niveau = 0
while True:
    if niveau == 0:
        affichage()
    input("Appuie sur entrer pour continuer.")
    niveau += 1
    cible = genere_liste_aleatoire(niveau)
    print(cible)
    sleep(niveau + 1)
    print("\n" * 40)
    reponse = saisie_liste(niveau)
    if compare_liste(cible, reponse) == 0:
        print()
        print("Bravo ! Tu passes au niveau suivant.")
        print()
    else:
        print("Perdu !")
        print("La réponse était :")
        for i in range(len(cible)):
            print(cible[i])
        print("Tu a perdu au niveau", niveau)
        break
