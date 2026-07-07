import java.util.ArrayList;
import java.util.Iterator;

public class iterador {
  public static void main(String[] args) {
    ArrayList<String> ciudades = new ArrayList<String>();
    ciudades.add("Paris");
    ciudades.add("Madrid");
    ciudades.add("Valencia");
    ciudades.add("Barcelona");
    
    Iterator<String> ciudad = ciudades.iterator(); 
    for (int i=0; i<ciudades.size();i++){
      System.out.println(ciudades.get(i));
    }

    while (ciudad.hasNext()) {
      System.out.println("Siguiente iterable: " + ciudad.next());
      
    }

    System.out.println("Uso de size(): " + ciudades.size());


  }
}
