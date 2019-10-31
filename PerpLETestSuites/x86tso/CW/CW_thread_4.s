	.section ".text"
	.globl P3
	.type P3, @function

P3:
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
	jmp .LOOPEND

.LOOPSTART:
	# CW Thread 3
movq (%rdi),%rax
movq (%rdi),%rbx

	# Store in correct location in bufs
	movq %rax, (%r10, %r12, 4)
	movq %rbx, (%r11, %r12, 4)

	# Increment loop index and writevals
	incq %r12
	addq $0, %r8
	addq $0, %r9

.LOOPEND:
	cmpq %r13,%r12
	jl .LOOPSTART

	popq %rbp
	popq %r13
	popq %r12
	popq %rbx
	ret
