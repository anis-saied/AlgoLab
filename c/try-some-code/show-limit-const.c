#include <stdio.h>
#include <limits.h>

#ifdef PATH_MAX
static long pathmax = PATH_MAX;
#else
statis long pathmax = 0;
#endif

int 
main(int argc, char *argv[]){
	printf("pathmax = %ld\n",pathmax);
	return 0;
}
