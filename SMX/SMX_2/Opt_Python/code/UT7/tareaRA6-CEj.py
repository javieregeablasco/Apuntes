# # 1. Crear el conjunto de usuarios
# usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}

# # 2. Crear el conjunto de administradores
# administradores = {"Juan", "Marta"}

# # 3. Eliminar a Juan del conjunto de administradores
# administradores.remove("Juan")
# # administradores.discard("Juan")

# # 4. Añadir a Marcos como administrador (sin eliminarlo de usuarios)
# administradores.add("Marcos")

# # 5. Mostrar todos los usuarios e indicar si son administradores
# for usuario in usuarios:
#     if usuario in administradores:
#         print(f"{usuario} → administrador")
#     else:
#         print(f"{usuario} → usuario normal")

cuadrado = [1,2,3,4,5]

def calculador_de_cuadrado(lista):
  for numero in lista:
    yield numero**2
 
resultado = calculador_de_cuadrado(cuadrado) 
 
for cuadrados in resultado:
  print(cuadrados)


print(next(resultado))
print(next(resultado))
print(next(resultado))
print(next(resultado))
print(next(resultado))