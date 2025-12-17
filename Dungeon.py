import random as rm, keyboard, time

niveau = 1

def personnage_user():
    choix = "default"
    pv = 0
    strengh = 0
    ok = False
    nom = input("Comment s'appelle votre personnage : ")
    classes = ["assassin", "archer", "guerrier", "mage"]
    print("""Voici la liste de classes de départ : ["Assassin", "Archer", "Guerrier", "Mage"]""")
    while ok != True :
        choix = str(input("Choisissez une classe : "))
        choix = choix.lower()
        if choix in classes : 
            ok = True
        else : 
            print("Choix invalide")
    caractéristiques = {"assassin" : {"pv_max" : 20, "pv" : 20, "strengh" : 14, "mana_max" : 8, "mana" : 8 }, 
                        "archer" : {"pv_max" : 26, "pv" : 26, "strengh" : 10, "mana_max" : 15, "mana" : 15 }, 
                        "guerrier" : {"pv_max" : 34, "pv" : 32, "strengh" : 8, "mana_max" : 12, "mana" : 12}, 
                        "mage" : {"pv_max" : 12, "pv" : 12, "strengh" : 20, "mana_max" : 20, "mana" : 20}}
    print(f"Ton personnage {nom} est un {choix} de niveau {niveau} avec {caractéristiques[choix]["pv"]} PV, un niveau de force de {caractéristiques[choix]["strengh"]} et un mana de {caractéristiques[choix]["mana"]}.")
    return nom, choix, niveau, caractéristiques[choix]["pv_max"], caractéristiques[choix]["pv"], caractéristiques[choix]["strengh"], caractéristiques[choix]["mana_max"], caractéristiques[choix]["mana"]

def premier_combat():
    global niveau
    pv_monstre = 10
    coup = rm.randint(5, 15)
    if pv_monstre - coup <= 0 :
        print("Squelette vaincu !")
        niveau += 1 
        print("Nouveau niveau atteint, niveau :", niveau,".")
    else :
        print("Le squelette se moque de toi...")

def combat_golem():
    ok = False
    pv_joueur = 20
    pv_golem = 50
    print("Votre personnage est monté de niveau : Niveau 18")
    print("Vous avez débloqué trois sorts : Coup d'épée, Lancer de dague, Boule de feu.")
    print("0 : Coup d'épée --> 10-14 dégâts.")
    print("1 : Lancer de dague --> 2-22 dégâts.")
    print("2 : Boule de feu --> 0/20 dégâts.")
    Compétences = {0 : rm.randint(10, 14), 1 : rm.randint(2, 22), 2 : {0, 20}} 
    print("Le combat commence.")
    while pv_golem > 0 and pv_joueur > 0 :
        ok = False
        while ok != True :
            attaque = int(input("Choisissez votre compétence à lancer à partir de son numéro :"))
            if attaque in [0, 1, 2] : 
                ok = True
            else : 
                print("Choix invalide") 
        if attaque != 2 :
            dégâts = Compétences[attaque]
        else : 
            dégâts = rm.choice(list(Compétences[attaque]))
        print(f"Vous infligez {dégâts} de dégâts au golem")
        pv_golem -= dégâts
        print(f"PV_Golem : {pv_golem}.")
        if pv_golem < 0 :
            print("Vous avez battu le golem bravo !")
            return pv_golem
        print("Le golem vous attaque !")
        pv_joueur -= 7
        print("Vous perdez 7 pv.")
        if pv_joueur < 0 :
            print("Vous avez perdu...")
            return pv_joueur
        print(f"PV_Joueur : {pv_joueur}")
        if pv_golem > 0 :
            print("Le combat continu")
    if pv_golem < 0 :
        print("Bravo continué au prochain niveau.")
    else :
        print("Recommencez une partie.")

