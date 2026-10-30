#include <stdio.h>
#include <pthread.h>

// mutex :spin & lock
int testAndSet(int *ptr, int new){
    int old = *ptr;
    *ptr = new;
    return old;
}

typedef struct __lock_t
{
    int flag;
}lock_t;

void init(lock_t *lock){
    // 0 indicates that the lock is available, 1 tha t is held
    lock->flag= 0;
}

void lock(lock_t *lock){
    while(testAndSet(&lock->flag,1)==1)
        ; //spin-wait (do nothing)
}
void unlock(lock_t *lock){
    lock->flag = 0;
}

// global
static volatile int counter = 0;
lock_t mutex;

void *mythread(void *arg){
    printf("%s: begin\n",(char *) arg);
    int  i;
    for(i=0; i <1e7; i++){
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