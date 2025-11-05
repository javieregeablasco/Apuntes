class Coche:
    # Atributo de clase (compartido por todas las instancias)
    ruedas = 4
    
    def __init__(self, marca, modelo, color, kilometros = 0):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.kilometros = kilometros
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

    def mostrar_marca(self):
        return f"Este coche es un {self.marca}"

    # Método estático
    @staticmethod
    def es_nuevo(kilometros):
        """Devuelve el estado del coche según los kilómetros."""
        if kilometros >= 10000: 
            return "de segunda mano"
        elif 500 < kilometros < 10000: 
            return "semi nuevo"
        else: 
            return "nuevo"

    # Método de clase
    @classmethod
    def cambiar_ruedas(cls, nuevas_ruedas):
        cls.ruedas = nuevas_ruedas
        print(f"Ahora todos los coches tienen {cls.ruedas} ruedas.")     

    @classmethod
    def crear_coche_predeterminado(cls):
        """Crea un coche con valores estándar."""
        return cls("Toyota", "Corolla", "gris", 0)       


# Ejemplo de uso
coche_1 = Coche("Toyota", "Corolla", "gris")
coche_2 = Coche("Ford", "Focus", "rojo", 8000)

# Método de instancia → depende del objeto
print(coche_1.mostrar_marca())  # "Este coche es un Toyota"

# Método de clase → afecta a la clase entera
Coche.cambiar_ruedas(6)  
print(f"El coche coche_2 tiene {coche_2.ruedas} ruedas")  # 6 (se actualizó para todas las instancias)

# Método estático → independiente de la clase o instancia
print("El coche 1 es", Coche.es_nuevo(coche_1.kilometros))  # nuevo
print("El coche 2 es",Coche.es_nuevo(coche_2.kilometros))  # semi nuevo

# Método de clase que crea un coche predefinido
coche_3 = Coche.crear_coche_predeterminado()
print(f"Coche 3 (predeterminado): {coche_3.marca}, {coche_3.modelo}, {coche_3.color}, {coche_3.kilometros} km")


