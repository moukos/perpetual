long condition(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, m=0, p=0, o=0, heuristicm=0, consecutive = 0;
	long sum=0, sumh=0;
	for( n=0; n<=N-1; n++ ){ 
		// Save heuristic condition in outer loop
		// print
		// For every internal check if it's a continuation of 
		// either n or the index of the heuristic within the condition
		if((buf1[buf0[1 * n + 0] + 0] < 1 * n + 1) && (buf0[1* n + 0] + 0     < N)){
			sumh++;
			heuristicm = buf0[n]
		}
		
		// Count only outcomes that have non consecutive m's or are =m

		consecutive = heuristicm; 

		for( m= heuristicm; m >=0; m--){
			long leftEdgeEnd = buf0[1 * n + 0];
			long rightEdgeEnd = buf1[1 * m + 0];		
			if(leftEdgeEnd < 1 * m + 1){
				if(rightEdgeEnd  < 1 * n + 1){
				    if(m == heuristicm){
				    	sum++;
				    }
				    else{
					if(m == consecutive - 1){
						consecutive = m
				    	}
					else{
						sum++;
					}
				    }
				}
			}
		}

		consecutive = heuristicm
		for( m=heuristicm + 1; m<= N-1; m++){
			long leftEdgeEnd = buf0[1 * n + 0];
			long rightEdgeEnd = buf1[1 * m + 0];		
			if(leftEdgeEnd < 1 * m + 1){
				if(rightEdgeEnd  < 1 * n + 1){
					if(m == consecutive + 1){
						consecutive = m
				    	}
					else{
						sum++;
					}
				}
			}

				    sum++;
			}
		}
	}
	
	printf("Accuracy %lf\n", (double) sumh/sum);
	return  sum;
}
