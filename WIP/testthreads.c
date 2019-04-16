#include <stdio.h>
#include <pthread.h>

void thread1func (int* x) {
    asm volatile("movl $1, %0"
        :"=r" (x)
       );
}

void thread2func (int* y) {
    asm volatile("movl $1, %0"
        :"=r" (y)
       );
}

// Must compile with -lpthread
// Will generate warnings

int main(argc,argv) {

    int x = 0;
    int y = 0;

    pthread_t thread1;
    pthread_t thread2;

    pthread_create(&thread1, NULL, thread1func, (void*) &x);
    pthread_create(&thread2, NULL, thread2func, (void*) &y);

    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    printf("x: %d\n", x);
    printf("y: %d\n", y);
}

