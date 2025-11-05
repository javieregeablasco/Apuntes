# class Coches:
#     def acelerar(self):
#         pass

# class Coupe(Coches):
#     def acelerar(self):
#         return "¡Acelerando a tope!"

# class Sedan(Coches):
#     def acelerar(self):
#         return "Acelerando con calma"

# for coche in [Coupe(), Sedan()]:
#     print(coche.acelerar())
    

class Coche:
    # Atributos de la clase
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.ruedas = 4
        self.abs_serie = True    

    # Métodos de la clase
    def arrancar(self):
        print("El coche está arrancando.")
    
    def acelerar(self, tope):
        print("El coche está acelerando:", tope)
    
    def frenar(self):
        print("El coche está frenando.")
    
    def girar(self):
        print("El coche está girando.")    

# Crear una instancia (objeto)
coche_nuevo = Coche("Toyota", "Corolla", "Rojo")

# Usar un método del objeto
print(coche_nuevo.acelerar("superRápido"))

