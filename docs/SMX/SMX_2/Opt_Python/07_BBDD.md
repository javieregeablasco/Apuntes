---
ciclo: CFGM - Técnico en Sistemas Microinformáticos y Redes
title: Introducción a la programación en Python
modulo number: 
lesson: UD. 6 - Modulos e interfaces gráficas  
author: Javier Egea Blasco  
layout: default  
year: 25-26  
keywords: SMX, Python
schedule: 96h - 3h/w
---

# **UT 7 - Manipulación y validación de datos**

![Descripción de la imagen](../Opt_Python/img/UT6/tk.jpg){ .cincozero }

<br>

**Resultados de aprendizaje y criterios de evaluacion que se evaluarán en esta unidad.**  

|RA6. Escribe programas que manipulen información, seleccionando y utilizando tipos avanzados de datos.|
|-|
|**c)** Se han utilizado listas para almacenar y procesar información.|
|**e)** Se han reconocido las características y ventajas de cada una de las colecciones de datos disponibles.|
|**f)** Se han creado clases y métodos genéricos.|
|**g)** Se han utilizado expresiones regulares en la búsqueda de patrones en cadenas de texto.|
|**i)** Se han realizado programas que realicen manipulaciones sobre documentos escritos en diferentes lenguajes de intercambio de datos.|
|**j)** Se han utilizado operaciones agregadas para el manejo de información almacenada en colecciones.|

<br>

## 1 - Estructuras de datos en Python

### 1.1 - Tipos de colecciones de datos
En unidades anteriores hemos ido utilizando estructuras de datos (listas, diccionarios, tuplas, etc.) para almacenar y manipular datos en nuestros programas. En esta sección repasaremos las diferentes estructuras de datos (o colecciones) disponibles en Python y veremos cómo utilizarlas de manera efectiva.

- **Listas**: Son colecciones ordenadas y mutables que pueden contener elementos de diferentes tipos. Se definen utilizando corchetes `[]`. Las listas permiten agregar, eliminar y modificar elementos fácilmente.
```py
# Ejemplo de lista
mi_lista = [1, 2, 3, "cuatro", 5.0]
```  

- **Tuplas**: Son colecciones ordenadas e inmutables que también pueden contener elementos de diferentes tipos. Se definen utilizando paréntesis `()`. Una vez creada una tupla, no se pueden modificar sus elementos.
```py
# Ejemplo de tupla
mi_tupla = (1, 2, 3, "cuatro", 5.0)
```
- **Conjuntos**: Son colecciones no ordenadas y mutables que **no permiten elementos duplicados**. Se definen utilizando llaves `{}` o la función `set()`.
```py
# Ejemplo de conjunto
conjunto_1 = {1, 2, 3, 4, 5}
conjunto_2 = set([4, 5, 6, 7, 8])
```
- **Diccionarios**: Son colecciones mutables que almacenan pares clave-valor. Desde Python 3.7 mantienen el orden de inserción. Se definen utilizando llaves `{}` con pares separados por dos puntos `:`.
```py
# Ejemplo de diccionario
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Catadau"}
```

Cada una de estas estructuras de datos tiene sus propias características y ventajas, y la elección de cuál utilizar depende del tipo de datos que se estén manejando y de las operaciones que se necesiten realizar sobre ellos.

### **1.2 - Métodos asociados a las listas**
#### **1.2.1 - Método .append()**
El método `append()` se utiliza para agregar un elemento **al final de una lista**.

```py
# Ejemplo de uso de append()
mi_lista = [1, 2, 3]
mi_lista.append(4)
print(mi_lista)  # Salida: [1, 2, 3, 4]
```


También se puede añadir elementos a una lista utilizando el operador `+=` pero, no se considera una buena práctica para añadir un solo elemento, ya que `+=` está pensado para concatenar listas completas.
```py
# Ejemplo de uso de +=
mi_lista = [1, 2, 3]
mi_lista += [4] 
```     

