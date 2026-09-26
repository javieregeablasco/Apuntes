class Coche:
    # Atributo de clase (compartido por todas las instancias)
    ruedas = 4  

    # Constructor
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.abs_serie = True    

    # Métodos de instancia
    def arrancar(self):
        print("El coche está arrancando.")
    
    def acelerar(self):
        print("El coche está acelerando.")
    
    def frenar(self):
        print("El coche está frenando.")
    
    def girar(self):
        print("El coche está girando.")

    # Método de clase
    @classmethod
    def cambiar_ruedas(cls, nuevas_ruedas):
        cls.ruedas = nuevas_ruedas
        print(f"Ahora todos los coches tienen {cls.ruedas} ruedas.")

# Intanciar el metodo de clase no el objeto
# Coche.cambiar_ruedas(6)

# Crear nuevo objeto

mi_primer_coche = Coche
print("Ruedas de mi primer coche:", mi_primer_coche.ruedas,"ruedas")

mi_segundo_coche = Coche
print("Ruedas de mi segundo coche:", mi_segundo_coche.ruedas,"ruedas")

mi_segundo_coche.ruedas=6
print("Ruedas de mi segundo coche:", mi_segundo_coche.ruedas,"ruedas")

mi_tercer_coche = Coche
print("Ruedas de mi tercer coche:", mi_tercer_coche.ruedas,"ruedas")

print("Ruedas de mi primer coche", mi_primer_coche.ruedas,"ruedas")

Coche.cambiar_ruedas(4)
print("Despues de la instancias de clase")
print("Ruedas de mi primer coche:", mi_primer_coche.ruedas,"ruedas")
print("Ruedas de mi segundo coche:", mi_segundo_coche.ruedas,"ruedas")
print("Ruedas de mi tercer coche:", mi_tercer_coche.ruedas,"ruedas")
# -----------------------------






