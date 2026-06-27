public class Circulo {
  static double cuadrado = 25.52;
  public String triangular = "Tiangulemos";
  private double radio;
  private double area;
  private double perimetro;
  private String color;
  private int centroX, centroY;

  public Circulo(){
    radio = 50;
    color = "negro";
    centroX = 100;
    centroY = 80;
  }  

  public Circulo(double radio, String color, int centroX, int centroY){
    this.radio = radio;
    this.color = color;
    this.centroX = centroX;
    this.centroY = centroY;
  
  }  
    

  public double getRadio() {
    return radio;
  }

  public void setRadio(double nuevoRadio){
    radio = nuevoRadio;
  }

  public void decrece(){
    radio = radio / 1.3;   
  }

  public double area(){
    return Math.PI * Math.pow(radio, 2); 
       
  }

  public String toString(){
    return "Círculo de radio " + radio + ", color " + color + " y centro ("+ centroX + ","+centroY + ")";
  }

  static void metodoEstatico(){
    System.out.println("Este es um metodo de clase 2");

  }
 
}
