long condition(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, m=0, p=0, o=0;
	long sum=0;
	for( n=N-1; n>=0; n-- ){ 
		for( m=0; m>= 0; m--){
			long leftEdgeEnd1 = buf2[2 * n];
			long leftEdgeEnd2 = buf2[2 * n + 1];
			long rightEdgeEnd1 = buf3[2 * m];
			long rightEdgeEnd2 = buf3[2 * m + 1];

			if((leftEdgeEnd1 % 2 == 1) && (leftEdgeEnd2 % 2 == 0))
			  if((rightEdgeEnd1 % 2 == 0) && (rightEdgeEnd2 % 2 == 1) &&
			     (rightEdgeEnd1 > leftEdgeEnd2) && (rightEdgeEnd2 < leftEdgeEnd1))
			    sum++;
							
		}
	}
	return sum;
}
