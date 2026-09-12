# ruta = "docs/SMX/SMX_2/Opt_Python/code/UT5/fichero.txt"
# with open(ruta, 'r', encoding='utf-8') as fichero:
#     contenido = fichero.read()
#     print(contenido)    

ruta= "docs/SMX/SMX_2/Opt_Python/code/UT5/"
archivo = "fichero.txt"
fichero = open(ruta + archivo, 'r', encoding='utf-8')
# contenido = fichero.read()
# print(contenido)



# fichero.seek(0) # Asegurarse de estar al inicio del archivo
# # Leer línea a línea usando readline()
# linea = fichero.readline()
# while linea != "":      # readline() devuelve "" cuando llega al final del archivo
#     print(linea.strip()) # strip() elimina espacios en blanco y saltos de línea
#     input("Pulsa Enter para leer la siguiente línea")
#     linea = fichero.readline()

fichero.seek(0)  # Asegurarse de estar al inicio del archivo

# # Obtener todas las líneas como una lista
# lista_lineas = fichero.readlines()


# # Recorrer la lista para trabajar con cada línea
# for linea in lista_lineas:
#     print("-"*45)
#     print("| Contenido con strip | Contenido sin strip |")
#     print(f"|{linea.strip():<21}|{linea:<21}",end='')
#     print("\r-"+"-"*44)
#     input("Pulsa Enter para leer la siguiente línea")
    


# Suponiendo que lista_lineas contiene todas las líneas del archivo
# lista_lineas = fichero.readlines()

# Cabecera de la tabla
# print(f"{'Columna 1':<12} | {'Columna 2':<15}")
# print("-" * 30)

# # Recorrer todas las líneas
# for linea in lista_lineas:
#     # Eliminar espacios y saltos de línea
#     texto = linea.strip()
    
#     # Imprimir la línea en columnas alineadas
#     print(f"|{texto:<12}|{texto:<15}|")

    # Esperar a que el usuario pulse Enter
    # input("Pulsa Enter para leer la siguiente línea")

# # Obtener todas las líneas como una lista
# lista_lineas = len(fichero.readline())
# print("Número de líneas en el archivo:", lista_lineas)




fichero.close()
