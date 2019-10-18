int condition(int *buf0,int *buf1,int *buf2,int *buf3){
	// possible changes needed for overflow
	ne = N-1
	me = N-1
	numberUp = 0;
	fractions = [0,1,0.5,1/3,0.25];
	// Loops in separate threads
	for( n=N-1; n>=0; n-- ){
		if(!(buf0[n] < n+1))
			continue;
		oldme = me;
		ne = n;
		me = buf0[n];
		numberUp = 1;
		for( m=oldme; m >=me; m--){
			if(buf1[m] < ne+1){

				if(buf1[m]<m+1){
					numberUp=2;
				}
				else{
					numberUp=1;
				}
				sum+= fractions[numberUp];
			}
		}
	}
	//Outer T2 loop
	for( m=N-1; m>=0; m-- ){
		if(!(buf1[m] < m+1))
			continue;
		oldne = ne;
		me = m;
		ne = buf1[m];
		numberUp = 1;
		for( n=oldne; n >=ne; n--){
			if(buf0[n] < me+1){

				if(buf0[n]<n+1){
					numberUp=2;
				}
				else{
					numberUp=1;
				}
				sum+= fractions[numberUp];
			}
		}
	}
}