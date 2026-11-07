# def factorial(n):
#     fact = 1
#     for i in range(n):
#         fact *= i+1
#     return fact

# print(factorial(4))
# print(factorial(20))

# def Intercambiar(mayor,menor):
# 	if mayor<menor:
# 		return menor,mayor
# 	else:
# 		return mayor,menor

# def CalcularFactorial(num):
# 	if num == 1:
# 		return 1
# 	else:
# 		return num*CalcularFactorial(num-1)

# numero1 = int(input("Número:"))
# print("El factorial es:",CalcularFactorial(numero1))


# Función Convertir_A_Segundos: Recibe una cantidad de horas, minutos y segundos 
# y calcula a cuantos segundos corresponde.
# Parámetros de entrada: hora, minutos y segundos
# Dato devuelto: Segundos totales

def Convertir_A_Segundos(h,m,s):
	return h * 3600 + m * 60 + s

# Función Convertir_A_HMS: Recibe una cantidad de segundos y debe calcular a 
# que hora, minutos y segundos corresponde 
# Parámetros de entrada: segundos
# Valores de salida: hora,minutos y segundos

def Convertir_A_HMS(seg):
	# Horas = Divisíón entera de los segundos entre 3600
	h = seg//3600
	# Decremento los segundos que me quedan por convertir
	seg = seg - h*3600
	# Minutos = División entera de los segundos entre 60
	m = seg//60
	# Decremento los segundos que me quedan por convertir
	seg = seg - m*60
	# Lo que me quedan corresponden a los segundos
	s = seg
	return h,m,s

# Escribe un programa principal con un menú donde se pueda elegir la opción de 
# convertir a segundos, convertir a horas,minutos y segundos o salir del programa.




# while True:
# 	print("1.- Convertir a segundos")
# 	print("2.- Convertir a horas, minutos y segundos")
# 	print("3.- Salir")
# 	opcion = int(input())
# 	if opcion == 1:
# 		hor = int(input("Horas:"))
# 		minu = int(input("Minutos:"))
# 		seg = int(input("Segundos:"))
# 		print("Corresponde a",Convertir_A_Segundos(hor,minu,seg),"segundos.")
# 	elif opcion == 2:
# 		segund=int(input("Segundos:"))
# 		hor,minu,seg = Convertir_A_HMS(segund)
# 		print("Corresponde a ",hor,":",minu,":",seg)
# 	elif opcion == 3:
# 		break
# 	else:
# 		print("Opción incorrecta")


# Función Convertir_A_Segundos: Recibe una cantidad de horas, minutos y segundos 
# y calcula a cuantos segundos corresponde.
# Parámetros de entrada: hora, minutos y segundos
# Dato devuelto: Segundos totales
def Convertir_A_Segundos(h, m, s):
    return h * 3600 + m * 60 + s

# Función Convertir_A_HMS: Recibe una cantidad de segundos y debe calcular a 
# que hora, minutos y segundos corresponde 
# Parámetros de entrada: segundos
# Valores de salida: hora, minutos y segundos
def Convertir_A_HMS(seg):
    # Horas = División entera de los segundos entre 3600
    h = seg // 3600
    # Decremento los segundos que me quedan por convertir
    seg = seg - h * 3600
    # Minutos = División entera de los segundos entre 60
    m = seg // 60
    # Decremento los segundos que me quedan por convertir
    seg = seg - m * 60
    # Lo que me quedan corresponden a los segundos
    s = seg
    return h, m, s

# --- Programa Principal ---

# while True:
#     print("\n--- Menú de Conversión de Tiempo ---")
#     print("1.- Convertir a segundos")
#     print("2.- Convertir a horas, minutos y segundos")
#     print("3.- Salir")
    
#     try:
#         # Nota: La sentencia 'match' funciona mejor con tipos simples como cadenas o enteros
#         opcion = int(input("Seleccione una opción: "))
#     except ValueError:
#         print("Opción incorrecta. Ingrese un número.")
#         continue # Vuelve al inicio del bucle

#     # Uso de la sentencia 'match' (Python 3.10+)
#     match opcion:
#         # Caso 1
#         case 1:
#             try:
#                 hor = int(input("Horas:"))
#                 minu = int(input("Minutos:"))
#                 seg = int(input("Segundos:"))
#                 resultado = Convertir_A_Segundos(hor, minu, seg)
#                 print(f"Corresponde a {resultado} segundos.")
#             except ValueError:
#                 print("Entrada inválida. Ingrese números enteros.")
        
#         # Caso 2
#         case 2:
#             try:
#                 segund = int(input("Segundos:"))
#                 hor, minu, seg = Convertir_A_HMS(segund)
#                 print(f"Corresponde a {hor}:{minu}:{seg}")
#             except ValueError:
#                 print("Entrada inválida. Ingrese un número entero.")
        
#         # Caso 3
#         case 3:
#             print("Saliendo del programa...")
#             break
            
#         # Caso por defecto (el equivalente al 'else' o 'default')
#         case _:
#             print("Opción incorrecta. Por favor, ingrese 1, 2 o 3.")