#include <stdio.h>

int main(argc,argv) {

    int x = 0;
    int y = 0;

    asm volatile("movl $1, %0\n\t"
                 "movl $1, %1"
        :"=r" (x), "=r" (y)
       );

    printf("x: %d\n", x);
    printf("y: %d\n", y);
}
