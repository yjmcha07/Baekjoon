import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int A = scanner.nextInt();
        int B = scanner.nextInt();
        int total = B-A;
        System.out.println(total + " " + B);
        
        scanner.close();
    }
}