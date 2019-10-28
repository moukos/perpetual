long condition2(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, m=0;
	double sum=0, oldne=0, oldme=0;
	long numberUp = 0;

	long mend = N-1;
	long nend = N-1;
	
	for( n=N-1; n>=0; n-- ){
	  long leftEdgeEnd = buf0[1*n+ 0];
	  if(!( leftEdgeEnd < 1 * n + 1))
	     continue;
	
	  for( m=mend; m>= leftEdgeEnd; m--){
	    long rightEdgeEnd = buf1[1*m+ 0];

	    if(rightEdgeEnd < 1 * n + 1){
		  if(rightEdgeEnd < m + 1) {
		    sum += 0.5;
		  }
		    else sum++;
		}
		
		else mend = m;
	   }

	}

	for( n=N-1; n>=0; n-- ){
	  long edgeEnd = buf1[1*n+ 0];
	  if(!( edgeEnd < 1 * n + 1))
	     continue;
	
	  for( m=N-1; m>= edgeEnd; m--){
		  if(buf0[1*m+ 0] < 1 * n + 1){
		    if(buf0[m] < m + 1) sum += 0.5;
		    else sum++;
		
			}
		  else mend = m;
		}
	  
	}



	return ((long) sum);
}
