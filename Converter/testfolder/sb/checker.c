long condition(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, m=0, p=0, o=0;
	double sum=0;
	long nend = N-1;
	long mend = N-1;
	long numberUp = 0;
	for( n=N-1; n>=0; n-- ){ 
		long leftEdgeEnd
		if(!(buf0[1 * n + 0] < 1 * m + 1))
			continue;
		for( m=N-1; m>=0; m--){
			if(buf1[1 * m + 0] < 1 * n + 1){
				sum++;
			}
		}
	}
	return sum;
}
