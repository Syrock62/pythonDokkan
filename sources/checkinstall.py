########################################################
#                                                      #
# Author : Syrock                                      #
#                                                      #
# Version : 1.0                                        #
#                                                      #
########################################################

import os
import requests
from datetime import datetime

def dw_cr_file_folder(liste_dwl, liste_folder):
    """
    Permet de retelecharger les fichier demade dans la liste_dwl
    et de recreer les dossiers demander dans la liste_folder
    
    param liste_dwl: (list) liste des elements a telecharge
    param liste_folder: (list) liste des dossier a creer
    return: (bool) True si réussi, False sinon
    """
    
    # Déclaration des variables
    elt = ""
    cpliste_file = []
    cpliste_folder = []
    
    # Copie de la liste des fichiers
    if liste_dwl != []:
        for i in range(len(liste_dwl)):
            cpliste_file.append(liste_dwl[i])
                
    # Copie de la liste des folders
    if liste_folder != []:
        for i in range(len(liste_folder)):
            cpliste_folder.append(liste_folder[i])
    
    # Réparation fichiers et des dossiers
    for elt in cpliste_folder:
        if elt == "save":
            os.mkdir('../save')
            cpliste_folder = cpliste_folder.remove(elt)
            if cpliste_folder == None:
                cpliste_folder = []
        
        if elt == 'img':
            os.mkdir('img')
            cpliste_folder = cpliste_folder.remove(elt)
            if cpliste_folder == None:
                cpliste_folder = []
                
    for elt in cpliste_file:        
        if elt == "Programme.exe.lnk":
            url = "https://raw.githubusercontent.com/Syrock62/pythonDokkan/main/Progamme.exe.lnk"
            directory = "../Programme.exe.lnk"
            r = requests.get(url)
            f = open(directory, 'wb')
            f.write(r.content)
            cpliste_file = cpliste_file.remove(elt)
            if cpliste_file == None:
                cpliste_file = []
        
        if elt == "README.md":
            url = "https://raw.githubusercontent.com/Syrock62/pythonDokkan/main/README.md"
            directory = '../README.md'
            r = requests.get(url)
            f = open(directory, 'w')
            f.write(r.text)
            cpliste_file = cpliste_file.remove(elt)
            if cpliste_file == None:
                cpliste_file = []
        
        if elt == "all_class.py":
            url = "https://raw.githubusercontent.com/Syrock62/pythonDokkan/main/sources/all_class.py"
            directory = 'all_class.py'
            r = requests.get(url)
            f = open(directory, 'w')
            f.write(r.text)
            cpliste_file = cpliste_file.remove(elt)
            if cpliste_file == None:
                cpliste_file = []
                
        if elt == 'db_logo-modifier.ico':
            url = "https://raw.githubusercontent.com/Syrock62/pythonDokkan/main/sources/img/db_logo-modifier.ico"
            directory = 'img/db_logo-modifier.ico'
            r = requests.get(url)
            f = open(directory, 'wb')
            f.write(r.content)
            cpliste_file = cpliste_file.remove(elt)
            if cpliste_file == None:
                cpliste_file = []
    
    # Réparation Folder
    for i in range(len(liste_folder)):
        elt = liste_folder
        
    # Sortie
    print(cpliste_file, cpliste_folder)
    if cpliste_file == []:
        if cpliste_folder == []:
            print(True)
            return True
    else:
        print(False)
        return False
    

def verif_file(i=False):
    """
    Verifie si les fichiers de l'app et renvoie la liste
    des elements a retelecharger et la liste de dossier a recreer
    """
    
    # Définition des variables
    file_to_dwl = []
    folder_to_create = []
    
    # Est-ce que Dokkan.py existe ?
    if os.path.exists(r"../Programme.exe.lnk") == False:
        file_to_dwl.append('Programme.exe.lnk')
        print('ERROR ! Le fichier Programme.exe.lnk est manquant ou corrompue, il va etre aquis a nouveau')
    
    if os.path.exists(r'../README.md') == False:
        file_to_dwl.append('README.md')
        print('ERROR ! Le fichier README.md est manquant ou corrompue, il va etre aquis a nouveau')
    
    if os.path.exists(r'img') == False:
        folder_to_create.append('img')
        print('ERROR ! le dosier img est manquant et va etre recreer')
    
    # Est-ce que le dossier save existe ?
    if os.path.exists(r"../save") == False:
        folder_to_create.append('save')
        print('ERROR ! le dossier save est manquant et va etre recreer')
        
    if os.path.exists(r"img/db_logo-modifier.ico") == False:
        file_to_dwl.append('db_logo-modifier.ico')
        print('ERROR ! le logo est manquant et va etre recuperer')
        
    if os.path.exists(r'all_class.py') == False:
        file_to_dwl.append('all_class.py')
        print('ERROR ! le fichier all_class.py ca etre recuperer')
        
    # Tentative de réparation
    wrench_stat = dw_cr_file_folder(file_to_dwl, folder_to_create)
    
    # Renvoie True apres la seconde verification, si il n'y a eu que une verification, effectue la seconde
    if wrench_stat == True:
        if i == 1:
            return True
    
        if wrench_stat == True:
            return verif_file(1)
        
    else:
        if i == False:
            return verif_file(True)
        if i == True:
            if os.path.exists('../CrashReport') == False:
                os.mkdir('../CrashReport')
            now = str(datetime.now())
            f = open('../CrashReport/Crash-' + now[8:10] + '_' + now[5:7] + '_' + now[0:4] + '-' + now[11:13] + '_' + now[14:16] + '_' + now[17:19] + '.txt', 'w');
            f.write("Certains fichiers n'ont pas pu être reparé : \n\n   Details : \n\n      " + str(file_to_dwl) + "\n      " + str(folder_to_create) + "\n\n   Un ou plusieurs fichiers listé ci-dessus ont rencontré des problemes lors de la réparation\n\nAfin de réparer l'application, merci de telecharger l\'outil de réparation founi à cette url : (url)\n\nSuivez les instructions dans le fichier \'readme\' qui accompagne l'outil de réparation.\n\n  ~Syrock.\n\n")
            f.flush()
            f.close()
            raise TypeError('La réparation à échoué deux fois de suite, veiller utiliser l\'outil de reparation : "url"')
        
def init():
    
    # Skip la seconde verification (par console jusque Tkinter)
    verif_ask = 0
    if verif_ask == 0:
        verif_file()
        return True
    else:
        verif_file(True)
        return True