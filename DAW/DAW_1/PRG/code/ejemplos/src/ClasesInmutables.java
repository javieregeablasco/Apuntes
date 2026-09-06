public class ClasesInmutables {
  public static void main(String[] args) throws Exception {
    String palabra_1 = "palabra";
    String palabra_2 = "palabra";

    // if (palabra_1.equals(palabra_2)){
    if (palabra_1 == palabra_2){ // comparamos referencia de objetos
      System.out.println("las 2 palabras son la misma instancia");
    } else {
      System.out.println("Son 2 instancias diferentes");
    };
    
    
    String palabra_3 = new String("palabra");
    String palabra_4 = new String("palabra");

    if (palabra_3.equals(palabra_4)){
      System.out.println("las 2 palabras son la misma instancia");
    } else {
      System.out.println("Son 2 instancias diferentes");
    };
  }
}
