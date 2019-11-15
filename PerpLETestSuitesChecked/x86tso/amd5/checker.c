long condition(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, m=0, p=0, o=0;
	long sum=0;
	for( n=N-1; n>=0; n-- ){ 
		for( m=N-1; m>=0; m--){
			long leftEdgeEnd = buf0[1 * n + 0];
			if(leftEdgeEnd < 1 * m + 1){
				long rightEdgeEnd = buf1[1 * m + 0];
				if(rightEdgeEnd  < 1 * n + 1)
						sum ++;
			}
		}
	}
	return sum;
}
