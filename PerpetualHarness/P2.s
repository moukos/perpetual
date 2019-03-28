	.text
	.globl P2
#	.globl x
#	.globl y
	.type P2, @function

P2:
	pushq %rbp
	movq %rsp, %rbp
	movq %rdi, -24(%rbp)
	movl $0, -4(%rbp)
	movq -24(%rbp), %rax # struct pointer
#	movq 24(%rax), %rbx #number of iterations
#	movq $7, (%rax)
#	movq $9, 8(%rax)
	movq $0, -4(%rbp)
	movq $1, %r13
#	movq 16(%rax), %rax # pointer to array
#	movq $12, %rcx
#	addq %rcx, %rax
#	movl $11, (%rax)	
# 	movq $5, %rbx	
	jmp .L2
.L3:

	# LB Thread 1
	#movl -8(%rbp), %ecx	
	#movslq %ecx, %rcx
	movq -24(%rbp), %rax
	movq %r13, 8(%rax)  #write y
	movq (%rax), %rcx # read x
	#movq -24(%rbp), %rax
	# Manage writing into memory
	movq 16(%rax), %rax
	movl -4(%rbp), %edx
	movslq %edx, %rdx 
	salq $2, %rdx
	addq %rdx, %rax
#	movq -8(%rbp), %rcx
	movq %rcx, (%rax)

	#movl y, %ebx
	#movl y(%rip), %ebx 
	#movl -4(%rbp), %ecx	
#	movl %ecx, x(%rip) 
	#movl %ecx, x
	#movl %ebx, (%rax)
	#movl %ecx, (%rax)
	inc %r13
	addl $1, -4(%rbp)
.L2:
	movq -24(%rbp), %rax
	movl 24(%rax), %eax
	cmpl %eax,-4(%rbp)
	jle .L3
 	movq -24(%rbp), %rax
	movq $7, (%rax)
	movq $9, 8(%rax)		
	popq %rbp
	ret
