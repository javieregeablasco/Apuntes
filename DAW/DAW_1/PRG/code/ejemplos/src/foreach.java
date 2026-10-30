import java.util.Random;


public void foreach {
  static final int variableEstatica = 25;
  
  class Objeto {
  
    int entero_1 = 25;
    int entero_2 = 35;
    int entero_3 = 45;
  
    public void mostraValores(){
      System.out.println(entero_1);
    }
    
    public void mostraValores_2(){
      System.out.println(entero_2);
    }
  
  public static void main(String[] args) {
    
  }
  
  
  // static void vararg(int... num){
    //   if (num != null){
      //     System.out.println( "Numero de parametros recibidos: "+ num.length);
      
      //     for (int i=0; i<num.length;i++){
        //       System.out.println("Indice parametro recibido: "+ i + " contenido parametro: "+num[i]);
        //       }
        
        //   } else {
          //     System.out.println("No se ha pasado ningun parametro al metodo");
          //   }
          // }
          
          
          
          // public static void main(String[] args) {
          //   // vararg(null);
          //   // vararg(25,26,32);
          //   int[] numerosPrimos ={1,3,5,7,11,13,17,19,23};
          //   // int[] array_1;
          //   int[] array_2 = new int[numerosPrimos.length];
            
            // array_1= numerosPrimos.clone();
            // System.out.println("Resultado clonacion:");
    // for (int i:array_1){
    //   System.out.print( i + " ");
    //   }
    // array_2 = array_1;
    // array_2[0]=25;
    // System.out.println();
    // System.out.println("Valor en array_1: " + array_1[0]);
    // System.out.println("Valor en array_2: " + array_2[0]);

//     System.arraycopy(numerosPrimos, 2, array_2, 1, 4);
//     for (int i : array_2){
//       System.out.print(i+" ");

//     }
    


//   } 
// }  


    
    // int[] arrayForEach = new int[10];

    // Random aleatorio = new Random();

    // for (int i = 0; i<arrayForEach.length; i++){
    //   arrayForEach[i]=aleatorio.nextInt(25, 99);
    //   System.out.print(arrayForEach[i]+" ");
    // }
    // System.out.println();
    // for (int i: arrayForEach){
    //   i=aleatorio.nextInt(25, 99);
    //   System.out.print(i+" ");
    // }

  
