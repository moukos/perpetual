#include <stdio.h>
#include <pthread.h>

struct MemoryLocs {
        int x;
        int y;
};

void thread1func (struct MemoryLocs* mem) {
  int* x = (int *) mem;
  int* y = ((int *) mem) + 1;

  asm volatile("mov $1, %0\n\t"
                "mov $1, %1"
		 :"=r" (x), "=r" (y)
		 );
  printf("Thread 1 ran\n");
  
}
void thread2func (struct MemoryLocs* mem) {
  
    int r1 = 100;
    int r2 = 100;
    
    
    int* x = ((int*) mem);
    int* y = (((int*) mem) + 1);
    
    
    asm volatile("mov %3, %0\n\t"
                "mov %2, %1"
		 :"=r" (r1), "=r" (r2)
		 :"m" ((int*) mem), "m" (y)
    );

     printf("r1: %d\n", r1);
    printf("r2: %d\n", r2);
    printf("Thread 2 ran\n");
}

// Must compile with -lpthread
// Will generate warnings

int main(argc,argv) {

     struct MemoryLocs mem;
     mem.x = 0;
     mem.y = 0;
     
    pthread_t thread1;
    pthread_t thread2;

    pthread_create(&thread1, NULL, thread1func, (void*) &mem);
    pthread_create(&thread2, NULL, thread2func, (void*) &mem);

    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    printf("Final x: %d\n", mem.x);
    printf("Final y: %d\n", mem.y);
}

