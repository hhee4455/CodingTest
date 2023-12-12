import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long A = sc.nextLong();
        long B = sc.nextLong();
        long C = sc.nextLong();
        
        if ((B + C) >= 60) {
            long totalMinutes = A * 60 + B + C;
            long hours = totalMinutes / 60;
            long minutes = totalMinutes % 60;

            if (hours >= 24) {
                hours %= 24;
            }

            System.out.println(hours + " " + minutes);
        } else {
            System.out.println(A + " " + (B + C));
        }
        sc.close();
    }
}