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

void* P1_wrap(void * address) {
  printf("launched P1_wrap\n");
  fflush(stdout);
  #pragma omp barrier
  P1(address);

}

void* P2_wrap(void * address) {
  printf("launched P2_wrap\n");
  fflush(stdout);
  #pragma omp barrier
  P2(address);
}


int main(int argc,char *argv[]) {

    int i=0;
   
    if(argc < 2){
      	printf("Insufficient number of arguments. Specify # of iterations\n");
	return 1;
    }

      
    int ptr1=0;
    int spacing1[10000];
    int ptr2=0;
    args arg_t1;
    args arg_t2;
    int input = atoi(argv[1]);
    n = input;
    arg_t1.x = &ptr1;
    arg_t1.y = &ptr2;
    arg_t1.num_iterations = input; 
    arg_t1.num_threads = 2;
    arg_t2.x = &ptr1;
    arg_t2.y = &ptr2;
    arg_t2.num_iterations = input; 
    arg_t2.num_threads = 2;

    arg_t1.buf = (volatile int*) calloc(n, sizeof(volatile int));
    void* spacing2 = malloc(40000);
    arg_t2.buf = (volatile int*) calloc(n, sizeof(volatile int));

    printf("Global vars\nThread1\t x: %d, y: %d\nThread2\t x: %d, y: %d\n\n",*arg_t1.x,*arg_t1.y,*arg_t2.x,*arg_t2.y);

    omp_set_num_threads(2);
    #pragma omp parallel
    {
      if(omp_get_thread_num()==0) P1_wrap((void*)&arg_t1);
      else if (omp_get_thread_num() ==1) P2_wrap((void*)&arg_t2);
    }
    
     
    for(i = 0; i < n; i++){
      printf("Iteration %d \t Th1: %d Th2: %d\n", i, arg_t1.buf[i], arg_t2.buf[i]);
      fflush(stdout);
    }
    printf("\nGlobal vars\nThread1\t x: %d, y: %d\nThread2\t x: %d, y: %d\n",*arg_t1.x,*arg_t1.y,*arg_t2.x,*arg_t2.y);
  
    //free((void *)arg_t1.buf);
    //free((void *)arg_t2.buf);
    
    return 0;
}

