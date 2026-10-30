import requests

# 1. URL proporcionada
url = "AQUÍ_VA_LA_URL_DEL_ARCHIVO"   # Sustituye esto por la URL real del archivo

# 2. Nombre del archivo local (ejemplo: tu nombre)
nombre_archivo = "tu_nombre.txt"

# --- Descargar archivo desde internet ---
respuesta = requests.get(url)

# Guardar contenido en el archivo
with open(nombre_archivo, "w") as archivo:
    archivo.write(respuesta.text)

print(f"Archivo descargado y guardado como: {nombre_archivo}")

# --- Abrir archivo y multiplicar cada número por 2 ---
with open(nombre_archivo, "r") as archivo:
    lineas = archivo.readlines()

# Procesar líneas y multiplicar valores
nuevas_lineas = []
for linea in lineas:
    numero = float(linea.strip())      # Cada línea contiene un número
    numero *= 2
    nuevas_lineas.append(str(numero) + "\n")

# Guardar resultado en un nuevo archivo
nombre_archivo_resultado = "resultado_" + nombre_archivo
with open(nombre_archivo_resultado, "w") as archivo:
    archivo.writelines(nuevas_lineas)

print(f"Archivo procesado y guardado como: {nombre_archivo_resultado}")
