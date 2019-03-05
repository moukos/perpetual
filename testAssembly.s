	.text
	.globl runLitmus
	.type runLitmus, @function

runLitmus:
	pushq %rbp
	movq %rsp, %rbp

	movl    %edi, -4(%rbp)
        movl    -4(%rbp), %eax
        movl    $12, (%eax)
	
	popq %rbp
	ret
