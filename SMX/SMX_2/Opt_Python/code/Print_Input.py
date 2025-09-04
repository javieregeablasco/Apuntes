# a = "EsTa Es UnA cAdEnA dE cArÁctErEs"
# print(a[2:-2])

# #Separadores
# print("A", "B", "C")                     
# print("A", "B", "C", sep="")                     
# print("A", "B", "C", sep=" ") # sep=" " es el valor por defecto                
# print("A", "B", "C", sep=",")            
# print("A", "B", "C", sep=" >>> ")            
# print("A", "B", "C", sep=" \U0001F600 ") # sep admite símbolos soportados por python            

# Fin de linea
# print("No saltamos de linea.", end="")             
# print(" Este contenido sigue en la primera linea.")             
# print("\nSaltamos una linea ANTES Y DESPUES de pintar el texto.\n")             
# print("Ponemos un final de linea personalizado y no saltamos de linea.", end="...")
# print(" Este texto sigue en la linea anterior")             
# print("Final de linea personalizado CON salto de linea", end="... \n") 
# print("Final de linea con caracteres especiales", end=" ✅\n")  

#tabulacion
# print("Menu del dia")
# print("\tPrimer plato.")
# print("\tSegundo plato.")
# print("\t Postre.")
# print("-------------------------")
# print("---\tPrecio\tFinal.")

# print("Menu del dia")
# print("\tPrimer plato.")
# print("\tplato \rSegundo")

# print("Menu del dia")
# print("Primer plato.")
# print("Segundo plato.", end="")
# print("\r-sobreescribo-")

# valor = 12
# texto = "El precio del articulo es de"
# print(texto, valor,"euros")

# valor1 = 12
# valor2 = 5
# print("El resultado de 12 x 5 son:",valor1*valor2,"exactos")

# aprobado = 7.2
# print("Aprobado" if aprobado >= 5 else "Suspenso")

valor1 = 5
valor2 = 7
valor3 = 35
texto = "euros"
texto1 = "Pablo"

# print("El resultado de la mutiplicacion de",valor1,"por",valor2,"es",valor3,texto)
# # con cadenas f
# print(f"El resultado de la mutiplicacion de {valor1} por {valor2} es {valor3} {texto}")
# # Tambien se ejecutan funciones dentro de f
# print(f"El resultado de la mutiplicacion de {valor1} por {valor2} es {valor1*valor2} {texto}")
# # Tambien se ejecuta código dentro de f
# print(f"El resultado del examen de {texto1} cuya nota el {valor2} es {"Aprobado" if valor2 >= 5 else "Suspenso"}")

# print("El resultado del examen de {} cuya nota el {} es {}".format(texto1,valor2,"Aprobado" if valor2 >= 5 else "Suspenso"))


# # for x in range(1, 11):

# #     print(x,"\t",x*x,"\t", x*x*x, sep="")

# #     # Note use of 'end' on previous line

# valor1 = 5.2536524
# valor2 = 7.3915896
# print(f"El resultado de la mutiplicacion de {valor1 :.2f} por {valor2} es {valor1*valor2}")

# print("Representacion en hexadecimal de 255: {:X}".format(255)) 

# hexa = 255
# print(f"Representacion en hexadecimal de 255: {hexa :X}") 


# print("Representacion en binario de 8: {:b}".format(8))      
# print("Equivalente en porcentaje de 0.85: {:.1%}".format(0.85))   



# print("El valor es {:.2f}".format(3.14159))  # 3.14



# print("Número: {:05d}".format(42))  # 00042
# print("Precio: {:,}".format(12000000))  # 12,000
# print("Representacion en hexadecimal de 255: {:X}".format(255)) 
# print("Representacion en binario de 8: {:b}".format(8))      
# print("Equivalente en porcentaje de 0.85: {:.1%}".format(0.85)) 

# # definimos una variable de tipo lista
# datos = []
# # Usamos un iterador para llenar la lista
# for i in range(3):
#   dato = input("Introducir cualquier cosa: ")
#   datos.append(dato)
# # Usamos otro iterador para leer la lista y sacamos el tipo de variable que contiene
# # for i in range(3):
# #  # print(f"Posición {i}, valor {datos[i]}, tipo {type(datos[i])}") 
# #   print(f"Posición {i}, valor {datos[i]}, tipo: {'string' if isinstance(datos[i],str) else ''}")

# dato1 = input("Introducor un valor: ")
# dato2 = input("Introducor un valor: ")
# dato3 = input("Introducor un valor: ")
# print(f"La suma de {dato1} + {dato2} + {dato3} es: {dato1+dato2+dato3}")

# cadena1 = "10"
# cadena2 = "20"
# valor1 = int(cadena1)
# valor2 = int(cadena2) 
# print("sin casting", cadena1+cadena2)
# print("con casting", valor1+valor2)

# nombre = input("Introducir nombre")
# print(f"Hola {nombre}, buenos días")

# variable = int(input("Introduce un valor: "))
# print("El tipo de la variable es: ", type(variable))


# cadena = "1234"
# numero = int(cadena)
# print(type(numero))

cadena1 = "10.125"
valor1 = float(cadena1)
print("sin casting", type(cadena1))
print("con casting", type(float(valor1)))