long condition(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, m=0, p=0, o=0;
	long sum=0;
	for( n=N-1; n>=0; n-- ){ 
		for( m=N-1; m>= 0; m--){
			long leftEdgeEnd1 = buf0[2 * n + 0];
			long leftEdgeEnd2 = buf0[2 * n + 1];
			long rightEdgeEnd1 = buf1[2 * m + 0];
			long rightEdgeEnd2 = buf1[2 * m + 1];		
			if((leftEdgeEnd1 == n + 1) && (leftEdgeEnd2 < 1 * m + 1))
			  if((rightEdgeEnd1 == m + 1) && (rightEdgeEnd2  < 1 * n + 1))
				    sum++;
			
		}
	}
	
	return  sum;
}
