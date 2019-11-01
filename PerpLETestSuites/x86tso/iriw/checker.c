long condition(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, m=0, p=0, o=0;
	double sum=0;
	long nend = N-1;
	long mend = N-1;
	long numberUp = 0;
	for( n=N-1; n>=0; n-- ){ 
		for( m=mend; m>= leftEdgeEnd; m--){
			long leftEdgeEnd = buf3[2 * p + 1];
			if(leftEdgeEnd < buf2[2 * o + 0]){
				long rightEdgeEnd = buf2[2 * o + 1];
				if(rightEdgeEnd  < buf3[2 * p + 0]){
					if(rightEdgeEnd < m + 1) { // for edges facing upwards
						sum += 0.5;
					}
					else sum++;
				}
				else mend = m;
			}
		}
	}
	for( n=N-1; n>=0; n-- ){ 
		for( m=N-1; m>= leftEdgeEnd; m--){
			long leftEdgeEnd = buf2[2 * p + 1];
			if( leftEdgeEnd < buf2[2 * o + 0]){
			long rightEdgeEnd = buf3[2 * o + 1];
				if(rightEdgeEnd  < buf3[2 * p + 0]){
					if(rightEdgeEnd < m + 1) { // for edges facing upwards
						sum += 0.5;
					}
					else sum++;
				}
				else mend = m;
			}
		}
	}
	return ((long) sum);
}
