package numbers;

import java.util.Scanner;

/**
 * Solves the quadratic equation a x² + b x + c = 0.
 */
public class Quadratic {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        // Input and validate coefficients a, b, and c
        System.out.println("Enter the values for a, b, and c:");

        double a = 0, b = 0, c = 0;

        // Loop for getting valid inputs
        for (int i = 0; i < 3; i++) {
            if (!in.hasNextDouble()) {
                System.err.println("Invalid input. Please enter a valid number.");
                System.err.println("Program exiting!");
                in.close();
                return;
            }
            switch (i) {
                case 0:
                    a = in.nextDouble();
                    if (a == 0) {
                        System.err.println("Cannot solve the equation when a = 0.");
                        in.close();
                        return;
                    }
                    break;
                case 1:
                    b = in.nextDouble();
                    break;
                case 2:
                    c = in.nextDouble();
                    break;
            }
        }

        // Print the quadratic equation in standard form
        System.out.printf("%.2f x² + %.2f x + %.2f = 0\n", a, b, c);

        // Calculate the discriminant (delta)
        double delta = b * b - 4 * a * c;

        // Handle different cases based on delta value
        if (delta < 0) {
            System.out.println("No real solutions exist (Delta < 0).");
        } else if (delta == 0) {
            double x = -b / (2 * a); // Only one solution
            System.out.printf("One real solution: x = %.3f\n", x);
        } else {
            // Two real solutions
            double sqr = Math.sqrt(delta);
            double x1 = (-b + sqr) / (2 * a);
            double x2 = (-b - sqr) / (2 * a);
            System.out.printf("Two real solutions: x1 = %.3f, x2 = %.3f\n", x1, x2);
        }

        // Close the scanner
        in.close();
    }
}
