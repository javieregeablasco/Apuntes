https://youtu.be/iJvLAZ8MJ2E?si=-Gb7VdqpgmsUh_Rz&t=11893

// proxy


// class coche {

// };
// carro = new coche();
// console.log("¿Es carro una instancia de la clase coche?", (carro instanceof coche) ? "Verdadero":"falso")
// ------------------------ SYMBOL REVISAR
// ------------------------ mixins REVISAR


// clase abstracta. no se puede instanciar directamente.

// class Animal {

//   constructor(nombre){
//     this.nombre=nombre
//   }
//   sonido(){
//     console.log("El animal eminte sonido")


//   }
// }

// class Persona {
//   constructor(nombre,edad){
//     this.nombre=nombre
//     this.edad=edad

//   }
//   saludos(){
//     console.log(`Hola mundo, soy ${this.nombre}`)
//   }
// }

// person1 = new Persona("Javier",34);
// person1.saludos();

// person1.sayAge = function(){
//   console.log(`Tengo ${this.edad} años`)
// }
// person1.sayAge()
// function funcion(param_1,param_2){

//   console.log("Hola mundo")
// }

// const funcion_1=(param_1,param_2)=>{
//   console.log("Hola mundo_1")

// } 

// funcion();
// funcion_1();
// iterar sets


// sets avanzados
// colecciones de valores unicos, no indexados, iterables y dinamicos.

// array_1 = [0,1,2,3,6,4,6]
// set_1 = new Set(array_1)
// // console.log([...set_1])

// // union
// set_2 = new Set([0,2,6,9,7,3])
// set_3 = new Set([...set_1,...set_2])
// // console.log([...set_3])

// array_4 = [2,2,...array_1,4,6]
// console.log(array_4)

//https://youtu.be/iJvLAZ8MJ2E?si=ARWqWgxqe4dNmSSZ&t=6292

// buscar elementos de un array.
// let desordenado = [0,10,5,9,3,6];
// console.log(desordenado.includes(11))
// console.log(desordenado.find(Element =>Element % 2)); // solo devuelve el primer elemento encontrado.


// ordenacion de arrays
// let desordenado = [0,10,5,9,3,6];
// console.log(desordenado.sort())

// console.log(desordenado.sort((a,b) => a-b))
// flatMap permite definir el nivel para aplanar.

// let frases = ["hola mundo", "adiós mundo"];
// let resultado = frases.flatMap(frases => (frases.split(" ")));
// console.log(resultado)

// flat permite aplanar arrays anidados.
// let array = [0,[1,2,[3,4,5,6,[7,8,9]]]]
// for (let i in [0,1,2,3]){
//   console.log(array.flat(i))
// }
// let flattenedArray = array.flat(0)
// reduce
// let numbers = [0,1,2,3,4,5,6,7,8,9,10];
// let sum = numbers.reduce((previous,current)=>previous + current);
// let sum = numbers.reduce((previous,current)=>console.log(previous,current));
// console.log(sum);
// filter
// let even = numbers.filter(Element => Element % 2 ==0)
// console.log(even)


// map permite aplicar una operacion a cada uno de los elementos
// let array = numbers.map(Element => Element*2)
// console.log(array.forEach(Element => console.log(Element)))


// forEach
// numbers.forEach(() => console.log(numbers));
// numbers.forEach(element => console.log(element));



// callback.
// pasar funcion a otra funcion para modificar su comportamiento (introduccion a la asincronia).

// function processData(data, callback){


// }

//https://youtu.be/iJvLAZ8MJ2E?si=YEKmXcQm3jugMXiG&t=3678

// currying

// function curry(a){
//   return function(b){
//     return function(c){
//       return a+b+c
//     }
//   }
// }

// const sumaAB = curry(1)(2)(3)
// const sumaAB = curry(1)(2)

// console.log(sumaAB)

// funciones parciales
// function funcionParcial(a){
//   return function(b,c) {
//     return a+b+c
//   }
// };

// const constante = funcionParcial(2);

// console.log(constante(3,4));

//invento
// const funcion = () => console.log("halo mundo");

// funcion()

// recursividad se invoca a si misma
// function factorial(n) {
//   if (n<=1){
//     return 1
//   }
//   return n * factorial(n-1) 
// };

// console.log(factorial(10))


// operador spread [...numbers]
//expandir un Array  desempquetar un array
// const array = [1,2,3,4,5,6];
// function sumarArray(a,b,c) {
//   return a+b+c 
// };

// console.log(sumarArray(...array))





// operador REST [...numbers]
// function sumar(...numeros){
//   let resultado = 0;
//   for (let iterador of numeros){
//     resultado += iterador
//   };
//   return resultado
// }

// console.log(sumar(5,5,5))

