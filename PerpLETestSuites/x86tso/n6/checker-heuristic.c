long condition2(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, sum=0;
	long numberUp = 0;
	for(n = 0; n < N; n++ ){ 
		if(buf0[2 * n + 0] < buf0[2 * n + 0] + 2)
			sum++;
	}
	return sum;
}
