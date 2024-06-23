import java.util.Scanner;

public class C {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] NM = sc.nextLine().split(" ");
        int N = Integer.parseInt(NM[0]);
        int M = Integer.parseInt(NM[1]);
        int[] SS = new int[N];
        int elemMin = N;
        for(int i = 0;i < N;i++){
            SS[i] = convert2bit(sc.nextLine());
        }

        for(int i = 1;i < (int) Math.pow(2, N);i++){
            String binChars = Integer.toBinaryString(i);
            binChars = String.format("%" + N + "s", binChars).replace(' ', '0');
            int seeValidDigit = 0;
            int elemCt = 0;
            for(int j = 0;j < binChars.length();j++){
                if (binChars.charAt(j) == '1'){
                    elemCt += 1;
                    seeValidDigit |= SS[j];
                }
            }
            if (seeValidDigit == (int) Math.pow(2, M) - 1 && elemMin > elemCt){
                elemMin = elemCt;
            }
        }
        System.out.println(elemMin);
    }

    public static int convert2bit(String line){
        int bitSequence = 0;
        for (int j = 0; j < line.length(); j++) {
            if (line.charAt(j) == 'o') {
                bitSequence |= (1 << (line.length() - 1 - j));
            }
        }
        return bitSequence;
    }
}