// IIFE
//funciones especiuales que se ejecutan en el momento en que se definen.

// console.log("Hello world")

// (() =>{
//   console.log("Hello world")
// })()


// funciones flecha

// const nombre = "Javier";

// const contenedor = {

//   nombre: "Javier",
//   saludos_1: function(){
//     console.log(`Hola ${this.nombre}`)
//   },

//   saludos_2: () => {
//     console.log(`Hola ${nombre}`)
//   }
// }

// contenedor.saludos_1()
// contenedor.saludos_2()
//retorno implicito
//const mutiplicar = (a,b) => a*b;
//console.log(mutiplicar(2,5))



// funciones

// function funcion(nombre, numero=5){
//   console.log(`Hola ${nombre}, ${numero}`);
// }

// funcion("mundo",46)

// https://youtu.be/iJvLAZ8MJ2E?si=3_R3ZxDXSq8nwPf8&t=30


// metodos de console.log()
//console.assert(condicion)

// const edad = 18;
// console.assert(edad > 20)

// metodos estaticos.
// class operacionMatematica {

//   static suma(a,b){
//     return console.log(`La suma de ${a}+${b} es`,a+b);
//   }
// }

// operacionMatematica.suma(15,20);


// herencia
// class Animal {
//   constructor(nombre,patas,pelage){
//     this.nombre=nombre;
//     this.patas=patas;
//     this.pelage=pelage;
//   }
//   salida() {
//     console.log("objeto creado correctamente");
//   }


// }

// const gallina = new Animal("Ave",2,"plumas")

// console.log(gallina.salida())

// https://youtu.be/1glVfFxj8a4?si=jKltKV2qmT4Uozwy&t=18002

// getters y setters


// propagacion
// let array_1 = [1,2,3]; 
// let array_2 = [4,5,6]; 
// let array_3 = ["a","b","c"];

// console.log(array_3)

// let [a, b, c] = array_2; 

// array_3 = [...array_3, ...array_1]
// console.log(a,b,c)

// destructuracion

// let myArray = ["Javier","Egea","Blasco",36,"Varón"]
// console.log(myArray)

// let [desc_1, desc_2, desc_3] = myArray
// console.log(desc_1)
// console.log(desc_2)
// console.log(desc_3)
// let persona = {
//   "nombre": "Javier",
//   "apellido_1": "Egea",
//   "apellido_2": "Blasco",
//   "edad": 37
// }

// let propiedad_1 = persona.nombre
// let propiedad_2 = persona.apellido_2
// console.log(`Edad: ${propiedad_1}`)
// console.log(`Edad: ${propiedad_2}`)

// https://youtu.be/1glVfFxj8a4?si=412PDUev5A09Nx0T&t=14637

// const myfunct = (a,b) => {
//   console.log(`Hello world, valor de a: ${a}, valor de b: ${b}  `)

// }


// function myfunct() {
//   console.log("Hello world")
// };

// myfunct("JaVIER",30);

// for (let i = 0; i<10; i++) {
//   console.log(`Resultado: ${i}`)
//   document.write(`<h5>Resultado: ${i}` )
// }

// https://youtu.be/1glVfFxj8a4?si=Yox3no-eU15Y0buq&t=11930



// console.log("hello world");
// console.log('hello world');
// console.log(`hello world`);

// variables

// var → no se recomienda su uso al ser variable globales
// console.log(hello);
// var hello = "helloworld con var";

// let → uso obligatorio
// let hello = "version-1";
// console.log(hello)
// hello = "version-2";
// console.log(hello)
// hello = "version-3";
// console.log(hello)

// const

// tipos de datos
// let simbol = Symbol("simbol")

// // cuidado con el consumo de memoria
// // solo para enteros
// let enteroGrande = BigInt(222222222222222222222222222222222222222222222222);
// enteroGrande = 3222222222222222222222222222222222222222222222222n;

// let variable_1 = 4;
// let variable_2 = "4";
 
// console.log("Tipo de variable_1:",typeof(variable_1));
// console.log("Tipo de variable_2:",typeof(variable_2));
// console.log("Tipo abstracto",variable_1==variable_2);
// console.log("Tipo por tipo",variable_1===variable_2);

// let palabreria = "Hola que tal";
// console.log(palabra.length);
// console.log(palabra.slice(6,10))
// console.log(`La palabra ${palabreria} contiene`+palabreria.length);
// console.log(`La palabra ${palabreria} contiene`,palabreria.length);
// let miArray = [];
// let miArray2 = new Array();
// miArray2[0]= "palabras333";
// console.log(miArray2);
// miArray2.push("otra palabra");
// console.log(miArray2);
// pop ultimo y devuvle.
// shift agrega al principio.
