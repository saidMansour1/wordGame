from donnees import *
from random import randrange

def masqueMot(mot) :
    """fonction masquant le mot choisit"""
    chaine = ""
    i = 0
    while i < len(mot) :
        chaine += "*"
        i += 1
    return chaine

def demasqueMot(lettre, mot, masque) :
    chaine = list(masque)
    i = 0
    while i < len(mot) :
        if lettre == mot[i] :
            chaine[i] = mot[i]
        i += 1
    return "".join(chaine)

def chargeDonnees() :
    """fonction chargeant les donnees des joueurs"""
    with open("donnees", "rb") as fichier :
        mUpickler = pickle.Unpickler(fichier)
        contenue = mUpickler.load()
    return contenue

def saveDonnees(score) :
    """fonction enregistrant les donnees de joueurs"""
    with open("donnees", "wb") as fichier :
        mPickler = pickle.Pickler(fichier)
        mPickler.dump(score)

def verifPays(Vpays) :
    """fonction verifiant le pays entré"""
    res = 1
    if Vpays.capitalize() in pays :
        res = 0
    return res

def verifjoueur(joueur) :
    """fonction charger d'enregistrer de nouvaux joueurs dans le dictionaire de joueurs
    et de renvoyer le score"""
    try :
        score = donnees[joueur]
    except KeyError :
        donnees[joueur] = 0
        score = donnees[joueur]
    return score

def choixPays(joueur) :
    """foction permetant de choisir et de masquer un pays"""
    print("\n\tChoix du pays\n")
    print(joueur)
    if joueur == "CPU" :
        payC = pays[randrange(len(pays))].lower()
    else :
        payC = input("Entrez votre pays : ")
    while verifPays(payC) :
        print("Erreur : Revoyez votre orthographe")
        payC = input("Entrez votre pays : ")
    payCm = masqueMot(payC)
    i = 0
    while i < 40 :
        print("")
        i += 1
    return payC, payCm

def choixMode() :
    print("\nMODE DE JEUX")
    print("1~  Joeur VS CPU\n2~  Multijoueurs")
    mode =  input("\nchoisissez le mode de jeux : ")
    return mode

if __name__ == "__main__" :
    while 1 :
        a = input("votre pays : ")
        if verifPays(a) :
            print("{} appartient a la liste".format(a))
        else :
            print("{} n'apartient pas a la liste".format(a))


os.system("pause")