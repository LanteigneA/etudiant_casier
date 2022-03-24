from Etudiant import *

# Sérialiser l'objet instancié
# etud=Etudiant("1234567","Hasna","informatique")
# etud.serialiser("FichierSerialiser1.json")

# Désérialisation

etud1 = Etudiant()

etud1.deserialiser("FichierSerialiser1.json")

print(etud1.Nom_Etud)
