# num_entero = 5       # tipo int
# num_decimal = 2.5    # tipo float

# resultado = num_entero + num_decimal  # Python convierte automáticamente num_entero a float

# print(resultado)      # 7.5
# print(type(resultado))  # <class 'float'>

# # Ejemplo de casting implícito
# num_entero = 5       # tipo int
# num_decimal = 2.5    # tipo float

# resultado = num_entero + float(num_decimal)  # Python convierte automáticamente num_entero a float
# print(resultado)      # 7.5
# print(type(resultado))  # <class 'float'>

# Crear un set
# frutas = {"manzana", "plátano", "cereza", "manzana"}

# print(frutas)  # {'manzana', 'plátano', 'cereza'}  -> elimina duplicados
# print(type(frutas))  # <class 'set'>


# Sintaxis de string a decimal
# a = "1234"
# b = int(a)
# print(b, type(b))

# list = ["la", "lista",  "de", "la", "compra", "la", "hare", "manyana"]
# print(set(list))
# a = 13.5
# print("Bueno") if type(a)==float else print("malo")  
while True:
  variable = input("Introducir cualquier cosa: ")
  if variable == "salir": break
  print(type(variable))
print("Programa terminado")