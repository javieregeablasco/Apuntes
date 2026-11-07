# def agregar_elemento(lista):
#     lista.append(4)
#     print("Dentro de la función:", lista)

# numeros = [1, 2, 3]
# agregar_elemento(numeros[:])   # Se pasa una copia de la lista
# print("Fuera de la función:", numeros)

# def modificar(x):
#     print("ID dentro de la función (antes):", id(x)) # 140715771130920
#     x += 1
#     print("ID dentro de la función (después):", id(x)) # 140715771130952
#     return x

# a = 5
# print("ID fuera de la función:", id(a)) # 140715771130920
# x = modificar(a)
# print("ID fuera de la función (final):", id(a)) # 140715771130920
# print("ID devuelto por la función (final):", id(x), x) # 140715771130952

# def modificar_lista(lst):
#     print("ID dentro de la función (antes):", id(lst)) # 1971487072512
#     lst.append(4)
#     print("ID dentro de la función (después):", id(lst)) # 1971487072512
#     return lst

# numeros = [1, 2, 3]
# print("ID fuera de la función (antes):", id(numeros)) # 1971487072512

# resultado = modificar_lista(numeros)

# print("ID fuera de la función (final):", id(numeros)) # 1971487072512
# print("ID devuelto por la función (final):", id(resultado))
# print("Contenido final de la lista:", numeros) # 1971487072512


 