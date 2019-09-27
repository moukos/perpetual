#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>
#include <sched.h>
#include <time.h>
#include "uthash.h"

struct my_struct{
  int id;
  int value;
  UT_hash_handle hh;
};

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
extern void P3(void * address);
extern void P4(void * address);
int n=0;
struct my_struct *item1 = NULL;
struct my_struct *item2 = NULL;
struct my_struct *item3 = NULL;
struct my_struct *item4 = NULL;

void* P1_wrap(void * address) {
//  printf("launched P1_wrap\n");
  fflush(stdout);
  #pragma omp barrier
  P1(address);

}

void* P2_wrap(void * address) {
//  printf("launched P2_wrap\n");
  fflush(stdout);
  #pragma omp barrier
  P2(address);
}

void* P3_wrap(void * address) {
//  printf("launched P3_wrap\n");
  fflush(stdout);
  #pragma omp barrier
  P3(address);
}

void* P4_wrap(void * address) {
//  printf("launched P4_wrap\n");
  fflush(stdout);
  #pragma omp barrier
  P4(address);
}

void add_kv1( int key, int value) {
	struct my_struct *s;
	
	s = malloc(sizeof(struct my_struct));
	s->id = key;
	s->value = value;
	HASH_ADD_INT( item1, id, s);
}

void add_kv2( int key, int value) {
	struct my_struct *s;
	
	s = malloc(sizeof(struct my_struct));
	s->id = key;
	s->value = value;
	HASH_ADD_INT( item2, id, s);
}

void add_kv3( int key, int value) {
	struct my_struct *s;
	
	s = malloc(sizeof(struct my_struct));
	s->id = key;
	s->value = value;
	HASH_ADD_INT( item3, id, s);
}

void add_kv4( int key, int value) {
	struct my_struct *s;
	
	s = malloc(sizeof(struct my_struct));
	s->id = key;
	s->value = value;
	HASH_ADD_INT( item4, id, s);
}

int main(int argc,char *argv[]) {
    // Setup
    int i=0;

    if(argc < 2){
      	printf("Insufficient number of arguments. Specify # of iterations\n");
	return 1;
    }
    int ptr1=0;
    int spacing1[10000];
    int ptr2=0;
    int spacing2[10000];
    int ptr3=0;
    int spacing3[10000];
    int ptr4=0;
    args arg_t1;
    args arg_t2;
    args arg_t3;
    args arg_t4;
    int input = atoi(argv[1]);
    n = input;
    arg_t1.x = &ptr1;
    arg_t1.y = &ptr2;
    arg_t1.num_iterations = input; 
    arg_t1.num_threads = 4;
    arg_t2.x = &ptr1;
    arg_t2.y = &ptr2;
    arg_t2.num_iterations = input;
    arg_t2.num_threads = 4;
    arg_t3.x = arg_t2.x;
    arg_t3.y = arg_t2.y;
    arg_t3.num_iterations = input;
    arg_t3.num_threads = 4;
    arg_t4.x = arg_t2.x;
    arg_t4.y = arg_t2.y;
    arg_t4.num_iterations = input;
    arg_t4.num_threads = 4;

    arg_t1.buf = (volatile int*) calloc(n, sizeof(volatile int));
    void* spacing2 = malloc(40000);
    arg_t2.buf = (volatile int*) calloc(n, sizeof(volatile int));
    void* spacing3 = malloc(40000);
    arg_t3.buf = (volatile int*) calloc(n, sizeof(volatile int));
    void* spacing4 = malloc(40000);
    arg_t4.buf = (volatile int*) calloc(n, sizeof(volatile int));

    // Harness
    clock_t begin_harness = clock();

    omp_set_num_threads(4);
    #pragma omp parallel
    {
      if(omp_get_thread_num()==0) P1_wrap((void*)&arg_t1);
      else if (omp_get_thread_num() ==1) P2_wrap((void*)&arg_t2);
      else if (omp_get_thread_num() ==2) P3_wrap((void*)&arg_t3);
      else if (omp_get_thread_num() ==3) P4_wrap((void*)&arg_t4); 
    }

    clock_t end_harness = clock();
    double time_harness = (double) (end_harness - begin_harness) / CLOCKS_PER_SEC;
    //printf("Harness time spent %f \n",  time_harness);

    
    int SBinterleavingsCnt = 0;

    // Checker - Base
    clock_t begin_base = clock();

    for(i = 0; i < n; i++) 
      if(arg_t2.buf[arg_t1.buf[i]] < i + 1) SBinterleavingsCnt++;

    clock_t end_base = clock();
    double time_base = (double) (end_base - begin_base) / CLOCKS_PER_SEC;
    //printf("(Base) SB weak orderings %d \n",SBinterleavingsCnt);
    //printf("(Base) Checker time spent %f \n",  time_base);
    printf("%d %d %f %f\n", n, SBinterleavingsCnt, time_harness, time_base);
    
    SBinterleavingsCnt = 0;
    //Checker - Multithreaded
    /*    clock_t begin_multi = clock();

    int max_threads = omp_get_max_threads();
    int block_size = n / max_threads;
    int* counts = (int*) calloc(max_threads, sizeof(int));

    omp_set_num_threads(max_threads);    
    #pragma omp parallel
    // for(i = 0; i < n; i++) 
    // if(arg_t2.buf[arg_t1.buf[i]] < i + 1) SBinterleavingsCnt++;
    {
      int thread_num = omp_get_thread_num();
      int j = thread_num * block_size;
      int max = j + block_size;
      int count = 0;
      
      for(; j < max; j++) 
	if(arg_t2.buf[arg_t1.buf[j]] < j + 1) count++;

      counts[thread_num] = count;
    }

    for (i = 0; i < max_threads; i++) SBinterleavingsCnt += counts[i];
    
    clock_t end_multi = clock();
    double time_multi = (double) (end_multi - begin_multi) / CLOCKS_PER_SEC;
    printf("(Multi) SB weak orderings %d \n",SBinterleavingsCnt);
    printf("(Multi) Checker time spent %f \n",  time_multi);


    
    SBinterleavingsCnt = 0;*/
    // Checker - Hash table
    /*    clock_t begin_hash = clock();
    
    for( i = 0; i < n; i++){
 	add_kv1( i+1, arg_t1.buf[i]);
  	add_kv2( i+1, arg_t2.buf[i]);
    }
    struct my_struct *t1, *t2;
    t1 = malloc(sizeof(struct my_struct));
    t2 = malloc(sizeof(struct my_struct));
 
    for( i = 1; i <= n; i++){
      
   	HASH_FIND_INT( item1, &i, t1);
	int valueplus = t1->value + 1;	
	if(valueplus > n) valueplus = n;	
	HASH_FIND_INT( item2, &valueplus, t2);
	
	// SB Check
	if ( t2->value < i ){
	  SBinterleavingsCnt++;
	  //  printf("1: key:%d value:%d, 2: key:%d value:%d\n",i,t1->value,valueplus,t2->value);
	}
    }

    clock_t end_hash = clock();
    double time_hash = (double) (end_hash - begin_hash) / CLOCKS_PER_SEC;
    printf("(Hash) SB weak orderings %d \n",SBinterleavingsCnt);
    printf("(Hash) Checker time spent %f \n",  time_hash);
    */
    return 0;
}

