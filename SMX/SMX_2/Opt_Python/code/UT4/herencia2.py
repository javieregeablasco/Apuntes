class Fruta:
    def __init__(self, tamanyo=None, peso=None, sabor=None, calibre=None):
        self.tamanyo = tamanyo
        self.peso = peso
        self.sabor = sabor
        self.calibre = calibre
    
    def mostrar_consejo(self, tipo_fruta, consejo):
        return (f"Instancia {tipo_fruta}\n, tamaño: {self.tamanyo}, peso: {self.peso}, sabor: {self.sabor}, calibre: {self.calibre}\n, consejo: {consejo})")


class Limon(Fruta):
    def __init__(self, tamanyo=None, peso=None, sabor=None, calibre=None):
        super().__init__(tamanyo, peso, sabor, calibre)
        
    def mostrar(self):
        return self.mostrar_consejo("Limon, ¡Bueno para refrescos!")


# Creamos un limón.
limon = Limon(calibre="pequeño", sabor="ácido", peso=150)
print(limon)


# class Fruit:
#     def __init__(self, taille=None, masse=None, saveur=None, forme=None):
#         print("(2) Je suis dans le constructeur de la classe Fruit")
#         self.taille = taille
#         self.masse = masse
#         self.saveur = saveur
#         self.forme = forme
#         print("Je viens de créer self.taille, self.masse, self.saveur "
#               "et self.forme")

#     def affiche_conseil(self, type_fruit, conseil):
#         print("(2) Je suis dans la méthode .affiche_conseil() de la "
#               "classe Fruit\n")
#         return (f"Instance {type_fruit}\n"
#                 f"taille: {self.taille}, masse: {self.masse}\n"
#                 f"saveur: {self.saveur}, forme: {self.forme}\n"
#                 f"conseil: {conseil}\n")


# class Citron(Fruit):
#     def __init__(self, taille=None, masse=None, saveur=None, forme=None):
#         print("(1) Je rentre dans le constructeur de Citron, et je vais "
#               "appeler\n"
#               "le constructeur de la classe mère Fruit !")
#         Fruit.__init__(self, taille, masse, saveur, forme)
#         print("(3) J'ai fini dans le constructeur de Citron, "
#               "les attributs sont :\n"
#               f"self.taille: {self.taille}, self.masse: {self.masse}\n"
#               f"self.saveur: {self.saveur}, self.forme: {self.forme}\n")

#     def __str__(self):
#         print("(1) Je rentre dans la méthode .__str__() de la classe "
#               "Citron")
#         print("Je vais lancer la méthode .affiche_conseil() héritée "
#               "de la classe Fruit")
#         return self.affiche_conseil("Citron", "Bon en tarte :-p !")


# if __name__ == "__main__":
#     # On crée un citron.
#     citron1 = Citron(taille="petite", saveur="acide", 
#                      forme="ellipsoïde", masse=50)
#     print(citron1)
