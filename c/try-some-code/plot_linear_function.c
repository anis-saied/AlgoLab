/*
http://www.gnuplot.info/
https://en.wikipedia.org/wiki/Gnuplot

sudo apt-get update
sudo apt-get install gnuplot
gcc -o plot_linear_function plot_linear_function.c
./plot_linear_function
*/

#include <stdio.h>


int main(){
    FILE *gnuplotPipe = popen("gnuplot -persistent","w");
    
    if (gnuplotPipe == NULL){
        fprintf(stderr, "Error opening pipe to gnuplot.\n");
        return -1;
    }
    
    double a,b;
    
    // prompt user for input
    printf("Enter the value of 'a':");
    scanf("%lf",&a);
    
    printf("Enter the value of 'b':");
    scanf("%lf",&b);
    
    
    // Plottinng the linar function ax + b
    fprintf(gnuplotPipe,"set title 'Graph of %.2fx + %.2f'\n", a, b);
    fprintf(gnuplotPipe, "plot [x=-10:10]%f*x + %f\n", a, b);
    
    // close the gnuplot pipe
    fclose(gnuplotPipe);
    
    
    return 0;
}
