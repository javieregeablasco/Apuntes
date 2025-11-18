from urllib import request
from urllib.parse import urljoin
import os

# Definicion de las rutas y nombres de archivos
ruta_origen = "https://www.gutenberg.org/cache/epub/51804/"
ruta_destino = "docs/SMX/SMX_2/Opt_Python/code/UT5/"
archivo_origen = "pg51804.txt"
archivo_nuevo = "Plaga de pitones.txt"

# Construccion de las rutas completas
origen = urljoin(ruta_origen, archivo_origen)
destino = os.path.join(ruta_destino, archivo_nuevo)

# Descargar el archivo desde Gutenberg
fichero = request.urlopen(origen)
contenido_libro = fichero.read()

# Guardar el contenido en el archivo local
with open(destino, 'wb') as archivo:  # 'wb' porque es bytes
    archivo.write(contenido_libro)

# Leer el archivo 
with open(destino, 'r', encoding='utf-8') as archivo:
    for lineas in range(0,25):
        print(archivo.readline().strip()) 
    