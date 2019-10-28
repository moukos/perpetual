	.section ".text"
	.globl P0
	.type P0, @function

P0:
	pushq %rbp
	pushq %r12
	pushq %r13
	pushq %r14
	movq %rsp, %rbp
	
	movq (%rdi), %r8	# ptr to x
	movq 8(%rdi), %r9	# ptr to y
	movq 16(%rdi), %r10  	# ptr to buf[0]
	movslq 24(%rdi), %r11	# no of iterations
	movslq 28(%rdi), %r12	# no of threads
	movq $0, %r13		# loop index
	movq $1, %r14		# write value
	jmp .L2
.L3:

	# SB Thread 1
	movq %r14, (%r8)	# write x
	movq (%r9), %rcx	# read y
	
	# Store in correct location in buf
	movq %rcx, (%r10, %r13, 4)

	# Increment loop index and write value 
	incq %r13
	incq %r14
.L2:
	cmpq %r11,%r13
	jl .L3

	popq %r14
	popq %r13
	popq %r12
	popq %rbp
	ret
