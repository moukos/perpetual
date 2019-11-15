#START _litmus_P1
	movl $1,(%rdi,%rcx)
	movl (%rdx,%rcx),%eax
#START _litmus_P0
	movl $1,(%rdx,%r14)
	movl (%rcx,%r14),%eax