#### **1.2.3 - Método .insert()**
El método `insert()` permite insertar un elemento en una posición específica de la lista.

```py
# Ejemplo de uso de insert()
# Insertar el número 10 en la posición 1
mi_lista = [1, 2, 3]
mi_lista.insert(1, 10)
print(mi_lista)  # Salida: [1, 10, 2, 3]
```

#### **1.2.4 - Método .del()**
El método `del` permite eliminar un elemento de una lista en una posición específica.

```py    
# Ejemplo de uso de del
mi_lista = [1, 2, 3, 4]
del mi_lista[2]  # Elimina el elemento en la posición 2
print(mi_lista)  # Salida: [1, 2, 4]
```

#### **1.2.5 - Método .remove()**
Realiza la misma funcion que el métod `del()` pero, esta vez, en vez de eliminar un elemento en base a su índice, lo hace por su valor.

```py
# Ejemplo de uso de remove()
mi_lista = [1, 2, 3, 4]
mi_lista.remove(3)  # Elimina el primer elemento con valor 3
print(mi_lista)  # Salida: [1, 2, 4]
```

**Nota:** Si el valor aparece varias veces en la lista, solo se eliminará la primera aparición.

```py
mi_lista = [1, 2, 3, 4, 8, 9, 3, 4, 5]
mi_lista.remove(3)  # Elimina el primer elemento con valor 3
print(mi_lista)  # Salida: [1, 2, 4, 8, 9, 3, 4, 5]
```

#### **1.2.5 - Método .clear()**
El método `clear()` elimina todos los elementos de una lista, dejándola vacía.

```py
# Ejemplo de uso de clear()
mi_lista = [1, 2, 3, 4]
mi_lista.clear()  # Elimina todos los elementos de la lista
print(mi_lista)  # Salida: []
```

#### **1.2.6 - Método .pop()**
El método `pop()` elimina y devuelve un elemento de la lista en una posición específica. Si no se especifica una posición, elimina y devuelve el último elemento de la lista. 

```py
# Ejemplo de uso de pop()
mi_lista = [1, 2, 3, 4]
elemento_eliminado = mi_lista.pop(1)  # Elimina y devuelve el elemento en la posición 1
print(elemento_eliminado)  # Salida: 2
```
```py
mi_lista = [1, 2, 3, 4]
elemento_eliminado = mi_lista.pop()  # Elimina y devuelve el último elemento
print(elemento_eliminado)  # Salida: 4
```

#### **1.2.7 - Método .sort()**
El método `sort()` ordena los elementos de una lista **modificando la lista original**. Por defecto, ordena los elementos en orden ascendente.

```py
# Ejemplo de uso de sort()
mi_lista = [4, 2, 1, 3] 
mi_lista.sort()  # Ordena la lista en orden ascendente
print(mi_lista)  # Salida: [1, 2, 3, 4]
```

**Nota 1:** También se puede ordenar en orden descendente utilizando el argumento `reverse=True` o usando el método **.reverse()**. 

```py
mi_lista = [4, 2, 1, 3] 
mi_lista.sort(reverse=True)  # Ordena la lista en orden descendente
print(mi_lista)  # Salida: [4, 3, 2, 1]

mi_lista = [4, 2, 1, 3]
milista.reverse()  # Invierte el orden de los elementos de la lista
print(mi_lista)  # Salida: [3, 1, 2, 4]
```

**Nota 2:** Si no se desea modificar la lista original, se puede utilizar la función `sorted()`, que devuelve una nueva lista ordenada.

```py
mi_lista = [4, 2, 1, 3]
lista_ordenada = sorted(mi_lista)  # Devuelve una nueva lista ordenada
print(lista_ordenada)  # Salida: [1, 2, 3, 4]
print(mi_lista)  # Salida: [4, 2, 1, 3] (la lista original no se modifica)
```   

### **1.3 - Métodos asociados a los diccionarios**
#### **1.3.1 - Método .keys()**
El método `keys()` devuelve una vista de las claves del diccionario.

