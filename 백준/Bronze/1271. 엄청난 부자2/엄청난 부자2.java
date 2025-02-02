import java.math.BigInteger;
import java.util.Scanner; 

public class Main{
    public static void main(String[]args){
        Scanner scanner = new Scanner(System.in);
        BigInteger A = scanner.nextBigInteger();
        BigInteger B = scanner.nextBigInteger();
        
        BigInteger quotient = A.divide(B);
        BigInteger remainder = A.remainder(B);
        
        System.out.println(quotient);
        System.out.println(remainder);
    }
}