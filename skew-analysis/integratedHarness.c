#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>
#include <sched.h>
#include <time.h>
#include "checker.c"
#include "checker-heuristic.c"

typedef struct {
  long *x;
  long *y;
  long *z;
  volatile long *buf;
  long num_iterations;
  int num_threads;
} args;

// Must compile with -lpthread and -fopenmp
extern void P1(void * address);
extern void P2(void * address);
extern void P3(void * address);
extern void P0(void * address);
struct my_struct *item1 = NULL;
struct my_struct *item2 = NULL;
struct my_struct *item3 = NULL;
struct my_struct *item0 = NULL;

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

void* P0_wrap(void * address) {
//  printf("launched P4_wrap\n");
  fflush(stdout);
  #pragma omp barrier
  P0(address);
}
int main(int argc,char *argv[]) {
    // Setup
    //

    long i=0;
    int numReads[4];
   
    if(argc < 2){
      	printf("Insufficient number of arguments. Specify # of iterations\n");
	return 1;
    }
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    fp = fopen("./num_reads.perple", "r");
    if (fp==NULL)
	exit(EXIT_FAILURE);
    for( i=0; i<4; i++ ) {
	read = getline(&line, &len, fp);
 	numReads[i] = atoi(line);
    }
    if (line)
	free(line);

    // Populate structs
    long ptr1=0;
    int spacing1[10000];
    long ptr2=0;
    int spacing6[10000];
    long ptr3=0;
    int spacing5[10000];
    long ptr0=0;

    args arg_t0;
    args arg_t1;
    args arg_t2;
    args arg_t3;
    long n = atoi(argv[1]);

    arg_t0.x = arg_t1.x = arg_t2.x = arg_t3.x = &ptr1;
    arg_t0.y = arg_t1.y = arg_t2.y = arg_t3.y = &ptr2;
    arg_t0.z = arg_t1.z = arg_t2.z = arg_t3.z = &ptr3;
    arg_t0.num_iterations = arg_t1.num_iterations = arg_t2.num_iterations = arg_t3.num_iterations = n;
    arg_t0.num_threads = arg_t1.num_threads = arg_t2.num_threads = arg_t3.num_threads = 4;

    
    arg_t0.buf = (volatile long*) calloc((numReads[0]?numReads[0]:1)*n, sizeof(volatile long));
    void* spacing2 = malloc(40000);
    arg_t1.buf = (volatile long*) calloc((numReads[1]?numReads[1]:1)*n, sizeof(volatile long));
    void* spacing3 = malloc(40000);
    arg_t2.buf = (volatile long*) calloc((numReads[2]?numReads[2]:1)*n, sizeof(volatile long));
    void* spacing4 = malloc(40000);
    arg_t3.buf = (volatile long*) calloc((numReads[3]?numReads[3]:1)*n, sizeof(volatile long));

    // Harness
    struct timespec start, end;
    clock_gettime(CLOCK_MONOTONIC_RAW, &start);

    omp_set_num_threads(4);
    #pragma omp parallel
    {
      if(omp_get_thread_num()==0) P0_wrap((void*)&arg_t0);
      else if (omp_get_thread_num() ==1) P1_wrap((void*)&arg_t1);
      else if (omp_get_thread_num() ==2) P2_wrap((void*)&arg_t2);
      else if (omp_get_thread_num() ==3) P3_wrap((void*)&arg_t3); 
    }
    for( i=0; i<n; i++){
   	printf("%ld\n",arg_t0.buf[i]-(i+1));	
	fflush(stdout);
    }
/*
    clock_gettime(CLOCK_MONOTONIC_RAW, &end);
    double time_h = (double) end.tv_sec + (double) end.tv_nsec / 1000000000.0 - (double)start.tv_sec - (double) start.tv_nsec / 1000000000.0;
    //printf("Harness time %.9f \n",  time_h);

    long interleavingsCnt = 0;
    long interleavingsCnt2 = 0;
    long oldCnt = 0;
    
    double time_n = 0;
    // Checker - Base
    if( n <= 100000 ){
    	clock_gettime(CLOCK_MONOTONIC_RAW, &start);
    	interleavingsCnt = condition(arg_t0.buf,arg_t1.buf,arg_t2.buf,arg_t3.buf,n);
    	clock_gettime(CLOCK_MONOTONIC_RAW, &end);
    	time_n = (double) end.tv_sec + (double) end.tv_nsec / 1000000000.0 - (double)start.tv_sec - (double) start.tv_nsec / 1000000000.0;
    	fprintf(stderr,"Outcome (0,0) %ld Outcome (0,1) %ld Outcome (1,0) %ld Outcome 4 (1,1) %ld\n",arg_t3.buf[0], arg_t3.buf[1], arg_t3.buf[2], arg_t3.buf[3]);
    }
    clock_gettime(CLOCK_MONOTONIC_RAW, &start);
    interleavingsCnt2 = condition2(arg_t0.buf,arg_t1.buf,arg_t2.buf,arg_t3.buf,n);
    clock_gettime(CLOCK_MONOTONIC_RAW, &end);
    double time_n2 = (double) end.tv_sec + (double) end.tv_nsec / 1000000000.0 - (double)start.tv_sec - (double) start.tv_nsec / 1000000000.0;
    // printf("NEW2 checker time: %.9f, weak %d\n", time_n2, interleavingsCnt2);

    
    clock_gettime(CLOCK_MONOTONIC_RAW, &start);
     for(i = 0; i < n; i++) if(arg_t1.buf[arg_t0.buf[i]] < i + 1) {
	oldCnt++;
	//	printf("T0 read %d at iter %d, T1 read %d at iter %d\n", arg_t0.buf[i], i, arg_t1.buf[arg_t0.buf[i]], arg_t0.buf[i]);
	}
    clock_gettime(CLOCK_MONOTONIC_RAW, &end);
    double time_o = (double) end.tv_sec + (double) end.tv_nsec / 1000000000.0 - (double)start.tv_sec - (double) start.tv_nsec / 1000000000.0;
    //printf("OLD checker time: %.9f, weak %d\n", time_o, oldCnt);
    printf("%d %d %d %.9f %.9f %.9f\n", n,  interleavingsCnt, interleavingsCnt2, time_h, time_n, time_n2);
    fprintf(stderr, "%d %d %d %.9f %.9f %.9f\n", n,  interleavingsCnt, interleavingsCnt2, time_h, time_n, time_n2);
  */
     //printf("(Base) SB weak orderings %d \n",SBinterleavingsCnt);
    //printf("(Base) Checker time spent %f \n",  time_base);
    
//    SBinterleavingsCnt = 0;
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

