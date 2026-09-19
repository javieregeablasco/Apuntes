# class Persona:
#     def __init__(self, nombre, edad):
#         self.__nombre = nombre   
#         self.__edad = edad

#     # Setter para nombre
#     def set_Nombre(self, nuevo_Nombre):
#         self.__nombre = nuevo_Nombre

#     # Getter para nombre
#     def get_Nombre(self):
#         return self.__nombre


# # --- Uso del objeto ---
# persona = Persona("Ana", 25)

# # Acceso mediante metodos
# #print("Edad de la persona", persona.__edad)      # Producira un error
# #print("Nombre de la persona", persona.__nombre)  # Producira un error

# # Modificar mediante getters 
# persona.set_Nombre("Arturo")       

# # Acceder mediante setters 
# print("Nuevo nombre de la persona:", persona.get_Nombre())     
 
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    # Getter para nombre
    @property
    def nombre(self):
        return self.__nombre

    # Setter para nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre


# --- Uso del objeto ---
persona = Persona("Ana", 25)

# Acceso directo a __nombre o __edad produciría error
# print(persona.__nombre)  # ❌ AttributeError
# print(persona.__edad)    # ❌ AttributeError

# Modificar usando el setter
persona.nombre = "Arturo"

# Acceder usando el getter
print("Nuevo nombre de la persona:", persona.nombre)  # ✅ Correcto
