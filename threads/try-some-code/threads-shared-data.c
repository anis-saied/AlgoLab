#include <stdio.h>
#include <pthread.h>

static volatile int counter = 0;

void *mythread(void *arg){
    printf("%s: begin\n",(char *) arg);
    int  i;
    for(i=0; i <1e7; i++){
        counter += 1;
    }
    printf("%s: done\n",(char *) arg);
    return NULL;
}

int
main(int argc, char *argv[]){
    pthread_t p1, p2;
    int rc;
    printf("main: begin (counter = %d)\n",counter);
    // create 2 threads
    rc = pthread_create(&p1, NULL, mythread, "A"); 
    rc = pthread_create(&p2, NULL, mythread, "B"); 

    // join : waits for the treads to finish
    rc = pthread_join(p1, NULL); 
    rc = pthread_join(p2, NULL); 
    
    printf("main: done with (counter = %d)\n",counter);
    return 0;
}