```py
# Ejemplo de uso de keys()
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Catadau"}
claves = mi_diccionario.keys()
print(claves)  # Salida: dict_keys(['nombre', 'edad', 'ciudad'])
```
#### **1.3.2 - Método .values()**
El método `values()` devuelve una vista de los valores del diccionario.

```py
# Ejemplo de uso de values()
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Catadau"}
valores = mi_diccionario.values()
print(valores)  # Salida: dict_values(['Juan', 30, 'Catadau'])
```

#### **1.3.3 - Método .items()**
El método `items()` devuelve una vista de los pares clave-valor del diccionario.

```py   
# Ejemplo de uso de items()
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Catadau"}
pares = mi_diccionario.items()  
print(pares)  # Salida: dict_items([('nombre', 'Juan'), ('edad', 30), ('ciudad', 'Catadau')])
```

#### **1.3.4 - Método .get()**
El método `get()` se utiliza para obtener el valor asociado a una clave específica en el diccionario. Si la clave no existe, devuelve `None` o un valor predeterminado especificado.

```py
# Ejemplo de uso de get()
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Catadau"}
valor = mi_diccionario.get("edad")  # Obtiene el valor asociado a la clave "edad"
print(valor)  # Salida: 30
valor_no_existente = mi_diccionario.get("pais", "No especificado")  # Devuelve un valor predeterminado si la clave no existe
print(valor_no_existente)  # Salida: No especificado
```

#### **1.3.5 - Añadir, modificar elementos**
Para añadir un nuevo par clave-valor o modificar el valor asociado a una clave existente, se puede utilizar la sintaxis de asignación.

```py
# Ejemplo de añadir o modificar elementos
mi_diccionario = {"nombre": "Juan", "edad": 30}
mi_diccionario["ciudad"] = "Catadau"  # Añadir un nuevo par clave-valor
mi_diccionario["edad"] = 31  # Modificar el valor asociado a la clave "edad"
print(mi_diccionario)  # Salida: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Catadau'}
```

También se puede utilizar el método `update()` para añadir o modificar múltiples pares clave-valor a la vez.

```py
# Ejemplo de uso de update()
mi_diccionario = {"nombre": "Juan", "edad": 30} 
mi_diccionario.update({"ciudad": "Catadau", "edad": 31})  # Añadir/modificar múltiples pares clave-valor
print(mi_diccionario)  # Salida: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Catadau'}
```
### **1.4 - Métodos asociados a las tuplas**
Las tuplas son inmutables, por lo que no tienen métodos para modificar su contenido. Sin embargo, tienen algunos métodos útiles:
#### **1.4.1 - Método .count()**
El método `count()` devuelve el número de veces que un elemento aparece en la tupla.
```py
# Ejemplo de uso de count() 
mi_tupla = (1, 2, 3, 2, 4, 2)
veces = mi_tupla.count(2)  # Cuenta cuántas veces aparece el número 2
print(veces)  # Salida: 3
```
#### **1.4.2 - Método .index()**
El método `index()` devuelve el índice de la primera aparición de un elemento en la tupla.
```py   
# Ejemplo de uso de index()
mi_tupla = (1, 2, 3, 4)
indice = mi_tupla.index(3)  # Obtiene el índice del número
print(indice)  # Salida: 2
``` 

### **1.5 - Métodos asociados a los conjuntos**
#### **1.5.1 - Método .add()**
El método `add()` se utiliza para agregar un elemento a un conjunto.

```py   
# Ejemplo de uso de add()
mi_conjunto = {1, 2, 3}
mi_conjunto.add(4)  # Agrega el elemento 4 al conjunto  
print(mi_conjunto)  # Salida: {1, 2, 3, 4}
```

#### **1.5.2 - Método .remove()**
El método `remove()` se utiliza para eliminar un elemento específico de un conjunto. Si el elemento no existe, se genera un error.
```py
# Ejemplo de uso de remove()
mi_conjunto = {1, 2, 3, 4}
mi_conjunto.remove(3)  # Elimina el elemento 3 del conjunto
print(mi_conjunto)  # Salida: {1, 2, 4}
```

