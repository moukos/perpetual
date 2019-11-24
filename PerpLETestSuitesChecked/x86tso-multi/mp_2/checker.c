long condition(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, sum=0;
	long numberUp = 0;
	long leftEdgeEnd = buf1[2 * n + 1];
	for(n = 0; n < N; n++ ){ 
	leftEdgeEnd = buf1[2 * n + 1];
		if(leftEdgeEnd < buf1[2 * n + 0]) 
			sum++;
		
	}
	return sum;
}