def inventaire() :
    liste=["Potion de soin", "Potion de mana", "Pièce d'or"]
    print("Un mystérieux coffre apparaît devant vous : ")
    choix = input("Voulez-vous l'ouvrir ? yes/no ")
    if choix.lower() == "yes" :
        print("Le coffre est protégée par un code magique (un nombre aléatoire de 1 à 20 inclus) :")
        print("Vous avez trois essais pour trouver le bon numéro ou chiffre.")
        code = rm.randint(1, 20)
        for i in range(4) :
            if i >= 3 :
                print("Vous n'avez pas réussi.")
                print("Le coffre mange votre or.")
                liste.remove("Pièce d'or")
                break
            choix = int(input("Faites un choix : "))
            if choix == code :
                print("Vous obtenez l'arme ultime.")
                épée = input("La récupérer dans votre inventaire ? yes/no ")
                if épée.lower() == "yes" :
                    liste.append("Arme ultime")
                    print("Vous obtenez 'Arme ultime")
                    break
                else :
                    print("Une opportunité vous glisse entre les mains.")
                    break
            elif choix > code :
                print("Vous visez trop haut.")
            else :
                print("Vous visez trop bas.")
    else :
        print("Vous avancez plus loin.")
    print("Sur votre chemin en continuant un groupe de monstre apparaît.")
    print("Vous êtes bléssé.")
    soin = input("Utiliser la potion de soin ? yes/no ")
    if soin.lower() == "yes" :
        liste.pop(0)
        print("Vous restauré totalement vos pv.")
        print("Vous réussissez à battre les monstres.")
    else :
        if "Arme ultime" in liste :
            print("Grâce à l'arme ultime vous réussissez bien que difficilement à passer cettte épreuve.")
        else :
            print("Vous succombez aux mains des monstres.")
            print("C'est la fin...")
            return print("Liste_final :", liste)
    print("Vous sortez du donjon, soyez fier de votre avancée.")
    print("Voyez votre inventaire et ce à quoi ont amené vos choix :")
    print("Liste final :", liste)

def calcul_degats(force=0, Arme=0):
    n, force = personnage_user()
    print("Votre force est de :", force)
    print("Les dégâts se calculent de la façon suivante :")
    print("Dégâts : Force + Dégâts_Arme")
    print("Quel est la puissance de votre arme ?")
    print("Ne soyez pas trop cupide.")
    print("Car au dessus d'une cetaine valeur le calcul de dégâts devient une soustraction")
    Arme = int(input("Puissance Arme : "))
    if Arme > 15 :
        calcul_degats = force - Arme
    else : 
        calcul_degats = force + Arme
    if calcul_degats >= 0:
        print(f"Votre personnage {n} peut infliger {calcul_degats} de dégâts.")
    else :
        soin = calcul_degats * -1
        print(f"Votre personnage {n} soigne les ennemais de {soin} pv en les frappant...")






combat = False 

nom, choix, niveau, pv_max, pv, force, mana_max, mana = personnage_user()

pv_monstre = 10

monstre = "Squelette"

arme = False

