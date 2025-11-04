---
ciclo: CFGM - Técnico en Sistemas Microinformáticos y Redes
title: Introducción a la programación en Python
modulo number: 
lesson: UD. 4 - POO  
author: Javier Egea Blasco  
layout: default  
year: 25-26  
keywords: SMX, Python
schedule: 96h - 3h/w
---

# **UT 4 - Programación orientada a objetos**

![Descripción de la imagen](../Opt_Python/img/maxresdefault.jpg){ .img1 }

<br>

**Resultados de aprendizaje y criterios de evaluacion que se evaluarán en esta unidad.**  

|RA2. Escribe y prueba programas sencillos, reconociendo y aplicando los fundamentos de la programación orientada a objetos.|
|-|
|**a)** Se han identificado los fundamentos de la programación orientada a objetos. |
|**c)** Se han instanciado objetos a partir de clases predefinidas.|
|**d)** Se han utilizado métodos y propiedades de los objetos.|
|**e)** Se han escrito llamadas a métodos estáticos.|
|**f)** Se han utilizado parámetros en la llamada a métodos.|

|RA4. Desarrolla programas organizados en clases analizando y aplicando los principios de la programación orientada a objetos.|
|-|
|**a)** Se ha reconocido la sintaxis, estructura y componentes típicos de una clase.|
|**b)** Se han definido clases.|
|**c)** Se han definido propiedades y métodos.|
|**d)** Se han creado constructores.|
|**e)** Se han desarrollado programas que instancien y utilicen objetos de las clases creadas anteriormente.|
 
 <br>


<!-- https://jsp.shiksha/index.php/portfolio/bacse101-problem-solving-using-python/introduction-python -->
<!-- https://nachoiborraies.github.io/python/08.html -->
<!-- https://www.luisllamas.es/que-es-un-objeto-en-programacion/ -->
<!-- https://ellibrodepython.com/programacion-orientada-a-objetos-python -->
<!-- https://gitlab.com/josedom24/curso_programacion_python3/-/tree/master/curso/u39?ref_type=heads -->


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
    |**a)** Se han identificado los fundamentos de la programación orientada a objetos. |12%|    
    |**c)** Se han instanciado objetos a partir de clases predefinidas.|11%|
    |**d)** Se han utilizado métodos y propiedades de los objetos.|11%|
    |**e)** Se han escrito llamadas a métodos estáticos.|11%|
    |**f)** Se han utilizado parámetros en la llamada a métodos.|11%|

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
    |**a)** Se ha reconocido la sintaxis, estructura y componentes típicos de una clase.|12%|
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
    |**d)** Se han utilizado ficheros para almacenar y recuperar información.|12%|
    |**e)** Se han creado programas que utilicen diversos métodos de acceso al contenido de los ficheros.|12%|
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