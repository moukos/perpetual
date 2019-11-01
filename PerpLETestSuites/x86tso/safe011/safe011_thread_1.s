	.section ".text"
	.globl P1
	.type P1, @function

P1:
	pushq %rsi
	pushq %r12
	pushq %r13
	pushq %r14
	pushq %r15
	pushq %rbp
	movq  %rsp, %rbp

	movslq 40(%rdi), %r12	# no of threads
	movq 32(%rdi), %r11	# no of iterations
	movq 24(%rdi), %r10		# ptr to buf[0]
	movq 16(%rdi), %r15		# ptr to z
	movq 8(%rdi), %r14		# ptr to y
	movq (%rdi), %rsi		# ptr to x
	movq $0, %r13			# loop index
	movq $0, %rdx			# buffer address offset
	movq $2, %r8			# writeval 1
	movq $1, %r9			# writeval 2
	jmp .LOOPEND

.LOOPSTART:
	# safe011 Thread 1
	movq %r8,(%r14)
	movq %r9,(%r15)
	
	# Store in correct location in bufs
	movq %rax, (%r10, %rdx, 8)
	incq %rdx
	movq %rbx, (%r10, %rdx, 8)

	# Increment loop index and writevals
	incq %r13
	incq %rdx
	addq $2, %r8
	addq $2, %r9

.LOOPEND:
	cmpq %r11,%r13
	jl .LOOPSTART

	popq %rbp
	popq %r15
	popq %r14
	popq %r13
	popq %r12
	popq %rsi
	ret
