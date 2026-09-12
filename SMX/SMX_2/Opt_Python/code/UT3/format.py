# Utilizando el nombre de variables:
# frase2 = "Hola, mi nombre es {nombre} y tengo {edad} años.".format(nombre, edad)
## Sintaxis más corta, definimos las variables 
# frase2 = "Hola, mi nombre es {nombre} y tengo {edad} años.".format(nombre="Carlos", edad=30)
# print(frase2)

# nombre = "Carlos"
# edad = 30
# frase1 = "Tengo {1} años y me llamo {0}.".format(nombre, edad)
# print(frase1)

# frase2 = "Hola, mi nombre es {nombre} y tengo {edad} años.".format(nombre="Carlos", edad=32)
# print(frase2)

# nombre = 'Pablo'
# print(f'{nombre:>20}')    # Justificado a la derecha
# print(f'{nombre:>30}')    # Justificado a la derecha
# print(f'{nombre:<20}')    # Justificado a la izquierda
# print(f'{nombre:^20}')    # Centrado
# print(f'{nombre:_^20}')   # Centrado con relleno '_'

# pi = 3.14159
# print(f"{3.14159:>10.3f}") # Alinea a la derecha en ancho de 10 espacios con 3 decimales
# print(f"{255:0>6x}")         # Hexadecimal con relleno de ceros: '000ff'
# print(f'{pi:010.5f}') # Cinco decimales y ceros a la izquierda
# print(f'{pi:10.0f}')  # Igual que el primero, con cero decimales
# print(f'{pi:10.4e}')  # Igual que el primero, en notación científica
# pi = 3.14159265359
# print(f"{pi:>10.3f}") # Alinea a la derecha, ancho de 10 caracteres, flotante de 3 decimales
# print(f"{255:0>6x}") # Hexadecimal, centrado derecha con relleno de ceros y anche de 6 caracteres
# print(f'{pi:010.5f}') # Cinco decimales ancho de 10 caracteres y relleno de ceros
# print(f'{pi:.0f}')  # Cero decimales ancho de 10 caracteres
# print(f'{pi:10.4e}')  # Notación científica, ancho 10 caracteres

x=5
print("-"*33)
print(f"| {'d':^{x}} | {'b':^{x}} | {'o':^{x}} | {'x':^{x}} |")
# print("|   d   |   b   |   o   |   x   |")
print("-"*33)
for n in range(25):
    print(f"| {n:^5d} | {n:5b} | {n:5o} | {n:<5x} |")
print("-"*33)