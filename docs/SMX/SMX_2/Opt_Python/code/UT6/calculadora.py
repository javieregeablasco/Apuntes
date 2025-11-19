# calculadora.py
print("Módulo calculadora cargado.")

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