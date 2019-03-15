	.text
	.globl P2
	.type P2, @function

P2:
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
	movl $1, (%rax)
	addl $1, -4(%rbp)
.L2:
	movl n(%rip), %eax
	cmpl %eax, -4(%rbp) 
	jle .L3
	popq %rbp
	ret
