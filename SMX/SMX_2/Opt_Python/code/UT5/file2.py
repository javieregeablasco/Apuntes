ruta= "docs/SMX/SMX_2/Opt_Python/code/UT5/"
archivo = "fichero.txt"

# with open(ruta+archivo, 'r') as fichero:
#     contenido = fichero.read()
#     print(contenido)


with open(ruta + archivo, 'r', encoding='utf-8') as fichero:
    lista_lineas = fichero.readlines()
    for linea in lista_lineas:
        print(linea.strip()) # evita doble salto de línea    