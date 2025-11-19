---
ciclo: CFGM - Técnico en Sistemas Microinformáticos y Redes
title: Introducción a la programación en Python
modulo number: 
lesson: UD. 5 - Acceso a datos básico  
author: Javier Egea Blasco  
layout: default  
year: 25-26  
keywords: SMX, Python
schedule: 96h - 3h/w
---

# **UT 5 - Manejo de ficheros**

![Descripción de la imagen](../Opt_Python/img/UT5/dataaaccess.webp){ .cincozero }

<br>

**Resultados de aprendizaje y criterios de evaluacion que se evaluarán en esta unidad.**  

|RA5. Realiza operaciones de entrada y salida de información, utilizando procedimientos específicos del lenguaje y librerías de clases.|
|-|
|**d)** Se han utilizado ficheros para almacenar y recuperar información.|
|**e)** Se han creado programas que utilicen diversos métodos de acceso al contenido de los ficheros.|

<br>

## **1 - Manejo de ficheros en Python**
El manejo de archivos permite leer y escribir información en ficheros almacenados en el sistema. Python proporciona funciones que facilitan este proceso, y a continuación veremos cómo acceder a un archivo y leer su contenido.

### **1.1 - Apertura y lectura de un fichero**

#### **1.1.1 - Abrir un archivo con open()**
Para acceder a un archivo, en primer lugar debemos abrirlo indicando **la ruta y el nombre del fichero** al que queremos acceder. Además, debemos especificar **el modo de apertura** (p.e., lectura `r` o escritura `w`).

```py
ruta= "docs/SMX/SMX_2/Opt_Python/code/UT5/"
archivo = "fichero.txt"
fichero = open(ruta + archivo, 'r', encoding='utf-8')
```
**Nota:** La ruta puede ser absoluta o relativa. En este caso es relativa a la carpeta desde la que se ejecuta el entorno de Python, lo que a veces puede resultar poco práctico si cambiamos de ubicación el proyecto.

#### **1.1.2 - Leer un archivo**
Una vez abierto el archivo, podemos leer su contenido utilizando métodos como **read()**, **readline()** o **readlines()**.

- **Ejemplo con read():**
```py
# Leer todo el contenido del archivo
contenido = fichero.read()
print(contenido)
```
    Si el archivo es muy grande, es recomendable leerlo línea por línea para evitar cargar todo el contenido en memoria de una sola vez.  
    <br>

- **Ejemplo con readline():**  
readline() lee una línea del archivo cada vez que se llama. 
```py
fichero.seek(0) # Asegurarse de estar al inicio del archivo

# Leer línea a línea usando readline()
linea = fichero.readline()

# Recuperar la cantidad de líneas del objeto fichero
cantidad_lineas = len(fichero.readline())
print("Número de líneas en el archivo:", cantidad_lista_lineas)

# Leer todas las líneas del objeto fichero
while linea != "":      # readline() devuelve "" cuando llega al final del archivo
    print(linea.strip()) # strip() elimina espacios en blanco y saltos de línea
    input("Pulsa Enter para leer la siguiente línea")
    linea = fichero.readline()
```
<br>

- **Ejemplo con readlines():**  
readlines() lee todas las líneas del archivo de una vez y devuelve **una lista**, donde cada elemento es una línea del fichero.
```py
fichero.seek(0)  # Asegurarse de estar al inicio del archivo

# Obtener todas las líneas como una lista
lista_lineas = fichero.readlines()


# Recorrer la lista para trabajar con cada línea
for linea in lista_lineas:
    print("-"*45)
    print("| Contenido con strip | Contenido sin strip |")
    print(f"|{linea.strip():<21}|{linea:<21}",end='')
    print("\r-"+"-"*44)
    input("Pulsa Enter para leer la siguiente línea")
```     

#### **1.1.2 - Cerrar un archivo con close()**
El método close() cierra el fichero referenciado por el objeto creado con open().  
Es importante cerrar el archivo después de terminar las operaciones para liberar recursos del sistema. Si no se cierra explícitamente un fichero, Python intentará cerrarlo cuando estime que ya no se va a usar más.

