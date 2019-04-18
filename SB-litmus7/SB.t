#START _litmus_P1
	movl $1,(%rsi,%rcx)
	movl (%rdx,%rcx),%eax
#START _litmus_P0
	movl $1,(%rdx,%rcx)
	movl (%rsi,%rcx),%eax
