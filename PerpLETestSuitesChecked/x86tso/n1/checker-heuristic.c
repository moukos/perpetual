long condition2(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, sum=0;

	for (n=N-1; n>=0; n--) {
	  if((buf0[buf2[2 * n + 1] /2] < buf2[2 *n]) && (buf2[2 * n] % 2  == 1) && (buf2[2 * n + 1] % 2 == 1))
	    sum++;
	}
	
	return sum;
}
