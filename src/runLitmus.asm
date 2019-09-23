global runLitmus
section .text

runLitmus:
	push rbp
	mov rbp, rsp
	mov rsp, rbp
	pop rbp
	ret
