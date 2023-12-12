import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] M = new int[N];

        for (int i = 0; i < N; i++) {
            M[i] = sc.nextInt();
        }

        int maxV = M[0];
        int minV = M[0];

        for (int i = 1; i < N; i++) {
            if (M[i] > maxV) {
                maxV = M[i];
            }

            if (M[i] < minV) {
                minV = M[i];
            }
        }
        System.out.println(minV + " " + maxV);

        sc.close();
    }
}
