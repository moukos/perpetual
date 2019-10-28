long condition(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){
	long ne = N-1;
	long me = N-1;
	long n=0, m=0, sum=0, oldne=0, oldme=0;
	long numberUp = 0;
	for( n=N-1; n>=0; n-- ){ 
		for( m=N-1; m>=0; m--){
		if(!(buf0[1*n+ 0] < 1 * m + 1))
			continue;
		  if(buf1[1*m+ 0] < 1 * n + 1){
				sum++;
				//				printf("T0 read %d at iter %d, T1 read %d at iter %d\n", buf0[n], n, buf1[m], m);
			}
		}
	}
	return sum;
}
