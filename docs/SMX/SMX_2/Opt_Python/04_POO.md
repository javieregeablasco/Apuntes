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

## **1 - Introducción a la programación orientada a objetos** 
La Programación Orientada a Objetos (POO) (Object-Oriented Programming (OOP) en inglés) es un paradigma de programación que surgió en los años 1970.

Este enfoque permite organizar el código en **clases y objetos**, de forma que el diseño del software se asemeje al modo en que representamos los elementos del mundo real.

Cada clase define las características (atributos) y los comportamientos (métodos) de un tipo de objeto.  
De esta forma, la POO permite modelar entidades y sus relaciones de forma modular, reutilizable y mantenible.

!!! abstract "Ejemplo: Objeto “Coche”"
    !!! info "Atributos:"  
        - color  
        - ruedas  
        - peso  
        - tamaño  

    !!! info "Métodos:"  
        - arrancar()  
        - frenar()  
        - acelerar()  
        - girar()  


## **2 - Principios básicos de la POO** 
La programación orientada a objetos está basada en 6 principios o pilares básicos:

- Abstracción
- Encapsulamiento
- Herencia
- Polimorfismo
- Cohesión
- Acoplamiento

### **2.1 - Abstracción**
La abstracción consiste en representar los aspectos esenciales de un objeto, ocultando los detalles innecesarios.
En otras palabras, se centra en qué hace un objeto y no cómo lo hace.

**Ejemplo:**  
Al conducir un coche, no se necesita saber cómo funciona el motor, solo se usan los pedales y el volante.
En código, se define una clase con métodos como arrancar() o frenar() sin necesidad de mostrar su implementación interna.

### **2.2 - Encapsulamiento**
El encapsulamiento consiste en proteger los datos de un objeto para evitar que se acceda o modifique su estado directamente desde fuera de la clase.
Los atributos suelen declararse como privados o protegidos, y se accede a ellos mediante métodos públicos llamados getters y setters.

**Ejemplo:**  
```PY
class Coche:
    def __init__(self):
        self.__velocidad = 0  # atributo privado

    def acelerar(self):
        self.__velocidad += 10

    def obtener_velocidad(self):
        return self.__velocidad
```

### **2.3 - Herencia**
La herencia permite que una clase **herede atributos y métodos de otra clase**. Esto facilita la **reutilización** del código y la creación de jerarquías de clases.

**Ejemplo:**    
En este ejemplo vemos como la clase `Coche` hereda el atributo `color` de `Vehiculo`.
```py
class Vehiculo:
    def __init__(self, color):
        self.color = color

class Coche(Vehiculo):
    def __init__(self, color, modelo):
        super().__init__(color)
        self.modelo = modelo
```

### **2.4 - Polimorfismo**
El polimorfismo permite que un **mismo método tenga distintos comportamientos** según el objeto que lo invoque.
En Python, esto se logra mediante la sobrescritura de métodos o el uso de métodos con el mismo nombre en diferentes clases.

**Ejemplo:**  
En este ejemplo vemos como las clases Perro y Gato heredan de animal 
```py
class Coches:
    def acelerar(self):
        pass

class Coupe(Coches):
    def acelerar(self):
        return "¡Acelerando a tope!"

class Sedan(Coches):
    def acelerar(self):
        return "Acelerando con calma"

for coche in [Coupe(), Sedan()]:
    print(coche.acelerar())
```

### **2.5 - Cohesión**
La cohesión mide cuán relacionadas están las responsabilidades dentro de una clase.
Una clase altamente cohesionada tiene una única responsabilidad bien definida, lo que facilita su mantenimiento, reutilización y comprensión.

**Ejemplo:**  
Una clase GestorCoches debería encargarse únicamente de gestionar las **características de los coches**, no de manejar información de **camiones o motocicletas**.

La alta cohesión mejora la **legibilidad del código** y reduce errores, siguiendo el principio de **una clase, una responsabilidad**.

### **2.6 - Acoplamiento**
El acoplamiento mide el grado de dependencia entre las clases o módulos.
En la POO se busca un bajo acoplamiento, es decir, que las clases dependan lo menos posible unas de otras.

