long condition(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long n=0, m=0, p=0, o=0;
	double sum=0;
	double fractions = [0,1,0.5,1/3,0.25];	long nend = N-1;
	long mend = N-1;
	long pend = N-1;
	long oend = N-1;
	long numberUp = 0;
	for( n=N-1; n>=0; n-- ){ 
		if(!(buf2[2 * o + 0] >= 1 * m + 1 - 1))
			continue;
		for( m=N-1; m>=0; m--){
			if(buf2[2 * o + 1] < buf1[1 * m + 0]){
				sum++;
			}
		}
	}
	return sum;
}
