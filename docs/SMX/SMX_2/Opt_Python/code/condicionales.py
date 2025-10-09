# numero = int(input("Introducir un número entre 1 y 10: "))

# while numero<0 or numero>10:
#    print("Introducir de nuevo el numero")
#    numero = int(input("Introducir un número entre 1 y 10: "))

# print("Programa terminado")


# condicion = True
# contador = 0

# while condicion:
#    contador += 3
#    print("Iteracion:",contador)
#    if contador==10:
#       condicion= False

# print("Programa terminado")



# for i in range(1, 500, 1):
#   if i%7==0 and i%8==0:
#     print(i)

    

# cadena = "Python es mi lenguaje de programacion favorito"
# letra_a_eliminar = "a"

# for letra in cadena:
#   if letra == letra_a_eliminar:
#     continue
#   print(letra, end="") #end="" evita el salto de línea

# # 7.2.2 ej 1
# for i in range(1, 21):
#   if i % 2 == 0:
#     print(i)

# 7.2.2 ej 2
# numero = int(input("Introducir un número: "))

# for i in range(1, 11):
#     print("Resultado= ", numero * i)


# # 7.2.2 ej 3
# frutas = ["manzana", "pera", "naranja", "plátano", "kiwi"]
# colores = ["rojo", "verde", "naranja", "amarillo", "verde", "morado", "azul"]

# for fruta, color in zip(frutas, colores):
#   print("Fruta:",fruta + ", color:", color)

# lista = ["Este", "es", "un", "gran", "día"]

# for (indice,valor) in enumerate(lista):
#     print("Iteración:", indice, "Elemento:", valor)


# continuar = True

# while continuar:
#   opcion = int(input("Elige una opción (1, 2 o 3): "))
#   match opcion:
#     case 1:
#       print("Has elegido la opción 1.")
#     case 2:
#       print("Has elegido la opción 2.")
#     case 3:
#       print("Has elegido la opción 3.")
#     case _:
#       print("Opción no válida.")
  
#   decision = input("Desea continua, intro para 'Sí', teclar 'no' para salir: ") 
#   if decision.lower() == "no": 
#     print("Programa finalizado")
#     # continuar = False
#     break

# print("Salida del bucle while")

  


# import os

# try:
#     ruta_archivo = os.path.join(os.path.dirname(__file__), "datos.txt")
#     with open(ruta_archivo, "r") as archivo:
#         contenido = archivo.read()
#         numero = int(contenido)  # puede lanzar ValueError si el contenido no es número
# except FileNotFoundError:
#     print("El archivo no existe.")
# except ValueError:
#     print("El contenido del archivo no es un número.")
# else:
#     print("El número leído es:", numero)
# finally:
#     print("Operación de lectura finalizada")


  #print("Vamos por la letra:", letra)





# calificacion = 7

# if calificacion >=5 & calificacion <7:
#  print("Enhorabuena, has aprobado el examen")
#  #pass se usa pass como placeholder para que no haya error

# elif calificacion >= 7 and calificacion<=10:
#   print("Excelente examen")   

# else:
#  print("Lamentablemente no has aprobado el examen")

# # seguir con el programa

# notas = [1,2,4,7,9]

# calificacion = 8

# if calificacion in notas:
#   print("Excelente examen")   
# elif calificacion >=5:
#   print("Enhorabuena, has aprobado el examen")
# else:
#   print("Lamentablemente no has aprobado el examen")

# # seguir con el programa

# notas = [1,2,4,7,9]

# calificacion = 8

# if calificacion in notas:
#    print("Al menos 1 alumno ha sacado la nota de", calificacion)   
# else:
#    print(f"Ningun alumno ha sacado un {calificacion}")

# # # seguir con el programa



# calificacion = 70

# if calificacion < 0 or calificacion > 100:
#     print("La calificación debe estar en la escala de 0 a 100")
   
# elif calificacion >= 95 and calificacion <= 100:
#     print("Excelente")
# elif calificacion >= 85 and calificacion <= 94:
#     print("Muy bien")
# elif calificacion >= 75 and calificacion <= 84:
#     print("Bien")
# elif calificacion >= 70 and calificacion <= 74:
#     print("Regular")
# else:
#     print("Insuficiente")

