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

|RA4. Desarrolla programas organizados en clases analizando y aplicando los principios de la programación orientada a objetos.|
|-|
|**e)** Se han desarrollado programas que instancien y utilicen objetos de las clases creadas anteriormente.|



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
        - Si ocurre una excepción, se capturará y manejará con los siguientes casos específicos:
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
<br>

- **Mismo ejemplo que el anterior pero con el método .writelines():**
```py
ruta = "docs/SMX/SMX_2/Opt_Python/code/UT5/"
archivo = "fichero2.txt"

# Generar todas las líneas primero en una lista (cada una incluye \n)
lineas = []
for i in range(5):
    lineas.append(f"Línea añadida número {i+1}\n")
# otra manera de hacerlo:
# lineas = [f"Línea añadida número {i+1}\n" for i in range(5)]

with open(ruta + archivo, "a", encoding="utf-8") as fichero:
    fichero.writelines(lineas)

```
    **Explicación del código**:  
    - Se abre el archivo en modo añadir ('a'). Si el archivo no existe, se crea.  
    - Se generan cinco líneas mediante un bucle for y se guardan en una lista.  
    - Se añaden todas las líneas al final del archivo utilizando el método writelines(), que escribe una lista de cadenas en el archivo.
<br>
    !!! tip "Diferencia entre write() y writelines()"
        - El método write() escribe una sola cadena en el archivo. Si se desea escribir múltiples líneas, se debe llamar a write() varias veces o utilizar un bucle.
        - El método writelines() escribe una lista de cadenas en el archivo de una sola vez. Cada cadena en la lista se escribe tal cual, por lo que es **necesario incluir manualmente los saltos de línea (`\n`)** si se desea que cada cadena aparezca en una línea separada.  
        **Ejemplo:** nuevas_lineas.append(str(numero) + "\n").

<br>

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

### **Tarea RA5-CEe**
!!! excercise "Descargar y modificar un archivo.txt desde internet" 
    1. Escribir un programa en Python que haga lo siguiente:    
        - Descargar un archivo de texto desde la URL proporcionada: [descargar archivo](./code/UT5/fichero.txt)
        - Guardar el archivo en una ubicación local con un nombre específico (p.e. vuestro nombre).
        - Abrir el archivo y multiplicar el valor numérico que aparece en cada línea por 2.
        - Guardar los resultados en un nuevo archivo de texto llamado "resultados.txt".
        Podéis usar cualquiera de los métodos write o writelines para guardar los resultados.
<br >

### **1.5 - POO y manejo de ficheros**
**Ejemplo de una clase que maneja ficheros:**

??? note "Clase LeerArchivo"
    ```py
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
    input("(Pulsa Enter para continuar)\n")

    nombre_archivo = input("Introduce el nombre del archivo a abrir: ")
    ruta_archivo = input("Introduce la ruta del archivo a abrir: ")
    input("(Pulsa Enter para continuar)\n")

    if ruta_archivo == "":
        ruta = ruta_defecto
    if nombre_archivo == "":
        nombre = archivo_defecto

    archivo = LeerArchivo(ruta, nombre)


    print("|----------------------------------------|")
    print("| (1) Para leer la totalidad del archivo |")
    print("| (2) Para leer el archivo linea a linea |")
    print("| (3) Para leer una linea del archivo    |")
    print("| (0) Para salir del programa            |")
    print("|----------------------------------------|")
    eleccion  = input("Elegir la opción (0 o Enter para salir): ")

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
    
### **Tarea RA4-CEe**
!!! excercise "Método escribir en un archivo"
    1. Revisar el programa anterior para entender su lógica y realizar lo siguiente.
        - Ampliar la clase **LeerArchivo** añadiendo un método que permitirá añadir una linea al archivo abierto. 
    2. El nuevo método debe llamarse **escribir_linea(self, ...)** y debe hacer lo siguiente:
        - Pedir por consola al usuario la información a añadir (una línea de texto)
        - Escribir esa línea nueva **al final del archivo**.
        - Guardar y cerrar el archivo. 

       


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