long condition2(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, sum=0;
	long numberUp = 0;
	for(n = 0; n < N; n++ ){ 
	  if((buf2[buf1[buf0[n]]] >= n + 1) && (buf0[n] < N) && (buf1[buf0[n]] < N))
			sum++;
	}
	return sum;
}
