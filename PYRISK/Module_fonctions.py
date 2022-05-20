import random
from Module_variables import*

def compt_Nb_Troupes(player1):
    """
        Fonctions qui prend un joueur(Tableau) comme argument et reenvoy le nombre de troupes que
        ce joueur a
    """
    nbplayer1 = 0
    for i in player1:
        nbplayer1 += soldats[i]
    return nbplayer1
        
def veri_Frontiere(P1,P2):
    """
        Fonction qui prend 2 pays(index) comme argument et vérifie si le pays1 fait frontière
        avec pays2
    """
    return P2 in pays[P1]

def veri_Pays_Joueur(P,Joueur):
    """
        Fontion qui prend un pays(index) et un joueur et vérifie si le pays apartient au joueur
    """
    return P in Joueur

def distrib_soldats(Joueur):
    """
        Fonction qui prend un joueur(Tableau) comme argument et renvoy combien de troupe il doit recevoir
        par rapport au nb de territoires du joueur et au bonus_continent
    """
    soldats = len(Joueur)//3
    return soldats + bonus_continent(Joueur)

def capture(JoueurA,JoueurD,PD,PA):
    """
        Fonction qui prend deux joueurs(Tableaux et deux pays(Index) respectifs et qui transfère un pays d'un joueur à l'autre
    """
    JoueurA.append(PD)
    JoueurD.remove(PD)
    soldats[PD] += 1
    soldats[PA] -= 1
    
def bonus_continent(Joueur):
    """
        Fonction qui prend un joueur(Tableau) comme argument et qui renvoy quel est son bonus continent
    """
    bonus = 0
    AmeriqueN = [0,1,2,3,4,5,6,7,8]
    AmeriqueS = [9,10,11,12]
    Afrique   = [13,14,15,16,17,18]
    Europe    = [19,21,22,23,24,25,28]
    Asie      = [20,26,27,29,30,31,32,33,34,37,38,41]
    Oceanie   = [35,36,39,40]
    var = 0
    for i in range(len(AmeriqueS)):
        if AmeriqueS[i] in Joueur:
            var += 1
    if var == len(AmeriqueS):
        bonus += 2
    var = 0
    
    for i in range(len(AmeriqueN)):
        if AmeriqueN[i] in Joueur:
            var += 1
    if var == len(AmeriqueN):
        bonus += 5
    var = 0
    
    for i in range(len(Europe)):
        if Europe[i] in Joueur:
            var += 1
    if var == len(Europe):
        bonus += 5
    var = 0
    
    for i in range(len(Asie)):
        if Asie[i] in Joueur:
            var += 1
    if var == len(Asie):
        bonus += 7
    var = 0
    
    for i in range(len(Oceanie)):
        if Oceanie[i] in Joueur:
            var += 1
    if var == len(Oceanie):
        bonus += 2
    var = 0
    
    for i in range(len(Afrique)):
        if Afrique[i] in Joueur:
            var += 1
    if var == len(Afrique):
        bonus += 3
    var = 0
    
    return bonus
            
def distribution_Pays():
    """
        Fonction qui distribue les pays entre les deux joueurs aléatoirement
    """
    tab = [i for i in range(len(pays))]
    player1 = []
    for i in range(21):
        alea = random.randint(0,41-i)
        player1.append(tab[alea])
        del tab[alea]
    player2 = tab
    player1 = sorted(player1)
    return [player2,player1]

def des(PA,PD):
    """
        Fontion qui fait la bataille de dés qui prend comme argument deux pays(index) et qui modifie le tableau
        des soldats
    """
    global soldats
    V = 0
    D = 0
    if soldats[PA] > 1:
        if soldats[PA] > 2:
            TdesA = sorted([random.randint(1,6),random.randint(1,6),random.randint(1,6)],reverse=True)
        else:
            TdesA = sorted([random.randint(1,6),random.randint(1,6)],reverse=True)
        if soldats[PD] > 1:
            TdesD = sorted([random.randint(1,6),random.randint(1,6)],reverse=True)
        else:
            TdesD = [random.randint(1,6)]
        for i in range(len(TdesD)):
            if TdesD[i] >= TdesA[i]:
                D += 1
            else:
                V += 1
        soldats[PA] -= D
        soldats[PD] -= V
    
def soldats_initiaux(Joueur1,Joueur2):
    """
        Fonction qui distribu 19 soldats aléatoirement pour chaque joueur
    """
    n = 19
    while n > 0:
        var = random.choice(Joueur1)
        if not soldats[var] >= 4:
            nb_ajouté = random.randint(1,4)
            soldats[var] += nb_ajouté
            n -= nb_ajouté
    
    n = 19
    while n > 0:
        var = random.choice(Joueur2)
        if not soldats[var] >= 4:
            nb_ajouté = random.randint(1,3)
            soldats[var] += nb_ajouté
            n -= nb_ajouté
    return soldats

teri = distribution_Pays()
player1 = teri[0]
player2 = teri[1]
soldats_initiaux(player1,player2)