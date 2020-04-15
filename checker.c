long condition(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N, long *sum){
	long n=0, m=0, p=0, o=0, consecutive = 0;
	long originalsum=0;
	for( n=0; n<=N-1; n++ ){ 
		consecutive = -1;
		for( m=0; m<=N-1; m++){
			long leftEdgeEnd = buf0[1 * n + 0];
			if(leftEdgeEnd < 1 * m + 1){
				long rightEdgeEnd = buf1[1 * m + 0];
				if(rightEdgeEnd  < 1 * n + 1){
				  originalsum++; 
				  if(m == 0){
				    *sum = *sum + 1;
				    consecutive = 0;
				  }
				  else{
				    if(m == consecutive + 1){
				      consecutive = m;
				    }
				    else{
				      *sum = *sum+1;
				      consecutive = m;
				    }
				  }
				}
			}
		}
	}
	
	return  originalsum;
}
