long condition(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, m=0, p=0, o=0;
	double sum=0;
	long nend = N-1;
	long mend = N-1;
	long numberUp = 0;
	for( n=N-1; n>=0; n-- ){ 
		for( m=mend; m>= leftEdgeEnd; m--){
			long leftEdgeEnd = buf1[1 * m + 0];
			if(leftEdgeEnd >= 2 * n + 1 - 1){
				long rightEdgeEnd = buf2[1 * o + 0];
				if(rightEdgeEnd  < buf1[1 * m + 0]){
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
			long leftEdgeEnd = buf2[1 * m + 0];
			if( leftEdgeEnd >= 2 * n + 1 - 1){
			long rightEdgeEnd = buf1[1 * o + 0];
				if(rightEdgeEnd  < buf1[1 * m + 0]){
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
