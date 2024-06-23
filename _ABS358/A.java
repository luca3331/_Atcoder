import java.util.Scanner;

public class A{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] ST = sc.nextLine().split(" ");
        System.out.println(ST[0].equals("AtCoder") && ST[1].equals("Land") ? "Yes" : "No");
    }
}