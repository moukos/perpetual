	.text
	.globl P2
	.globl x
	.globl y
	.type P2, @function

P2:
	pushq %rbp
	movq %rsp, %rbp
	movq %rdi, -24(%rbp) # Copies address of array
	movl $0, -4(%rbp) # Sets loop counter to 0
	jmp .L2
.L3:
	movl -4(%rbp), %eax #copy counter to eax
	cltq	# extend eax to rax
	leaq 0(,%rax,4), %rdx # based on counter, load array offset into rdx
	movq -24(%rbp), %rax #move array address to rax
	addq %rdx, %rax # array address + offset into rax
	# LB Thread 2
#	movl x(%rip), %ebx # Copy global x to ebx 
	movl x, %ebx
	movl -4(%rbp), %ecx # Copy counter to ecx
#	movl %ecx, y(%rip) # write counter to global y
	movl %ecx, y
	movl %ebx, (%rax) # write value read to array
	addl $1, -4(%rbp) # Increment loop counter
.L2:
	movl n(%rip), %eax
	cmpl %eax, -4(%rbp) 
	jle .L3
	popq %rbp
	ret
