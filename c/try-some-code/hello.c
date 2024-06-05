#include <stdio.h>

int main() {
    // Declare variables to store user input
    double num1, num2;

    // Prompt user for input
    printf("Enter the first number: ");
    scanf("%lf", &num1);

    printf("Enter the second number: ");
    scanf("%lf", &num2);

    // Calculate and print the sum
    double sum = num1 + num2;
    printf("The sum is: %.2lf\n", sum);

    return 0;
}

