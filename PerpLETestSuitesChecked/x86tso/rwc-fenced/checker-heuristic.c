long condition2(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, m=0, p=0, o=0;
	long sum=0;
	for( n=N-1; n>=0; n-- ){ 
	  if((buf1[2*n] > buf2[buf1[2* n + 1]]) && (buf1[2* n + 1] < N)){
		sum++;
	  }
	}
	return  sum;
}
