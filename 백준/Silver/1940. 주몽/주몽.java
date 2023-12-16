import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] A = new int[N];

        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }

        Arrays.sort(A);

        int left = 0, right = N - 1;
        int cnt = 0;

        while (left < right) {
            int sum = A[left] + A[right];

            if (sum == M) {
                cnt++;
                left++;
                right--;
            } else if (sum < M) {
                left++;
            } else {
                right--;
            }
        }

        System.out.println(cnt);
    }
}