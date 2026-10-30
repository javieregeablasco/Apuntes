public class Estidiante extends Persona {
  private int NIE;
    
  public Estidiante(String nombre, int edad, int NIE){
    super (nombre, edad);
    this.NIE = NIE;
  }

  public int obtenerDatosAlumno(){
    return NIE;
  }

  public void mostrarDatos(){
    super.mostrarDatos();
    System.out.println("Estudiante matriculado con NIE: " + NIE);
  }

  public String toString(){
    return super.toString() + " NIE: " + NIE;
  }

}
