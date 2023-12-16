import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] A = new int[N];
        int cnt = 0;

        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }
        Arrays.sort(A);

        for (int k = 0; k < N; k++) {
            int find = A[k];
            int left = 0;
            int right = N - 1;

            while (left < right) {
                if (A[left] + A[right] == find){
                    if(left != k && right != k){
                        cnt++;
                        break;
                    } else if(left == k){
                        left++;
                    } else if(right == k){
                        right--;
                    }
                } else if (A[left] + A[right] < find) {
                    left++;
                } else {
                    right--;
                }
            }
        }
            System.out.println(cnt);

    }

}