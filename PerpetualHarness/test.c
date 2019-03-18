#include <stdlib.h>
#include <stdio.h> 
extern void runLitmus(int * address, int *address2);

int main()
  {
  int *x = (int *)malloc(sizeof(int));
  int *y = (int *)malloc(sizeof(int));
  runLitmus(x,y);
  printf("numbers %d %d\n",*x,*y);
  return 0;
}