#### **1.5.3 - Método .discard()**
El método `discard()` también se utiliza para eliminar un elemento específico de un conjunto, pero a diferencia de `remove()`, no genera un error si el elemento no existe.
```py
# Ejemplo de uso de discard()
mi_conjunto = {1, 2, 3, 4}
mi_conjunto.discard(5)  # Intenta eliminar el elemento 5 (no existe, pero no genera error)
print(mi_conjunto)  # Salida: {1, 2, 3, 4}
```

#### **1.5.4 - Método .pop()**
El método `pop()` elimina y devuelve un elemento arbitrario del conjunto. Si el conjunto está vacío, genera un error.
```py
# Ejemplo de uso de pop()
mi_conjunto = {1, 2, 3, 4}
elemento_eliminado = mi_conjunto.pop()  # Elimina y devuelve un elemento arbitrario
print(elemento_eliminado)  # Salida: (puede ser cualquier elemento del conjunto)
print(mi_conjunto)  # Salida: (el conjunto sin el elemento eliminado)
```

#### **1.5.5 - Método .clear()**
El método `clear()` elimina todos los elementos de un conjunto, dejándolo vacío.
```py
# Ejemplo de uso de clear()
mi_conjunto = {1, 2, 3, 4}  
mi_conjunto.clear()  # Elimina todos los elementos del conjunto
print(mi_conjunto)  # Salida: set()
```

### **1.6 - Accesso a elementos de las colecciones**
#### **1.6.1 - Acceso a elementos en listas y tuplas**
Se puede acceder a los elementos de una lista o tupla utilizando índices. Los índices comienzan en 0 para el primer elemento, 1 para el segundo, y así sucesivamente. También se pueden utilizar índices negativos para acceder a los elementos desde el final de la colección.

```py
# Ejemplo de acceso a elementos en listas y tuplas
mi_lista = [10, 20, 30, 40, 50]
primer_elemento = mi_lista[0]  # Accede al primer elemento (10)
ultimo_elemento = mi_lista[-1]  # Accede al último elemento (50)
print(primer_elemento)  # Salida: 10
print(ultimo_elemento)  # Salida: 50
```

!!! tip "Al igual que podemos acceder a los elementos individuales de una lista o tupla utilizando índices, también podemos modificar los elementos de una lista utilizando índices (no es posible hacerlo con las tuplas al ser inmutables)."
```py
# Ejemplo de modificación de elementos en listas
mi_lista = [10, 20, 30, 40, 50]
mi_lista[2] = 35  # Modifica el tercer elemento (índice 2) a 35
print(mi_lista)  # Salida: [10, 20, 35, 40, 50]
```

#### **1.6.2 - Acceso a elementos en diccionarios**
Se puede acceder a los valores de un diccionario utilizando sus claves.

```py
# Ejemplo de acceso a elementos en diccionarios
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Catadau"}
nombre = mi_diccionario["nombre"]  # Accede al valor asociado a la clave "nombre"
print(nombre)  # Salida: Juan
```

!!! tip "De una manera similar a las listas, también se puede modificar o añadir nuevos pares clave-valor en un diccionario utilizando las claves." 
```py
# Ejemplo de modificación y adición de elementos en diccionarios
mi_diccionario = {"nombre": "Juan", "edad": 30}
mi_diccionario["edad"] = 31  # Modifica el valor asociado a la clave "edad"
mi_diccionario["ciudad"] = "Catadau"  # Añade un nuevo par clave-valor
print(mi_diccionario)  # Salida: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Catadau'}
```

!!! tip "No se puede cambiar una clave existente, pero se puede eliminar el par clave-valor y añadir uno nuevo con la clave deseada. El método `pop()` resulta particularmente útil para este propósito" 
```py
# Ejemplo de cambio de clave en diccionarios
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Catadau"}
valor_edad = mi_diccionario.pop("edad")  # Elimina el par clave-valor con clave "edad"
mi_diccionario["años"] = valor_edad  # Añade un nuevo par clave-valor con la nueva clave "años"
print(mi_diccionario)  # Salida: {'nombre': 'Juan', 'años': 30}
```

