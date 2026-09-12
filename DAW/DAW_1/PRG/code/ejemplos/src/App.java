public class App {
    public static void main(String[] args) throws Exception {
        Circulo C1 = new Circulo();
        C1.setRadio(2.9);
        System.out.println("Los datos del ciculo son: "+ C1.toString());
        // System.out.println(Circulo.metodoEstatico());
        Circulo.metodoEstatico();
        
        Circulo C2 = new Circulo(24,"verde",34,45);
        System.out.println("Los datos del ciculo son: "+ C2.toString());
        Circulo.cuadrado = 2505.22;
        C2.triangular = "Nueva definicion";
        

    }
}
 