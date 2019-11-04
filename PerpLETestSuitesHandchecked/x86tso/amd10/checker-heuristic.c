long condition2(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, sum=0;
	long numberUp = 0;
	for(n = 0; n < N; n++ ){ 
		if(buf0[2 * buf1[2 * n + 1] + 1] < n)
			sum++;
	}
	return sum;
}
