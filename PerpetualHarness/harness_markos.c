#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>
#include <sched.h>
#include <time.h>

pthread_mutex_t join_mut = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cond = PTHREAD_COND_INITIALIZER;
pthread_barrier_t barrier;

typedef struct {
  int *x;
  int *y;
  volatile int *buf;
  int num_iterations;
  int num_threads;
} args;

inline static void mbar(void) {
  asm __volatile__ ("mfence" ::: "memory");
}

// Must compile with -lpthread and -fopenmp
extern void P1(void * address);
extern void P2(void * address);
int n=0;

void* P1_wrap(void * address) {
  //  pthread_mutex_lock(&join_mut);
  // pthread_cond_wait(&cond, &join_mut);
  //  pthread_mutex_unlock(&join_mut); 
  mbar();
  pthread_barrier_wait(&barrier);
  P1(address);
  mbar();
}

void* P2_wrap(void * address) {
  // pthread_mutex_lock(&join_mut);
  // pthread_cond_wait(&cond, &join_mut);
  // pthread_mutex_unlock(&join_mut);
  mbar();
  pthread_barrier_wait(&barrier);
  P2(address);
  mbar();
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

    //  printf( "Hello world from thread %d of %d running on cpu %2d!\n", 
    //      omp_get_thread_num()+1, 
    //      omp_get_num_threads(),
    //      sched_getcpu());	

    pthread_t thread1;
    pthread_t thread2;
    printf("Global vars\nThread1\t x: %d, y: %d\nThread2\t x: %d, y: %d\n\n",*arg_t1.x,*arg_t1.y,*arg_t2.x,*arg_t2.y);

    pthread_barrier_init(&barrier, NULL, 3);
    pthread_create(&thread2, NULL, P2_wrap, (void*)&arg_t2);
    pthread_create(&thread1, NULL, P1_wrap, (void*)&arg_t1);
    //  sleep(1);
    //  pthread_cond_broadcast(&cond);
    pthread_barrier_wait(&barrier);
    pthread_join(thread2, NULL);
    pthread_join(thread1, NULL);
    pthread_barrier_destroy(&barrier);
    
    for(i = 0; i < n; i++){
      printf("Iteration %d \t Th1: %d Th2: %d\n", i, arg_t1.buf[i], arg_t2.buf[i]);
      fflush(stdout);
    }
    printf("\nGlobal vars\nThread1\t x: %d, y: %d\nThread2\t x: %d, y: %d\n",*arg_t1.x,*arg_t1.y,*arg_t2.x,*arg_t2.y);
  
    //    free((void *)arg_t1.buf);
    //    free((void *)arg_t2.buf);
    
    return 0;
}

