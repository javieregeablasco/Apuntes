import calculadora, sys, importlib

# print(calculadora.__name__)
print(sys.path)
# sys.path.append("C:\\Users\\titan\\Documents\\GitHub\\githubpages\\Apuntes\\docs\\Experimentos")
print("Nombre del módulo que se está ejecutando", __name__)

# sys.path.remove("C:\\Users\\titan\\Documents\\GitHub\\githubpages\\Apuntes\\docs\\Experimentos")
importlib.reload(calculadora)