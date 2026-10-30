import java.util.Random;

public class excepciones {
  public static void main(String[] args) {
    int num1 = 1;
    int[] array = new int[3];

    Random aleatorio = new Random();

    for (int i = 0; i<3 ; i++){
      array[i] = aleatorio.nextInt(0, 10);
      System.out.println("Valor almacenado en el arrat: " + array[i] + " en la posicion: " + i );

    }
    
    try {
      System.out.println("Valor array posicion :" + array[3]);
    } catch (Exception e) {
      System.out.println("El indice 3 no es valido");
      // TODO: handle exception
    }
  }
}
