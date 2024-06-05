#include <stdio.h>
#include <pthread.h>

// mutex :spin & lock
int fetchAndAdd(int *ptr){
    int old = *ptr;
    *ptr = old + 1;
    return old;
}

typedef struct __lock_t
{
    int ticket;
    int turn;
}lock_t;

void lock_init(lock_t *lock){
    lock->ticket = 0;
    lock->turn   = 0;
}

void lock(lock_t *lock){
    int myturn = fetchAndAdd(&lock->ticket);
    while (lock->turn != myturn)
        ; // spin
    
}
void unlock(lock_t *lock){
    fetchAndAdd(&lock->turn);
}

// global
static volatile int counter = 0;
lock_t mutex;

void *mythread(void *arg){
    printf("%s: begin\n",(char *) arg);
    int  i;
    for(i=0; i <1e5; i++){
        lock(&mutex);
        counter += 1;
        unlock(&mutex);
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