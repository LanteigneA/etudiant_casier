class Casier:
    """
    Classe casier
    """
    #
    def __init__(self, pNoCasier="", pTailleCasier="", pLocalCasier="", pPrixCasier = 20):
        """
        Constructeur de la classe Casier
        """
        self.__numero_casier = pNoCasier
        self.taille_casier = pTailleCasier
        self.localisation_casier = pLocalCasier
        self.__prix_casier = pPrixCasier

    #######################
    #Ascesseur et mutateur#
    #######################
    def _get_Numero_Casier(self):
        """

        """
        return self.__numero_casier

    def _set_Numero_Casier(self, pNoCasier):
        """

        """
        if len(pNoCasier) == 5 and pNoCasier[0].isalpha() and pNoCasier[1:4].isnumeric():
            self.__numero_casier = pNoCasier

    NumeroCasier = property(_get_Numero_Casier,_set_Numero_Casier)


    def _get_Prix_Casier(self):
       """

       """
       return self.__prix_casier

    PrixCasier = property(_get_Prix_Casier)
