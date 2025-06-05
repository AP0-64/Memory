from random import randint
from time import sleep


def genere_liste_aleatoire(niveau):
    """ Génère une liste de longueur n avec des éléments aléatoires """
    assert niveau > 0
    global lst_aleatoire
    lst_aleatoire = []
    lst_aleatoire.extend(randint(10, 99) for _ in range(niveau))
    return lst_aleatoire


def saisie_liste(niveau):
    """ Génère une liste de longueur n en demandant les entiers voulus """
    assert niveau > 0
    lst_saisie = []
    for i in range(niveau):
        while True:
            try:
                entier_saisie = int(input(
                    f"Veuillez taper l'entier numéro {i+1} : "))
                lst_saisie.append(entier_saisie)
                break
            except ValueError:
                print("Entrée invalide. Veuillez taper un entier.")
    return lst_saisie


def mystere(lst, n):
    """ Renvoie le nombre de fois que le chiffre n est dans la liste """
    compteur = 0
    for elt in lst:
        if elt == n:
            compteur = compteur + 1
    return compteur


def compare_liste(lst1, lst2):
    """ Compare deux listes et renvoie le nombre d'erreurs """
    assert len(lst1) == len(lst2)
    return sum(a != b for a, b in zip(lst1, lst2))


def affichage():
    print("\n" * 40)
    print("Bienvenu au jeu de mémoire.")
    _extracted_from_affichage_4(
        "Objectif : ",
        "Le but du jeu est de tester ta mémoire et de voir jusqu'à",
        "quel niveau tu peux aller en reproduisant des séquences",
    )
    print("de nombres qui seront de plus en plus longues à travers")
    print("les niveaux.")
    _extracted_from_affichage_4(
        "À chaque niveau, tu verras une séquence de nombres s'afficher",
        " à l'écran. Regarde bien cette séquence, car tu aura quelques",
        "secondes pour la mémoriser. Ensuite, tu devras taper une liste",
    )
    print("de nombres. Tape un nombre à la fois, en appuyant sur entrer.")
    _extracted_from_affichage_4(
        "Si tu parviens à reproduire la séquence exactement comme elle",
        "était affichée, tu passes au niveau suivant, et tu gagnes !",
        "Du moins, pour l'instant.",
    )
    print()
    print("Si tu te trompes en tapant la liste de nombres, tu perdra.")
    _extracted_from_affichage_4(
        "L'objectif ultime est de voir jusqu'à quel niveau tu peux",
        "arriver en te rappelant et en tapant correctement ces séquences",
        "de nombres.",
    )
    print()


# TODO Rename this here and in `affichage`
def _extracted_from_affichage_4(arg0, arg1, arg2):
    print()
    print(arg0)
    print(arg1)
    print(arg2)


niveau = 0

# Programme principal
while True:
    if niveau == 0:
        affichage()
    niveau += 1
    if niveau != 0:
        print("Niveau", niveau)
    input("Appuie sur entrer pour continuer.")
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
        print("La réponse était :                   Tu as répondu :")
        for i in range(len(cible)):
            print(cible[i], "                                 ", reponse[i])
        print("Tu a perdu au niveau", niveau)
        break
