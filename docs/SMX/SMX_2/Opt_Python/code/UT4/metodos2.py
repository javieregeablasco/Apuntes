class Coche:
    def __init__(self, marca, modelo, color, kilometros):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.kilometros = kilometros
        self.ruedas = 4
        self.abs_serie = True    

    def arrancar(self):
        print("El coche está arrancando.")
    
    def acelerar(self):
        print("El coche está acelerando.")
    
    def frenar(self):
        print("El coche está frenando.")
    
    def girar(self):
        print("El coche está girando.")

    @staticmethod
    def es_nuevo(kilometros):
        if kilometros >= 10000: return "de segunda mano"
        elif kilometros > 500 and kilometros <10000: return "semi nuevo"
        else: return "nuevo"

coche1 = Coche("Toyota", "Corolla", "gris", 0)
coche2 = Coche("Ford", "Focus", "rojo", 100)

print("El coche es", Coche.es_nuevo(coche1.kilometros))  
print("El coche es", Coche.es_nuevo(coche2.kilometros))  

