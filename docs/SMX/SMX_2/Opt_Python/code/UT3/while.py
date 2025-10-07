# i = 1
# while i<=10:
#   print(i)
#   i+=1
# print("Programa finalizado")  

# condicion = True
# i = 1

# while condicion:
#   print(i)
#   if i==10: condicion = False
#   i += 1

# print("Programa finalizado")  

# import time

# numero = int(input("Introducir un número entre 1 y 10: "))

# while numero < 1 or numero > 10:
#   print("El numéro no es correcto")
#   time.sleep(1)
#   numero = int(input("Introducir un número entre 1 y 10: "))

# print(f"El numéro introducido es: {numero}")

# print("Programa que calcula la raíz cuadrada de un valor")
# numero = int(input("Introducir un valor positivo: "))
# intentos = 1

# while numero < 0 and intentos < 5:
#   print("El valor introducido no es correcto")
#   intentos +=1  
#   print("Intento: ", intentos)
#   numero = int(input("Introducir un valor positivo: "))

# if numero >0: print("El valor de la raíz cuadrada es:", numero**0.5)
# else: print("No se ha podido calcular la raíz cuadrada del número introducido.")

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

# print("Programa terminado")  


# print("Programa que calcula la raíz cuadrada de un valor")
# numero = int(input("Introducir un valor positivo: "))
# intentos = 1

# while numero < 0:
#   intentos +=1  
#   if intentos>5: break
#   print("El valor introducido no es correcto")
#   print("Intento: ", intentos)
#   numero = int(input("Introducir un valor positivo: "))

# if numero >0: print("El valor de la raíz cuadrada es:", numero**0.5)
# else: print("No se ha podido calcular la raíz cuadrada del número introducido.")

print("Programa que solo muestra los valores pares")
numero = int(input("Introducir un valor positivo: "))

for i in range(numero+1):
  
  if i%2 != 0: 
    continue
  
  else: 
    print("Resultado división:",i)
    
print("Programa finalizado.")
