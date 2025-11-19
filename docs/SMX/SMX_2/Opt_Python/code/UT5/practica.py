class LeerArchivo:
    def __init__(self, ruta_archivo, nombre_archivo):
        self.ruta = ruta_archivo
        self.nombre = nombre_archivo        

    def leer_todo(self):
        with open(self.ruta, 'r', encoding='utf-8') as f:
            contenido = f.read()
        return contenido

    def leer_linea(self):
        with open(self.ruta, 'r', encoding='utf-8') as f:
            linea = f.readline()
        return linea
    
    def leer_lineas(self):
        while True:
          indice_linea = input("Introduce el número de línea a leer entre (1 y {self.contar_lineas()})/"
          "o 'salir' para terminar: ")

          if indice_linea.lower() != 'salir':
            return None

          if not indice_linea.isdigit():
            print("Error: Debes introducir un número")
            continue

          indice_linea = int(indice_linea)
          if (int(indice_linea) not in range(1, self.contar_lineas()+1)): 
            print("Error: Debes introducir un número entre 1 y", self.contar_lineas())
            continue
                     
          with open(self.ruta, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
          return lineas[indice_linea - 1]

    def contar_lineas(self):
        return len(self.leer_lineas())

    def buscar_texto(self, texto):
        lineas_encontradas = []
        with open(self.ruta, 'r', encoding='utf-8') as f:
            for numero, linea in enumerate(f, start=1):
                if texto in linea:
                    lineas_encontradas.append((numero, linea.strip()))
        return lineas_encontradas


# Programa principal
ruta_defecto = "docs/SMX/SMX_2/Opt_Python/code/UT5/"

print("|------------------------------------------------------------|")
print("| Bienvenido a mi programa de apertura y lectura de archivos |")
print("|------------------------------------------------------------|")
input("(Pulsa Enter para continuar)")

nombre_archivo = input("Introduce el nombre del archivo a abrir: ")
ruta_archivo = input("Introduce la ruta del archivo a abrir: ")
if ruta_archivo == "":
    ruta = ruta_defecto
  
archivo = LeerArchivo(ruta_archivo, nombre_archivo)

print("Contenido completo:")
print(archivo.leer_todo())
print("\nLíneas del archivo:")
print(archivo.leer_lineas())
print("\nNúmero de líneas:", archivo.contar_lineas())
print("\nBúsqueda de la palabra 'python':")
print(archivo.buscar_texto("python"))
