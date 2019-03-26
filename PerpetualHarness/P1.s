	.text
	.globl P1
#	.globl x
#	.globl y
	.type P1, @function

P1:
	pushq %rbp
	movq %rsp, %rbp
	movq %rdi, -24(%rbp)
	movl $0, -4(%rbp)
	movq -24(%rbp), %rax # struct pointer
#	movq 24(%rax), %rbx #number of iterations
	movq $7, (%rax)
	movq $9, 8(%rax)
	movq $0, -4(%rbp)
#	movq 16(%rax), %rax # pointer to array
#	movq $12, %rcx
#	addq %rcx, %rax
#	movl $11, (%rax)	
# 	movq $5, %rbx	
	jmp .L2
.L3:
	movq -24(%rbp), %rax
	movq 16(%rax), %rax
	movl -4(%rbp), %edx
	movslq %edx, %rdx
	salq $2, %rdx
	addq %rdx, %rax
	movl $13, (%rax)

/*	# LB Thread 1
	movl y, %ebx
	#movl y(%rip), %ebx 
	movl -4(%rbp), %ecx	
#	movl %ecx, x(%rip) 
	movl %ecx, x
	movl %ebx, (%rax)
	#movl %ecx, (%rax)
*/
	addl $1, -4(%rbp)
.L2:
	movq -24(%rbp), %rax
	movl 24(%rax), %eax
	cmpl %eax,-4(%rbp)
	jle .L3
	popq %rbp
	ret
