int condition2(volatile int *buf0, volatile int *buf1, volatile int *buf2, volatile int *buf3, int N){
	int n=0, m=0;
	double sum=0, oldne=0, oldme=0;
	int numberUp = 0;

	int mend = N-1;
	int nend = N-1;
	
	for( n=N-1; n>=0; n-- ){
	  int leftEdgeEnd = buf0[1*n+ 0];
	  if(!( leftEdgeEnd < 1 * n + 1))
	     continue;
	
	  for( m=mend; m>= leftEdgeEnd; m--){
	    int rightEdgeEnd = buf1[1*m+ 0];

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
	  int edgeEnd = buf1[1*n+ 0];
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



	return ((int) sum);
}
