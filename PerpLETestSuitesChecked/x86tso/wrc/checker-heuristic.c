long condition2(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long m=0, sum=0;
	long numberUp = 0;
	for(m = 0; m < N; m++ ){ 
	  if((buf1[buf2[2 * m + 1] - 1] > buf2[2 * m + 2]) && (buf2[2 * m + 1] > 0)
	     && (buf2[2 * m + 1] - 1 < N))
			sum++;
	}
	return sum;
}
