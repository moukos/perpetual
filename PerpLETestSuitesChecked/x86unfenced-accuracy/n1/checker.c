long condition(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N, long *sum){
	long n=0, m=0, p=0, o=0, heuristicm=0, consecutive = 0;
	long sumh=0, originalsum=0;
	for( n=0; n<=N-1; n++ ){ 
		// Save heuristic condition in outer loop
		// print
		// For every internal check if it's a continuation of 
		// either n or the index of the heuristic within the condition
		if((buf0[buf2[2 * n + 1] /2] < (buf2[2 * n] / 2 + 1)) && (buf2[2 * n] % 2  == 1) && (buf2[2 * n + 1] % 2 == 0)){
			sumh++;
			heuristicm = buf2[2*n + 1]/2;
		}
		
		// Count only outcomes that have non consecutive m's or are =m

		consecutive = heuristicm; 

		for( m= heuristicm; m >=0; m--){
			long leftEdgeEnd = buf0[n];
			long rightEdgeEnd1 = buf2[2 * m];		
			long rightEdgeEnd2 = buf2[2 * m + 1];		
			if((leftEdgeEnd < (rightEdgeEnd1/2 + 1)) && (rightEdgeEnd1 % 2 ==1)){
				if((rightEdgeEnd2 <= 2 * n) &&(rightEdgeEnd2 % 2 == 0)){
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
			long leftEdgeEnd = buf0[n];
			long rightEdgeEnd1 = buf2[2 * m];		
			long rightEdgeEnd2 = buf2[2 * m + 1];		
			if((leftEdgeEnd < (rightEdgeEnd1/2 + 1)) && (rightEdgeEnd1 % 2 ==1)){
				if((rightEdgeEnd2 <= 2 * n) &&(rightEdgeEnd2 % 2 == 0)){
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
