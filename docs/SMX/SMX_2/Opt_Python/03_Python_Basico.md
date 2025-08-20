---
title: CFGM - Técnico en Sistemas Microinformáticos y Redes
lesson: UD. 3 - Python básico  
#subtitle: "Módulo: 0223 - Aplicaciones ofimáticas"
author: Javier Egea Blasco  
year: Año 25-26  
keywords: SMX, Py
layout: default  
---

![Descripción de la imagen](../Opt_Python/img/Python-logo.png){ .img1 }

<br>


## **Sintáxis básica**
La sintaxis es a la programación lo que la gramática es a los idiomas. De la misma forma que la frase “Yo estamos aquí” no es correcta ...tampoco lo es un programa con errores de sintaxis, ya que el ordenador no podrá interpretarlo ni ejecutarlo de la manera esperada.

Ejemplo de sintaxis correcta de un programa hecho en Python.  

```py
# Definimos una variable x con una cadena
x = "El valor de (a+b)*c es"

# Podemos realizar múltiples asignaciones
a, b, c = 4, 3, 2

# Realizamos unas operaciones con a,b,c
d = (a + b) ** c

# Definimos una variable booleana
imprimir = True

# Si imprimir, print()
if imprimir:
    print(x, d)

# Salida: El valor de (a+b)*c es ??
```

!!! Pregunta 
    ¿Qué realiza el programa anterior?

### Elementos de un programa de Python
Un programa de Python es un fichero de texto (codificado en formato UTF-8) que contiene expresiones y sentencias que se consiguen combinando los elementos básicos del lenguaje.  

El lenguaje Python está formado por elementos (tokens) de diferentes tipos:

  - Lineas y espacios.
  - Palabras reservadas (keywords)
  - Variables, operadores y expresiones
  - Funciones integradas (built-in functions).
  - Delimitadores
  - Identificadores

!!! Pregunta 
    Del ejemplo de código anterior, identificar los diferentes elementos constituyentes del programa.

En la documentación de Python se puede consultar una descripción mucho más detallada y completa de <a href=https://docs.python.org/3/reference/lexical_analysis.html>los elementos constitutivos</a> del lenguaje Python.

Para que un programa se pueda ejecutar, el programa debe ser sintácticamente correcto, es decir, utilizar los elementos del lenguaje Python respetando su reglas de "ensamblaje". 

### Líneas y espacios
Básicamente, un programa de Python está formado por líneas de texto.
```python
radio = 5
area = 3.1415 * radio ** 2
print("La superificie es:", area)
```
<br>
Se recomienda que cada línea contenga una única instrucción, aunque puede haber varias instrucciones en una línea, separadas por un punto y coma (;).
```python
radio = 5; area = 3.1415 * radio ** 2
print("La superificie es:", area)
```
<br>
Los elementos del lenguaje se separan por espacios en blanco (normalmente, uno), aunque en algunos casos no se escriben espacios:

- Entre los nombres de las funciones y el paréntesis
- Antes de una coma (,)
- Entre los delimitadores y su contenido (paréntesis, llaves, corchetes o comillas)
```py
def suma(a,b):
  resultado = a + b
  return resultado

print(suma(2,3))
```

### Delimitadores
Los delimitadores son los caracteres que permiten delimitar, separar o representar expresiones. 

🔹 1. Paréntesis, corchetes y llaves  

- ( ) → agrupar expresiones, llamadas a funciones, tuplas  
- [ ] → listas, indexación, slicing  
- { } → diccionarios, conjuntos, bloques en f-strings  

<br>
🔹 2. Separadores de código

- coma ( , ) → separa elementos en listas, tuplas, parámetros de funciones
- 2 puntos ( : ) → define bloques (if, for, def, class, etc.) o pares clave:valor en diccionarios
- punto ( . ) → acceso a atributos y métodos (obj.attr)
- punto y coma ( ; ) → separa varias instrucciones en una misma línea

<br>
🔹 3. Delimitadores de cadenas

- Comillas simples: 'texto'
- Comillas dobles: "texto"
- Comillas triples: '''texto''' o """texto""" (también para docstrings y cadenas multilínea)

<br>
🔹 4. Delimitadores especiales

- Igual ( = ) → asignación
- Flecha ( -> ) → anotaciones de tipo en funciones (def f(x) -> int:)
- 3 puntos ( ... ) (ellipsis) → marcador especial usado en slicing o como placeholder

```py
( )   [ ]   { }
,     :     .     ;
@     =     ->    ...
' '   " "   ''' '''   """ """
```

<br>
**Nota**:  
Los delimitadores no se pueden usar para otra cosa que no sea su uso como delimitador. Cualquier uso indebido generará un error en tiempo de ejecución.

!!! Ejercicio
    Escribir un programa que pretenda asignar el valor 64 a una variable de nombre vari@bl&.
    Comprobar lo que ocurre entonces. 

