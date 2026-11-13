# mi_conjunto = {1, 2, 3}
# mi_conjunto.add(3)  # Agrega el elemento 4 al conjunto  
# print(mi_conjunto)  # Salida: {1, 2, 3, 4}

import random

print("aleatorioo" , random.random())

mi_lista = [10, 20, 30, 40, 50]
# print(max(mi_lista))
# sublista = mi_lista[2:4]  # Obtiene los elementos desde el índice 1 hasta el 3 (4 no incluido)
# print(sublista)  # Salida: [20, 30, 40]

# frutas = {"Naranja": 20, "Fresa": 30, "Limon":40, "Sandia":50 }

# # for claves, valores in zip(frutas.keys(), frutas.values()):
# for claves, valores in frutas.items():
#   print(claves)
#   print(valores)

# lista_1 = [1,2,3,4]
# lista_2 = ["a","b","c","d"]
# lista_suma = lista_1+lista_2
# lista_suma.insert(3, "nueva insercion")
# lista_suma.remove("nueva insercion")
# lista_1.reverse()
# print(lista_1)

# mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Catadau"}
# pares = mi_diccionario.items()  
# print(pares)

# mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Catadau"}
# valor_edad = mi_diccionario.pop("edad")  # Elimina el par clave-valor con clave "edad"
# mi_diccionario["años"] = valor_edad  # Añade un nuevo par clave-valor con la nueva clave "años"
# print(mi_diccionario) 

# mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Catadau"}
# valor = mi_diccionario.get("edad")  # Obtiene el valor asociado a la clave "edad"
# print(f"El valor asociado a edad es: {valor}")  # Salida: 30
# valor_no_existente = mi_diccionario.get("pais", "No encontrado")  # Devuelve un valor predeterminado si la clave no existe
# print(valor_no_existente)  # Salida: No especificado

 
# Declarar el generador
def generador_numeros_pares(num):
    for i in range(num):
        yield i*2

# Instanciar el generador
numeros_pares = generador_numeros_pares(5)

# Usar del generador
## Llamada 1
print("Aquí hay código")
print(f"Llamada 1 al generador que extrae el valor: {next(numeros_pares)}")
## Llamada 2
print("Aquí hay código")
print(f"Llamada 2 al generador que extrae el valor: {next(numeros_pares)}")
## Llamada 3
print("Aquí hay código")
print(f"Llamada 3 al generador que extrae el valor: {next(numeros_pares)}")
...

# def generador_numeros_pares(num):
#     for i in range(num):
#         yield i*2

# def generador_letras():
#     yield "a"
#     yield "b"
#     yield "c"
#     yield "d"

# def generador_principal():
#     yield from generador_numeros_pares(5)
#     yield from generador_letras()

# # Usar el generador principal
# generador = generador_principal()
# for valor in generador:
#     print(valor)

# # código sin yield from
# def devuelve_ciudades(*ciudades):
#   for ciudad in ciudades:
#     for letras in ciudad:
#       yield letras

# ciudades_generadas = devuelve_ciudades("Llombay", "Catadau", "Alfarp")
# for letras in range(20):
#   print(next(ciudades_generadas), end="_")

# # código CON yield from
# def devuelve_ciudades(*ciudades):
#   for ciudad in ciudades:
#     yield from ciudad

# ciudades_generadas = devuelve_ciudades("Llombay", "Catadau", "Alfarp")
# for letras in range(20):
#   print(next(ciudades_generadas), end="_")
