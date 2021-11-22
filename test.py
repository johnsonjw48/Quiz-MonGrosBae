
dictionnaire={'lundi ':'monday', 'mardi ':'tuesday', 'mercredi ':'wednesday'}
print ("*** Début du Quiz ***\n")
nom = input (" Entrez votre nom: ")
##Pense  à forcer l'utilisateur à entrez son nom. 
print ()

def quiz(dico):
        points = 0
        for cle,valeur in dico.items():
            print("Question:  " + str(cle) + " ? \n")
            reponse= input("entrez la réponse svp: \n")
           
            #La méthode lower() renvoie une chaîne où tous les caractères sont en minuscules. 
            # j'ai utilisé ca pour evitez que l'utilisateur est faux parcequil  ait mis tel ou tel en majuscule et toi non.
            # Tu peux aussi utilser la methode upper() qui fait l'inverse de lower()
            
            if reponse.lower() == valeur.lower():
                points += 1
                print("Bonne réponse " + nom + "\n")
            else:
                print("cest mal joué, la bonne réponse est" + " " + valeur + "\n" )
        return print("\n Merci pour ta participacition à ce Quiz " + nom + "\n Tu as obtenu " + str(points) + " sur 3 points \n A bientot!"  )

quiz(dictionnaire)






