int condition(volatile int *buf0, volatile int *buf1, volatile int *buf2, volatile int *buf3, int N){
	int ne = N-1;
	int me = N-1;
	int n=0, m=0, sum=0, oldne=0, oldme=0;
	int numberUp = 0;
	for( n=N-1; n>=0; n-- ){ 
		if(!(buf0[1*n+ 0] < 1 * m + 1))
			continue;
		for( m=N-1; m>=0; m--){
			if(buf1[1*m+ 0] < 1 * n + 1){
				sum++;
				printf("T0 read %d at iter %d, T1 read %d at iter %d\n", buf0[n], n, buf1[m], m);
			}
		}
	}
	return sum;
}
