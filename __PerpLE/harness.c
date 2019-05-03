#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>
#include <sched.h>
#include <time.h>
#include "omp.h"


typedef struct {
  int *x;
  int *y;
  volatile int *buf;
  int num_iterations;
  int num_threads;
} args;

// Must compile with -lpthread and -fopenmp
extern void P1(void * address);
extern void P2(void * address);
int n=0;


// Wrapper functions for the two threads, to ensure synchronization
void* P1_wrap(void * address) {
  #pragma omp barrier
  P1(address);
}

void* P2_wrap(void * address) {
  #pragma omp barrier
  P2(address);
}


int main(int argc,char *argv[]) {

    int i=0;
   
    if(argc < 2){
      	printf("Usage: ./harness [number of iterations]");
	return 1;
    }

    // Read in number of iterations
    int input = atoi(argv[1]);
    n = input;

    // Initialize shared x and y, with spacing in between to place in different cache lines
    int ptr1=0;
    int spacing1[10000];
    int ptr2=0;

    // Initialize structs
    args arg_t1;
    arg_t1.x = &ptr1;
    arg_t1.y = &ptr2;
    arg_t1.num_iterations = n; 
    arg_t1.num_threads = 2;

    args arg_t2;
    arg_t2.x = &ptr1;
    arg_t2.y = &ptr2;
    arg_t2.num_iterations = n; 
    arg_t2.num_threads = 2;

    // Initialize thread-local buffers to store read values,
    // with spacing in between to place in different cache lines
    arg_t1.buf = (volatile int*) calloc(n, sizeof(volatile int));
    void* spacing2 = malloc(40000);
    arg_t2.buf = (volatile int*) calloc(n, sizeof(volatile int));

 
    // Run the two threads in parallel
    omp_set_num_threads(2);
    #pragma omp parallel
    {
      if(omp_get_thread_num()==0) P1_wrap((void*)&arg_t1);
      else if (omp_get_thread_num() ==1) P2_wrap((void*)&arg_t2);
    }
    
    // Print out buffers
    for(i = 0; i < n; i++){
      printf("%d: \t T1: %d T2: %d\n", i, arg_t1.buf[i], arg_t2.buf[i]);
      fflush(stdout);
    }
    
    return 0;
}

