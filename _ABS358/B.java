import java.util.Scanner;
import java.util.LinkedList;
import java.util.Queue;

public class B {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] NA = sc.nextLine().split(" ");
        int N = Integer.parseInt(NA[0]);
        int A = Integer.parseInt(NA[1]);
        String[] T = sc.nextLine().split(" ");
        int endTime = 0;
        for (String t : T){
            int time = Integer.parseInt(t);
            if (time < endTime){ //ならぶ
                System.out.println(endTime + A);
                endTime = endTime + A;
            }
            else{ //ならばない
                System.out.println(time + A);
                endTime = time + A;
            }
        }
        }
}
