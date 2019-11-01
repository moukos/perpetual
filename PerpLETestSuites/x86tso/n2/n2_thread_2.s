	.section ".text"
	.globl P2
	.type P2, @function

P2:
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
	jmp .LOOPEND

.LOOPSTART:
	# n2 Thread 2
	movq (%rsi),%rax
	movq (%rsi),%rbx
	
	# Store in correct location in bufs
	movq %rax, (%r10, %rdx, 8)

	# Increment loop index and writevals
	incq %r13

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
