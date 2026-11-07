class Limon:
    def __init__(self, peso=200):
        print(f"Estoy en el método construtor __init__ y me han pasado el valor peso = {peso}")
        self.__peso = peso
        input("Pulsar intro para seguir")
        print("-" * 21)
        print(f"El atributo estático __peso ya tiene el valor de peso = {self.__peso}")
        input("Pulsar intro para seguir")
        
    @property
    def peso(self):
        print("Estoy dentro de property (getter) pero aún no he hecho nada")
        input("Pulsar intro para seguir...")        
        print("El valor de __peso dentro de @property es:", self.__peso)
        input("Pulsar intro para seguir...")
        print("Voy a devolver el valor de __peso")        
        return self.__peso 


    @peso.setter
    def peso(self, nuevo_peso):
        print("Estoy dentro de @peso.setter pero aun no he hecho nada")
        input("Pulsar intro para continuar...")
        print("El valor de __peso dentro de @peso.setter antes de hacer anda es:", self.__peso)
        input("Pulsar intro para continuar...")
        self.__peso = nuevo_peso
        print("-" * 21)
        print("Acabo de modificar el valor de __peso a: ", self.__peso)
        print("-" * 21)
 
print("Empezamos el programa")
print("-" * 21)
input("Pulsar intro para continuar...")
print("Voy a instanciar la clase Limon con limon = Limon(peso)")
print("Tambien puede hacerlo con limon = Limon(), entonces me asignara por defecto peso=200")
print("Antes de todo pediré por consola el peso del limón")
print("-" * 21)
input("Pulsar intro para instanciar la clase limón")
print("-" * 21)
peso = int(input("Introducir el peso del limon: "))
limon = Limon(peso)
print("-" * 21)
print("Con isinstance(objeto, clase), podemos verificar que el objeto creado pertenece a la clase correcta")
input("Pulsar intro para continuar...")
print("-" * 21)
print("¿Pertenece limon a la clase Limon?", "→", isinstance(limon, Limon))
input("Pulsar intro para continuar...")
print("-" * 21)
print("Tenemos a nuestra disposicion el objeto 'limon'")
input("Pulsar intro para continuar...")
print("-" * 21)
print("Vamos a obtener el valor de __peso")
input("Pulsar intro para continuar...")
print("-" * 21)
print("Con el método peso con decorador @property obtendremos el valor de __peso")
input("Pulsar intro para continuar...")
print("-" * 21)
input("Pulsar intro para instanciar limon.peso")
print("El valor de __peso fuera de la clase es:", limon.peso)
input("Pulsar intro para continuar...")
print("-" * 21)
print("Con el método peso con decorador @peso.setter modificaremos el valor de __peso")
input("Pulsar intro para continuar...")
nuevo_peso = int(input("Introducir el nuevo peso del limon: "))
limon.peso = nuevo_peso
print("Fin del programa")

# citron.masse = 25
# print()
# print(f"(5) Je suis dans le prog principal, je vais afficher "
#         "la masse du citron")
# print(f"La nouvelle masse de notre citron est {citron.masse} g")
# print(f"L'attribut citron.__dict__ m'indique bien le nom réel "
#           f"de l'attribut contenant la masse :")
# print(citron.__dict__)
# print()
#     # On mange la fin du citron.
# print(f"(6)  Je suis dans le prog principal, " 
#           f"je détruis l'attribut .masse")
# del citron.masse
# print(f"Ainsi, citron.__dict__ est maintenant vide :")
# print(citron.__dict__)        