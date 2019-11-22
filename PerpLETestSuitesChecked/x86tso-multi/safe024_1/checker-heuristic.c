long condition2(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, sum=0;
	long numberUp = 0;
	for(n = 0; n < N; n++ ){ 
		if((buf1[2*n] > buf2[buf1[2 * n + 1]]) && (buf1[2*n + 1] >= 0) && (buf1[2*n+1]<=N-1))
			sum++;
	}
	return sum;
}
