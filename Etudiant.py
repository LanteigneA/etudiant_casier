####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Exercice 1 - Interface graphique
###  Nom: Hasna Hocini
###  No étudiant: 123456
###  No Groupe:
###  Description du fichier: Description de la classe Etudiant
####################################################################################
import datetime
import json
from Casier import *

class Etudiant:
    """
     Classe Etudiant

    """

    ###################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ###################################
    def __init__(self,p_num="",p_nom="",p_prog="",p_date_naiss="",p_casier = Casier()):
        """
                Méthode de type Constructeur avec paramètres et valeurs par défaut
                Définition des attributs publics d'un étudiant
        """
        self.__num_etud = p_num
        self.__nom_etud = p_nom
        self.Programme = p_prog
        self.__date_naiss = p_date_naiss
        self.casier = p_casier


    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ####                                          ####
    ##################################################

    # Propriété NomEtud
    def _get_num_etud(self):
        """
           Accesseur de l'attribut privé  __num__etud
        """
        return self.__num_etud
    def _set_num_etud(self,p_num_etud):
        """
        Mutateur de l'attribur privé __num_etud
        """
        if p_num_etud.isnumeric() is True:
            self.__num_etud = p_num_etud

    NumEtud = property(_get_num_etud,_set_num_etud)

    # Propriété NomEtud
    def _get_nom_etud(self):
        """
           Accesseur de l'attribut privé  __num__etud
        """
        return self.__nom_etud

    def _set_nom_etud(self, p_nom_etud):
        """
        Mutateur de l'attribur privé __num_etud
        """
        if p_nom_etud.isalpha():
            self.__nom_etud = p_nom_etud

    NomEtud = property(_get_nom_etud, _set_nom_etud)


    # Propriété DateNaiss
    def _get_date_naiss(self):
        """
           Accesseur de l'attribut privé  __num__etud
        """
        return self.__date_naiss

    def _set_date_naiss(self, p_date_naiss):
        """
        Mutateur de l'attribur privé __num_etud
        """
        if self.age(p_date_naiss) >= 18 :
            self.__date_naiss = p_date_naiss


    DateNaiss = property(_get_date_naiss, _set_date_naiss)

    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################

    def __str__(self) :
        """
                Méthode spéciale d'affichage. À utiliser avec print(objet)
                :return: Chaine à afficher
        """
        chaine = " "*60+"\n"+"*"*60+"\n\n"+"   Le numéro de l'étudiant : "+self.NumEtud+"\n"+\
                 "   Le nom de l'étudiant : "+self.NomEtud+"\n"+\
                "   Le programme de l'étudiant : "+self.Programme+"\n"+\
                 "   La date de naissance de l'étudiant : "+str(self.DateNaiss.year())+"-" \
                 +str(self.DateNaiss.month())+"-"+ str(self.DateNaiss.day())+"\n\n"+"*"*60
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
        self.__dict__["_Etudiant__date_naiss"]=str(self.DateNaiss.year())+"-"+str(self.DateNaiss.month())+"-"\
                                               +str(self.DateNaiss.day())

        try:
            with open(p_fichier , "w") as fichier:
                try:
                    #json.dump(self.__dict__, fichier)
                    json.dump(self.__dict__, fichier)
                    return 0
                except:
                    return 1
        except:
            return 2



    def age(self,p_date_naiss):
        """
           Méthode permettant de calculer l'age de l'étudiant
           :: return : retourne l'âge de l'étudiant
        """
        import datetime
        today = datetime.date.today()
        return today.year - p_date_naiss.year() - (
                     (today.month, today.day) < (p_date_naiss.month(), p_date_naiss.day()))