def donjon():
    global combat, nom, choix, niveau, pv_max, pv, force, mana_max,mana
    global pv_monstre
    global sac
    global monstre
    print("Votre aventure commence.")
    touches()
    print("\nVous entrez dans un donjon sombre et profond.")
    time.sleep(2)
    print("Cela n'a pas l'air de bonne augure.")
    time.sleep(2)
    print("Vous sentez quelque chose vous frôle...")
    time.sleep(1)
    print("""
          Combat contre un squelette !""")
    combat = True
    print(f"{monstre} --> PV : {pv_monstre}")
    touches()
    while pv_monstre > 0 :
        print("Le squelette attaque.")
        print("Vous perdez 7 pv")
        pv -= 7
        if pv <= 0 :
            return print("Le joueur est mort...")
        print("PV Joueur :", pv)
        touches()
    print("\nVous avez vaincu le squelette.")
    print("Vous gagnez de l'expérience.")
    niveau += 1
    print ("Niveau :", niveau)
    pv += pv_max * 0.2
    pv_max += pv_max * 0.2
    print("Vos pv augmentent.")
    time.sleep(1)
    print("Votre attaque augmente.")
    combat = False
    time.sleep(2)
    print("Vous continuez d'avancer dans le donjon.")
    time.sleep(2)
    print("Des lumières s'allument au fur et à mesure de votre avancée.")
    time.sleep(2)
    print("Vous tombez nez à nez face à une porte.")
    time.sleep(2)
    print("Elle semble assez vieille et ne s'ouvrira pas facilement.")
    time.sleep(2)
    print("Il y a un code à deux chiffres à trouver sur le cadenas dessus.")
    time.sleep(1)
    liste_porte = list(range(100))
    imminent = 0
    code_porte = rm.randint(0, 99)
    réponse = nombre("Code du cadenas : ")
    if réponse not in liste_porte :
        print("Vous êtes idiots ??")
        imminent += 1
    if réponse == code_porte :
            print("La porte s'ouvre.")
    if réponse in liste_porte and réponse != code_porte :
        print("Mauvais code.")
        print("Retentez")
        imminent += 1
    if réponse != code_porte :
        while réponse != code_porte :
            réponse = nombre("Code du cadenas : ")
            if réponse not in liste_porte :
                print("Vous êtes idiots ??")
            if réponse in liste_porte and réponse != code_porte and imminent < 49 :
                print("Mauvais code.")
                print("Retentez")
            if réponse == code_porte and imminent < 20 :
                time.sleep(1)
                print("La porte s'ouvre.")
                break
            if réponse == code_porte and imminent >= 20 :
                time.sleep(1)
                print("La porte s'ouvre.")
                time.sleep(2)
                print("Vous avez réussi à échapper à l'obscurité.")
                break
            imminent += 1
            if imminent == 10 :
                print("Vous vous retournez et vous apercevez que la pièce s'assombrit.")
            if imminent == 20 :
                print("La légère obscurité de la pièce commence à laisser place à des ténèbres.")
            if imminent == 30 :
                print("Les ténèbres se rapprochent de plus en plus vite.")
            if imminent == 40 :
                print("Les ténèbres ont conquis la pièce.")
                time.sleep(2)
                print("Vous commencez à perdre l'esprit.")
            if imminent == 50 :
                print("Les ténèbres vous engloutissent.")
                time.sleep(1)
                print("Le joueur est mort...")
                return
    time.sleep(2)
    print("\nVous entrez dans une nouvelle pièce.")
    time.sleep(2)
    print("Vous voyez une épée sur un piédestal.")
    prendre = input("Voulez-vous la prendre ? yes/no ")
    if prendre != "yes" and prendre != "no" :
        while prendre != "yes" and prendre != "no" :
            print("Choix Invalide")
            prendre = input("Voulez-vous la prendre ? yes/no ")
    if prendre == "yes" :
        print("Vous obtenez l'arme ultime.")
        print("L'arme ultime est ajoutée à votre inventaire.")
        sac["Arme ultime"] = "équipement"
    if prendre == "no" :
        print("Vous passez votre chemin")
    time.sleep(2)
    touches()
    monstre = "Golem"
    pv_monstre = 50
    print("\nEn cherchant un peu plus dans la pièce vous vous apercevez qu'il y a un passage étroit.")
    time.sleep(2)
    print("Vous forcez votre chemin à travers.")
    time.sleep(2)
    print("Vous tombez dans une salle remplie de rien d'autre que de pierres.")
    time.sleep(2)
    print("En regardant un peu mieux vous voyez une salle au trésor.")
    time.sleep(1)
    print("Vous avancez vers elle.")
    time.sleep(0.5)
    print("De plus en plus vite.")
    touches()
    print("\nLes pierres commencent à bouger, mais ce n'était pas des pierres..")
    time.sleep(2)
    print("""
          Combat contre le Boss : Golem !""")
    combat = True
    print(f"{monstre} --> PV : {pv_monstre}")
    touches()
    while pv_monstre > 0 :
        espoir = rm.randint(1, 10)
        print("Le Golem attaque.")
        if espoir == 1 or espoir == 2 :
            time.sleep(1)
            print("Le golem rate son attaque.")
        elif espoir == 10 : 
            time.sleep(1)
            print("Le Golem lance son attaque spéciale.")
            print("Vous perdez 10 pv")
            pv -= 10
        else :
            print("Vous perdez 7 pv")
            pv -= 7
        if pv <= 0 :
            return print("Le joueur est mort...")
        print("PV Joueur :", pv)
        touches()
    print("Le Golem est vaincu.")
    time.sleep(1)
    print("La salle aux trésors est à vous.")
    time.sleep(1)
    print("Félicitaions vous avez terminé le donjon.")
    print("")
    print("")
    print("""Crédits \n
          \n
        Créateur du jeu : Alexandre Caré""")


        
def nombre(message):
    try :
        return int(input(message))
    except ValueError:
        print("Vous êtes idiots ??")

def touches():
    global combat
    ot = True
    if combat == False :
        print(""" 
        Touches : \n
        'I : Inventaire'\n
        'C : Continuer'""")
        while ot == True :
            if keyboard.is_pressed("c") :
                ot = False
            if keyboard.is_pressed("i") :
                return invent()
    else :
        print(""" 
        Touches : \n
        'I : Inventaire'\n
        'C : Capacités'\n
        'N : Ne rien faire'""")
        while ot == True :
            if keyboard.is_pressed("i") :
                return invent()
            if keyboard.is_pressed("c"):
                return capacités()
            if keyboard.is_pressed('n') :
                print("\nVous ne faites rien.")
                ot = False
                time.sleep(0.2)

sac = {"Potion de soin" : "consommable", "Potion de mana" : "consommable", "Pièce d'or" : "monnaie"}

