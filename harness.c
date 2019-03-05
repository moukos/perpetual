#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

// Must compile with -lpthread
// Will generate warnings
extern void P1(int * address);

int main(argc,argv) {

    int i = 0;
    int n = 10;
    int *x = (int*) malloc(n*sizeof(int));
    pthread_t thread1;
//    pthread_t thread2;
    pthread_create(&thread1, NULL, P1, x);
//    pthread_create(&thread2, NULL, P1, &y);

    pthread_join(thread1, NULL);
   // pthread_join(thread2, NULL);
    for(i=0;i<10;i++){
	printf("x: %d\n", x[i]);
    }
    return 1;
}

