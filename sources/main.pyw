########################################################
#                                                      #
# Author : Syrock                                      #
#                                                      #
# Version : 1.0                                        #
#                                                      #
########################################################

# les imports
import os, sys, sqlite3
from tkinter import *
from tkinter import ttk as ttk
from all_class import file_info
from all_class import Player
from tkinter.filedialog import *
from tkinter.messagebox import *
from checkinstall import *

# class file (permet de recuperer les infos du fichiers
file = file_info(1.0, 'Syrock', 'Application / generation de la de la fenetre et incrementations d\'elements')

# Liste des joueurs
PlayerList = []
aff_plr = []
to_destroy = []

if init() == True:
    # Configure la fenetre principale
    root = Tk()
    style = ttk.Style(root)
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth()/3 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/3 - windowHeight/2)
    root.geometry("+{}+{}".format(positionRight, positionDown))
    root.title('Dokkan Point Counter')
    root.minsize(750,500)
    root.iconbitmap(str('img/db_logo-modifier.ico'))
    root.configure(bg='#bccfd3')
    style.configure('TButton')

# Bouton de creation de joueurs
add_player = ttk.Button(root, text='Ajouter Joueur', command = lambda : [add_plr(), add_player.destroy()])

def afficher_point():
    # Chargement de variables
    global PlayerList
    
    # Création de fenêtre de points
    aff_pt = Tk()
    windowWidth = aff_pt.winfo_reqwidth()
    windowHeight = aff_pt.winfo_reqheight()
    positionRight = int(aff_pt.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(aff_pt.winfo_screenheight()/2 - windowHeight/2)
    aff_pt.geometry("+{}+{}".format(positionRight, positionDown))
    aff_pt.title('Point de la partie')
    aff_pt.iconbitmap(r'img/db_logo-modifier.ico')
    aff_pt.configure(bg='#bccfd3')
    style4 = ttk.Style(aff_pt)
    style4.configure('TButton')
    style4.configure('TLabel')
    
    # Affichage des points
    for i in range(len(PlayerList)):
        lbl = Label(aff_pt, text='Point de ' + PlayerList[i].nom + ' : ' + str(PlayerList[i].point))
        lbl.pack()

def ajouter_point(player_index, pt_to_ajt):
    """
    Ajouter les points au joueur de joueur_index
    
    param player_index:(int) index du joueur
    """
    # Chargement de variables
    global PlayerList
    
    # Modifier les points du joueur
    PlayerList[player_index].modifier_point(PlayerList[player_index].point + pt_to_ajt)
    print(PlayerList[player_index].point)

def GUI_point(player_index):
    """
    Ajouter les points au joueur concerne
    
    param player:(int) L'indice du joueur dans la liste PlayerList
    """
    # Chargement de variables
    global PlayerList
    
    # Création de fenêtre de points
    ptGUI = Tk()
    windowWidth = ptGUI.winfo_reqwidth()
    windowHeight = ptGUI.winfo_reqheight()
    positionRight = int(ptGUI.winfo_screenwidth()/2.15 - windowWidth/2)
    positionDown = int(ptGUI.winfo_screenheight()/2 - windowHeight/2)
    ptGUI.geometry("+{}+{}".format(positionRight, positionDown))
    ptGUI.title('Ajouter des points a ' + PlayerList[player_index].afficher_nom())
    ptGUI.iconbitmap(r'img/db_logo-modifier.ico')
    ptGUI.configure(bg='#bccfd3')
    style3 = ttk.Style(ptGUI)
    style3.configure('TButton')
    style3.configure('TLabel')
    
    # Creation des widgets
    lbl = Label(ptGUI, text='Combien de points souhaiter vous ajouter a ' + PlayerList[player_index].afficher_nom(), background='#bccfd3')
    lbl.pack()
    nbr_ptr = StringVar()
    ptEntry = ttk.Entry(ptGUI, text=nbr_ptr)
    ptEntry.pack()
    btn = ttk.Button(ptGUI, text='Envoyer les points', command=lambda : [ajouter_point(player_index, int(ptEntry.get())), ptGUI.destroy()])
    btn.pack()

def Widgets(level):
    """
    Permet d'ajouter recursivement des wigets
    """
    global PlayerList
    if level != len(PlayerList):
        lbl = Label(root, text='Joueur : ' + PlayerList[level].nom, background='#bccfd3')
        lbl.pack()
        to_destroy.append(lbl)
        btn = ttk.Button(root, text='Ajouter des points', command=lambda : [GUI_point(level)]) # Probleme i change donc pas meme valeur envoye
        btn.pack()
        to_destroy.append(btn)
        to_destroy.append(lbl)
        Widgets(level+1)
        
def launch():
    """
    Permet d'initialier le jeu
    """
    # Chargement des variables
    global aff_plr
    global PlayerList
    
    # Suppression des elments inutiles
    while aff_plr != []:
        aff_plr[0].destroy()
        aff_plr.remove(aff_plr[0])
    
    end = fileMenu.index('Quit')
    for i in range(end + 1):
        fileMenu.delete(0)
    fileMenu.add_command(label='Save', command=Save, underline=0)
    fileMenu.add_separator()
    fileMenu.add_command(label='Quit', command= root.destroy, underline=0)
    Widgets(0)
    
    skipline = Label(root, text='\n', background='#bccfd3')
    skipline.pack()
    aff_btn = ttk.Button(root, text='Afficher les points', command=lambda : [afficher_point()])
    aff_btn.pack()

def ajt_plr_frm_open(name):
    """
    Creer le joueur et l'affiche sur root
    
    param name:(str) le nom du joueur
    """
    
    # Chargement de variables
    global aff_plr
    
    # Ajout de widgets
    lbl = ttk.Label(root, text='Joueur : ' + str(name), background='#bccfd3')
    lbl.pack()
    aff_plr.append(lbl)

def ajt_plr(name):
    """
    Creer le joueur et l'affiche sur root
    
    param name:(str) le nom du joueur
    """    
    # Chargement de variables
    global aff_plr
    
    # Ajout de widgets
    PlayerList.append(Player(name))
    lbl = ttk.Label(root, text='Joueur : ' + str(name), background='#bccfd3')
    lbl.pack()
    aff_plr.append(lbl)
    add_player = ttk.Button(root, text='Ajouter Joueur', command = lambda : [add_plr(), add_player.destroy(), start_game.destroy(), skipline.destroy()])
    add_player.pack()
    skipline = Label(root, text='\n', background='#bccfd3')
    skipline.pack()
    start_game = ttk.Button(root, text='Commencer le jeu', command = lambda : [launch(), add_player.destroy(), skipline.destroy(), start_game.destroy()])
    start_game.pack()

def add_plr():
    """
    Permet de creer la fenetre d'ajout de joueur
    """    
    # Configuration de la fenetre de creation de joueur
    plrGUI = Tk()
    windowWidth = plrGUI.winfo_reqwidth()
    windowHeight = plrGUI.winfo_reqheight()
    positionRight = int(plrGUI.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(plrGUI.winfo_screenheight()/2 - windowHeight/2)
    plrGUI.geometry("+{}+{}".format(positionRight, positionDown))
    plrGUI.title('Ajouter un joueur')
    plrGUI.iconbitmap(r'img/db_logo-modifier.ico')
    plrGUI.configure(bg='#bccfd3')
    style2 = ttk.Style(plrGUI)
    style2.configure('TButton')
    style2.configure('TLabel')
    
    # Ajouter les widgets
    namevar = StringVar()
    lbl = ttk.Label(plrGUI, text='Nom du joueur :', background='#bccfd3')
    lbl.pack()
    nameEntry = ttk.Entry(plrGUI, text=namevar)
    nameEntry.pack()
    SendName = ttk.Button(plrGUI, text='Ajouter le Joueur', command=lambda : [ajt_plr(nameEntry.get()), plrGUI.destroy()])
    SendName.pack()

def initEntry():
    """
    Initilise le bouton de creation de joueur
    """
    global add_player
    a = add_player
    a.pack()

# Lancement automatique (seras remplacer par main)
initEntry()

def winner():
    """
    Compare les points et determine le vainqueur
    """
    # Chargement des variables
    global PlayerList
    vainq_index = 0
    
    # Comparer les points
    for elt in PlayerList:
        if PlayerList[vainq_index].point < elt.point:
            vainq_index = PlayerList.index(elt)
            
    PlayerList[vainq_index].modifier_win(PlayerList[vainq_index].nbr_win + 1)
            

def Save():
    """
    Permet de sauvegarder la partie via un fichier db.
    ~~ ATTENTION ! Le programme ne sauvegarde que la personne qui a le plus de points, ine ne sauvegarde pas le nombre de points !
    ~~ ATTENTION ! Le programme se ferme a l'issue de la sauvegarde !
    """
    #Chargement de variables
    global PlayerList
    
    # Demande le lien d'enregistrement
    save_link = asksaveasfile(title='Save the game (.db)', filetypes=[("Base de données", ".db")], initialdir='../save')
    save_link.close()
    os.remove(save_link.name)
    save_link = save_link.name
    save_link = save_link + '.db'
    
    #Verifier que le fichier existe pas
    if os.path.exists(save_link) == False:
        
        # Se connecter au fichier
        con = sqlite3.connect(save_link)
        cur = con.cursor()
    
        # Creer la table
        cur.execute('''CREATE TABLE Players (id INT PRIMARY KEY, nom TEXT, win INT)''')
    
        # Determiner vainqueur(s)
        winner()
    
        # Ajouter les valeurs de sauvegardes
        for elt in PlayerList:
            cur.execute('INSERT INTO Players VALUES (' + str(PlayerList.index(elt)) + ', \'' + str(elt.nom) + '\', ' + str(elt.nbr_win) + ''')''')
     
        con.commit()
        con.close()
        
    else:
        
        os.remove(save_link)
        
        # Se connecter au fichier .db
        con = sqlite3.connect(save_link)
        cur = con.cursor()
        
        # Modifier les valeurs existantes
        for elt in PlayerList:
            cur.execute('UPDATE Players SET win = ' + str(elt.nbr_win) + ' WHERE nom IS TEXT')
            
        # Enregistrer et fermer la base db
        con.commit()
        con.close()
        
    os.rename(save_link, save_link[:-6])
    root.destroy()

def ShowAbout():
    """
    Affiche les infos du programme
    """
    f = open('../Info.txt', 'r')
    extract = f.read()
    f.close()
    showinfo(title='Informations', message=extract)

def Open():
    """
    Permet d'ouvrir une sauvegarde via un fichier .db (database)
    """
    # Demande ou ce trouve le fichier db
    save_link = askopenfilename(title='Choose your save file', filetypes=[("Tout les fichiers", "*")], initialdir='../save')
    print(save_link)
    os.rename(save_link, save_link + '.db')
    save_link = save_link + '.db'
    
    # Supprime le bouton Open de filemenu
    fileMenu.delete('Open')
    
    # Se connecte au fichier db
    con = sqlite3.connect(save_link)
    cur = con.cursor()
    
    # Chargement de la variable PlayerList
    global PlayerList
    
    # Ajouter chaque joueur contenue dans le fichier db
    for row in cur.execute('''SELECT nom, win FROM Players'''):
        PlayerList.append(Player(row[0], nbr_win=row[1]))
        ajt_plr_frm_open(row[0])
    
    # Creer le bouton pour lancer le jeu
    start_game = ttk.Button(root, text='Commencer le jeu', command = lambda : [launch(), start_game.destroy()])
    start_game.pack()
    add_player.destroy()

menuBar = Menu(root)
root['menu'] = menuBar
fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='File', menu = fileMenu)
fileMenu.add_command(label='Open', command=Open, underline=0)
fileMenu.add_separator()
fileMenu.add_command(label='Quit', command= root.destroy, underline=0)
helpMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='About', menu = helpMenu)
helpMenu.add_command(label='Help', underline=0)
helpMenu.add_command(label='About', command= ShowAbout, underline=0)

root.mainloop()