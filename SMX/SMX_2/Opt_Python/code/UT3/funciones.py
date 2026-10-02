# print("A", "B", "C")                     
# print("A", "B", "C", sep="") # sin separacion entre los datos                     
# print("A", "B", "C", sep=" ") # sep=" " es el valor por defecto                
# print("A", "B", "C", sep=",")            
# print("A", "B", "C", sep=" >>> ")            
# print("A", "B", "C", sep=" \U0001F600 ") # sep admite símbolos soportados por python

# print("Menu del dia")
# print("\tPrimer plato.")
# print("\tSegundo plato.")
# print("\t Postre.")
# print("-------------------------")
# print("---\tPrecio\tFinal.")

# print("Menu del dia")
# print("Primer plato.")
# print("Segundo plato.", end="")
# print("\r-sobreescribo-")

# valor1 = 12
# valor2 = 5
# print("El resultado de 12 x 5 son:",valor1*valor2,"exactos")

# def sumar(a, b):
#     return a + b

# resultado = sumar(3, 5)  # sumar(a=3, b=5)

# def sumar_todo(*args):
#     print("Tipo de variable arg: ", type(args))
#     return sum(args)

# print(sumar_todo(1, 2, 3, 4))  

# def mostrar_info(**kwargs):
#     print("Tipo de variable kwargs: ", type(kwargs))
#     for clave, valor in kwargs.items():
#         print(f"{clave}: {valor}")

# mostrar_info(nombre="Luis", edad=25, ciudad="Valencia")

# def funcion():
#     print("Ejecución de la funcion")
#     return
#     print("No llega") # esta línea no se ejecutará

# funcion()
#  
# def funcion(a,b,c):
#     return a*10, b-5, c-32
    
# funcion(10,20,40)

# print("Solo recuperamos el primer valor:",funcion(10,20,40)[0])
# print("Solo recuperamos el segundo valor:",funcion(10,20,40)[1])
# print("Solo recuperamos el tercer valor:",funcion(10,20,40)[2])


def mi_decorador(funcion):
    def nueva_funcion(a, b):
        print("Se va a llamar")
        c = funcion(a, b)
        print("Se ha llamado")
        return c
    return nueva_funcion

@mi_decorador
def suma(a, b):
    print("Entra en funcion suma")
    return a + b

suma(5,8)