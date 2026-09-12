public class poo {
  private static class Persona{

    int edad;
    String nombre;
    String appelido_1;
    private String appelido_2;
    String dni;

    public void mostrarDatos(){
      System.out.println("datos: "+ edad + " " + nombre + " apellido 2 " + appelido_2);
    }

    public Persona(int edad){
      this.edad = edad;
      nombre = "javier";
      dni = "12345678U";
      appelido_2 = "egea";

      
    }

  } 
  
  
  
  
  public static void main(String[] args) {
    Persona alumno_1 = new Persona(20);
    alumno_1.mostrarDatos();  
    alumno_1.appelido_2="Blasco";
    alumno_1.mostrarDatos();

    

    
  }
}
