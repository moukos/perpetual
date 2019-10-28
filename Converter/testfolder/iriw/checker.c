long condition(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long ne = N-1;
	long me = N-1;
	long n=0, m=0, sum=0, oldne=0, oldme=0;
	long numberUp = 0;
	for( n=N-1; n>=0; n-- ){ 
		if(!(buf3[2*p+ 1] < buf2[2*o+ 0]))
			continue;
		for( m=N-1; m>=0; m--){
			if(buf2[2*o+ 1] < buf3[2*p+ 0]){
				sum++;
			}
		}
	}
	return sum;
}
