	.section ".text"
	.globl P3
	.type P3, @function

P3:
	pushq %rbp
	pushq %r12
	pushq %r13
	pushq %r14
	movq %rsp, %rbp
	
	popq %r14
	popq %r13
	popq %r12
	popq %rbp
	ret
