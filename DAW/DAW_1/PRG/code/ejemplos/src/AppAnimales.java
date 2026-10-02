import java.util.ArrayList;


class Animal {
  public void hacerRuido(){
    System.out.println("El animal hacer un ruido");
  }
} 

class Perro extends Animal {
  public void hacerRuido(){
    System.out.println("El perro ladra");
  }
} 

class Pitbull extends Perro {
  public void hacerRuido(){
    System.out.println("El pitbull tiene un fuerte ladrido");
  }
} 

public class AppAnimales {
  
  public static void main(String[] args) {
    
    ArrayList<Animal> animales = new ArrayList<>();
    animales.add(new Animal());
    animales.add(new Perro());
    animales.add(new Pitbull());
    for (Animal a : animales) a.hacerRuido();

  }
}