def invent() :
    global combat
    global sac
    global arme
    oi = True
    if combat == False :
        print("""
        Touches : \n
        'T : Afficher la taille de l'inventaire.'\n
        'U : Utiliser un consommable.'\n
        'A : Afficher l'inventaire.'\n
        'E : Équiper une arme'\n
        'Q : Quitter l'inventaire.'""")
        while oi == True :
            if keyboard.is_pressed("t") :
                print (f"""
                Votre inventaire fait {len(sac)} de taille.""")
                time.sleep(1)
                return invent()
            if keyboard.is_pressed('u') :
                return utiliser()
            if keyboard.is_pressed('a') :
                print("""
                      Inventaire : """, sac)
                time.sleep(1)
                return invent()
            if keyboard.is_pressed('e') :
                if arme == True :
                    time.sleep(1)
                    print("""
                          L'arme ultime est déjà équipée.""")
                    return invent()
                if "Arme ultime" in sac :
                    arme = True
                    print("""
                          L'arme ultime a été équipée""")
                    del sac["Arme ultime"]
                    time.sleep(1) 
                    return invent()
                else :
                    print("""
                          Aucune arme ne peut être équipée.""")
                    time.sleep(1)
                    return invent()
            if keyboard.is_pressed('q'):
                return touches()
    if combat == True :
        print("""
        Touches : \n
        'U : Utiliser un consommable.'\n
        'A : Afficher l'inventaire.'\n
        'Q : Quitter l'inventaire.'""")
        while oi == True :
            if keyboard.is_pressed('u') : 
                return utiliser()
            if keyboard.is_pressed('a') :
                print("""
                      Inventaire : """, sac)
                time.sleep(1)
                return invent()
            if keyboard.is_pressed('q'):
                return touches()
            
def utiliser() :
    global sac, pv_max, pv, mana_max, mana
    consommable = {}
    i = 0
    for cle, value in sac.items() :
        if value == "consommable" :
            consommable[str(i)] = cle
            i += 1
    continuer = input("""
                      Continuer ? yes/no """)
    if continuer == "yes" :
        print("\nVoici vos consommables:", consommable)
        choix = input("Que souhaitez vous utiliser : ")
        if choix not in consommable :
            print("Rentrez une valeur correcte.")
            return utiliser()
        if consommable[choix] == "Potion de soin" and pv_max != pv :
            if pv + 8 > pv_max :
                pv = pv_max
                print("Vous récupérez des pv.")
                print("PV Joueur :", pv)
            else :
                pv += 8
                print("Vous récupérez des pv.")
                print("PV Joueur :", pv)
            del sac["Potion de soin"]
            return utiliser()
        elif consommable[choix] == "Potion de soin" and pv == pv_max :
            print("Vos pv sont full.")
            return utiliser()
        if consommable[choix] == "Potion de mana" and mana_max != mana :
            if mana + 8 > mana_max :
                mana = mana_max
                print("Vous récupérez du mana.")
                print("Mana Joueur :", mana)
            else :
                mana += 8
                print("Vous récupérez du mana.")
                print("Mana Joueur :", mana)
            del sac["Potion de mana"]
            return utiliser()
        elif consommable[choix] == "Potion de mana" and mana_max == mana :
            print("Votre mana est full.") 
            return utiliser() 
    elif continuer == "no" :
        return invent()
    else :
        print("Rentrez un choix valide.")
        return utiliser()
    
def capacités() :
    nono = True
    global arme
    global pv_monstre
    global force, niveau, choix, mana
    global monstre
    if arme == False :
        calcul_degats_user = force * 0.5 * niveau
    else :
        calcul_degats_user = force * 0.5 * niveau * 1.2
    print("""
        Touches : \n
        'N : Capacité normal'\n
        'S : Capacité spéciale'\n
        'A : Annuler'""")
    while nono == True :
        if keyboard.is_pressed('n') :
            print ("\nCoup Simple !")
            time.sleep(1)
            pv_monstre -= calcul_degats_user
            if pv_monstre < 0 :
                print(f"PV {monstre} : 0")
                return
            print(f"PV {monstre} : ", pv_monstre)
            time.sleep(1)
            return
        if keyboard.is_pressed('s') and mana >= 5 :
            print("\nCoup Spécial !")
            print("Vous perdez 5 de mana")
            mana -= 5
            time.sleep(0.5)
            print("Mana Joueur : ", mana)
            time.sleep(1)
            chance = rm.randint(0, 2)
            pv_monstre -= calcul_degats_user * chance
            if chance == 0 :
                print("Le coup a échoué.")
                time.sleep(1)
                return
            elif chance == 2 :
                print("Coup critique !")
                time.sleep(1)
                if pv_monstre < 0 :
                    print(f"PV {monstre} : 0")
                    return
                print(f"PV {monstre} : ", pv_monstre)
                time.sleep(1)
                return
            if pv_monstre < 0 :
                print(f"PV {monstre} : 0")
                return
            print(f"PV {monstre} : ", pv_monstre)
            time.sleep(1)
            return
        elif keyboard.is_pressed('s') and mana < 5 :
            print("\nPas assez de mana.")
            return capacités()
        if keyboard.is_pressed("a") :
            return touches()

donjon()

time.sleep(2)
input("\n\nAppuyer sur entrée pour fermer la console...")