# for i in "interacción":
#   print("Iteración: ", i)

# lista= ["Este", "es", "un", "gran", "día"]

# for i in lista:
#   print("Iteración: ", i)

# lista = ["Este", "es", "un", "gran", "día"]

# for i in range(len(lista)):
#     print("Iteración:", i, "Elemento:", lista[i])

# lista = ["Este", "es", "un", "gran", "día"]

# for indice,valor in enumerate(lista):
#     print("Iteración:", indice, "Elemento:", lista[indice])

# nombres = ["Ana", "Luis", "Marta"]
# edades = [25, 30, 22]

# for nombre, edad in zip(nombres, edades):
#     print(nombre, "tiene", edad, "años")

# cantidad = 0

# for numero in range(1, 501, 1):
#   #print(numero)
#   if numero % 6 == 0 and numero % 7 == 0:
#     cantidad =+ 1
#     print(numero)
# print("Cantidad total de número encontrados:",cantidad)

# from random import randint

# print("¡Bienvenido al juego: 'Adivina el número'")
# numero = randint(1,10) # genera un entero entre 1 y 10
# intentos = 1 # inicializamos la variable incrementable

# while True: #definimos un bucle while infinito
#   valor = int(input("Introducir un número entero entre 1 y 10: "))
#   if valor == numero:
#     print(f"Has adivinado el número correcto {numero} después de {intentos} intentos")
#     break
#   else:
#     print(f"{valor} no es el numero correcto, intentalo nuevamente\n")
#   intentos += 1    

# print(len("pablo"))

# palabra = "Python"
# letra_a_encontrar = "o"

# for letra in palabra:
#   if letra == letra_a_encontrar:
#     print(f"Hemos encontrado la letra {letra_a_encontrar}")
#     # print("hemos encontrado la letra ", letra_a_encontrar)
#     break
#   print(f"Vamos por la letra: {letra}")
#   #print("Vamos por la letra:", letra)

# cadena = "Python es mi lenguaje de programacion favorito"
# letra_a_eliminar = "a"

# for letra in cadena:
#   if letra == letra_a_eliminar:
#     continue
#   print(letra, end="") #end="" evita el salto de linea
 

# while True:
#     entrada = input("Introduce un número (o 'salir' para terminar): ")
    
#     if entrada.lower() == "salir":  # comprueba si el usuario quiere salir
#         print("Programa terminado.")
#         break
    
#     try:
#         numero = int(entrada)
#         resultado = 10 / numero
#         print("El resultado es:", resultado)
#     except ValueError:
#         print("¡Eso no es un valor numérico!")
#     except ZeroDivisionError:
#         print("Estás intentando dividir por cero.")


# print("Tabla de multiplicación hasta 10")
# input("Pulsar enter para continuar")

# for i in range(1, 11):  # bucle externo
#     print(f"Tabla del {i}:")
#     for j in range(1, 11):  # bucle interno
#         producto = i * j
# #        if producto % 7 == 0:  # si el producto es múltiplo de 7
#  #           print(f"  {i} x {j} = {producto} (múltiplo de 7, saliendo del bucle interno)")
#   #          break  # sale del bucle interno
#         print(f"  {i} x {j} = {producto}")

# print("Tabla de multiplicación hasta 10")
# input("Pulsar enter para continuar")

# for i in range(1, 11):  # bucle externo
#     print("Tabla del: ", i)
#     for j in range(1, 11):  # bucle interno
#         if j == 7:
#             continue
#         producto = i * j
#         print(i, "x", j, "=", producto)

# print("Tabla de multiplicación hasta 10")
# input("Pulsar enter para continuar")

# salir = False

# for i in range(1, 11):  # bucle externo
#     print("Tabla del:", i)
#     for j in range(1, 11):  # bucle interno
#         if i == 5 and j > 7:
#             salir =True
#             break
#         print(i, "x", j, "=", i * j)
#     if salir:
#         print("Limite alcanzado, finalizando el programa.")
#         break 
