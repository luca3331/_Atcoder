import java.util.*;

public class B{
  public static void main (String arg[]){
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int M = sc.nextInt();
    int [] A = new int [M];
    int[][] X = new int[N][M];  

    for (int i = 0;i < M;i++){
        A[i] = sc.nextInt();
    }
    for (int i = 0;i < N;i++){
        for (int j = 0;j < M;j++){
            if (i == 0){
                X[i][j] = sc.nextInt();
            }
            else{
                X[i][j] = sc.nextInt() + X[i-1][j];
            }
        }
    }
    System.out.println(ishealthy(A, X));
  }

  private static String ishealthy(int[] A, int[][] X){
    for (int i=0;i<A.length;i++){
        if (A[i] > X[X.length - 1][i]){
            return "No";
        }
    }
    return "Yes";
  }
}