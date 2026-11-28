# archivo = "fichero2.txt" 
# with open(ruta + archivo, "a", encoding="utf-8") as fichero:
#     for i in range(5):
#         fichero.write(f"Línea añadida número {i+1}\n")

import os

# Definicion de las rutas y el archivo
ruta_origen = "docs/SMX/SMX_2/Opt_Python/code/UT5/"
ruta_destino = "docs/SMX/SMX_2/Opt_Python/code/UT5/copias/"
archivo = "fichero.txt"
archivo_nuevo = "fichero_nuevo.txt"

# Construccion de las rutas completas
origen = os.path.join(ruta_origen, archivo)
destino = os.path.join(ruta_destino, archivo_nuevo)

# Asegurarse de que la carpeta de destino existe
if not os.path.exists(ruta_destino):
    os.makedirs(ruta_destino)

# Renombrar o mover el archivo
os.rename(ruta_origen + archivo, ruta_destino + archivo_nuevo)
print("Archivo renombrado o movido correctamente.")        