#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>
#include <sched.h>

// Must compile with -lpthread
// Will generate warnings
extern void P1(int * address);
extern void P2(int * address);
int n=0;
extern int x=0,y=0;
/*
 * TODO: 1) force threads to run on different cores
 * 	 2) specify memory locations of Litmus tests a) as global variables ?
 * 	 	b) beginning of memory array ?, c) part of struct?, d) other?
 */
int main(int argc,char *argv[]) {

    int i=0;
    
    if(argc >= 2)
    {
	int input = atoi(argv[1]);
	n = input;
    	int *a = (int*) malloc((n+1)*sizeof(int));  
    	int *b = (int*) malloc((n+1)*sizeof(int));

	printf( "Hello world from thread %d of %d running on cpu %2d!\n", 
            omp_get_thread_num()+1, 
            omp_get_num_threads(),
            sched_getcpu());	

    	pthread_t thread1;
    	pthread_t thread2;
	printf("Global vars x: %d, y: %d\n",x,y);
    	pthread_create(&thread1, NULL, P1, a);
    	pthread_create(&thread2, NULL, P2, b);

    	pthread_join(thread1, NULL);
    	pthread_join(thread2, NULL);
    	for(i=0;i<n;i++){
		printf("a: %d, b: %d\n", a[i],b[i]);
    	}
	printf("Global vars x: %d, y: %d\n",x,y);
	free(a);
	free(b);
    }
    else
    {
	printf("Insufficient number of arguments. Specify # of iterations\n");
    }
    return 1;
}

