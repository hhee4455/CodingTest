import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long H = sc.nextInt();
        long M = sc.nextInt();
        long A = (M - 45);
        if(M >= 45) {
            System.out.println(H + " " + A);
        }
        else if(M < 45) {
            if(H == 0){
                H = 23;
                System.out.println(H + " " + (15 + M));
            }
            else {
                H = H - 1;
                System.out.println(H + " " + (15 + M));
            }
        }
    }
}
