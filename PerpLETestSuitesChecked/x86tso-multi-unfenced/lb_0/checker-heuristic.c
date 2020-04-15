long condition2(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, sum=0;
	long numberUp = 0;
	for(n = 0; n < N; n++ ){ 
		if(buf1[buf0[1 * n]] <= n && (buf0[1 * n] < N) && (buf0[1*n] >= 0)){
		  //			printf("n:%ld buf0[n]:%ld buf1[n]:%ld buf1[buf0[n]] %d \n",n,buf0[n],buf1[n],buf1[buf0[n]-1]);  
			sum++;
		}
	}
	return sum;
}
