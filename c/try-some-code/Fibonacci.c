#include <stdio.h>

// function to generate and print a Fibonacci sequence
void fibonacci(int n){
    unsigned long first = 0, second = 1, next;
    printf("Fibonacci sequence up to %d terms : \n",n);
    
    for(int i=0; i<n; i++){
        if(i<=1){
            next = i;
        } else {
            next = first + second;
            first = second;
            second = next;
        }
        printf("%lu ",next);
    }
    
    printf("\n");
    
}
int main(){
    int numTerms;
    
    // prompt user for input
    printf("Enter the number of terms for the Fibonacci sequence:");
    scanf("%d",&numTerms);
    
    // check if the input is positive
    if (numTerms <= 0){
        printf("Please enter a positive number of terms.\n");
    } else {
        // generate and print the fibonacci sequence
        fibonacci(numTerms);
    }
    
    
    return 0;
}
