# Clase base 1
class Persona:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    def mostrar(self):
        return f"Nombre: {self.nombre} con DNI: {self.dni}"

# Clase base 2
class Trabajador:
    def __init__(self, perfil):
        self.perfil = perfil

    def mostrar_puesto_trabajo(self):
        return f"Puesto: {self.perfil}"

# Clase hija que hereda de Persona y Trabajador
class Empleado(Persona, Trabajador):
    def __init__(self, nombre, dni, perfil, salario):
        # Llamadas a los constructores de ambas superclases
        Persona.__init__(self, nombre, dni)
        Trabajador.__init__(self, perfil)
        self.salario = salario

    def mostrar(self):
        # Combina los métodos heredados
        return f"{super().mostrar()} | {self.mostrar_puesto_trabajo()} | Salario: {self.salario}€"

# Uso de la clase
e1 = Empleado("Carlos", "22656198Y", "Desarrollador", 2800)
print(e1.mostrar())


# class Persona:

#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def mostrar(self):
#         return self.nombre + ", " + str(self.edad) + " años"

#     # Otros métodos...

# # Clase hija

# class Programador(Persona):

#     def __init__(self, nombre, edad, lenguaje):
#         super().__init__(nombre, edad)
#         self.lenguaje = lenguaje


#     def mostrar(self):
#        return super().mostrar() + "\nPrograma en " + self.lenguaje
    

# persona_1 = Programador("Pedro", 28,"Python")
# print(persona_1.mostrar())
