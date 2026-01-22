import java.util.Scanner;

/**
 * Exercise 18.2: Compute greatest common divisor using recursion
 * 
 * The gcd(m, n) can be defined recursively as follows:
 * - If m % n is 0, gcd(m, n) is n
 * - Otherwise, gcd(m, n) is gcd(n, m % n)
 * 
 * This is the Euclidean algorithm.
 * 
 * Write a recursive method to find the GCD.
 * Prompt the user to enter two integers and display their GCD.
 * 
 * @author Christopher Markham
 */
public class exercise18_02 {
    public static int gcd(int m, int n) {
        if (m % n == 0) {
            return n;
        } else {
            return gcd(n, m % n);
        }
    }
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter first integer: ");
        int m = input.nextInt();
        
        System.out.print("Enter second integer: ");
        int n = input.nextInt();
        
        // Calculate GCD
        int result = gcd(m, n);
        
        // Display result
        System.out.println("The greatest common divisor of " + m + 
                           " and " + n + " is " + result);
        
        input.close();
    }
}