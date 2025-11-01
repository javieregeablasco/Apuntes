# def mayusculas(saludar):
#     def funcion_interna():
#         texto = saludar()
#         return texto.upper()
#     return funcion_interna

# @mayusculas
# def saludar():
#     return "hola mundo"

# print(saludar())  # "HOLA MUNDO"

# def mayusculas(saludar):
#     def funcion_interna():
#         texto = saludar()
#         return texto.upper()
#     return funcion_interna

# def saludar():
#     return "hola mundo"

# # Aplicamos manualmente el decorador
# saludar = mayusculas(saludar)

# print(saludar())  # "HOLA MUNDO"


def decorador(funcion):
  def funcion_interna(*args):         # ← paso de argumentos
    print("Inicio funcion decoradora")
    print(f"Valores recibidos: a={args[0]}, b={args[1]}")
    print(funcion(*args))             # ← paso de argumentos
    print("Fin funcion decoradora")
  return funcion_interna

@decorador
def sumar(a,b):
  return a+b 

def restar(a,b):
  return a-b 

def multiplicar(a,b):
  return a*b 

def dividir(a,b):
  return a/b 

sumar(3,5)


# def decorador(funcion):
#   def funcion_interna(**kwargs):         # ← paso de argumentos
#     print("Inicio funcion decoradora")
#     print(f"Valores recibidos: a={kwargs['a']}, b={kwargs['b']}")
#     print(funcion(**kwargs))             # ← paso de argumentos
#     print("Fin funcion decoradora")
#   return funcion_interna

# @decorador
# def sumar(a,b):
#   return a+b 

# def restar(a,b):
#   return a-b 

# def multiplicar(a,b):
#   return a*b 

# def dividir(a,b):
#   return a/b 

# sumar(a=3,b=5)


