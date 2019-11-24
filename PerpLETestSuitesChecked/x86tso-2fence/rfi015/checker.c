long condition(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, m=0, p=0, o=0;
	long sum=0;
	for( n=N-1; n>=0; n-- ){ 
		for( m=N-1; m>= 0; m--){
			long leftEdgeEnd1 = buf1[2 * n + 0];
			long leftEdgeEnd2 = buf1[2 * n + 1];
			
			long rightEdgeEnd1 = buf2[2 * m + 0];		
			long rightEdgeEnd2 = buf2[2 * m + 1];		
			if(leftEdgeEnd1 > rightEdgeEnd2)
				if(leftEdgeEnd2 < rightEdgeEnd1)
				    sum++;
			
		}
	}
	
	return  sum;
}
