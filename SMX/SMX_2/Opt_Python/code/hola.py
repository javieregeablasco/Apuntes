# print("Hola mundo")

# # Definimos una variable x con una cadena
# x = "El valor de (a+b)*c es"

# # Podemos realizar múltiples asignaciones
# a, b, c = 4, 3, 2

# # Realizamos unas operaciones con a,b,c
# d = (a + b) * c

# # Definimos una variable booleana
# imprimir = True

# # Si imprimir, print()
# if imprimir:
#     print(x, d)

# # Salida: El valor de (a+b)*c es ??

# radio = 5; area = 3.1415 * radio ** 2
# print('''La superificie es:''', area)

# vari@able& = 64

# # Esta linea está comentada. El interprete no intentará ejecutarla.
# # 
# a = True and False
# print("El valor de 'a' es:", a, "y es de tipo: ", type(a))
# #
# """
# Nada de lo contenido entre las comillas dobles será ejecutado
# b = True and True
# print("El valor de 'b' es:", b, "y es de tipo: ", type(a))
# """


# radio = 5
# area = 3.14159265358979323846 \
#        * radio **2
# print(area) 

# texto = "Perdóname, amigo, de la ocasión que te he dado de parecer\
#          loco como yo, haciéndote caer en el error en que yo he caído\
#          de que hubo y hay caballeros andantes en el mundo."
# print(texto)

# a = 5
# b = 6
# c = '¡Hola mundo!'

# print(c, a+b)

# b = 26
# c = 42
# print(b+c)

# a = 5
# b = 16
# c = 2
# print(c, type(c))
# c = a / b
# print(c, type(c))


# # Demostración del problema de precisión con float en Python
# print("¿La suma de 0.1 y 0.2 es igual a 0.3?", 0.1 + 0.2 == 0.3) 
# print("Valor real de 0.1 + 0.2:", 0.1 + 0.2)   

# # Solución con Decimal para precisión exacta
# from decimal import Decimal
# a = Decimal("0.1")
# b = Decimal("0.2")
# c = Decimal("0.3")
# print("Con Decimal:", a + b == c)

# a = True
# b = False
# print(a, b, a + b, type(a+b))

# print(a == b)
# print(a == (not(b))) 

# a = "hello"
# b = " "
# c = "world"
# d = a + b + c
# print(a,b,c)
# print(d)

# a = "24"
# b = "12.25"
# c = "16"
# d = a + b + c
# print(a,b,c)
# print(d)

# resultado = 3 + (8/60 + 29/(60**2) + 40/(60**3))
# print(resultado) 

# resultado = (7 + (6 + (5**.5))**.5)**.5
# print(resultado) 

# resultado = 5 + 1/(1 - 1/(5**0.35))
# print(resultado) 

# Forma literal de escribir numeros complejos
# a = 5 + 7j
# b = 3 - 4j
# c = a + b
# print(c)
# # Uso de complex para definir números complejos
# d = complex(2, 3)   # (2+3j)
# e = complex(-1, -5) # (-1-5j)
# f = d * e
# print(d)


# import math

# # Calcular la raíz cuadrada de un valor
# a = 4
# b = math.sqrt(a)
# print(b)

# # Calcular el coseno de 60º
# # c = math.cos(60)
# # c = math.cos(math.pi/3)
# c = math.cos(math.radians(60))
# print(c)

print(1==1)
a = 5
b = 7
print(a!=b)