import java.util.*;

public class A{
  public static void main (String arg[]){
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int l = sc.nextInt();
    int r = sc.nextInt();
    int i = 0;
    List <Integer> out = new ArrayList<>();
    for (i = 0;i < l - 1;i++){
      out.add(i + 1);
    }
    for (i = r - 1;i >= l - 1;i--){
      out.add(i + 1);
    }
    for (i = r;i < n;i++){
      out.add(i + 1);
    }
    printWithSpace(out);
    
  }

  public static void printWithSpace(List out){
    for (int i=0;i<out.size();i++){
      System.out.printf("%d ", out.get(i));
    }
  } 
}