#### **1.6.3 - Acceso a elementos en conjuntos**
Los conjuntos no permiten acceso a elementos individuales mediante índices, ya que son colecciones no ordenadas. Sin embargo, se puede verificar la existencia de un elemento en un conjunto utilizando el operador `in`.

```py   
# Ejemplo de acceso a elementos en conjuntos
mi_conjunto = {1, 2, 3, 4}
existe = 3 in mi_conjunto  # Verifica si el elemento 3 está en el conjunto
print(existe)  # Salida: True
```

#### **1.6.4 - Slicing (rebanado)**
El slicing permite obtener una sublista o subtupla de una lista o tupla original, especificando un rango de índices.

```py
# Ejemplo de slicing
mi_lista = [10, 20, 30, 40, 50]
sublista = mi_lista[1:4]  # Obtiene los elementos desde el índice 1 hasta el 3 (4 no incluido)
print(sublista)  # Salida: [20, 30, 40]
```

#### **1.6.5 - Iteración sobre colecciones**
Se puede iterar sobre los elementos de cualquier colección utilizando un bucle `for`.

```py
# Ejemplo de iteración sobre una lista
mi_lista = [10, 20, 30, 40, 50]
for elemento in mi_lista:
    print(elemento)
```

#### **1.6.6 - Comprensión de listas**
La comprensión de listas (list comprehensions) es una forma concisa de crear listas utilizando una sintaxis especial.

```py
# Ejemplo de comprensión de listas
mi_lista = [1, 2, 3, 4, 5]  
cuadrados = [x**2 for x in mi_lista]  # Crea una nueva lista con los cuadrados de los elementos
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]
```

#### **1.6.7 - Funciones agregadas para colecciones**
Python proporciona varias funciones integradas que permiten realizar operaciones agregadas sobre colecciones, como `len()`, `sum()`, `min()`, `max()`, entre otras.

```py
# Ejemplo de funciones agregadas
mi_lista = [10, 20, 30, 40, 50]
longitud = len(mi_lista)  # Obtiene la longitud de la lista
suma = sum(mi_lista)  # Calcula la suma de los elementos de la lista
minimo = min(mi_lista)  # Obtiene el valor mínimo de la lista
maximo = max(mi_lista)  # Obtiene el valor máximo de la lista
print(longitud)  # Salida: 5
print(suma)      # Salida: 150
print(minimo)    # Salida: 10
print(maximo)    # Salida: 50
```

### **1.7 - Colecciones genéricas**
Python permite crear clases y métodos genéricos utilizando el módulo `typing`, que proporciona herramientas para definir tipos genéricos.

```py
from typing import TypeVar, Generic, List
T = TypeVar('T')
class Caja(Generic[T]):
    def __init__(self):
        self.elementos: List[T] = []

    def agregar(self, elemento: T) -> None:
        self.elementos.append(elemento)

    def obtener_elementos(self) -> List[T]:
        return self.elementos
# Ejemplo de uso de la clase genérica Caja
caja_de_enteros = Caja[int]()
caja_de_enteros.agregar(1)
caja_de_enteros.agregar(2)
print(caja_de_enteros.obtener_elementos())  # Salida: [1, 2]
caja_de_cadenas = Caja[str]()
caja_de_cadenas.agregar("Hola")
caja_de_cadenas.agregar("Mundo")
print(caja_de_cadenas.obtener_elementos())  # Salida: ['Hola', 'Mundo']
```

### **1.8 - Generadores**

