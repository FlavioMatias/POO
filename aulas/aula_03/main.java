import java.util.Scanner;

public class main {
    public static void main(String[] args)
    {
        Scanner banana = new Scanner(System.in);

        double a = banana.nextDouble();

        int b = banana.nextInt();

        // int soma = a + b;

        System.out.println("soma:" + (a + b));        
        
        banana.close();




    }
}
