import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int buddhistYear = scanner.nextInt(); 
        int gregorianYear = buddhistYear - 543;
        System.out.println(gregorianYear);
        
        scanner.close();
        
    }
}