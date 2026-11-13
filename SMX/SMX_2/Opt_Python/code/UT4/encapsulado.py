# class Coche:
#     def __init__(self, marca, modelo, color):
#         # Atributos de instancia
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         self.velocidad = 0  # valor inicial

#     # Método para acelerar
#     def acelerar(self, cantidad):
#         self.velocidad += cantidad
#         print(f"El coche ha acelerado. Velocidad actual: {self.velocidad} km/h")

#     # Método para frenar
#     def frenar(self, cantidad):
#         self.velocidad = max(0, self.velocidad - cantidad)
#         print(f"El coche ha frenado. Velocidad actual: {self.velocidad} km/h")

#     # Método para mostrar información
#     def mostrar_info(self):
#         print(f"{self.marca} {self.modelo} ({self.color}) - {self.velocidad} km/h")

# # Intancia y manipulación de atributos

# # Crear un objeto (instancia de la clase)
# mi_coche = Coche("Toyota", "Corolla", "Rojo")

# # Acceder a los atributos
# print(mi_coche.marca)     # Toyota
# print(mi_coche.color)     # Rojo

# # Modificar un atributo directamente
# mi_coche.color = "Azul"
# print(mi_coche.color)     # Azul

# # Usar métodos
# mi_coche.mostrar_info()   # Toyota Corolla (Azul) - 0 km/h
# mi_coche.acelerar(50)     # Acelera a 50 km/h
# mi_coche.frenar(20)       # Baja a 30 km/h

# # Comprobar valores modificados
# mi_coche.mostrar_info()   # Toyota Corolla (Azul) - 30 km/h

########################

class Coche:
    def __init__(self, marca, modelo, color):
        # Atributos de instancia
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0  # valor inicial
        self.__ruedas = 4

    # Método para acelerar
    def acelerar(self, cantidad):
        self.velocidad += cantidad
        print(f"El coche ha acelerado. Velocidad actual: {self.velocidad} km/h")

    # Método para frenar
    def frenar(self, cantidad):
        self.velocidad = max(0, self.velocidad - cantidad)
        print(f"El coche ha frenado. Velocidad actual: {self.velocidad} km/h")

    # Método para mostrar información
    def __mostrar_info(self):
        print(f"{self.marca} {self.modelo} ({self.color}) - {self.velocidad} km/h")

# Intancia y manipulación de atributos

# Crear un objeto (instancia de la clase)
mi_coche = Coche("Toyota", "Corolla", "Rojo")

# Acceder a los atributos
print(mi_coche.marca)     # Toyota
print(mi_coche.color)     # Rojo

# Modificar un atributo directamente
mi_coche.color = "Azul"
print(mi_coche.color)     # Azul

# Usar métodos
mi_coche.acelerar(50)     # Acelera a 50 km/h
mi_coche.frenar(20)       # Baja a 30 km/h

# Comprobar valores modificados
mi_coche.__mostrar_info()   #  
print(mi_coche.__ruedas)
