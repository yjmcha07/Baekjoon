import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int A = scanner.nextInt();
        int B = scanner.nextInt();
        int C = scanner.nextInt();
        int D = scanner.nextInt();
        int E = scanner.nextInt();
        int sixedValue = (A*A+B*B+C*C+D*D+E*E)%10;
        System.out.println(sixedValue);
        
        scanner.close();
    }
}