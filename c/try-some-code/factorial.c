#include <stdio.h>

// function to calculate factorial
int factorial(int n){
    if(n==0 || n==1){
        return 1;
    } else {
        return n * factorial(n-1);
    }
}


int main(){
    int num;
    
    // prompt user for input
    printf("Enter a non-negative integer:");
    scanf("%d",&num);
    
    // check if input is a non-negative
    if (num < 0){
        printf("Please enter a non-negative number.\n");
    } else{
        // calculate and print the factorial
        printf("Factorial of %d is = %d\n", num, factorial(num));
    }
    
    return 0;
}


