https://www.youtube.com/watch?v=BugfoJ-ZM6U&list=PLG1qdjD__qH6ULjW5iN8E45m5nkaCNbUu&index=108

# clase inmutables

una clase inmutable es aquella que no permite modificar sus atributos una vez que se ha creado el objeto. Para crear una clase inmutable, se deben seguir las siguientes reglas: 

1. Declarar la clase como final, para que no pueda ser heredada.
2. Declarar todos los atributos como privados y finales, para que no puedan ser modificados.

```java
String s = "Hola";
S = s + " mundo!"; // se crea un nuevo objeto de tipo String con el valor "Hola mundo!" y se asigna a la variable s. El objeto original "Hola" no se modifica.
```

```java
String nombre;
public final class Persona {
  
    private final String nombre;
    private final int edad;

    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public int getEdad() {
        return edad;
    }
}
```

# paso por valor o por referencia en la POO

El paso de parametros en la POO es por valor, pero si el parametro es un objeto, se pasa la referencia del objeto.
En java los tipos primitivos se pasan por valor y los objetos se pasan por referencia.
Los tipos primitivos son: byte, short, int, long, float, double, char y boolean.
Las strings son objetos inmutables, por lo que se pasan por referencia, pero no se pueden modificar.


# metodo constructor

- Metodo especial que se ejecuta al crear un objeto de la clase.
- caracteristicas:
  - mismo nombre que la clase
  - no tiene tipo de retorno
  - puede tener argumentos
  - puede estar sobrecargado
  - puede ser publico, privado o protegido.
  - puede inicializar los atributos de la clase con valores por defecto o con valores pasados como argumentos.

# metodos de clase

- acceso: public: accesible desde cualquier clase
- acceso: private: accesible solo desde la clase donde se define.
- acceso: protected: accesible desde la clase donde se define y desde las clases que heredan de ella.
acceso: default: accesible desde la clase donde se define y desde las clases del mismo paquete.

- static: el metodo pertenece a la clase y no a los objetos de la clase.

- final: el metodo no puede ser sobrescrito por las clases que heredan de la clase donde se define.

- tipo de retorno: el tipo de dato que devuelve el metodo. Si no devuelve nada, se usa void.

- nombre del metodo: el nombre del metodo debe ser un identificador valido.

- args: los argumentos que recibe el metodo. Pueden ser de cualquier tipo de dato.

# poo programacion

clases: tipo de datos: definen el conjunto de atributos y de posibles valores.

clase programa: Es la que contiene el main.

[ambito] class NombreDeLaClase {
  // Definicion de atributos
  [ambito] tipo nombreDeVariable_1;
  [ambito] tipo nombreDeVariable_2;

  // Defincion de metodos
  // Contructores
  ...
  // Otros métodos
}


# sobrecarga de cosntructores en POO

# POO

clase: empieza con un mayuscula
metodo: comineza con una aminuscula
variable: empieza minuscula.

metodo de clase: static
metodo de objeto (instancia / constructor): public

# ordenar arrays

# clonar y copiar arrays

# var args

parametro de longitud variable.

# for each

# arrays

# sobrecarga de metodos

# metodos (funciones)

# casting y parse

conversiones de tipos (siempre que sea posible)

# identado automatico

para establecer el indentado usar en VSCV alt + shift + f
kernighan y ritchie (el más usado)

allman

# ambito de las variables

tambien conicido como scope.

# bucles anidados

# finalizacion condicional de bucles

break
continue

# bucles

while
for

# operador ternario

operador ternario.
variable = condicion ? resultado_si_cierto : resultado_si_falso

# estructuras de control

condicionales
switch

alt + shft + f → pone el codigo en linea

# caracteres especiales

# palabras reservadas de java

palabras que no se pueden usar para definir variables.

# declarar variables

uso de guion bajo para mejorar legibilidad
int mil = 1_000;
int millon = 1_000_0000;
float millon_2 = 1_00_00_00.0_0_5f;


La declaracion de las variables no puede empezar con un numero.
debe seguir el camelcase

variavles de tipo float
float f1 = 1f;
float f2 = 5.4f;
float f3 = 0.55e-2f;
float f3 = -5.44e-2f;

declarar una lista de variables
int a =5, b=7;
short c=-1, d,e,e=4;

declarar una a una las variables
int num; #sin asignar valor
int numeor = 22; #asignar valor

# tipos de variables

# syso

# hello world

compilar programa:
javac intro.java
→ intro.class

ejecutar programa:
java intro
tambien se puede dar al play de vsc

instalacion java

para usar un programa escrito en java:
JRE java runtime environment
JVM maquina virtual de java

para crear un programa en JAVA
JDK java developmwent kit
IDE (VSC)

instalacion
1 jdk.
2 vsc
3 extensiones de java para vsc (extension pack for java)
