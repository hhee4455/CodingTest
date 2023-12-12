import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int M = scanner.nextInt();
        int[] numbers = new int[N];
        for (int i = 0; i < N; i++) {
            numbers[i] = scanner.nextInt();
        }
        int[] prefixSum = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            prefixSum[i] = prefixSum[i - 1] + numbers[i - 1];
        }
        for (int k = 0; k < M; k++) {
            int i = scanner.nextInt();
            int j = scanner.nextInt();
            int result = prefixSum[j] - prefixSum[i - 1];
            System.out.println(result);
        }
    }
}