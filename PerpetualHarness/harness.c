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

typedef struct {
  int *x;
  int *y;
  int *buf;
  int num_iterations;
  int num_threads;
} args;
/*
 * TODO: 1) force threads to run on different cores
 * 	 2) specify memory locations of Litmus tests a) as global variables ?
 * 	 	b) beginning of memory array ?, c) part of struct?, d) other?
 */

/* Thread launch and join */

/*
void launch(pthread_t *th, f_t *f, void *a) {
  int e = pthread_create(th,NULL,f,a);
  if (e) errexit("phread_create",e);
}

void *join(pthread_t *th) {
  void *r ;
  int e = pthread_join(*th,&r) ;
  if (e)  errexit("pthread_join",e);
  return r ;
}
*/

int main(int argc,char *argv[]) {

    int i=0;
   
    if(argc >= 2)
    {
	int input = atoi(argv[1]);
	n = input;
	args arg_t;
	arg_t.x = 0;
	arg_t.y = 0;
	arg_t.num_iterations = input; 
	arg_t.num_threads = 2;
	//arg_t.num_iterations = input;
    //	int *a = (int*) malloc((n+1)*sizeof(int));  
	arg_t.buf = (int*) malloc((n+1)*sizeof(int));
    //	int *b = (int*) malloc((n+1)*sizeof(int));

	printf( "Hello world from thread %d of %d running on cpu %2d!\n", 
            omp_get_thread_num()+1, 
            omp_get_num_threads(),
            sched_getcpu());	

    	pthread_t thread1;
    	pthread_t thread2;
	printf("Global vars x: %d, y: %d, buf[3]:%d\n",arg_t.x,arg_t.y,arg_t.buf[3]);
    	pthread_create(&thread2, NULL, P2, &arg_t);
    	pthread_create(&thread1, NULL, P1, &arg_t);
    	pthread_join(thread1, NULL);
    	pthread_join(thread2, NULL);
    	for(i=0;i<n;i++){
		printf("a: %d \n", arg_t.buf[i]);
    	}
	printf("Global vars x: %d, y: %d, buf[3]:%d, iterations %d\n",arg_t.x,arg_t.y,arg_t.buf[3],arg_t.num_iterations);
//	free(arg_t.buf);
//	free(b);
    }
    else
    {
	printf("Insufficient number of arguments. Specify # of iterations\n");
    }
    return 1;
}

