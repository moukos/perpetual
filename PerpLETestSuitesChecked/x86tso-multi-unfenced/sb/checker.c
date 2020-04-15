long condition(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, m=0, p=0, o=0;
	long sum0=0, sum1=0, sum2=0, sum3=0;
	long sum=0;
	for( n=N-1; n>=0; n-- ){ 
		for( m=N-1; m>= 0; m--){
			sum++;
			long leftEdgeEnd = buf0[1 * n + 0];
			long rightEdgeEnd = buf1[1 * m + 0];		
			if((leftEdgeEnd < 1 * m + 1) && (rightEdgeEnd < 1 * n + 1)){
				    sum0++;
			}
			else if((leftEdgeEnd >= 1 * m + 1) && (rightEdgeEnd < 1 * n + 1)){
                                    sum1++;
                        }
			else if((leftEdgeEnd < 1 * m + 1) && (rightEdgeEnd >= 1 * n + 1)){
                                    sum2++;
                        }
			else if((leftEdgeEnd >= 1 * m + 1) && (rightEdgeEnd >= 1 * n + 1)){
                                    sum3++;
                        }
		}
	}
	fprintf(stderr,"Total %ld\n",sum);	
	fprintf(stderr, "%ld\n",sum0);
        fprintf(stderr, "%ld\n",sum1);
        fprintf(stderr, "%ld\n",sum2);
        fprintf(stderr, "%ld\n",sum3);
	printf("Total %ld\n",sum);
        printf("%ld\n",sum0);
        printf("%ld\n",sum1);
        printf("%ld\n",sum2);
        printf("%ld\n",sum3);	
	return  sum;
}
