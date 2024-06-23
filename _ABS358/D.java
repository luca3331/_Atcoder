import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class D {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] NM = sc.nextLine().split(" ");
        int N = Integer.parseInt(NM[0]);
        int M = Integer.parseInt(NM[1]);
        int[] AA = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] BB = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int result = 0;
        Arrays.sort(AA);
        Arrays.sort(BB);
        
        Queue<Integer> A = new LinkedList<>();
        for (int num : AA) {
            A.offer(num);
        }
        Queue<Integer> B = new LinkedList<>();
        for (int num : BB) {
            B.offer(num);
        }
        while (!B.isEmpty()){
            int b = B.poll();
            while(!A.isEmpty()){
                int a = A.poll();
                if (b <= a){
                    result += a;
                    break;
                }
            }
            if (A.isEmpty() && !B.isEmpty()){
                break;
            }
        }
        if (!B.isEmpty()){
            System.out.println("-1");
        }
        else{
            System.out.println(result);
        }


    }
}