```py  
fichero.close()
```

#### **1.1.3 - Abrir un archivo con with**
Una forma más segura y conveniente de manejar archivos en Python es utilizando la declaración **with**. Esta estructura garantiza que el archivo se cierre automáticamente al finalizar el bloque de código, **incluso si ocurre una excepción**.

- **Ejemplo con read():**  
```py
ruta= "docs/SMX/SMX_2/Opt_Python/code/UT5/"
archivo = "fichero.txt"

with open(ruta+archivo, 'r', encoding='utf-8') as fichero:
    contenido = fichero.read()
    print(contenido)
```
<br>

- **Ejemplo con readline():**
```py
with open(ruta + archivo, 'r') as fichero:
    linea = fichero.readline()
    while linea != "":       # mientras no esté vacía
        print(linea, end="") # evita doble salto de línea
        linea = fichero.readline()
```
<br>    

- **Ejemplo con readlines():**
```py
with open(ruta + archivo, 'r') as fichero:
    lista_lineas = fichero.readlines()
    for linea in lista_lineas:
        print(linea, end="") # evita doble salto de línea
``` 

#### **1.1.4 - Argumentos de open()**
Cuando se trabaja con archivos es importante especificar **el modo de apertura**. Ese modo indica cómo se abrirá el archivo (solo lectura, escritura, añadir, etc.).  
De esta forma el programador puede controlar el comportamiento del acceso al archivo y **la gestión de posibles excepciones**.

| Modo   | Significado         | Permite leer | Permite escribir | Crea archivo si no existe | Sobrescribe archivo | Posición inicial |
| ------ | ------------------- | ------------ | ---------------- | ------------------------- | ------------------- | ---------------- |
| `'r'`  | Lectura             | ✔            | ❌                | ❌                         | ❌                   | Inicio           |
| `'w'`  | Escritura           | ❌            | ✔                | ✔                         | ✔                   | Inicio           |
| `'a'`  | Añadir (append)     | ❌            | ✔                | ✔                         | ❌                   | Final            |
| `'r+'` | Lectura y escritura | ✔            | ✔                | ❌                         | ❌                   | Inicio           |
| `'w+'` | Lectura y escritura | ✔            | ✔                | ✔                         | ✔                   | Inicio           |
| `'a+'` | Lectura y escritura | ✔            | ✔                | ✔                         | ❌                   | Final            |
| `'x'`  | Creación exclusiva  | ❌            | ✔                | ✔ (solo si no existe)     | ❌                   | Inicio           |

!!! warning "Notas importantes"
    - Si el archivo no existe, 'r' produce error, mientras que 'w', 'a', 'w+', 'a+', y 'x' lo crean.
    - El modo 'x' sirve para crear archivos nuevos evitando sobrescrituras: si el archivo ya existe → lanza error.
    - Cuando el archivo se abre en modo añadir ('a' o 'a+'), la escritura siempre se realiza al final del archivo.

#### **1.1.5 - Tarea RA5-CEd** 
!!! excercise "Manejo de excepciones al abrir un archivo" 
    
    1. Crear un archivo de texto con 20 líneas de texto. 
    1. Escribir un programa en Python que haga lo siguiente:    
        - Solicite al usuario que ingrese el nombre del archivo a abrir.
        - Intente abrir el archivo en modo lectura 'r' usando **un bloque try**.
        - Si ocurre una excepción, cse capturará y manejará con los siguientes casos específicos:
            - Si ocurre un FileNotFoundError, se mostrará el mensaje: "Error de acceso: El archivo no existe."
            - Si ocurre un UnicodeDecodeError, se mostrará el mensaje: "Error al leer el archivo: Posible codificación incorrecta."
            - Para cualquier otra excepción, se mostrará el mensaje: "Error inesperado al abrir el archivo."
        - Si el archivo se abre correctamente, leer y mostrar las 10 primeras líneas del archivo.

<br>

### **1.2 - Escritura de un archivo**

