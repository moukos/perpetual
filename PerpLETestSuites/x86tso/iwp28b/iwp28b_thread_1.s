	.section ".text"
	.globl P0
	.type P0, @function

P0:
	pushq %rsi
	pushq %r12
	pushq %r13
	pushq %r14
	pushq %r15
	pushq %rbp
	movq  %rsp, %rbp

	movq 32(%rdi), %r12	# no of threads
	movq 28(%rdi), %r11	# no of iterations
	movq 24(%rdi), %r10	# ptr to buf[0]
	movq 16(%rdi), %r15	# ptr to z
	movq 8(%rdi), %r14	# ptr to y
	movq (%rdi), %rsi	# ptr to x
	movq $0, %r13		# loop index
	movq $0, %rdx		#buffer address offset
	movq $1, %r8		# writeval 1
	movq $ , %r9		# writeval 2
	movq $1, %r9		# writeval 2
	jmp .LOOPEND

.LOOPSTART:
	# iwp28b Thread 0
movq %r8,None
movq %r9,(%rsi)
movq %r9,(%r14)

	# Store in correct location in bufs
	movq %rax, (%r10, %rdx, 4)
	incq %rdx
	movq %rbx, (%r10, %rdx, 4)
	incq %rdx
	movq %rcx, (%r10, %rdx, 4)

	# Increment loop index and writevals
	incq %r13
	incq %rdx
	addq $3, %r8
	addq $3, %r9

.LOOPEND:
	cmpq %r13,%r11
	jl .LOOPSTART

	popq %rbp
	pushq %r15
	pushq %r14
	pushq %r13
	popq %r12
	pushq %rsi
	ret
