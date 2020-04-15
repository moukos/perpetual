long condition(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N, long *sum){
	long n=0, m=0, p=0, o=0, heuristicm=0, consecutive = 0;
	long sumh=0, originalsum=0;
	for( n=0; n<=N-1; n++ ){ 
		// Save heuristic condition in outer loop
		// print
		// For every internal check if it's a continuation of 
		// either n or the index of the heuristic within the condition
		if(buf1[2 * buf0[2 * n + 1] + 1] < n + 1 && (buf0[2 * n + 1] < N)){
			sumh++;
			heuristicm = buf0[2*n+1];
		}
		
		// Count only outcomes that have non consecutive m's or are =m

		consecutive = heuristicm; 

		for( m= heuristicm; m >=0; m--){
			long leftEdgeEnd = buf0[2 * n + 1];
			long rightEdgeEnd = buf1[2 * m + 1];		
			if(leftEdgeEnd < 1 * m + 1){
				if(rightEdgeEnd  < 1 * n + 1){
				    originalsum++;
				    if(m == heuristicm){
				    	*sum=*sum+1;
				    }
				    else{
					if(m == consecutive - 1){
						consecutive = m;
				    	}
					else{
						*sum=*sum+1;
						consecutive = m;
					}
				    }
				}
			}
		}

		consecutive = heuristicm;
		for( m=heuristicm + 1; m<= N-1; m++){
			long leftEdgeEnd = buf0[2 * n + 1];
			long rightEdgeEnd = buf1[2 * m + 1];		
			if(leftEdgeEnd < 1 * m + 1){
				if(rightEdgeEnd  < 1 * n + 1){
					originalsum++;
					if(m == consecutive + 1){
					   	consecutive = m;
				    	}
					else{
						*sum=*sum+1;
						consecutive = m;
				   	}
				}
			}
		}
	}
	
//	fprintf(stderr,"Accuracy %f %%", (double) sumh/sum);
//	fprintf(stderr,"%s","\n");
//	fprintf(stderr,"Exhaustive counter %f\n", originalsum);
//	fprintf(stderr,"Exhaustive modified counter %f\n", *sum);
//	fprintf(stderr,"Exhaustive counter %f\n", sumh);
	
	return  originalsum;
}