**Ejemplo:**    
Cuando una clase Concesionario necesita obtener información de un Coche, no debe acceder directamente a sus atributos internos, sino hacerlo mediante un método (público) que proporcione esos datos.

```py
class Coche:
    def obtener_modelo(self):
        return "Toyota Corolla"

class Concesionario:
    def __init__(self, coche):
        self.coche = coche

    def mostrar_coche(self):
        print(self.coche.obtener_modelo())

# Ejemplo de uso
mi_coche = Coche()
concesionario = Concesionario(mi_coche)
concesionario.mostrar_coche()
```

### **3 - Cómo usar los objetos**
Ahora que sabemos qué es un objeto, veamos paso a paso cómo trabajar con ellos en Python.

#### **3.1 - Crear una clase**
Una clase es como un molde o plantilla que define cómo serán los objetos que creemos a partir de ella.
Dentro de una clase se especifican sus atributos (las características) y sus métodos (las acciones que puede realizar).

**Ejemplo:**
```py
class Coche:
    # Atributos de la clase
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.ruedas = 4
        self.abs_serie = True    

    # Metodos de la clase
    def arrancar(self):
        print("El coche está arrancando.")
    
    def acelerar(self):
        print("El coche está acelerando.")
    
    def frenar(self):
        print("El coche está frenando.")
    
    def girar(self):
        print("El coche está girando.")
```

- **Método constructor __init__()**  
El método **__init__()**, es el constructor de la clase (Coche).  
Se ejecuta automáticamente cada vez que se crea una nueva instancia (crea un nuevo objeto) de la clase (Coche).  
Su función es inicializar los atributos del objeto con los valores que se le pasan al crear la instancia.  

- **Parámetro self**  
El parámetro self es el primer parámetro obligatorio de todos los métodos de instancia dentro de una clase (en Python).  
Representa al objeto actual (la instancia) que está utilizando el método.

Gracias a self, la clase puede acceder y modificar sus propios atributos.
Por convención se llama self, aunque podría llarmarse de cualquier otra forma, pero se recomienda mantener esta convención.

#### **3.2 - Instanciar una clase y usar métodos**
Una vez definida la clase, podemos crear objetos (también llamados instancias) a partir de ella.
Cada objeto es independiente, aunque comparta la misma estructura y métodos definidos en la clase.

**Ejemplo**
```py
# Crear (instanciar) un objeto de la clase Coche
mi_coche = Coche("Toyota", "Corolla", "Rojo")

# Usar los métodos del objeto
mi_coche.arrancar()
mi_coche.acelerar()
mi_coche.frenar()
mi_coche.girar()
```

Podemos crear tantos objetos como necesitamos.  
Cada objeto mantiene sus propios valores de atributos y no afecta a los demás.
```py
coche1 = Coche("Ford", "Focus", "Blanco")
coche2 = Coche("Honda", "Civic", "Gris")
coche2 = Coche("Toyota", "Corolla", "Verde")

print(coche1.marca, coche1.color)
print(coche2.marca, coche2.color)
print(coche3.marca, coche3.color)

```

#### **3.3 - Acceder a los atributos del objeto**
Los atributos definidos dentro del método __init__() pueden consultarse o modificarse directamente a través del nombre del objeto seguido de un punto (.):
```py
print(mi_coche.marca)     # Muestra la marca del coche
print(mi_coche.color)     # Muestra el color del coche
print(mi_coche.ruedas)    # Muestra el número de ruedas
```

!!! danger "¡Si no tomamos las  medidas oportunas, podremos modificarlos los atributos del objeto desde fuenra de la clase!"
    ```py
    print("Color coche original", mi_coche.color)
    mi_coche.color = "Azul"
    print("Color coche repintado", mi_coche.color)
    ```


<!-- Cómo usar los objetos
 https://www.luisllamas.es/que-es-un-objeto-en-programacion/ -->
<!-- https://gitlab.com/josedom24/curso_programacion_python3/-/tree/master/curso/u39?ref_type=heads -->
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