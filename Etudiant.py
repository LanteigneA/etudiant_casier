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
    def __init__(self,p_num="",p_nom="",p_prog=""):
        """
                Méthode de type Constructeur avec paramètres et valeurs par défaut
                Définition des attributs d'un étudiant
        """
        self.Num_Etud = p_num
        self.Nom_Etud = p_nom
        self.Programme=p_prog
        # ajouter self.date_naiss

    ############################################
    #####  MÉTHODES D'ACCÈS ET PROPRIÉTÉS  #####
    ############################################

    # À ajouter ici :-)

    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################

    def __str__(self) :
        """
                Méthode spéciale d'affichage. À utiliser avec print(objet)
                :return: Chaine à afficher
        """


        chaine = " "*30+"\n"+"*"*30+"\n\n"+"   Le numéro de l'étudiant : "+self.Num_Etud+"\n"+ "   Le nom de l'étudiant : "+self.Nom_Etud+"\n"+"   Le programme de l'étudiant : "+self.Programme\
                + "\n\n"+"*"*30

        return chaine

    ############################################
    #####          Autres MÉTHODES         #####
    ############################################

    def serialiser(self, p_fichier):
        """
           Méthode permttant de sérialiser un objet de la classe Etudiant
           ::param p_fichier : Le nom du fichier qui contiendra l'objet sérialisé
        """
        with open(p_fichier , "w") as fichier:
            json.dump(self.__dict__, fichier)


    def deserialiser(self, p_fichier):
        """
            Méthode permttant de désérialiser un objet de la classe Etudiant
            ::param p_fichier : Le nom du fichier qui contient l'objet sérialisé
                """

        with open(p_fichier , "r") as fichier :
            self.__dict__ = json.load(fichier)

