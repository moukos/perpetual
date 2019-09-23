#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void *print_message_function( void *ptr );

main()
{
	pthread_t thread1, thread2;
	char *message1 = "Thread 1";
	char *message2 = "Thread 2";
	int  iret1, iret2;

	/* Create independent threads each of which
	 * will execute function */

	iret1 = pthread_create( &thread1, NULL, print_message_function, (void*) message1);
	iret2 = pthread_create( &thread2, NULL, print_message_function, (void*) message2);

	/* Wait till threads are complete
	 * before main continues. Unless we
	 * */
	/* wait we run the risk of
	 * executing an exit which will
	 * terminate   */
	/* the process and all threads
	 * before the threads have
	 * completed.   */

	pthread_join( thread1, NULL);
	pthread_join( thread2, NULL); 

	printf("Thread 1 returns: %d\n",iret1);
	printf("Thread 2 returns: %d\n",iret2);
	exit(0);
}

void runLitmus_asm()
{
	int *x=0,*y=0;
	int dstx=0,dsty=0;
/*
	asm(
		"movl (%0),$1\n\t"
		"movl (%1),$1\n\t"
		:
		: "rm" (x),
		  "rm" (y)
	   );
	printf("%d\n", x);
	printf("%d\n", y);
	*/
}

void *print_message_function( void *ptr )
{
	char *message;
	int tid;
	
	
	message = (char *) ptr;
	printf("%d \n", pthread_self());
}
