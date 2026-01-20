# frutas = {"Naranja": 20, "Fresa": 30, "Limon":40, "Sandia":50 }

# # for claves, valores in zip(frutas.keys(), frutas.values()):
# for claves, valores in frutas.items():
#   print(claves)
#   print(valores)

diccionario = {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Catadau'}
diccionario("nom")

# Declarar el generador
# def generador_numeros_pares(num):
#     for i in range(num):
#         yield i*2

# # Instanciar el generador
# numeros_pares = generador_numeros_pares(5)

# # Usar del generador
# ## Llamada 1
# print("Aquí hay código")
# print(f"Llamada 1 al generador que extrae el valor: {next(numeros_pares)}")
# ## Llamada 2
# print("Aquí hay código")
# print(f"Llamada 2 al generador que extrae el valor: {next(numeros_pares)}")
# ## Llamada 3
# print("Aquí hay código")
# print(f"Llamada 3 al generador que extrae el valor: {next(numeros_pares)}")
# ...

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
