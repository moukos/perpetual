	.text
	.globl P1
	.globl x
	.globl y
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
	# LB Thread 1
	movl y, %ebx
	#movl y(%rip), %ebx 
	movl -4(%rbp), %ecx	
#	movl %ecx, x(%rip) 
	movl %ecx, x
	movl %ebx, (%rax)
	addl $1, -4(%rbp)
.L2:
	movl n(%rip), %eax
	cmpl %eax, -4(%rbp) 
	jle .L3
	popq %rbp
	ret
