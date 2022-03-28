####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Exercice 1 - Interface graphique
###  Nom: Hasna Hocini
###  No étudiant: 123456
###  No Groupe:
###  Description du fichier: Description de la classe Etudiant
####################################################################################

import json

class Etudiant:
    """
     Classe Etudiant

    """

    ###################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ###################################
    def __init__(self,p_num="",p_nom="",p_prog="",p_date_naiss=""):
        """
                Méthode de type Constructeur avec paramètres et valeurs par défaut
                Définition des attributs d'un étudiant
        """
        self.Num_Etud = p_num
        self.Nom_Etud = p_nom
        self.Programme = p_prog
        self.Date_Naiss = p_date_naiss



    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################

    def __str__(self) :
        """
                Méthode spéciale d'affichage. À utiliser avec print(objet)
                :return: Chaine à afficher
        """
        chaine = " "*60+"\n"+"*"*60+"\n\n"+"   Le numéro de l'étudiant : "+self.Num_Etud+"\n"+ "   Le nom de l'étudiant : "+self.Nom_Etud+"\n"+\
                 "   Le programme de l'étudiant : "+self.Programme+"\n"+"   La date de naissance de l'étudiant : "+self.Date_Naiss + "\n\n"+"*"*60
        return chaine

    ############################################
    #####          Autres MÉTHODES         #####
    ############################################

    def serialiser(self, p_fichier):
        """
           Méthode permttant de sérialiser un objet de la classe Etudiant
           ::param p_fichier : Le nom du fichier qui contiendra l'objet sérialisé
           :: return : retourne 0 si le fichier est ouvert et les informations y sont écrites,
                       1 s'il y a erreur d'écriture et 2 s'il y a erreur d'ouverture

        """
        try:
            with open(p_fichier , "w") as fichier:
                try:
                    json.dump(self.__dict__, fichier)
                    return 0
                except:
                    return 1
        except:
            return 2


    def deserialiser(self, p_fichier):
        """
            Méthode permttant de désérialiser un objet de la classe Etudiant
            ::param p_fichier : Le nom du fichier qui contient l'objet sérialisé
            :: return : retourne 0 si le fichier est ouvert et lu, 1 s'il y a erreur de lecture et 2 s'il y a erreur d'ouverture
            """
        try :
            with open(p_fichier , "r") as fichier :
                try :
                    self.__dict__ = json.load(fichier)
                    return 0
                except :
                    return 1
        except :

            return 2

    def age(self):
        """
           Méthode permettant de calculer l'age de l'étudiant
           :: return : retourne l'âge de l'étudiant
        """
        import datetime
        # Le formet de la date utilisé
        format = '%Y-%m-%d'
        date_naiss_str = datetime.datetime.strptime(self.Date_Naiss, format)
        today = datetime.date.today()
        return today.year - date_naiss_str.year - (
                    (today.month, today.day) < (date_naiss_str.month, date_naiss_str.day))
