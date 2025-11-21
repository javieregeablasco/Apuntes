class LeerArchivo:
    def __init__(self, ruta, nombre):
        self.ruta = ruta
        self.nombre = nombre        
        self.lista_lineas = []
        self.plano_lineas = ""
        self.cantidad = 0
        self.lectura_exitosa = False
    
        try:
            with open(self.ruta+self.nombre, 'r', encoding='utf-8') as file:
                self.lista_lineas = file.readlines()
                file.seek(0)
                self.plano_lineas = file.read()
                self.cantidad = len(self.lista_lineas)
                self.lectura_exitosa = True
        except FileNotFoundError:
            print(f"Error: El archivo '{self.nombre}' no se encontró en la ruta '{self.ruta}'.")
        except IOError:
            print(f"Error: No se pudo abrir el archivo '{self.nombre}'.")
        

    def leer_lineas(self):
        while True:
          indice_linea = input(f"Introduce el número de línea a leer entre (1 y {self.cantidad})/"
          "o 'salir' para terminar: ")

          if indice_linea.lower() == 'salir':
            print("Saliendo de la lectura de líneas...")
            break

          if not indice_linea.isdigit():
            print("Error: Debes introducir un número")
            continue
          
          indice_linea = int(indice_linea)
          
          if not(1 <= indice_linea <= self.cantidad): 
            print("Error: Debes introducir un número entre 1 y", self.cantidad + 1)
            continue
                     
          print(f"La linea {indice_linea} tiene el siguiente contenido:")
          print(self.lista_lineas[indice_linea - 1].strip())
        
    def leer_linea_a_linea(self):
        for linea in self.lista_lineas:
            print(linea.strip())
            input("Pulsa Enter para continuar...")

    def leer_todo(self):
        return self.plano_lineas
            
# Programa principal
ruta_defecto = "docs/SMX/SMX_2/Opt_Python/code/UT5/"
archivo_defecto = "archivo.txt"

print("|------------------------------------------------------------|")
print("| Bienvenido a mi programa de apertura y lectura de archivos |")
print("|------------------------------------------------------------|")
input("(Pulsa Enter para continuar)")

nombre_archivo = input("Introduce el nombre del archivo a abrir: ")
ruta_archivo = input("Introduce la ruta del archivo a abrir: ")

if ruta_archivo == "":
    ruta = ruta_defecto
if nombre_archivo == "":
    nombre = archivo_defecto

archivo = LeerArchivo(ruta, nombre)


print("|----------------------------------------|")
print("| (1) Para leer la totalidad del archivo |")
print("| (2) Para leer el archivo linea a linea  |")
print("| (3) Para leer una linea del archivo    |")
print("| (0) Para salir del programa            |")
eleccion  = input("Elegir la opción (0, para salir): ")

match eleccion:
    case "0":
        print("Saliendo del programa...")
        exit()
    case "1":
        print( "Contenido completo del archivo:")
        print(archivo.leer_todo())
    case "2":
        archivo.leer_linea_a_linea()
    case "3":
        archivo.leer_lineas()
    case "_":
        print("Opción no válida. Por favor, elige una opción del 0 al 4.")
