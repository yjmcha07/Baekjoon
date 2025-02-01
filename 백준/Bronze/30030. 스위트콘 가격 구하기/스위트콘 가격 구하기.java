import java.util.Scanner;

public class Main{
    public static void main(String[]args){
        Scanner scanner = new Scanner(System.in);
        int B = scanner.nextInt();
        int A = (int) Math.round(B/1.1);
        System.out.println(A);
        
        scanner.close();
        
    }
}