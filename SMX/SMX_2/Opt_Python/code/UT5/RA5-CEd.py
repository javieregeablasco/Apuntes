# archivo = input("Introduce el nombre del archivo a abrir: ")

# # Construir ruta completa
# ruta = "C:/Users/titan/Documents/GitHub/githubpages/Apuntes/docs/SMX/SMX_2/Opt_Python/code/UT5/"


# try:
#     with open(ruta+archivo, "r", encoding="utf-8") as fichero:
#         print("\nPrimeras 10 líneas del archivo:")
#         for i in range(10):
#             linea = fichero.readline()
#             print(linea.strip())

# except FileNotFoundError:
#     print("Error de acceso: El archivo no existe.")
# except UnicodeDecodeError:
#     print("Error al leer el archivo: Posible codificación incorrecta.")
# except Exception:
#     print("Error inesperado al abrir el archivo.")

print(dir())