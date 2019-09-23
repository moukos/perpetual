int main()
{
	int x;
	volatile int dstx=0;
	dstx=1;
	x=dstx;

	return 0;
}
