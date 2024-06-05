#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> // useful for get process id
#include <sys/wait.h> // useful for wait()

int main(){
  printf("hello (pid:%d)\n",(int)getpid());
  int rc = fork();
  if (rc < 0){ // fork failed; exit
    fprintf(stderr, "fork failed\n");
    exit(1);
  } else if (rc == 0){ // child (new process)
    printf("hello i am child (pid: %d)\n", (int)getpid());
  } else { // parent goes down this path (main)
    int wc = wait(NULL); 
    printf("hello, i am parent of %d (wc: %d) (pid: %d)\n", rc, wc, (int)getpid());
  }
  return 0;
}
