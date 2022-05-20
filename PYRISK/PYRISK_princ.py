import tkinter as tk
from PIL import ImageTk
from Module_variables import *
from Module_fonctions import *

def couleur_pays(player1,player2,button):
    """
        Changement des couleurs des boutons en fonction des pays de chaque joueur qui prend en argument les deux joueurs et la
        liste de bouton
    """
    for i in range(len(player1)):
        button[player1[i]].configure(bg ="#ff0921",activebackground = "#ff0921", )
    for j in range(len(player2)):
        button[player2[j]].configure(bg ="#65ff2d", activebackground = "#65ff2d")

def incr(indexp,a):
    """
        Incrémentation des troupes sur chaque boutons de pays
    """
    if indexp in a[player_in_turn]:
        if player_nbr_troupes[player_in_turn]>0:
            soldats[indexp] += 1
            troupe[indexp].set(str(soldats[indexp]))
            player_nbr_troupes[player_in_turn]-=1
            troupe_txt.configure(text = player_nbr_troupes[player_in_turn])

troupe = []

def lancer_partie():
    """
        Fonction associé au bouton lancer partie qui va créer les boutons de tous les pays et afficher le nombre de troupes
        dans le bouton du pays. Il va changer la commande du bouton lancer_partie pour lancer la fonction couleur_pays
        
    """
    soldats_initiaux(player1,player2)
    player_in_turn = 0
    player_nbr_troupes[player_in_turn] = distrib_soldats(player1)
    for i in range(len(soldats)):
        troupe.append(tk.StringVar())
        troupe[i].set(soldats[i])
    for i in range(len(button_coord)):
        button_incr.append(tk.Button(root, textvariable=troupe[i], command = lambda i=i: incr(i,teri), width = 5))#Création des boutons des pays
        button_fen1.append(canvas.create_window(button_coord[i][0], button_coord[i][1], anchor='nw', window=button_incr[i]))
    button_lp.configure(command = couleur_pays(player1,player2,button_incr))
    button_lp.destroy() #On supprime le bouton lancer partie
    troupe_win = canvas.create_window([250,900], window = troupe_txt)
    troupe_txt.configure(text = player_nbr_troupes[player_in_turn])
    button_ta_win = canvas.create_window([650,900], window = button_ta) #Crée l'autre bouton

def t_suivant():
    """
        Fonction de changement de tour qui va changer le player_in_turn pour changer le joueur qui va changer
    """
    global player_in_turn, button_att
    if player_in_turn == 0 :
        player_in_turn = 1
        player_nbr_troupes[player_in_turn] = distrib_soldats(player2)
    else :
        player_in_turn = 0
        player_nbr_troupes[player_in_turn] = distrib_soldats(player1)
    for i in button_att :
        i.destroy()
    button_att = []
    button_fen2 = []
    for i in range(len(button_coord)):
        button_incr.append(tk.Button(root, textvariable=troupe[i], command = lambda i=i: incr(i,teri), width = 5))#Création des boutons des pays
        button_fen1.append(canvas.create_window(button_coord[i][0], button_coord[i][1], anchor='nw', window=button_incr[i]))
    for i in range(len(player1)):
        button_incr[player1[i]].configure(bg ="#ff0921",activebackground = "#ff0921", )
    for j in range(len(player2)):
        button_incr[player2[j]].configure(bg ="#65ff2d", activebackground = "#65ff2d")
    button_ts.destroy()
    button_ts_win = 0
    button_ta = tk.Button(root, text = "TOUR D'ATTAQUE", command = t_attaque, width = 20)
    button_ta_win = canvas.create_window([650,900], window = button_ta)
    troupe_txt.configure(text = player_nbr_troupes[player_in_turn])
    
def t_attaque():
    """
        Fonction associe au bouton tour d'attaque qui va créer et afficher les boutons qui vont permettre d'attaquer et
        cacher les boutons associés à la fonction incrémenter
        
    """
    global button_incr
    for i in button_incr :
        i.destroy()
    button_incr = []
    button_fen1 = []
    for i in range(len(button_coord)):
        button_att.append(tk.Button(root, textvariable=troupe[i], command = lambda i=i: att(i,teri), width = 5))#Création des boutons des pays
        button_fen2.append(canvas.create_window(button_coord[i][0], button_coord[i][1], anchor='nw', window=button_att[i]))
    for i in range(len(player1)):
        button_att[player1[i]].configure(bg ="#ff0921",activebackground = "#ff0921", )
    for j in range(len(player2)):
        button_att[player2[j]].configure(bg ="#65ff2d", activebackground = "#65ff2d")
    button_ta.destroy()
    button_ta_win = 0
    button_ts = tk.Button(root, text = "TOUR SUIVANT", command = t_suivant, width = 20)
    button_ts_win = canvas.create_window([650,900], window = button_ts)
    
def att(indexp,pays):
    """
        Fontion associé aux boutons attaque qui va vérifier le player in turn qu va vérifier si le bouton cliqué nous appartient
        qui va garder en paramètre puis si le nouveau bouton cliqué est frontalier au bouton d'avant va lancer le "combat"
        puis si le bouton defenseur n'a plus de troupe on transfere 1 troupe de notre pays dans le nouveau.
    """
    global paysA,paysD
    if player_in_turn == 0:
        player_adv = 1
    else:
        player_adv = 0
    if indexp in pays[player_in_turn]:
        paysA = indexp
        pays_com_fen = canvas.create_window([950,900], window = pays_com)
        pays_com.configure(text = paysA)
        print("paysA", paysA)
    if not paysA == -1:
        if not indexp in pays[player_in_turn]:
            paysD = indexp
            print("paysD", paysD)
    if soldats[paysA] > 1:
        if not paysA == -1 and not paysD == -1:
            if veri_Frontiere(paysA,paysD) == True:
                des(paysA,paysD)
                troupe[paysA].set(str(soldats[paysA]))
                troupe[paysD].set(str(soldats[paysD]))
    if soldats[paysD] == 0:
        capture(teri[player_in_turn],teri[player_adv],paysD,paysA)
        if player_in_turn == 1:
            button_att[paysD].configure(bg ="#65ff2d",activebackground = "#65ff2d")
        else:
            button_att[paysD].configure(bg ="#ff0921",activebackground = "#ff0921", )
        troupe[paysA].set(str(soldats[paysA]))
        troupe[paysD].set(str(soldats[paysD]))
        paysD = 0
    
root = tk.Tk()
root.title("RISK")

canvas = tk.Canvas(root, width=1360, height=980, bg = "#4682B4") #Création de la fenêtre
canvas.pack()

tk_img = ImageTk.PhotoImage(file = 'image/risk.png') #Création de la fenêtre de l'image
canvas.create_image(600, 400, image=tk_img)

button_lp = tk.Button(root, text = "LANCER PARTIE", command = lancer_partie, width = 20) #Création du bouton lancer partie
button_lp_win = canvas.create_window([650,900], window=button_lp)

button_ta = tk.Button(root, text = "TOUR D'ATTAQUE", command = t_attaque, width = 20)#Création du bouton tour d'attaque

button_ts = tk.Button(root, text = "TOUR SUIVANT", command = t_suivant, width = 20)#Création du bouton tour suivant

troupe_txt = tk.Label(root, width = 5)

pays_com = tk.Label(root, width = 10)

root.iconbitmap(r"image/logo.ico")

root.mainloop()
