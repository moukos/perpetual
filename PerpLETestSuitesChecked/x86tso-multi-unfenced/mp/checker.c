long condition(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, sum=0;
	long sum0=0, sum1=0, sum2=0, sum3=0;
	long numberUp = 0;
	long leftEdgeEnd = buf1[2 * n + 1];
	for(n = 0; n < N; n++ ){ 
		leftEdgeEnd = buf1[2 * n + 1];
		if((leftEdgeEnd == buf1[2 * n + 0]) && leftEdgeEnd <= n){
			sum0++;
		}
		else if(leftEdgeEnd > buf1[2 * n + 0]){
                        sum1++;
		}
		else if(leftEdgeEnd < buf1[2 * n + 0]){
                        sum2++;
		}
		else if((leftEdgeEnd == buf1[2 * n + 0]) && leftEdgeEnd >= n+1){
                        sum3++;
		}
	}

	fprintf(stderr, "%ld\n",sum0);
	fprintf(stderr, "%ld\n",sum1);
	fprintf(stderr, "%ld\n",sum2);
	fprintf(stderr, "%ld\n",sum3);
	printf("%ld\n",sum0);
	printf("%ld\n",sum1);
	printf("%ld\n",sum2);
	printf("%ld\n",sum3);
	
	return sum;
}
