public class Persona{
  private String nombre;
  private int edad;

  public Persona(String nombre, int edad){
    this.nombre = nombre;
    this.edad = edad;
  }

  public String devuelveNombre() {
    return nombre;
  }

  public int devuelveEdad() {
    return edad;
  }
  
  public void mostrarDatos(){
    System.out.println("Nombre: "+ nombre);
  }

  public String toString(){
    return "Nombre: " + nombre + " Edad: " + edad;
  }

}