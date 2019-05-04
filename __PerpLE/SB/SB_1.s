	.section ".text"
	.globl P1
	.type P1, @function

P1:
	pushq %rbx
	pushq %r12
	pushq %r13
	pushq %rbp
	movq  %rsp, %rbp

	movq 48(%rdi), %r13	# no. of iterations
	movq 40(%rdi), %r11	# buf2
	movq 32(%rdi), %r10	# buf1
	movq 24(%rdi), %rcx	# ptr to w
	movq 16(%rdi), %rdx	# ptr to z
	movq 8(%rdi), %rsi	# ptr to y
	movq (%rdi), %rdi	# ptr to x
	movq $0, %r12		# loop index
	movq $1, %r8		# writeval 1
	jmp .LOOPEND

.LOOPSTART:
	# SB Thread 1
	movq %r8, (%rsi)
	movq (%rdi), %rax

	# Store in correct location in bufs
	movq %rax, (%r10, %r12, 4)
	movq %rbx, (%r11, %r12, 4)

	# Increment loop index and writevals
	incq %r12
	addq $1, %r8
	addq $1, %r9

.LOOPEND:
	cmpq %r13,%r12
	jl .LOOPSTART

	popq %rbp
	popq %r13
	popq %r12
	popq %rbx
	ret
