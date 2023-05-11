from fonction import *

print("\n\t\tB I E N V E N U E")
mode = choixMode()
while mode not in ["1", "2"] :
    print("valeur nonprix en compte")
    mode = input("Entrez votre choix : ")

if mode == "1" :
    print("\n\t\tJoueurs VS CPU")
    joueur1 = input("\nEntrez votre nom : ")
    joueur2 = "CPU"
else :
    joueur1 = input("\nEntrez le nom du joueur 1 : ")
    joueur2 = input("\nEntrez le nom du joueur 2 : ")
score1 = 0
score2 = 0
print("\n\n\t\t{}({})\t\t\t\t{}({})".format(joueur1.capitalize(), score1, joueur2.capitalize(), score2))

quitter = ""
while quitter.upper() != "Q" :
    
    pay1, pay1M = choixPays(joueur1)
    pay2, pay2M = choixPays(joueur2)
    print(joueur1, ":", pay1M, "\n")
    print(joueur2, ":", pay2M, "\n")

    while 1 :
        print("\t\t>>>>>{}<<<<<\t\t\t\t     {}".format(pay1M, pay2M), "\n")
        print(joueur2, ":", end=" ")
        if mode == "1" :
            lettre = alphabet[randrange(len(alphabet))]
            alphabet.remove(lettre)
            print(lettre)
        else :
            lettre = input()
        while len(lettre) != 1 :
            print("Veillez entrer une seulle lettre :", end=" ")
            lettre = input()
        pay1M = demasqueMot(lettre, pay1, pay1M)
        if pay1M == pay1 :
            print("\n\n\t***{}***\t\t\t{}".format(pay1, pay2))
            print("\nBravo {} !! (+1)".format(joueur2))
            score2 += 1
            break

        print("\t\t     {}     \t\t\t\t>>>>>{}<<<<<".format(pay1M, pay2M), "\n")
        print(joueur1, ":", end=" ")
        lettre = input()
        while len(lettre) != 1 :
            print("Veillez entrer une seulle lettre :", end=" ")
            lettre = input()
        pay2M = demasqueMot(lettre, pay2, pay2M)
        if pay2M == pay2 :
            print("\n\n\t   {}   ***{}***".format(pay1, pay2))
            print("\nBravo {} !! (+1)".format(joueur1))
            score1 += 1
            break

    print("\n\n\t\t{}({})\t\t{}({})".format(joueur1, score1, joueur2, score2))

    quitter = input("\nappuyez sur 'q' pour quiter\n")


os.system("pause")