- **Ejemplo de escritura en un archivo usando with:**
```py
ruta = "docs/SMX/SMX_2/Opt_Python/code/UT5/"
archivo = "fichero2.txt"

with open(ruta + archivo, "w", encoding="utf-8") as fichero:
    fichero.write("Esta es una línea escrita en el archivo.\n")
```

    **Explicación del código**:  
    
    - Se abre el archivo en modo escritura ('w'). Si el archivo ya existe, se sobrescribe.  
    - Se escribe una línea de texto en el archivo utilizando el método write().
    
    <br>


- **Otro ejemplo:**
```py
ruta = "docs/SMX/SMX_2/Opt_Python/code/UT5/"
archivo = "fichero2.txt" 
with open(ruta + archivo, "a", encoding="utf-8") as fichero:
    for i in range(5):
        fichero.write(f"Línea añadida número {i+1}\n")
```
    **Explicación del código**:  
    - Se abre el archivo en modo añadir ('a'). Si el archivo no existe, se crea.  
    - Se añaden cinco líneas al final del archivo utilizando un bucle for y el método write().  

### **1.3 - Renombrado y ruta a un archivo**
Para renombrar un archivo o moverlo a otra ubicación, podemos utilizar el módulo `os` de Python, que proporciona funciones para interactuar con el sistema operativo.  

- `os.rename(origen, destino)` : Renombra un archivo o lo mueve si el destino incluye una ruta diferente.
- `os.replace(origen, destino)` : Similar a `rename`, pero reemplaza el archivo destino si ya existe.
- `os.listdir(ruta)` : Devuelve una lista con los ficheros y directorios contenidos en la ruta.
- `os.getcwd()` : Devuelve la ruta completa del directorio actual.
- `os.chdir(ruta)` : Cambia el directorio de trabajo actual.
- `os.mkdir(ruta)` : Crea un nuevo directorio en la ruta indicada.
- `os.makedirs(ruta)` : Crea directorios recursivamente, creando todos los directorios intermedios necesarios.
- `os.rmdir(ruta)` : Borra el directorio indicado, siempre que esté vacío.
- `os.path.exists(ruta)` : Devuelve True si la ruta existe, False en caso contrario.

<br>

**Ejemplo:**
```py
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
```
   
### **1.4 - Leer un fichero de internet**
Python también permite leer archivos directamente desde internet utilizando módulos como `requests` o `urllib`. 

**Ejemplo con urllib:**
```py
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
```

### **1.5 - POO y manejo de ficheros**
<!-- metodos de cadenas -->



<!-- https://aprendeconalf.es/docencia/python/ejercicios/ficheros/-->
<!-- Ejercios de ficheros
https://aprendeconalf.es/docencia/python/ejercicios/ficheros/ -->
<!-- https://python.sdv.u-paris.fr/07_fichiers/ -->


 
  
<!--
poner __str__()
 https://hektorprofe.github.io/python/herencia-en-la-poo/ejercicios/ -->
    


<!-- https://dat-science.com/clases-y-objetos-en-python/#Metodos_especiales -->
 
 
 
<!-- 

```py
# definimos una variable de tipo lista
datos = []
# Usamos un iterador para llenar la lista
for i in range(5):
  dato = input("Introducir cualquier cosa: ")
  datos.append(dato)
# Usamos otro iterador para leer la lista y sacamos el tipo de variable que contiene
for i in range(5):
 # print(f"Posición {i}, valor {datos[i]}, tipo {type(datos[i])}") 
  print(f"Posición {i}, valor {datos[i]}, tipo: {'string' if isinstance(datos[i],str) else ''}")
```


 <!-- === "RA 1"
    |RA1. Reconoce la estructura de un programa informático, identificando y relacionando los elementos propios del lenguaje de programación utilizado.|Peso|
    |-|-|
    *|**a)** Se han identificado los bloques que componen la estructura de un programa informático. |12%|
    *|**b)** Se han respetado las especificaciones técnicas del proceso de instalación. |11%|
    *|**c)** Se han utilizado entornos integrados de desarrollo. |11%|
    *|**d)** Se han identificado los distintos tipos de variables y la utilidad específica de cada uno. |11%|
    *|**e)** Se ha modificado el código de un programa para crear y utilizar variables. |11%|
    *|**f)** Se han creado y utilizado constantes y literales. |11%|
    *|**g)** Se han clasificado, reconocido y utilizado en expresiones los operadores del lenguaje. |11%|
    *|**h)** Se ha comprobado el funcionamiento de las conversiones de tipo explícitas e implícitas. |11%|
    *|**i)** Se han introducido comentarios en el código. |11%|


