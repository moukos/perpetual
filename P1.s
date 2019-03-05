	.text
	.globl P1
	.type P1, @function

P1:
	pushq %rbp
	movq %rsp, %rbp
	movq %rdi, -24(%rbp)
	movl $0, -4(%rbp)
	jmp .L2
.L3:
	movl -4(%rbp), %eax
	cltq
	leaq 0(,%rax,4), %rdx
	movq -24(%rbp), %rax
	addq %rdx, %rax
	movl $4, (%rax)
	addl $1, -4(%rbp)
.L2:
	cmpl $9, -4(%rbp) 
	jle .L3
	popq %rbp
	ret
