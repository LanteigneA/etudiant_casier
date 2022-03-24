####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Exercice 1 - Interface graphique
###  Nom: Hasna Hocini
###  No étudiant: 123456
###  No Groupe:
###  Description du fichier: Programme principal
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################

# Importer le module sys nécessaire à l'exécution.
import sys

# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets

# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer Pour le model de la listView

from PyQt5.QtGui import QStandardItemModel, QStandardItem

#import les interfaces graphiques

import interfacegraphique_
import dialogue_listview_

# Importer la classe Etudiant
from Etudiant import *


##########################################################
###  DÉCLARATIONS ET INITIALISATIONS - Portée globale  ###
##########################################################

# Déclarer une liste d'étudiants
ls_Etudiants=[]


#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

def valider_nom(p_nom):
    """
    Vérifie si le nom de l'étudiant est valide
     :param p_nom:  le nom de l'étudiant
     :return: retrourne True est le nom est alphabétique et False sinon
    """
    if p_nom.isalpha() :
        return True
    else :
        return False


def valider_num(p_num):
    """
        Vérifie si le numéro d'étudiant est valide
         :param p_num:  le numéro d'étudiant
         :return: True si parm p_num est numérique et False sinon
        """
    for car in p_num:
        if car not in "0123456789":
            return False
    return True

def valider_date(p_date):

    """
        Vérifie si la date de naissance est valide : age de l'étudiant > 18 ans
         :param p_num : le numéro d'étudiant
         :return: True si parm p_date est valide et False sinon
        """
    import datetime
    print(datetime.date.today().year)
    print(p_date.year())
    if datetime.date.today().year - p_date.year() > 18:
        return True
    elif datetime.date.today().year - p_date.year() == 18:

            if datetime.date.today().month > p_date.month():
                return True
            elif datetime.date.today().month == p_date.month():
                if datetime.date.today().day >= p_date.day():
                    return True
                else:
                    return False
            else:
                return False
    else:
        return False
    return True


def verifier_etudiant_liste(p_num):
    """
         Vérifie si l'étudiant existe dans la liste des étudiants
             :param p_num:  le numéro d'étudiant
             :return: True si l'étudiant est trouvé dans la liste des étudiants et False sinon
    """
    for elt in ls_Etudiants :
        if elt.Num_Etud == p_num:
            return True
    return False



#############################################
###### DÉFINITIONS DE LA CLASSE demoQT ######
#############################################

# créer une classe qui hérite de Qt et de notre ui.
      # Nom de ma classe (demoQt)   # Nom de mon fichier ui