=== "RA 2"
    |RA2. Escribe y prueba programas sencillos, reconociendo y aplicando los fundamentos de la programación orientada a objetos.|Peso|
    |-|-|
    *|**a)** Se han identificado los fundamentos de la programación orientada a objetos. |12%|    
    *|**c)** Se han instanciado objetos a partir de clases predefinidas.|11%|
    *|**d)** Se han utilizado métodos y propiedades de los objetos.|11%|
    *|**e)** Se han escrito llamadas a métodos estáticos.|11%|
    *|**f)** Se han utilizado parámetros en la llamada a métodos.|11%|

=== "RA 3"
    |RA3. Escribe y depura código, analizando y utilizando las estructuras de control del lenguaje.|Peso|
    |-|-|
    *|**a)** Se ha escrito y probado código que haga uso de estructuras de selección.|12%|
    *|**b)** Se han utilizado estructuras de repetición.|11%|
    *|**c)** Se han reconocido las posibilidades de las sentencias de salto.|11%|
    *|**d)** Se ha escrito código utilizando control de excepciones.|11%|
    *|**e)** Se han creado programas ejecutables utilizando diferentes estructuras de control.|11%|
    *|**h)** Se han creado excepciones.|11%|
    *|**i)** Se han utilizado aserciones para la detección y corrección de errores durante la fase de desarrollo.|11%|

=== "RA 4"
    |RA4. Desarrolla programas organizados en clases analizando y aplicando los principios de la programación orientada a objetos.|Peso|
    |-|-|
    *|**a)** Se ha reconocido la sintaxis, estructura y componentes típicos de una clase.|12%|
    |**b)** Se han definido clases.|11%|
    |**c)** Se han definido propiedades y métodos.|11%|
    |**d)** Se han creado constructores.|11%|
    |**e)** Se han desarrollado programas que instancien y utilicen objetos de las clases creadas anteriormente.|11%|
    
=== "RA 5"
    |RA5. Realiza operaciones de entrada y salida de información, utilizando procedimientos específicos del lenguaje y librerías de clases.|Peso|
    |-|-|
    *|**a)** Se ha utilizado la consola para realizar operaciones de entrada y salida de información.|16%|
    *|**b)** Se han aplicado formatos en la visualización de la información.|12%|
    *|**c)** Se han reconocido las posibilidades de entrada / salida del lenguaje y las librerías asociadas.|12%|
    *|**d)** Se han utilizado ficheros para almacenar y recuperar información.|12%|
    *|**e)** Se han creado programas que utilicen diversos métodos de acceso al contenido de los ficheros.|12%|
    |**f)** Se han utilizado las herramientas del entorno de desarrollo para crear interfaces gráficos de usuario simples.|12%|
    |**g)** Se han programado controladores de eventos.|12%|
    |**h)** Se han escrito programas que utilicen interfaces gráficos para la entrada y salida de información.|12%|

=== "RA 6"
    |RA6. Escribe programas que manipulen información, seleccionando y utilizando tipos avanzados de datos.|Peso|
    |-|-|
    |**c)** Se han utilizado listas para almacenar y procesar información.|10%|
    |**e)** Se han reconocido las características y ventajas de cada una de las colecciones de datos disponibles.|10%|
    |**f)** Se han creado clases y métodos genéricos.|10%|
    |**g)** Se han utilizado expresiones regulares en la búsqueda de patrones en cadenas de texto.|10%|
    |**i)** Se han realizado programas que realicen manipulaciones sobre documentos escritos en diferentes lenguajes de intercambio de datos.|10%|
    |**j)** Se han utilizado operaciones agregadas para el manejo de información almacenada en colecciones.|10%| -->