- Los generadores son una forma especial de iteradores que extraen los valores de **uno en uno** lugar de almacenar todos los valores en memoria.  
- Hasta que no se solucite otro valor, el generador se mantiene pausado. Esta característica se conoce como **suspensión de estado**. 
- El generador se define utilizando la palabra clave `yield` en lugar de `return` dentro de una función. Cada vez que se llama al generador, este produce el siguiente valor en la secuencia y mantiene su estado para la próxima llamada.
- Para realizar la iteración sobre un generador, se puede utilizar un bucle `for` o la función `next()`.

```py
# Declarar el generador
def generador_numeros_pares(num):
    for i in range(num):
        yield i*2

# Instanciar el generador
numeros_pares = generador_numeros_pares(5)

# Usar del generador
## Llamada 1
print("Aquí hay código")
print(f"Llamada 1 al generador que extrae el valor: {next(numeros_pares)}")
## Llamada 2
print("Aquí hay código")
print(f"Llamada 2 al generador que extrae el valor: {next(numeros_pares)}")
## Llamada 3
print("Aquí hay código")
print(f"Llamada 3 al generador que extrae el valor: {next(numeros_pares)}")
...
```

!!! tip "Uso de yield from"
    También se puede utilizar `yield from` para delegar parte de la generación a otro generador o iterable. Este es particularmente útil para combinar múltiples generadores. 

```py
def generador_numeros_pares(num):
    for i in range(num):
        yield i*2

def generador_letras():
    yield "a"
    yield "b"
    yield "c"
    yield "d"

def generador_principal():
    yield from generador_numeros_pares(5)
    yield from generador_letras()

# Usar el generador principal
generador = generador_principal()
for valor in generador:
    print(valor)
```

También tendremos que tener en cuenta que `yield from` se comporta como un bucle `for` que itera sobre el iterable proporcionado, extrayendo cada valor y cediéndolo al llamador del generador principal.
```py
# código sin yield from
def devuelve_ciudades(*ciudades):
  for ciudad in ciudades:
    for letras in ciudad:
      yield letras

ciudades_generadas = devuelve_ciudades("Llombay", "Catadau", "Alfarp")
for letras in range(20):
  print(next(ciudades_generadas), end="_")

# código CON yield from
def devuelve_ciudades(*ciudades):
  for ciudad in ciudades:
    yield from ciudad

ciudades_generadas = devuelve_ciudades("Llombay", "Catadau", "Alfarp")
for letras in range(20):
  print(next(ciudades_generadas), end="_")
```




<!-- https://docs.python.org/es/3/tutorial/datastructures.html#dictionaries -->

<!-- https://tutorial.recursospython.com/colecciones/#diccionarios -->


<!-- https://www.pmareke.com/posts/generics/ -->
<!-- https://gemini.google.com/u/1/app/f1540b3c3cf5ad43?hl=es-ES -->



###################################
# hablar de los generadores en otro apartado ####
# hablar de los accesos a los elementos de las colecciones ####
mirar apuntes de iabd
################################################## -->

  




### https://docs.python.org/es/3/tutorial/datastructures.html








<!-- ### **2.6 - Expresiones regulares (validación de datos)** -->
<!-- https://hektorprofe.github.io/python/funcionalidades-avanzadas/expresiones-regulares/ -->

<!-- === "RA 6"
    |RA6. Escribe programas que manipulen información, seleccionando y utilizando tipos avanzados de datos.|Peso| -->
<!-- https://tutorial.recursospython.com/colecciones/ -->

<!-- |**c)** Se han utilizado listas para almacenar y procesar información.|10%| -->
<!-- PROGRAMACION GENERICA + GENERADORES -->

    <!-- |**g)** Se han utilizado expresiones regulares en la búsqueda de patrones en cadenas de texto.|10%| -->
<!-- https://python.sdv.u-paris.fr/17_expressions_regulieres/ -->
    
<!-- GENERICOS -->
<!-- https://chatgpt.com/c/69458417-050c-832e-9a1b-82f159d1ca90 -->
  <!-- |**f)** Se han creado clases y métodos genéricos.|10%| -->
<!-- https://ellibrodepython.com/abstract-base-class -->


<!-- https://python-para-impacientes.blogspot.com/ -->