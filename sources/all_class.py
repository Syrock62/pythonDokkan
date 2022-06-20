########################################################
#                                                      #
# Author : Syrock                                      #
#                                                      #
# Version : 1.0                                        #
#                                                      #
########################################################

class file_info:
    
    def __init__(self, ver, aut, wh):
        self.ver = ver
        self.aut = aut
        self.wh = wh
        
    def version(self):
        print('La version du fichier est : ' + str(self.ver))
        
    def auteur(self):
        print('L\'auteur de ce script est : ' + str(self.aut))
        
    def what(self):
        print(str(self.wh))
        
    def all_info(self):
        print('version : ' + str(self.ver) + '\nAutheur : ' + str(self.aut) + '\nUtility : ' + str(self.wh))

class Player:
    
    def __init__(self, nom, point = 0, nbr_win = 0):
        self.nom = nom
        self.point = point
        self.nbr_win = nbr_win
        
    def afficher_nom(self):
        return self.nom
    
    def afficher_point(self):
        return self.point
    
    def afficher_nbr_win(self):
        return self.nbr_win
    
    def modifier_point(self, new):
        self.point = new
    
    def modifier_nom(self, new):
        self.nom = new
        
    def modifier_win(self, new):
        self.nbr_win = new
    
    def pprint(self):
        print('Nom : ' + str(self.nom) + '\nPoints : ' + str(self.point))
    
    def all_pprint(self):
        a = self.pprint()
        print('Nombre de win : ' + str(self.nbr_win))
        
file = file_info(0.1, 'Syrock', 'Regroupe les class de l\'application')
