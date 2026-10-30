#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int main() {
    // global (shared) data
    int x=0;

    int rc = fork();
    if (rc == 0){
        // child process
        x += 1;
        printf("child process: x=%d\n",x);
    }else{
        // main process
        x += 1;
        printf("main process: x=%d\n",x);
    }
    return 0;
}
