long condition(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, m=0, p=0, o=0;
	long sum=0;
	for( n=N-1; n>=0; n-- ){ 
		for( m=N-1; m>= 0; m--){
			long leftEdgeEnd = buf2[m];
			if(leftEdgeEnd < buf1[2 * n]){
				long rightEdgeEnd = buf1[2 * n + 1];
				if(rightEdgeEnd  < m+1){
					sum++;
				}
			}
		}
	}
	return sum;
}
