#include <stdlib.h>
#include <stdio.h>

extern void runLitmus(int * address);

int main()
{
	int *p = (int *)malloc(sizeof(int));
	runLitmus(p);
	return 0;
}
