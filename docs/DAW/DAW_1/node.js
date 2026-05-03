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
let simbol = Symbol("simbol")

// cuidado con el consumo de memoria
// solo para enteros
let enteroGrande = BigInt(222222222222222222222222222222222222222222222222);
enteroGrande = 3222222222222222222222222222222222222222222222222n;

// https://youtu.be/1glVfFxj8a4?si=x68EJqBim_OnAWPc&t=4738
let variable_1 = 4;
let variable_2 = "4";
 
// console.log("Tipo de variable_1:",typeof(variable_1));
// console.log("Tipo de variable_2:",typeof(variable_2));
// console.log("Tipo abstracto",variable_1==variable_2);
// console.log("Tipo por tipo",variable_1===variable_2);

let palabreria = "Hola que tal";
// console.log(palabra.length);
// console.log(palabra.slice(6,10))
// console.log(`La palabra ${palabreria} contiene`+palabreria.length);
// console.log(`La palabra ${palabreria} contiene`,palabreria.length);
let miArray = [];
let miArray2 = new Array();
miArray2[0]= "palabras333";
console.log(miArray2);
miArray2.push("otra palabra");
console.log(miArray2);