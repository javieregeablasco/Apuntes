public class javer33 {
  public static void main(String[] args) {
    Persona pedro = new Persona("pablo", 46);
    Estidiante javier = new Estidiante("Javier", 33, 124);

    System.out.println(javier.devuelveEdad() + javier.devuelveNombre() + javier.obtenerDatosAlumno());
    System.out.println("Sin evocar al metodo: " + javier);
    System.out.println(pedro.devuelveEdad() + pedro.devuelveNombre());
    javier.obtenerDatosAlumno();
  }
}