<br>
**Nota**:  
Los delimitadores # y “”” “”” permiten insertar comentarios dentro de un programa.
```py
# Esta linea está comentada. El interprete no la ejecutará
# 
a = True and False
print("El valor de 'a' es:", a, "y es de tipo: ", type(a))
#
"""
Nada de lo contenido entre las comillas dobles será ejecutado
b = True and True
print("El valor de 'b' es:", b, "y es de tipo: ", type(a))
"""
```

!!! Ejercicio 
    En el código del ejemplo anterior encontrar la línea dónde se hace uso a la ver de comillas simples y comillas dobles.  
    ¿Por qué se usa esa sintaxis?

<br>
**Nota**:  
El delimitador contrabarra ( \ ) permite truncar una linea muy larga en varias líneas.
Por motivos de legibilidad, se recomienda que las líneas no superen los 79 caracteres. Si una instrucción supera esa longitud, se puede dividir en varias líneas usando la contrabarra ( \ ):

```py
radio = 5
area = 3.14159265358979323846 \
       * radio **2
print(area) 

texto = "Perdóname, amigo, de la ocasión que te he dado de parecer\
         loco como yo, haciéndote caer en el error en que yo he caído\
         de que hubo y hay caballeros andantes en el mundo."
print(texto)
```

!!! Ejercicio
    Escribir el programa anterior y comprobar el resultado.  
    Intentar arreglarlo de forma intuitiva. 

### **Palabras reservadas**
Las palabras reservadas de Python son las que forman **el núcleo del lenguaje** Python y **no se pueden usar para nombrar otros elementos** (variables, funciones, …).  
Se puede acceder al listado de las palabras reservadas desde la ayuda de IDLE (Python 3.11, 64bits).

![Descripción de la imagen](../Opt_Python/img/help_idle.png){ .img1 }

!!! Ejercicio 1
    Lanzar el interpretador **idle** (se instala a la vez que python).  
    Escribir en la terminal **help** y luego **keywords**.  

!!! Ejercicio 2
    ¿Podéis intuir el significado de alguna palabra reservada?

## **Variables**
De forma general, una variable es **un espacio de memoria** con un nombre asociado que se utiliza para **almacenar y manipular datos** que pueden **cambiar durante la ejecución** del programa.

### Declaración de variables
Python es un lenguaje de tipado dinámico por lo que no hace falta declarar **el tipo de dato** que se asignará a una variable. De igual manera una variable puede cambiar de tipo conforme la ejecución del programa (lo que no se considera una buena práctica de programación), por ello, se debe tener cuidado con la sintaxis para definir cada tipo de dato.
```py
a = 5
b = 6
c = '¡Hola mundo!'

print(c, a+b)
``` 
!!! Ejercicio
    Ampliar el programa anterior dónde se le asignará un nuevo valor a la variable 'b' y se le asignará un valor númerico a 'c'.  
    Escribir en pantalla (print()) el resultado de la suma de b+c. 
    
### Variables de tipo entero (int)
Los enteros son un tipo de dato básico en cualquier lenguaje de programación.  
```py
a = 5
print(a, type(a))
``` 
<br>
Si se usan enteros de 32 bits el rango a representar es de -2^31 a 2^31–1.  
Con 64 bits, el rango es de  -2^63 a 2^63–1.  
**No tenemos que preocuparnos** de la codificación de los enteros, ya que Python se encarga de asignar más o menos memoria al número en función de su valor. 
```py
a = 5
b = 16
c = a ** b
print(c)
``` 
!!! Ejercicio
    Ampliar el programa anterior para evidenciar la asingación dinámica del tipo de variable en python. 

### Variables de tipo coma flotante (float)
Las variables de tipo coma flotante (o float) son aquellas que almacenan números reales (es decir, con parte decimal).
```py
x = 3.14   # float
y = -2.5   # float
z = 0.0    # float
```
<br>

Los float se pueden escribir de dos formas:

1. Decimal normal:
```py
pi = 3.14159
```
<br>

1. Notación científica (usando e o E para potencias de 10):
```py
avogadro = 6.022e23   # 6.022 × 10^23
electron = 1.6e-19    # 1.6 × 10^-19
```

1. Precisión de las variables de tipo flotante.
    - Los float en Python son de doble precisión (64 bits, estándar IEEE 754) lo que da ~15–17 cifras decimales de precisión.
    ```py
    a = 7.0
    b = 5.0
    print(a, b, a+b, type(a+b))
    ```
    - No son exactos en muchos casos por cómo se representan en binario.
    ```py
    # Demostración del problema de precisión con float en Python
    print("¿La suma de 0.1 y 0.2 es igual a 0.3?", 0.1 + 0.2 == 0.3) 
    print("Valor real de 0.1 + 0.2:", 0.1 + 0.2)   

    # Solución con librería Decimal para cálculo exacto
    from decimal import Decimal
    a = Decimal("0.1")
    b = Decimal("0.2")
    c = Decimal("0.3")
    print("Con Decimal:", a + b == c)
    ```

### Variables de tipo booleano (bool)
Las variables booleanas sólo pueden adoptar dos valores: **verdadero (True)** o **falso (False)**.
```py
a = True
b = False
print(type(a), type(b))
```


