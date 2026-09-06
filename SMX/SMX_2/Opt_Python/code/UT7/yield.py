# # Declarar el generador
# def generador_numeros_pares(num):
#     for i in range(num):
#         yield i*2

# # Instanciar el generador
# numeros_pares = generador_numeros_pares(5)

# # Usar del generador
# print("Aquí hay código")
# ## Llamada 1
# print(f"Llamada 1 al generador que extrae el valor: {next(numeros_pares)}")
# print("Aquí hay código")
# ## Llamada 2
# print(f"Llamada 2 al generador que extrae el valor: {next(numeros_pares)}")
# print("Aquí hay código")
# ## Llamada 3
# print(f"Llamada 3 al generador que extrae el valor: {next(numeros_pares)}")
# ...


# numeros_pares = []

# # Declarar el generador
# def generador_numeros_pares(num):
#     for i in range(num):
#         numeros_pares.append(i**2)

# # Instanciar el generador
# generador_numeros_pares(5)

# # Usar del generador
# print("Aquí hay código")
# ## Llamada 1
# print(f"Llamada 1 al generador que extrae el valor: {numeros_pares[0]}")
# print("Aquí hay código")
# ## Llamada 2
# print(f"Llamada 2 al generador que extrae el valor: {numeros_pares[1]}")
# print("Aquí hay código")
# ## Llamada 3
# print(f"Llamada 3 al generador que extrae el valor: {numeros_pares[2]}")
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


# # Ejemplo de uso de filter()
# def es_par(x):
#     return x % 2 == 0
# numeros = [1, 2, 3, 4, 5, 6]
# resultados = filter(es_par, numeros)  # Filtra los números pares de la lista
# print(list(resultados))  # Salida: [2, 4, 6]