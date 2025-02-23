import java.util.Scanner;
public class Main{
  public static void main(String[] args){
    Scanner scanner = new Scanner (System.in); 
    int N = scanner.nextInt();
    int [] A = new int[N];
    
    for (int i = 0; i<N; i++){
      A[i] = scanner.nextInt(); 
    }
    
    int B = scanner.nextInt();
    int C = scanner.nextInt();
    
    scanner.close();
    
    long totalsupervisors = 0;
    for (int i = 0; i<N; i++){
      totalsupervisors ++;
      int remaining = A[i] - B;
      
      if (remaining > 0){
        totalsupervisors += (remaining + C - 1)/C;
        
      }
    }
    System.out.print(totalsupervisors);
  }
}