long condition(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, m=0, p=0, o=0;
	long sum=0;
	for( n=N-1; n>=0; n-- ){ 
		for( m=N-1; m>= 0; m--){
		  for (o=N-1; o>=0; o--) {
			long leftEdgeEnd = buf0[1 * n + 0];
			long midEdgeEnd = buf1[1 * m + 0];
			long rightEdgeEnd = buf2[1 * o + 0];
			if(leftEdgeEnd < 1 * m + 1)
				if(midEdgeEnd > 1 * o + 1)
				  if (rightEdgeEnd < 1 * n + 1)
				    sum++;
			}
		}
	}
	
	return  sum;
}
