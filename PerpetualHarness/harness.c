#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>
#include <sched.h>

typedef struct {
  int *x;
  int *y;
  volatile int *buf;
  int num_iterations;
  int num_threads;
} args;


// Must compile with -lpthread and -fopenmp
// Will generate warnings
extern void P1(args * address);
extern void P2(args * address);
int n=0;
//extern int x=0,y=0;
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
	int ptr1=0;
	int ptr2=0;
	args arg_t1;
	args arg_t2;
	int input = atoi(argv[1]);
	n = input;
//	args arg_t1; 
//	args arg_t2;
	arg_t1.x = &ptr1;
	arg_t1.y = &ptr2;
	arg_t1.num_iterations = input; 
	arg_t1.num_threads = 2;
	arg_t2.x = &ptr1;
	arg_t2.y = &ptr2;
	arg_t2.num_iterations = input; 
	arg_t2.num_threads = 2;

	//arg_t.num_iterations = input;
    //	int *a = (int*) malloc((n+1)*sizeof(int));  
	arg_t1.buf = (volatile int*) malloc((n+1)*sizeof(volatile int));
	arg_t2.buf = (volatile int*) malloc((n+1)*sizeof(volatile int));
    //	int *b = (int*) malloc((n+1)*sizeof(int));

	printf( "Hello world from thread %d of %d running on cpu %2d!\n", 
            omp_get_thread_num()+1, 
            omp_get_num_threads(),
            sched_getcpu());	

    	pthread_t thread1;
    	pthread_t thread2;
	printf("Global vars x: %d, y: %d, x:%d, y: %d ptr1 %d ptr2\n",arg_t1.x,arg_t1.y,arg_t2.x,arg_t2.y,ptr1,ptr2);
    	pthread_create(&thread1, NULL, &P1, &arg_t1);
    	pthread_create(&thread2, NULL, &P2, &arg_t2);
    	pthread_join(thread1, NULL);
    	pthread_join(thread2, NULL);
   	for(i=0;i<n;i++){
		printf("a: %d b: %d\n", arg_t1.buf[i], arg_t2.buf[i]);
		fflush(stdout);
   	}
	printf("Global vars x: %d, y: %d, ptr1:%d, ptr2 %d\n",arg_t1.buf[0],arg_t2.buf[0],arg_t2.x,arg_t2.y);

//	free(arg_t.buf);
//	free(b);
    }
    else
    {
	printf("Insufficient number of arguments. Specify # of iterations\n");
    }
    return 1;
}

