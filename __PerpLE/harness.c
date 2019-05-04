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
  int *z;
  int *w;
  volatile int *buf1;
  volatile int *buf2;
  long num_iterations;
} args;

// Must compile with -fopenmp
extern void P0(void * address);
extern void P1(void * address);
extern void P2(void * address);
extern void P3(void * address);


// Wrapper functions for the threads, to ensure synchronization
void* P0_wrap(void * address) {
  #pragma omp barrier
  P0(address);
}

void* P1_wrap(void * address) {
  #pragma omp barrier
  P1(address);
}

void* P2_wrap(void * address) {
  #pragma omp barrier
  P2(address);
}
void* P3_wrap(void * address) {
  #pragma omp barrier
  P3(address);
}


// Launch threads & time
int main(int argc,char *argv[]) {

    int i;
  
    if(argc < 3){
      	printf("Usage: ./harness [# threads] [# iterations] [mode]\n");
	printf("\t mode should be 0 for classic and 1 for perpetual test\n");
	return 1;
    }

    
    // Read in number of threads and iterations
    int thrs = atoi(argv[1]);
    int iters = atoi(argv[2]);
   
    // Initialize shared memory locations
    int i1 = 0;
    int i2 = 0;
    int i3 = 0;
    int i4 = 0;

    // Initialize structs
    args arg_t0;
    args arg_t1;
    args arg_t2;
    args arg_t3;


    arg_t0.x = &i1;
    arg_t0.y = &i2;
    arg_t0.z = &i3;
    arg_t0.w = &i4;    
    arg_t0.num_iterations = iters; 
    arg_t0.buf1 = (volatile int*) calloc(iters, sizeof(volatile int));
    arg_t0.buf2 = (volatile int*) calloc(iters, sizeof(volatile int));
        
    arg_t1.x = &i1;
    arg_t1.y = &i2;
    arg_t1.z = &i3;
    arg_t1.w = &i4;    
    arg_t1.num_iterations = iters; 
    arg_t1.buf1 = (thrs > 1) ? (volatile int*) calloc(iters, sizeof(volatile int)) : NULL;
    arg_t1.buf2 = (thrs > 1) ? (volatile int*) calloc(iters, sizeof(volatile int)) : NULL;

    arg_t2.x = &i1;
    arg_t2.y = &i2;
    arg_t2.z = &i3;
    arg_t2.w = &i4;    
    arg_t2.num_iterations = iters; 
    arg_t2.buf1 = (thrs > 2) ? (volatile int*) calloc(iters, sizeof(volatile int)) : NULL;
    arg_t2.buf2 = (thrs > 2) ? (volatile int*) calloc(iters, sizeof(volatile int)) : NULL;

    arg_t3.x = &i1;
    arg_t3.y = &i2;
    arg_t3.z = &i3;
    arg_t3.w = &i4;    
    arg_t3.num_iterations = iters; 
    arg_t3.buf1 = (thrs > 3) ? (volatile int*) calloc(iters, sizeof(volatile int)) : NULL;
    arg_t3.buf2 = (thrs > 3) ? (volatile int*) calloc(iters, sizeof(volatile int)) : NULL;
   
   
    // Run the threads in parallel
    omp_set_num_threads(thrs);
    #pragma omp parallel
    {
      if (omp_get_thread_num() == 0) P0_wrap((void*)&arg_t0);
      else if (omp_get_thread_num() == 1) P1_wrap((void*)&arg_t1);
      else if (omp_get_thread_num() == 2) P2_wrap((void*)&arg_t2);
      else if (omp_get_thread_num() == 3) P3_wrap((void*)&arg_t3);
    }
    
    // Print out buffers
    for(i = 0; i < iters; i++){
      printf("%d ", i);
      printf("\tT0: %d %d", arg_t0.buf1[i], arg_t0.buf2[i]);
      if (thrs > 1)  printf("\tT1: %d %d", arg_t1.buf1[i], arg_t1.buf2[i]);
      if (thrs > 2)  printf("\tT2: %d %d", arg_t2.buf1[i], arg_t2.buf2[i]);
      if (thrs > 3)  printf("\tT3: %d %d", arg_t3.buf1[i], arg_t3.buf2[i]);
      printf("\n");
    }
    
    return 0;
}
