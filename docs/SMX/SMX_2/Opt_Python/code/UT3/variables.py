# a = True
# b = False

# # Tipos de a y b
# print("Tipos:", type(a), type(b))

# # Suma lógica de a y b
# suma_logica = a + b
# print("Suma lógica (a + b):", suma_logica, "Tipo:", type(suma_logica))

# # Comparar a con la negación de b
# print("a:", a, "not b:", not b)
# print("¿a es igual a not b?:", a == (not b))


# Crea una matriz 3x3 utilizando listas
# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # Muestra la matriz completa
# print("Matriz completa:")
# print(matriz)

# # Muestra cada fila en una línea distinta
# print("\nFilas de la matriz:")
# for fila in matriz:
#     print(fila)

# # Muestra un elemento concreto (por ejemplo, el de la fila 2, columna 3)
# print("\nElemento de la fila 2, columna 3:")
# print(matriz[1][2])  # (recuerda que el índice empieza en 0)


# mi_tupla = (1, 2, 3, "cuatro", True)
# print(mi_tupla)
# print(mi_tupla[0])     
# print(mi_tupla[-1]) 
# mi_tupla = (1,3,3, "cuatro", True,[1,2,3,"verde"])
# print(mi_tupla)

# mi_lista = [1, 2, 3, "cuatro", True]
# print(mi_lista)
# print(mi_lista[0])      # Primer elemento
# print(mi_lista[-1])     # Último elemento


# Diccionario
mi_diccionario = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}
print(mi_diccionario)
print(mi_diccionario["nombre"])  # Acceder al valor de una clave
print(mi_diccionario.get("edad")) # Otra manera de extraer valores del diccionario
