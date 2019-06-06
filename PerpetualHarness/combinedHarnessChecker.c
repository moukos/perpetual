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
int n=0;
struct my_struct *item1 = NULL;
struct my_struct *item2 = NULL;

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
 //   printf("Global vars\nThread1\t x: %d, y: %d\nThread2\t x: %d, y: %d\n\n",*arg_t1.x,*arg_t1.y,*arg_t2.x,*arg_t2.y);

    omp_set_num_threads(2);
    #pragma omp parallel
    {
      if(omp_get_thread_num()==0) P1_wrap((void*)&arg_t1);
      else if (omp_get_thread_num() ==1) P2_wrap((void*)&arg_t2);
    }
    
    for( i = 0; i < n; i++){
 	add_kv1( i+1, arg_t1.buf[i]);
  	add_kv2( i+1, arg_t2.buf[i]);
      //printf("Iteration %d \t Th1: %d Th2: %d\n", i, arg_t1.buf[i], arg_t2.buf[i]);
      //fflush(stdout);
    }
    int SBinterleavingsCnt = 0;
    int LBinterleavingsCnt = 0;
    struct my_struct *t1, *t2, *t3;
    t1 = malloc(sizeof(struct my_struct));
    t2 = malloc(sizeof(struct my_struct));
    t3 = malloc(sizeof(struct my_struct));

    for( i = 0; i < n; i++){
	int temp = i + 1;
   	HASH_FIND_INT( item1, &temp, t1);
	int valueplus = t1->value + 1;
	int valueminus = t1->value - 1;
	if( valueplus > n ){
	  valueplus = n;
	}
	if( valueminus < 0 ){
	  valueminus = 0;
	}
	HASH_FIND_INT( item2, &valueplus, t2);
	//printf("%d %d \n", valueplus, t2->value);
	//HASH_FIND_INT( item2, &valueminus, t3);
	//printf("%d %d\n", valueminus, t3->value);
	
	// SB Check
	if ( t2->value == temp-1 ){
	  SBinterleavingsCnt += 1;
	  printf("1: key:%d value:%d, 2: key:%d value:%d\n",temp-1,t1->value,valueplus,t2->value);
	}

	// LB Check
	//if ( t3->value == temp+1 ){
	//  LBinterleavingsCnt += 1;
	//}
	//printf("1: key:%d value:%d, 2: key:%d value:%d\n",temp-1,t1->value,valueplus,t2->value);
    }

/*    for( i = 0; i < n; i++){
	struct my_struct *s;
	int temp = i + 1;
   	HASH_FIND_INT( item2, &temp, s);
	printf("Id %d, value %d\n",i+1,s->value);
    }
*/	
	printf("SB weak orderings %d \n",SBinterleavingsCnt);
   // printf("\nGlobal vars\nThread1\t x: %d, y: %d\nThread2\t x: %d, y: %d\n",*arg_t1.x,*arg_t1.y,*arg_t2.x,*arg_t2.y);
  
    //free((void *)arg_t1.buf);
    //free((void *)arg_t2.buf);
    
    return 0;
}

