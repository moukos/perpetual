long condition(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, m=0, p=0, o=0;
	long sum=0;
	long sum0=0, sum1=0, sum2=0, sum3=0;
	long sum4=0, sum5=0, sum6=0, sum7=0;
	for( n=N-1; n>=0; n-- ){ 
		for( m=N-1; m>= 0; m--){
		  for (o=N-1; o>=0; o--) {
			sum++;
			long leftEdgeEnd = buf0[1 * n + 0];
			long midEdgeEnd = buf1[1 * m + 0];
			long rightEdgeEnd = buf2[1 * o + 0];
			if((leftEdgeEnd < 1 * m + 1) && (midEdgeEnd < 1 * o + 1) && (rightEdgeEnd < 1 * n + 1)){
				    sum0++;
			}
			else if((leftEdgeEnd < 1 * m + 1) && (midEdgeEnd < 1 * o + 1) && (rightEdgeEnd >= 1 * n + 1)){
                                    sum1++;
                        }
			else if((leftEdgeEnd < 1 * m + 1) && (midEdgeEnd >= 1 * o + 1) && (rightEdgeEnd < 1 * n + 1)){
                                    sum2++;
                        }
			else if((leftEdgeEnd < 1 * m + 1) && (midEdgeEnd >= 1 * o + 1) && (rightEdgeEnd >= 1 * n + 1)){
                                    sum3++;
                	}
			else if((leftEdgeEnd >= 1 * m + 1)
                                && (midEdgeEnd < 1 * o + 1)
                                  && (rightEdgeEnd < 1 * n + 1)){
                                    sum4++;
                        }
			else if((leftEdgeEnd >= 1 * m + 1)
                                && (midEdgeEnd < 1 * o + 1)
                                  && (rightEdgeEnd >= 1 * n + 1)){
                                    sum5++;
                        }
			else if((leftEdgeEnd >= 1 * m + 1)
                                && (midEdgeEnd >= 1 * o + 1)
                                  && (rightEdgeEnd < 1 * n + 1)){
                                    sum6++;
                        }
			else if((leftEdgeEnd >= 1 * m + 1)
                                && (midEdgeEnd >= 1 * o + 1)
                                  && (rightEdgeEnd >= 1 * n + 1))
                                    sum7++;
                        }


		}
	}
	
	fprintf(stderr,"Total %ld\n",sum);
        fprintf(stderr, "%ld\n",sum0);
        fprintf(stderr, "%ld\n",sum1);
        fprintf(stderr, "%ld\n",sum2);
        fprintf(stderr, "%ld\n",sum3);
	fprintf(stderr, "%ld\n",sum4);
        fprintf(stderr, "%ld\n",sum5);
        fprintf(stderr, "%ld\n",sum6);
        fprintf(stderr, "%ld\n",sum7);
        printf("%ld\n",sum0);
        printf("%ld\n",sum1);
        printf("%ld\n",sum2);
        printf("%ld\n",sum3);
        printf("%ld\n",sum4);
        printf("%ld\n",sum5);
        printf("%ld\n",sum6);
        printf("%ld\n",sum7);
	return  sum;
}