!!! Ejercicio
    Ampliar el programa anterior para que compara el tipo resultante de la suma lógica de a y b, y también compare a con la negación de b. 

### Variables de tipo número complejo
En Python, los números complejos se representan literalmente con el tipo complex.  
En python, uUn número complejo tiene la forma: a + bj donde j es la unidad unidad imaginaria (en matemáticas se usa i).
```py
# Forma literal de escribir números complejos
a = 5 + 7j
b = 3 - 4j
c = a + b
print(c)
# Uso de complex para definir números complejos
d = complex(2, 3)   # (2+3j)
e = complex(-1, -5) # (-1-5j)
f = d * e
print(d)
```

!!! Ejercicio
    Calcular con papel y boli el resultado de la variable 'f'.

### Variables de tipo cadena de caracteres (string) 
Es un tipo de dato que contiene símbolos (alfanuméricos). Los strings se definen utilizando **comillas dobles o simples**.
```py
a = "hello"
b = " "
c = "world"
d = a + b + c
print(a,b,c)
print(d)
```

!!! Ejercicio
    Rehacer el programa anterior para que esta vez, las variables de tipo string contengan valores númericos.

## **Operadores aritméticos**
Los operadores aritméticos permiten realizar operaciones aritméticas básicas con las variables de tipo numérico. 

|Operación|Operador |
|-|:-:|
Suma|+|
|Resta|-|
|Multiplicación|*|
|División|/|
|División entera|//|
|Módulo|%|
|Potencia|**|

!!! Ejercicio  
    Escribir la expresión que permita calcular los siguientes valores: 

    ![Descripción de la imagen](../Opt_Python/img/potencias.png){ .potencias }

**Nota:**  
Aunque no lo hayamos visto aun, existe una manera más simple de escribir las expresiones. Si usamos la biblioteca math accedemos a todos sus operadores matemáticos (métodos) lo que da más claridad al código.

```py 
import math

# Calcular la raíz cuadrada de un valor
a = 4
b = math.sqrt(a)
print(b)

# Calcular el coseno de 60º
c = math.cos(60)
print(c)
```

!!! Ejercicio  
    Copiar el código anterior y comprobar los resultados obtenidos.  
    ¿Son los esperados?  
    ¿Qué se debería hacer para que sean correctos?


## **Operadores relacionales (o de comparación)**
Permiten efectuar comparaciones entre objetos de Python.  
El resultado de una comparación es un valor booleano (True o False).  

|Sintaxis|Ejemplo|Resultado|
|-|-|-|
|"igual que"|1 == 1 |True|
|"diferente a"|"a" != "a" |False|
|"mayor que"|5 < 1 |False|
|"menor que"|5<1 |False|
|"mayor o igual que"|30>=10 |True|
|"menor o igual que"|20<>=10 |False|

**Nota:** 
Los operadores relacionales solo se pueden ejecutar para comparar valores del mismo tipo.

- "a" > 10 devolverá un error.
- [0,4] < (1,2) devolverá un error al no poder comparar una lista con una tupla.
- También se pueden concatenar: 3 == 3 >= 2 (true)
      
!!! Ejercicio  
    Transcribir a python las expresiones que acabamos de ver.      

## **Operadores lógicos**
Sirven para realizar operaciones de lógica booleana entre valores de tipo bool. Los operadores lógicos son (las palabras reservadas) **and, or y not**.  

|Operador|Descripción|Ejemplo|
|-|-|-|
|"and"|Verdadero si ambas condiciones son True|True and False → False|
|"or"|Verdadero si al menos una condición es True|True or False → True|
|"not"|Invierte el valor de la condición|not True → False|

**Nota:**  
Cuidado con la sintaxis. Si usamos los símbolos de la lógica combinatoria los resultados pueden no ser los esperados.

## **Estructuras de control**
Un código es una secuencia de instrucciones, que por norma general son ejecutadas una tras otra.   
Sin embargo, en muchas ocasiones no basta con ejecutar las instrucciones una tras otra desde el principio hasta llegar al final. Puede ser que ciertas instrucciones se tengan que ejecutar si y sólo si se cumple una determinada condición.

![Descripción de la imagen](../Opt_Python/img/estructuras-de-control.svg){ .img1 }

En un lenguaje de programación, las estructuras de control permiten modificar el flujo de ejecución de un conjunto de instrucciones. Los tipos más comunes son:

|Elemento|Tipo|
|-|-|
|**if, elif, else**|Estructura condicionales|
|**for**|Bucle (o iteración)|
|**while**|Bucle (o iteración)|
|**try-except**|Manejo de excepciones(errores)|  

### **Bucle condicional if-elif-else**


https://docs.python.org/es/3/tutorial/controlflow.html

https://www.learnpython.org/

https://arturoblasco.github.io/prg/ut01/actividades/ut01ac1f/

https://ellibrodepython.com/sintaxis-python

IA BD PIA UT 2. ... pagina 19.


 

https://jorgedelossantos.github.io/apuntes-python/Estructuras%20de%20control.html#


