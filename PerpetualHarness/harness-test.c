#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>
#include <sched.h>

typedef struct {
  //int num_threads;
  int *x;
  int *y;
  int *buf;
  int num_iterations;
} args;

// Must compile with -lpthread
// Will generate warnings
void P1(args *str){
  int i=0;
  str->x = 42;
  for(i=0; i<str->num_iterations; i++){
    str->buf[i]=10;
  }
}

void P2(args *str){
  str->y = 16;
}

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

	args arg_t;
	arg_t.x = 0;
	arg_t.y = 0;
	//arg_t.num_iterations = input;
    //	int *a = (int*) malloc((n+1)*sizeof(int));  
	arg_t.buf = (int*) malloc(10*sizeof(int));

    	pthread_t thread1;
    	pthread_t thread2;
    	pthread_create(&thread1, NULL, P1, &arg_t);
    	pthread_create(&thread2, NULL, P2, &arg_t);

    	pthread_join(thread1, NULL);
    	pthread_join(thread2, NULL);
	printf("Global vars x: %d, y: %d buf[2]%d\n",arg_t.x,arg_t.y,arg_t.buf[2]);
	free(arg_t.buf);
    return 0;
}

