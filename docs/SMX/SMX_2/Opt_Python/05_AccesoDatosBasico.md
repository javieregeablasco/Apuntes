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

# **UT 5 - Acceso a ficheros**

![Descripción de la imagen](../Opt_Python/img/UT5/dataaaccess.webp){ .cincozero }

<br>

**Resultados de aprendizaje y criterios de evaluacion que se evaluarán en esta unidad.**  

|RA4. Desarrolla programas organizados en clases analizando y aplicando los principios de la programación orientada a objetos.|
|-|
|**a)** Se ha reconocido la sintaxis, estructura y componentes típicos de una clase.|
|**b)** Se han definido clases.|
|**c)** Se han definido propiedades y métodos.|
|**d)** Se han creado constructores.|
|**e)** Se han desarrollado programas que instancien y utilicen objetos de las clases creadas anteriormente.|
    
|RA5. Realiza operaciones de entrada y salida de información, utilizando procedimientos específicos del lenguaje y librerías de clases.|
|-|
|**d)** Se han utilizado ficheros para almacenar y recuperar información.|
|**e)** Se han creado programas que utilicen diversos métodos de acceso al contenido de los ficheros.|
|**f)** Se han utilizado las herramientas del entorno de desarrollo para crear interfaces gráficos de usuario simples.|
|**g)** Se han programado controladores de eventos.|
|**h)** Se han escrito programas que utilicen interfaces gráficos para la entrada y salida de información.|

<br>

## **1 - Manejo de ficheros en Python**
El manejo de archivos permite leer y escribir en archivos. Para ello, Python proporciona una serie de funciones que veremos a continuación.
### **1.1 - Abrir un archivo**
Para abrir un archivo se puede usar la función open() pasando por argumento la ruta y el nombre del archivo al cual queremos acceder.


<!-- https://ellibrodepython.com/ficheros-python -->
<!-- Ejercios de ficheros
https://aprendeconalf.es/docencia/python/ejercicios/ficheros/ -->
<!-- https://python.sdv.u-paris.fr/07_fichiers/ -->

<!--
7. File Handling

File handling allows you to read from and write to files. Python provides built-in functions for file handling.

    Opening Files: Use the open() function to open a file.
    Reading Files: Use methods like read(), readline(), readlines() to read file contents.
    Writing to Files: Use methods like write(), writelines() to write to a file.
    Closing Files: Always close the file after performing file operations using the close() method.
 -->
 
  
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