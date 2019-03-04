	.text
	.globl runLitmus
	.type runLitmus, @function

runLitmus:
	pushq %rbp
	movq %rsp, %rbp

	movl    %edi, -4(%rbp)
	movl	%esi, -8(%rbp)
        movl    -4(%rbp), %eax
        movl    $12, (%eax)
	movl	-8(%rbp), %eax
	movl	$3, (%eax)
	
	popq %rbp
	ret