class demoQt(QtWidgets.QMainWindow, interfacegraphique_.Ui_MainWindow):
    '''
    Nome de la classe : demoQt
    Héritages :
    - QtWidgets.QMainWindow : Type d'interface créé par QtDesigner
    - interfacegraphique.Ui_MainWindow : Ma classe générée avec QtDesigner
    '''
    def __init__(self, parent=None):
        '''
        Constructeur de la classe
        :param parent: QtWidgets.QMainWindow et interfacegraphique.Ui_MainWindow
        '''
        # Appeler le constructeur parent avec ma classe en paramètre...
        super(demoQt, self).__init__(parent)
        # Préparer l'interface utilisateur.
        self.setupUi(self)

    # Utiliser le décorateur ici
    @pyqtSlot()
    # Bouton Ajouter
    def on_pushButton_ajouter_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Ajouter
        """

        nom = self.lineEdit_nom.text()
        valid_nom = valider_nom(nom)
        valid_num = valider_num(self.lineEdit_numero.text())
        valid_date = valider_date(self.dateEdit_DNaiss.date())

        # On aurait pu nous passer des variables valid_nom, valid_num et nom :
        #if  valider_nom(self.lineEdit_nom.text()) and valider_num(self.lineEdit_numero.text()) and valider_date(self.dateEdit_DNaiss.date()):
        if valid_nom and valid_num and valid_date :
            self.label_erreur.setVisible(False)
            # Tester si l'étudiant a déjà été ajouté
            if  verifier_etudiant_liste(self.lineEdit_numero.text())== False :
                 # Instancier un objet Etudiant avec le nom, numéro éudiant et le programme entrés par l'utilisateur

                 etud = Etudiant(self.lineEdit_numero.text(), self.lineEdit_nom.text(), self.comboBox_programme.currentText())
                 # Ajouter l'objet instancié à la liste des étudiants
                 ls_Etudiants.append(etud)
                 # Ajouter les informations de l'étudiant entré au TextBrowser
                 self.textBrowser_afficher.append(etud.__str__())
                 # Effacer les lineEdits du nom et du numéro d'étudiant
                 self.lineEdit_numero.clear()
                 self.lineEdit_nom.clear()
                 # Sérialiser l'objet instancié
                 #etud.serialiser("FichierSerialiser.json")
                 #etud.deserialiser("FichierSerialiser.json")
                 #print(etud.Nom_Etud)

            else :
                 self.lineEdit_numero.clear()
                 self.lineEdit_numero.clear()
                 self.label_erreur.clear()
                 self.label_erreur.setText("L'étudiant existe dans la liste des étudiants.")
                 self.label_erreur.setVisible(True)

        elif valider_nom(self.lineEdit_nom.text())==False and valider_num(self.lineEdit_numero.text()) == True:
            self.lineEdit_nom.clear()
            self.label_erreur.clear()
            self.label_erreur.setText("Le nom est invalide. ")
            self.label_erreur.setVisible(True)
        elif valider_num(self.lineEdit_numero.text()) == False and valider_nom(self.lineEdit_nom.text()) == True:
            self.lineEdit_numero.clear()
            self.label_erreur.clear()
            self.label_erreur.setText("Le numéro est invalide. ")
            self.label_erreur.setVisible(True)
        else :
            self.lineEdit_numero.clear()
            self.lineEdit_numero.clear()
            self.label_erreur.clear()
            self.label_erreur.setText("Le numéro et le nom sont invalides. ")
            self.label_erreur.setVisible(True)

    @pyqtSlot()
    # Bouton Modifier
    def on_pushButton_modifier_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Modifier
        """


    @pyqtSlot()
    # Bouton Supprimer
    def on_pushButton_supprimer_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Supprimer
        """


    @pyqtSlot()
    # Bouton Sauvegarder
    def on_pushButton_sauvegarder_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Sauvegarder
        """

    # Bouton Afficher listview
    @pyqtSlot()
    def on_pushButton_afficher_listview_clicked(self):
        dialog = Fenetrelistview()
        dialog.setWindowTitle("Liste des étudiant.e.s")

        # model = QStandardItemModel()
        # dialog.listView_etudiants.setModel(model)
        # for e in ls_Etudiants:
        #     item = QStandardItem(e.Nom_Etud)
        #     model.appendRow(item)

        dialog.show()
        reply = dialog.exec_()

#############################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
#############################################

class Fenetrelistview(QtWidgets.QDialog, dialogue_listview_.Ui_Dialog):
    def __init__(self, parent=None):
        super(Fenetrelistview, self).__init__(parent)
        self.setupUi(self)
    @pyqtSlot()
    def on_pushButton_quitter_clicked(self):
        self.close()


#################################
###### PROGRAMME PRINCIPAL ######
#################################

# Créer le main qui lance la fenêtre de Qt

def main():
    '''
    Méthode main : point d'entré du programme.
    Exécution de l'applicatin avec l'interface graphique.
    reply = Dialog.exec_()

    '''
    app = QtWidgets.QApplication(sys.argv)
    form = demoQt() #Nom de ma classe
    form.setWindowTitle("Gestion de scolarité")
    form.label_erreur.setVisible(False)
    form.show()
    app.exec()


if __name__ == "__main__":
    main()