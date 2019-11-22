long condition(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, m=0, p=0, o=0;
	long sum=0;
	for( n=N-1; n>=0; n-- ){ 
		for( m=N-1; m>= 0; m--){
			//fprintf(stderr,"buf3[2*m] %ld buf3[2*m+1] %ld,n %ld, m %ld\n",buf3[2*m],buf3[2*m+1],n,m);
			long leftEdgeEnd = buf3[2 * m + 1];
			if(leftEdgeEnd > buf2[2 * n + 0]){
				long rightEdgeEnd = buf2[2 * n + 1];
				if(rightEdgeEnd > buf3[2 * m + 0]){
				    //fprintf(stderr,"buf2[2*n] %ld, buf2[2*n+1] %ld, buf3[2*m],%ld, buf3[2*m+1] %ld, n %ld, m %ld buf0[2*m] %ld, buf1[2*m] %ld \n", buf2[2*n], buf2[2*n+1], buf3[2*m], buf3[2*m+1], n, m,buf0[2*m], buf1[2*m]);
				    sum++;
				}
			}
		}
	}
	return sum;
}
