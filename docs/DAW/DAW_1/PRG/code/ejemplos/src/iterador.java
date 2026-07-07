import java.util.ArrayList;
import java.util.Iterator;

public class iterador {
  public static void main(String[] args) {
    ArrayList<String> ciudades = new ArrayList<String>();
    ciudades.add("Paris");
    ciudades.add("Madrid");
    ciudades.add("Valencia");
    ciudades.add("Barcelona");

    for (int i=0; i<ciudades.size();i++){
      Iterator<String> ciudad = ciudades.iterator(); 
      System.out.println(ciudad.next());
    }



  }
}
