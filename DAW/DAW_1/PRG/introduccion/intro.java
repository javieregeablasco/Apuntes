package introduccion;

import java.util.Random;
import java.util.Scanner;
import java.math.*;
import java.util.random;

public class Intro {

  static void saludar(String nombre){
    System.out.println("Te saluda: "+nombre);
  }
  static String saludar(String nombre, String appelidos){
    return nombre+appelidos;
  }
  static void saludar(String nombre,Boolean casado){
    System.out.println("Es "+ nombre + casado);
  }

  // static void metodoLogico (int a, int b){
  //   System.out.println("resultado de a +b"+ (a+b));
    
  // }

  //  static int sumar(int a, int b, boolean operando){

  //   if (operando){
  //     return a+b;
  //   } else {
  //     return a-b;
  //   }
  //  }
  // static int metodoLogico (Boolean a, Boolean b){
  //   boolean resultado = a && b;
  //   int valor_1 = 42;
  //   int valor_2 = 24;
  //   if (resultado){
  //     return 42;
  //   } else {
  //     return 24;
  //   }
  //  }

  public static void main(String[] args) {
    int[][] arrayDesigual = new int[4][0];
    System.out.println(arrayDesigual[0].length);
    
    
    arrayDesigual[0] = new int[10];
    arrayDesigual[1] = new int[8];
    arrayDesigual[3] = new int[6];
    System.out.println(arrayDesigual[0].length);
    System.out.println(arrayDesigual.length);

    // int[] arrayEnteros = new int[10];
    // int[] otroArrayEnteros ={0,1,2,3,4,5};
    // int anotherArray[]=new int[10];
    // // int multiDimensionArray[][]=new int[10][8];

    // // multiDimensionArray[1][5]=52;
    // int[][] multiDimensionArray = {
    //   {1,0,2,5,12,1},
    //   {1,2,3,6,5,8},
    //   {9,8,5,3,5,2}
    // };

    // System.out.println(multiDimensionArray.length);

    // anotherArray[5]=25;
    // Random aleatorio = new Random();

    // for (int i=0; i<arrayEnteros.length; i++){
    //   arrayEnteros[i]=aleatorio.nextInt(99);
    // }
    
    // System.out.println(otroArrayEnteros[3]);
    // System.out.println("valor del array en pos 0 es: "+arrayEnteros[8]);

    // for (int i=0; i<=arrayEnteros.length-1;i++){
    //   System.out.println("indice: " + i + " " + arrayEnteros[i]);

    // };

    // String resultado = saludar("Carlos", "domingo");
    // System.out.println(saludar("Carlos", "domingo"));
    // System.out.println(resultado);

    // System.out.println("Resultado de a sumar: "+sumar(32, 44, false));
    // saludar("Pedro");
    // boolean b = true;
    // boolean a = false;
    
    // metodoLogico(24, 48);

    // System.out.println("Resultado de la operacion logica: " + resultado);
    // int a=2, b=3;
    // int c = (int)Math.pow(a, b);
    // System.out.println("Resultado de "+a+"potencia "+b+" = "+ c);

    // String cadena = "1234";
    // System.out.println("Suma de string +1: "+((Integer.parseInt(cadena))+1)); 

    // int variable = Integer.parseInt(cadena);
    // System.out.println("auto suma: " + (variable+1));
    // {
    //   int i = 0, j = 0;
    //   for (; i <= 10; i++) {
    //     for (; j <= 5; j++) {
    //       System.out.println("valor de i: " + i + " valor de j: " + j);
    //     }
    //   }
    //   ;
    //   System.out.println(i + " " + j);
    // }
    // {
    //   int i = 5, j = 4;
    //   System.out.println(i + " " + j);
    // }
    // System.out.println("Resultado final" + i + j);

    // for (int i=0; i<=10; i++){
    // for (int j=0; j<=5; j++){
    // System.out.println("valor de i: "+i+" valor de j: "+j);
    // }
    // }

    // for (int i=0; i<=10; i++){
    // if (i==8){
    // continue;
    // }
    // System.out.println("valor de i: "+i);
    // }
    // for (int i=0; i<=10; i++){
    // if (i !=8){
    // System.out.println("valor de i: "+i);
    // } else if (i==8){
    // System.out.println("i es igual a 8");
    // }
    // }

    // for (int i = 20; i==0; i-=3){

    // int valorIntroducido;
    // Scanner tecladoScanner = new Scanner(System.in);

    // do {
    // System.out.println(("introducir valor entero, 0 para salir"));
    // valorIntroducido = tecladoScanner.nextInt();
    // if (valorIntroducido !=0){
    // for (int i =valorIntroducido; i>=0; i-=3){
    // System.out.println("valor introducido: "+i);
    // }
    // } else {
    // System.out.println("Has introducido el valor 0 el programa finalizará...");
    // tecladoScanner.nextLine();
    // }

    // } while (valorIntroducido !=0);
    // System.out.println("Programa finalizado");
    // tecladoScanner.close();

    // for (int i = 0; i<=10; i+=2){
    // System.out.println("valor de i: "+i);

    // }

    // int numeroIntroducido=1;
    // Scanner introducirValor = new Scanner(System.in);

    // while (numeroIntroducido !=0){
    // System.out.println(("introducir valor numerico, 0 para salir del
    // programa."));
    // numeroIntroducido = introducirValor.nextInt();
    // };
    // System.out.println("Programa finalizado");
    // introducirValor.close();
    // while (a<=10){

    // a++;
    // System.out.println("valor de a: "+a);

    // }

    // do {
    // System.out.println("valor: "+ a);
    // a++;

    // } while(a<=10);

    // int ternario = 110;
    // int x;

    // x = ternario == 111 ? ternario*2: ternario+10;

    // equivale a
    // if (ternario == 111) {
    // x= ternario*2;
    // } else {
    // ternario += 10;
    // }
    // System.out.println(x);

    // int a = 22;
    // int b = 3;
    // int i = 5;

    // switch (a) {
    // case 10:
    // System.out.println("el valor es: 10");
    // break;

    // case 20:
    // System.out.println("el valor es: 20");
    // break;

    // case 30:
    // System.out.println("el valor es: 30");
    // break;

    // default:
    // System.out.println("ningun valor encontrado");

    // }
    // if (i == 2){
    // System.out.println(("i es igual a: "+ a));
    // } else if (i == 3) {
    // System.out.println("i es igual a: "+ b);
    // } else {
    // System.out.println("i no es igual a: "+ a +" o a: "+b);
    // };

    // System.out.println("Programa finalizado");
    // double a = 10;
    // double b = 3;
    // double c = a/b;
    // System.out.println(c);
    // float d = 10;
    // float e = 3;
    // float f = d/e;
    // System.out.println(f);
    // Scanner entrada = new Scanner(System.in);
    // System.out.println("introducir texto");
    // System.out.println("resultado de la entrada 1: " + entrada.nextLine());
    // System.out.println("introducir texto");
    // System.out.println("resultado de la entrada 2: " + entrada.next());
    // entrada.close();

    // int a = 3;
    // // int c = ++a;
    // int d = a++;

    // System.out.println(c);
    // System.out.println(d);
    // var palabra = "Esto es un texto";
    // System.out.println(palabra.length());
    // int a = 0x03;
    // System.out.println(a);
    // int b = 0b11;
    // System.out.println(b);
    // float c = 3f;
    // System.out.println((int)c);
    // int d = 2;
    // System.out.println(~d);
    // System.out.println(d>>1);
    // System.out.println(d<<1);
    // int a = 5;
    // int b = 10;
    // int c = ++b;
    // System.out.println(c);
    // String frase = "Esto es una cadena de texo";
    // // System.out.println("\"+"+esto es un texto entre comillas+"\"");
    // System.out.println("\"" + "esto es un texto entre comillas" + "\"");

    // String frase_2 = " Esto es una cadena de texo con espacion antes y/o despues
    // ";
    // String frase_3 = "Esto es una cadena de texo con espacion antes y/o despues";
    // System.out.println(frase_2.trim());
    // System.out.println(frase_3);
    // System.out.println(frase+" "+frase.length());
    // System.out.println(frase.charAt(5) );
    // System.out.println(frase.toUpperCase() );
    // System.out.println(frase.trim() );
    // System.out.println(frase.substring(5,10).length());
    // float flotante = 0.25f;
    // int entero = 25;
    // float resultado = flotante*entero;
    // System.out.println(resultado );

    // char unicode = '\u00a9';
    // System.out.println(unicode);
    // char letra = 'A'; // cuidado con las comillas simples
    // char letra_1 = 0x7d; // cuidado con las comillas simples
    // letra +=1;
    // System.out.println("resuñtado "+letra_1);
    // boolean binario = true;
    // boolean booleano = 7 == 8;
    // boolean booleano_2 = 7 != 8;
    // byte hexadecimal = (byte)0xFF;
    // int decimal = 0xff;
    // byte decimal_2 = (byte)0b11110000;
    // byte binario = 25;
    // float variableFlotante = -5.44e-2f;
    // float millon_2 = 1_00_02_00.0_0_5f; // no funciona solo 6 digitos en pantalla
    // double millon_3 = 1_00_02_00.0_0_5; //

    // var resultado = 22;
    // int resultado = 22;
    // final int resultado = 22;
    // int resultado_2 = 33;
    // System.out.println("Hello x con salto de linea");
    // System.out.print("Hello x sin salto de linea "+"Este contenido esta
    // concatenado");
    // System.err.println();
    // System.out.println("Hello x sin salto de linea "+resultado+resultado_2);
    // System.out.println("Hello x sin salto de linea "+"(Este contenido esta
    // sumado)");
    // System.out.println("Hello x sin salto de linea "+(resultado+resultado_2));
    // System.out.println(resultado);
    // System.out.println("resultado binario es "+ binario);
    // System.out.println("resultado flotante es "+ millon_2);
    // System.out.println("resultado double es "+ millon_3);
    // System.out.println("resultado hexadecimal es "+ decimal_2);
    // System.out.println("resultado booleano es "+ booleano);
  }
}