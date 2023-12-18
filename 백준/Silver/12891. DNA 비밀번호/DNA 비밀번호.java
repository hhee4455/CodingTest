import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        String inputString = sc.next();
        char[] charArray = inputString.toCharArray();

        char[] resultArray = new char[N];
        for (int i = 0; i < N; i++) {
            resultArray[i] = charArray[i];
        }

        int[] minOccurrences = new int[4];
        minOccurrences[0] = sc.nextInt(); 
        minOccurrences[1] = sc.nextInt(); 
        minOccurrences[2] = sc.nextInt(); 
        minOccurrences[3] = sc.nextInt(); 

        int passwordCount = countPossiblePasswords(resultArray, M, minOccurrences);

        System.out.println(passwordCount);
    }

    private static int countPossiblePasswords(char[] resultArray, int M, int[] minOccurrences) {
        int[] occurrences = new int[4];
        int passwordCount = 0;

        for (int i = 0; i < M; i++) {
            char ch = resultArray[i];
            occurrences[getIndex(ch)]++;
        }

        if (checkOccurrences(occurrences, minOccurrences)) {
            passwordCount++;
        }

        for (int i = M; i < resultArray.length; i++) {
            char outChar = resultArray[i - M];
            char inChar = resultArray[i];

            occurrences[getIndex(outChar)]--;
            occurrences[getIndex(inChar)]++;

            if (checkOccurrences(occurrences, minOccurrences)) {
                passwordCount++;
            }
        }

        return passwordCount;
    }

    private static int getIndex(char ch) {
        switch (ch) {
            case 'A':
                return 0;
            case 'C':
                return 1;
            case 'G':
                return 2;
            case 'T':
                return 3;
            default:
                return -1;
        }
    }

    private static boolean checkOccurrences(int[] occurrences, int[] minOccurrences) {
        for (int i = 0; i < 4; i++) {
            if (occurrences[i] < minOccurrences[i]) {
                return false;
            }
        }
        return true;
    }
}