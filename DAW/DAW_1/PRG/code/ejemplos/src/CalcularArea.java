// Clase abstracta base
abstract class Calculador {
    private int numeroLados;

    public Calculador(int numeroLados) {
        this.numeroLados = numeroLados;
    }

    public abstract double area();
}

// Representación de un punto en el plano
class Punto2D {
    private double x, y;

    public Punto2D(double x, double y) {
        this.x = x;
        this.y = y;
    }

    // Calcula la distancia euclidiana entre dos puntos
    public static double distancia(Punto2D p1, Punto2D p2) {
        return Math.sqrt(Math.pow(p2.x - p1.x, 2) + Math.pow(p2.y - p1.y, 2));
    }
}

// Clase Triángulo que hereda de Calculador
class Triangulo extends Calculador {
    private Punto2D p1; // Corregido: Ahora son de tipo Punto2D
    private Punto2D p2;
    private Punto2D p3;

    public Triangulo(Punto2D p1, Punto2D p2, Punto2D p3) {
        super(3); // Un triángulo siempre tiene 3 lados
        this.p1 = p1;
        this.p2 = p2;
        this.p3 = p3;
    }

    @Override // Buena práctica aplicada
    public double area() {
        // Corregido: Pasamos las variables directamente sin redeclarar el tipo
        double a = Punto2D.distancia(p1, p2);
        double b = Punto2D.distancia(p2, p3);
        double c = Punto2D.distancia(p3, p1);
        
        // Fórmula de Herón
        double s = (a + b + c) / 2;
        return Math.sqrt(s * (s - a) * (s - b) * (s - c));
    }
}


// Clase principal que contiene el método main
public class CalcularArea {
    public static void main(String[] args) {
        // Definimos un triángulo rectángulo de base 3 y altura 4
        Punto2D puntoA = new Punto2D(0, 0);
        Punto2D puntoB = new Punto2D(3, 0);
        Punto2D puntoC = new Punto2D(0, 4);

        Calculador miTriangulo = new Triangulo(puntoA, puntoB, puntoC);
        
        // El área debería ser (base * altura) / 2 -> (3 * 4) / 2 = 6
        System.out.println("El área del triángulo es: " + miTriangulo.area());
    }
}