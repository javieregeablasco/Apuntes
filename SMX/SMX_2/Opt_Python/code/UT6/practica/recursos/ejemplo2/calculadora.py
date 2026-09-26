print("Módulo calculadora cargado.")

if __name__ == "__main__":
   print("Solo me ejecuto si no me han importado")
   print("Me llamo: ", __name__)
else:
   print("Me han importado")
   print("Me llamo: ",__name__)

# calculadora.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "No se puede dividir por 0"
    
