def countCycles(t0b1, t0b2, t1b1, t1b2, t2b1, t2b2, t3b1, t3b2):
	cycCnt = 0
	for k,v in t0b1.items():
		if(t1b1.get(v + 1) == k - 1):
			cycCnt += 1
	return cycCnt
