	.section ".text"
	.globl P3
	.type P3, @function

P3:
	pushq %rsi
	pushq %r12
	pushq %r13
	pushq %r14
	pushq %r15
	pushq %rbp
	movq  %rsp, %rbp

	movslq 36(%rdi), %r12	# no of threads
	movslq 32(%rdi), %r11	# no of iterations
	movq 24(%rdi), %r10		# ptr to buf[0]
	movq 16(%rdi), %r15		# ptr to z
	movq 8(%rdi), %r14		# ptr to y
	movq (%rdi), %rsi		# ptr to x
	movq $0, %r13			# loop index
	movq $0, %rdx			# buffer address offset
	jmp .LOOPEND

.LOOPSTART:
	# iriw Thread 3
	movq (%r14),%rax
	movq (%rsi),%rbx
	
	# Store in correct location in bufs
	movq %rax, (%r10, %rdx, 4)

	# Increment loop index and writevals
	incq %r13

.LOOPEND:
	cmpq %r13,%r11
	jl .LOOPSTART

	popq %rbp
	popq %r15
	popq %r14
	popq %r13
	popq %r12
	popq %rsi
	ret
