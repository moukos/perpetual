	.file	"SB.c"
	.section	.rodata.str1.8,"aMS",@progbits,1
	.align 8
.LC0:
	.string	"%-6lu%c>0:EAX=%i; 1:EAX=%i; x=%i; y=%i;\n"
	.text
	.p2align 4,,15
	.type	do_dump_outcome, @function
do_dump_outcome:
.LFB35:
	.cfi_startproc
	subq	$24, %rsp
	.cfi_def_cfa_offset 32
	cmpl	$1, %ecx
	movq	16(%rsi), %rax
	movq	24(%rsi), %r10
	sbbl	%ecx, %ecx
	movq	8(%rsi), %r9
	movq	(%rsi), %r8
	andl	$16, %ecx
	movl	$.LC0, %esi
	movl	%eax, (%rsp)
	addl	$42, %ecx
	xorl	%eax, %eax
	movl	%r10d, 8(%rsp)
	call	fprintf
	addq	$24, %rsp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE35:
	.size	do_dump_outcome, .-do_dump_outcome
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC1:
	.string	"SB, check_globals failed"
	.text
	.p2align 4,,15
	.type	check_globals, @function
check_globals:
.LFB40:
	.cfi_startproc
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	movq	%rdi, %r15
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	subq	$8, %rsp
	.cfi_def_cfa_offset 64
	movq	96(%rdi), %rax
	movq	(%rdi), %r14
	movq	8(%rdi), %r13
	movl	4(%rax), %eax
	testl	%eax, %eax
	jle	.L9
	subl	$1, %eax
	leaq	88(%rdi), %rbp
	xorl	%ebx, %ebx
	movl	%eax, %r12d
	cltq
	salq	$2, %rax
	notq	%r12
	salq	$2, %r12
	addq	%rax, %r14
	addq	%rax, %r13
	jmp	.L10
	.p2align 4,,10
	.p2align 3
.L7:
	movq	%rbp, %rdi
	call	rand_bit
	testl	%eax, %eax
	je	.L8
	movl	0(%r13,%rbx), %eax
	testl	%eax, %eax
	jne	.L19
.L8:
	subq	$4, %rbx
	cmpq	%r12, %rbx
	je	.L9
.L10:
	movq	%rbp, %rdi
	call	rand_bit
	testl	%eax, %eax
	je	.L7
	movl	(%r14,%rbx), %edx
	testl	%edx, %edx
	je	.L7
	movl	$.LC1, %edi
	call	fatal
	jmp	.L7
	.p2align 4,,10
	.p2align 3
.L19:
	movl	$.LC1, %edi
	subq	$4, %rbx
	call	fatal
	cmpq	%r12, %rbx
	jne	.L10
	.p2align 4,,10
	.p2align 3
.L9:
	movq	32(%r15), %rdi
	addq	$8, %rsp
	.cfi_def_cfa_offset 56
	popq	%rbx
	.cfi_def_cfa_offset 48
	popq	%rbp
	.cfi_def_cfa_offset 40
	popq	%r12
	.cfi_def_cfa_offset 32
	popq	%r13
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_def_cfa_offset 16
	popq	%r15
	.cfi_def_cfa_offset 8
	jmp	pb_wait
	.cfi_endproc
.LFE40:
	.size	check_globals, .-check_globals
	.section	.rodata.str1.1
.LC2:
	.string	"%i: Stabilizing final state!\n"
	.text
	.p2align 4,,15
	.type	stabilize_globals, @function
stabilize_globals:
.LFB41:
	.cfi_startproc
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	leaq	48(%rsi), %r13
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	leaq	64(%rsi), %r12
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	movq	%rsi, %rbp
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	subq	$56, %rsp
	.cfi_def_cfa_offset 112
	movq	96(%rsi), %rax
	movq	8(%rsi), %r15
	movl	%edi, 44(%rsp)
	movq	32(%rsi), %rdi
	movq	(%rsi), %r14
	movl	4(%rax), %ebx
	call	pb_wait
	movl	44(%rsp), %edi
	subl	$1, %ebx
	movslq	%edi, %rax
	salq	$3, %rax
	leaq	0(%r13,%rax), %rcx
	addq	%r12, %rax
	movq	%rax, 8(%rsp)
	movl	%edi, %eax
	addl	$1, %eax
	movq	%rcx, 16(%rsp)
	movl	%eax, %edx
	shrl	$31, %edx
	addl	%edx, %eax
	andl	$1, %eax
	subl	%edx, %eax
	cltq
	salq	$3, %rax
	leaq	0(%r13,%rax), %rdi
	addq	%r12, %rax
	movl	%ebx, %r12d
	notq	%r12
	movslq	%ebx, %r13
	movq	%rax, 32(%rsp)
	salq	$2, %r12
	salq	$2, %r13
	movq	%rdi, 24(%rsp)
	movq	%r12, %rax
	addq	%r13, %r15
	addq	%r13, %r14
	movq	%r13, %r12
	movq	%rax, %r13
	.p2align 4,,10
	.p2align 3
.L29:
	testl	%ebx, %ebx
	js	.L21
	movq	16(%rsp), %rax
	movq	%r12, %rsi
	movq	%r12, %rcx
	addq	(%rax), %rsi
	movq	8(%rsp), %rax
	addq	(%rax), %rcx
	xorl	%eax, %eax
	.p2align 4,,10
	.p2align 3
.L23:
	movl	(%r15,%rax), %edx
	movl	%edx, (%rsi,%rax)
	movl	(%r14,%rax), %edx
	movl	%edx, (%rcx,%rax)
	subq	$4, %rax
	cmpq	%r13, %rax
	jne	.L23
	movq	40(%rbp), %rdi
	call	po_reinit
	movq	16(%rsp), %rax
	movq	%r12, %r10
	movq	%r12, %r9
	movq	%r12, %rdi
	movq	%r12, %rsi
	movl	%ebx, %r11d
	addq	(%rax), %r10
	movq	24(%rsp), %rax
	addq	(%rax), %r9
	movq	8(%rsp), %rax
	addq	(%rax), %rdi
	movq	32(%rsp), %rax
	addq	(%rax), %rsi
	xorl	%eax, %eax
.L30:
	movl	(%rsi,%rax), %r8d
	cmpl	%r8d, (%rdi,%rax)
	movl	(%r10,%rax), %ecx
	movl	(%r9,%rax), %edx
	je	.L38
.L24:
	movl	44(%rsp), %esi
	movl	$.LC2, %edi
	xorl	%eax, %eax
	call	log_error
	movl	$1, %esi
.L27:
	movq	40(%rbp), %rdi
	call	po_wait
	testl	%eax, %eax
	jne	.L29
	addq	$56, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	popq	%rbx
	.cfi_def_cfa_offset 48
	popq	%rbp
	.cfi_def_cfa_offset 40
	popq	%r12
	.cfi_def_cfa_offset 32
	popq	%r13
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_def_cfa_offset 16
	popq	%r15
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L38:
	.cfi_restore_state
	cmpl	%edx, %ecx
	setne	%dl
	subl	$1, %r11d
	subq	$4, %rax
	testb	%dl, %dl
	jne	.L32
	testl	%r11d, %r11d
	jns	.L30
.L32:
	testb	%dl, %dl
	jne	.L24
	xorl	%esi, %esi
	.p2align 4,,4
	jmp	.L27
	.p2align 4,,10
	.p2align 3
.L21:
	movq	40(%rbp), %rdi
	call	po_reinit
	xorl	%esi, %esi
	jmp	.L27
	.cfi_endproc
.LFE41:
	.size	stabilize_globals, .-stabilize_globals
	.p2align 4,,15
	.type	P1, @function
P1:
.LFB43:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rdi, %rbp
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	subq	$8, %rsp
	.cfi_def_cfa_offset 32
#APP
# 40 "SB.c" 1
	mfence
# 0 "" 2
#NO_APP
	movq	8(%rdi), %rbx
	movq	%rbx, %rdi
	call	check_globals
	movq	96(%rbx), %rax
	movl	0(%rbp), %r10d
	movq	80(%rbx), %r9
	movq	24(%rbx), %rdi
	movl	4(%rax), %r8d
	subl	$1, %r8d
	movslq	%r8d, %rcx
	salq	$2, %rcx
	testl	%r8d, %r8d
	js	.L44
	.p2align 4,,10
	.p2align 3
.L48:
	movl	%r8d, %eax
	leaq	(%r9,%rcx), %rdx
	andl	$1, %eax
	cmpl	%r10d, %eax
	je	.L53
	.p2align 4,,10
	.p2align 3
.L49:
	movl	(%rdx), %eax
	testl	%eax, %eax
	je	.L49
.L42:
	movq	8(%rbx), %rdx
	movq	(%rbx), %rsi
#APP
# 284 "SB.c" 1
	
#START _litmus_P1
#_litmus_P1_0
	movl $1,(%rsi,%rcx)
#_litmus_P1_1
	movl (%rdx,%rcx),%eax
#END _litmus_P1
	
# 0 "" 2
#NO_APP
	subl	$1, %r8d
	movl	%eax, (%rdi,%rcx)
	subq	$4, %rcx
	cmpl	$-1, %r8d
	jne	.L48
.L44:
	movq	%rbx, %rsi
	movl	$1, %edi
	call	stabilize_globals
#APP
# 40 "SB.c" 1
	mfence
# 0 "" 2
#NO_APP
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	xorl	%eax, %eax
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L53:
	.cfi_restore_state
	movl	$1, (%rdx)
	jmp	.L42
	.cfi_endproc
.LFE43:
	.size	P1, .-P1
	.p2align 4,,15
	.type	P0, @function
P0:
.LFB42:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rdi, %rbp
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	subq	$8, %rsp
	.cfi_def_cfa_offset 32
#APP
# 40 "SB.c" 1
	mfence
# 0 "" 2
#NO_APP
	movq	8(%rdi), %rbx
	movq	%rbx, %rdi
	call	check_globals
	movq	96(%rbx), %rax
	movl	0(%rbp), %r10d
	movq	80(%rbx), %r9
	movq	16(%rbx), %rdi
	movl	4(%rax), %r8d
	subl	$1, %r8d
	movslq	%r8d, %rcx
	salq	$2, %rcx
	testl	%r8d, %r8d
	js	.L59
	.p2align 4,,10
	.p2align 3
.L63:
	movl	%r8d, %eax
	leaq	(%r9,%rcx), %rdx
	andl	$1, %eax
	cmpl	%r10d, %eax
	je	.L68
	.p2align 4,,10
	.p2align 3
.L64:
	movl	(%rdx), %eax
	testl	%eax, %eax
	je	.L64
.L57:
	movq	8(%rbx), %rdx
	movq	(%rbx), %rsi
#APP
# 255 "SB.c" 1
	
#START _litmus_P0
#_litmus_P0_0
	movl $1,(%rdx,%rcx)
#_litmus_P0_1
	movl (%rsi,%rcx),%eax
#END _litmus_P0
	
# 0 "" 2
#NO_APP
	subl	$1, %r8d
	movl	%eax, (%rdi,%rcx)
	subq	$4, %rcx
	cmpl	$-1, %r8d
	jne	.L63
.L59:
	movq	%rbx, %rsi
	xorl	%edi, %edi
	call	stabilize_globals
#APP
# 40 "SB.c" 1
	mfence
# 0 "" 2
#NO_APP
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	xorl	%eax, %eax
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L68:
	.cfi_restore_state
	movl	$1, (%rdx)
	jmp	.L57
	.cfi_endproc
.LFE42:
	.size	P0, .-P0
	.section	.rodata.str1.1
.LC3:
	.string	"Run %i of %i\r"
.LC4:
	.string	"SB, global x unstabilized"
.LC5:
	.string	"SB, global y unstabilized"
	.text
	.p2align 4,,15
	.type	zyva, @function
zyva:
.LFB44:
	.cfi_startproc
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	subq	$264, %rsp
	.cfi_def_cfa_offset 320
	movq	16(%rdi), %rax
	movq	8(%rdi), %rdi
	movq	%rax, %r14
	movq	%rax, 16(%rsp)
	call	pb_wait
	movl	$24, %edi
	movq	$P0, 64(%rsp)
	movq	$P1, 72(%rsp)
	call	malloc_check
	movslq	4(%r14), %rbp
	movq	$0, (%rax)
	movq	%rax, %rbx
	movq	$0, 16(%rax)
	movq	$0, 8(%rax)
	movq	%r14, 240(%rsp)
	call	rand
	salq	$2, %rbp
	movl	%eax, 232(%rsp)
	movq	%rbp, %rdi
	call	malloc_check
	movq	%rbp, %rdi
	movq	%rax, 160(%rsp)
	call	malloc_check
	movq	%rbp, %rdi
	movq	%rax, 168(%rsp)
	call	malloc_check
	movq	%rbp, %rdi
	movq	%rax, 144(%rsp)
	call	malloc_check
	movl	$2, %edi
	movq	%rax, 152(%rsp)
	call	pb_create
	movl	$2, %edi
	movq	%rax, 176(%rsp)
	call	po_create
	movq	%rbp, %rdi
	movq	%rax, 184(%rsp)
	call	malloc_check
	movq	%rbp, %rdi
	movq	%rax, 200(%rsp)
	call	malloc_check
	movq	%rbp, %rdi
	movq	%rax, 216(%rsp)
	call	malloc_check
	movq	%rbp, %rdi
	movq	%rax, 192(%rsp)
	call	malloc_check
	movq	%rbp, %rdi
	movq	%rax, 208(%rsp)
	call	malloc_check
	movl	8(%r14), %ecx
	movq	%rax, 224(%rsp)
	leaq	144(%rsp), %rax
	movl	$1, 96(%rsp)
	movl	$0, 80(%rsp)
	movq	%rax, 104(%rsp)
	movq	%rax, 88(%rsp)
	testl	%ecx, %ecx
	jle	.L80
	leaq	232(%rsp), %rax
	movl	$0, 28(%rsp)
	movq	%rax, 40(%rsp)
	leaq	96(%rsp), %rax
	movq	%rax, 32(%rsp)
	.p2align 4,,10
	.p2align 3
.L90:
	movq	16(%rsp), %rax
	cmpl	$1, (%rax)
	jle	.L71
	movl	28(%rsp), %edx
	movq	stderr(%rip), %rdi
	movl	$.LC3, %esi
	xorl	%eax, %eax
	call	fprintf
.L71:
	movq	240(%rsp), %rax
	movl	4(%rax), %eax
	subl	$1, %eax
	js	.L75
	movl	%eax, %r10d
	cltq
	leaq	0(,%rax,4), %rcx
	notq	%r10
	xorl	%eax, %eax
	salq	$2, %r10
	movq	%rcx, %r9
	movq	%rcx, %r8
	movq	%rcx, %rdi
	movq	%rcx, %rsi
	addq	144(%rsp), %r9
	addq	152(%rsp), %r8
	addq	160(%rsp), %rdi
	addq	168(%rsp), %rsi
	addq	224(%rsp), %rcx
	.p2align 4,,10
	.p2align 3
.L76:
	movl	$0, (%r9,%rax)
	leaq	(%rax,%rcx), %rdx
	movl	$0, (%r8,%rax)
	movl	$-239487, (%rdi,%rax)
	movl	$-239487, (%rsi,%rax)
	subq	$4, %rax
	cmpq	%r10, %rax
	movl	$0, (%rdx)
	jne	.L76
.L75:
	movq	16(%rsp), %rax
	movl	12(%rax), %edx
	testl	%edx, %edx
	jne	.L94
.L74:
	movq	32(%rsp), %rdx
	movq	72(%rsp), %rsi
	leaq	56(%rsp), %rdi
	call	launch
	movq	64(%rsp), %rsi
	leaq	80(%rsp), %rdx
	leaq	48(%rsp), %rdi
	call	launch
	movq	16(%rsp), %rax
	movl	12(%rax), %eax
	testl	%eax, %eax
	jne	.L95
.L77:
	leaq	56(%rsp), %rdi
	call	join
	leaq	48(%rsp), %rdi
	call	join
	movq	16(%rsp), %rax
	movl	4(%rax), %eax
	movl	%eax, 8(%rsp)
	subl	$1, %eax
	js	.L88
	movslq	%eax, %rdx
	movl	%eax, %eax
	leaq	0(,%rdx,4), %r15
	subq	%rax, %rdx
	leaq	-4(,%rdx,4), %rax
	movq	%rax, 8(%rsp)
	jmp	.L89
	.p2align 4,,10
	.p2align 3
.L96:
	testl	%r14d, %r14d
	jne	.L85
	movq	(%rbx), %rdi
	leaq	112(%rsp), %rsi
	movl	$1, %r8d
	movl	$1, %ecx
	movl	$4, %edx
	movq	$0, 112(%rsp)
	movq	$0, 120(%rsp)
	movq	%r12, 128(%rsp)
	subq	$4, %r15
	movq	%rbp, 136(%rsp)
	call	add_outcome_outs
	addq	$1, 8(%rbx)
	cmpq	8(%rsp), %r15
	movq	%rax, (%rbx)
	je	.L88
.L89:
	movq	160(%rsp), %rax
	movslq	(%rax,%r15), %r13
	movq	168(%rsp), %rax
	movslq	(%rax,%r15), %r14
	movq	152(%rsp), %rax
	movslq	(%rax,%r15), %r12
	movq	144(%rsp), %rax
	movslq	(%rax,%r15), %rbp
	movq	200(%rsp), %rax
	cmpl	%r12d, (%rax,%r15)
	je	.L81
	movl	$.LC4, %edi
	call	fatal
.L81:
	movq	192(%rsp), %rax
	cmpl	%r12d, (%rax,%r15)
	je	.L82
	movl	$.LC4, %edi
	call	fatal
.L82:
	movq	216(%rsp), %rax
	cmpl	%ebp, (%rax,%r15)
	je	.L83
	movl	$.LC5, %edi
	call	fatal
.L83:
	movq	208(%rsp), %rax
	cmpl	%ebp, (%rax,%r15)
	je	.L84
	movl	$.LC5, %edi
	call	fatal
.L84:
	testl	%r13d, %r13d
	je	.L96
.L85:
	movq	(%rbx), %rdi
	leaq	112(%rsp), %rsi
	xorl	%r8d, %r8d
	movl	$1, %ecx
	movl	$4, %edx
	movq	%r13, 112(%rsp)
	movq	%r14, 120(%rsp)
	movq	%r12, 128(%rsp)
	subq	$4, %r15
	movq	%rbp, 136(%rsp)
	call	add_outcome_outs
	addq	$1, 16(%rbx)
	cmpq	8(%rsp), %r15
	movq	%rax, (%rbx)
	jne	.L89
.L88:
	movq	16(%rsp), %rax
	addl	$1, 28(%rsp)
	movl	8(%rax), %ecx
	cmpl	28(%rsp), %ecx
	jg	.L90
.L80:
	movq	144(%rsp), %rdi
	call	free
	movq	152(%rsp), %rdi
	call	free
	movq	160(%rsp), %rdi
	call	free
	movq	168(%rsp), %rdi
	call	free
	movq	176(%rsp), %rdi
	call	pb_free
	movq	184(%rsp), %rdi
	call	po_free
	movq	200(%rsp), %rdi
	call	free
	movq	216(%rsp), %rdi
	call	free
	movq	192(%rsp), %rdi
	call	free
	movq	208(%rsp), %rdi
	call	free
	movq	224(%rsp), %rdi
	call	free
	addq	$264, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	movq	%rbx, %rax
	popq	%rbx
	.cfi_def_cfa_offset 48
	popq	%rbp
	.cfi_def_cfa_offset 40
	popq	%r12
	.cfi_def_cfa_offset 32
	popq	%r13
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_def_cfa_offset 16
	popq	%r15
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L94:
	.cfi_restore_state
	movq	40(%rsp), %rdi
	leaq	64(%rsp), %rsi
	movl	$2, %edx
	call	perm_funs
	jmp	.L74
	.p2align 4,,10
	.p2align 3
.L95:
	movq	40(%rsp), %rdi
	leaq	48(%rsp), %rsi
	movl	$2, %edx
	call	perm_threads
	jmp	.L77
	.cfi_endproc
.LFE44:
	.size	zyva, .-zyva
	.section	.rodata.str1.1
.LC6:
	.string	"Never"
.LC7:
	.string	"Sometimes"
.LC8:
	.string	"Always"
.LC9:
	.string	"SB: n=%i, r=%i, s=%i"
.LC10:
	.string	"\n"
.LC11:
	.string	"SB, sum_hist"
.LC12:
	.string	"Test SB Allowed\n"
.LC13:
	.string	"Histogram (%i states)\n"
.LC14:
	.string	"Observation SB %s %lu %lu\n"
.LC16:
	.string	"Time SB %.2f\n"
.LC17:
	.string	"No"
.LC18:
	.string	"%s\n"
.LC19:
	.string	"\nWitnesses\n"
.LC20:
	.string	"Positive: %lu, Negative: %lu\n"
.LC21:
	.string	"NOT "
	.section	.rodata.str1.8
	.align 8
.LC22:
	.string	"Condition exists (0:EAX=0 /\\ 1:EAX=0) is %svalidated\n"
	.align 8
.LC23:
	.string	"Hash=2d53e83cd627ba17ab11c875525e078b\n"
	.section	.rodata.str1.1
.LC24:
	.string	"Ok"
.LC25:
	.string	""
	.section	.text.startup,"ax",@progbits
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB47:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	pushq	%r15
	leaq	-160(%rbp), %rcx
	leaq	-272(%rbp), %rdx
	pushq	%r14
	pushq	%r13
	pushq	%r12
	pushq	%rbx
	subq	$344, %rsp
	.cfi_offset 15, -24
	.cfi_offset 14, -32
	.cfi_offset 13, -40
	.cfi_offset 12, -48
	.cfi_offset 3, -56
	movl	$0, -272(%rbp)
	movl	$10, -268(%rbp)
	movq	-272(%rbp), %rax
	movl	$100000, -264(%rbp)
	movl	$-1, -260(%rbp)
	movl	$1, -256(%rbp)
	movl	$0, -252(%rbp)
	movl	$0, -248(%rbp)
	movq	%rax, -160(%rbp)
	movq	-264(%rbp), %rax
	movl	$0, -244(%rbp)
	movl	$0, -240(%rbp)
	movl	$0, -236(%rbp)
	movl	$-1, -232(%rbp)
	movq	%rax, -152(%rbp)
	movq	-256(%rbp), %rax
	movq	$0, -224(%rbp)
	movq	$0, -216(%rbp)
	movl	$-1, -208(%rbp)
	movl	$0, -204(%rbp)
	movq	$0, -200(%rbp)
	movq	$0, -192(%rbp)
	movl	$-1, -184(%rbp)
	movl	$-1, -180(%rbp)
	movl	$-1, -176(%rbp)
	movl	$0, -172(%rbp)
	movl	$0, -168(%rbp)
	movq	%rax, -144(%rbp)
	movq	-248(%rbp), %rax
	movq	$0, -112(%rbp)
	movq	$0, -104(%rbp)
	movq	$0, -88(%rbp)
	movq	$0, -80(%rbp)
	movq	%rax, -136(%rbp)
	movq	-240(%rbp), %rax
	movq	%rax, -128(%rbp)
	movq	-232(%rbp), %rax
	movq	%rax, -120(%rbp)
	movq	-208(%rbp), %rax
	movq	%rax, -96(%rbp)
	movq	-184(%rbp), %rax
	movq	%rax, -72(%rbp)
	movq	-176(%rbp), %rax
	movq	%rax, -64(%rbp)
	movq	-168(%rbp), %rax
	movq	%rax, -56(%rbp)
	call	parse_cmd
	movq	stdout(%rip), %rax
	movq	%rax, -344(%rbp)
	call	timeofday
	movl	-60(%rbp), %esi
	movq	%rax, -360(%rbp)
	movl	-152(%rbp), %ecx
	movl	-160(%rbp), %eax
	movl	-156(%rbp), %edx
	movl	$1, -308(%rbp)
	testl	%esi, %esi
	movl	%eax, -320(%rbp)
	movl	%ecx, -316(%rbp)
	movl	%edx, -312(%rbp)
	je	.L98
	movl	$0, -308(%rbp)
.L98:
	movl	-140(%rbp), %ebx
	movl	-144(%rbp), %esi
	testl	%ebx, %ebx
	jle	.L128
.L99:
	testl	%eax, %eax
	jne	.L129
.L100:
	leal	-1(%rbx), %eax
	xorl	%r12d, %r12d
	xorl	%r15d, %r15d
	movl	%eax, -328(%rbp)
	cltq
	leaq	22(,%rax,8), %rax
	andq	$-16, %rax
	subq	%rax, %rsp
	movslq	%ebx, %rax
	movq	%rax, -368(%rbp)
	leaq	(%rax,%rax,2), %rax
	movq	%rsp, %r13
	movq	%rsp, -384(%rbp)
	leaq	22(,%rax,8), %rax
	andq	$-16, %rax
	subq	%rax, %rsp
	call	pm_create
	movl	%ebx, %edi
	movq	%rax, -336(%rbp)
	call	pb_create
	movq	%r12, -352(%rbp)
	movq	%rax, -376(%rbp)
	movl	%r15d, %r12d
	movq	%rax, %r15
	movq	%r13, %rax
	movq	%rsp, %r13
	movq	%rax, %r14
	.p2align 4,,10
	.p2align 3
.L104:
	leaq	-320(%rbp), %rax
	cmpl	%r12d, -328(%rbp)
	movq	%r15, 8(%r13)
	movq	%rax, 16(%r13)
	movq	-336(%rbp), %rax
	movq	%rax, 0(%r13)
	jle	.L101
	movq	%r13, %rdx
	movl	$zyva, %esi
	movq	%r14, %rdi
	call	launch
.L102:
	addl	$1, %r12d
	addq	$24, %r13
	addq	$8, %r14
	cmpl	%r12d, %ebx
	jg	.L104
	movslq	-316(%rbp), %rax
	movslq	-312(%rbp), %r14
	movq	-352(%rbp), %r12
	imulq	%rax, %r14
	movl	-328(%rbp), %eax
	testl	%eax, %eax
	je	.L110
	leal	-2(%rbx), %eax
	xorl	%r13d, %r13d
	leaq	8(,%rax,8), %r15
	movq	%r15, -328(%rbp)
	movq	-384(%rbp), %r15
	.p2align 4,,10
	.p2align 3
.L111:
	leaq	(%r15,%r13), %rdi
	call	join
	movq	(%rax), %rdi
	movq	%rax, %rbx
	call	sum_outs
	cmpq	%rax, %r14
	jne	.L108
	movq	8(%rbx), %rdx
	movq	16(%rbx), %rax
	leaq	(%rax,%rdx), %rcx
	cmpq	%rcx, %r14
	je	.L109
.L108:
	movl	$.LC11, %edi
	call	fatal
	movq	8(%rbx), %rdx
	movq	16(%rbx), %rax
.L109:
	addq	%rdx, 8(%r12)
	addq	%rax, 16(%r12)
	movl	$4, %edx
	movq	(%rbx), %rsi
	movq	(%r12), %rdi
	addq	$8, %r13
	call	merge_outs
	movq	%rax, (%r12)
	movq	(%rbx), %rdi
	call	free_outs
	movq	%rbx, %rdi
	call	free
	cmpq	-328(%rbp), %r13
	jne	.L111
.L110:
	call	timeofday
	movq	-336(%rbp), %rdi
	movq	%rax, %rbx
	subq	-360(%rbp), %rbx
	call	pm_free
	movq	-376(%rbp), %rdi
	call	pb_free
	imulq	-368(%rbp), %r14
	movq	(%r12), %rdi
	call	sum_outs
	cmpq	%rax, %r14
	je	.L130
.L106:
	movl	$.LC11, %edi
	call	fatal
	movq	8(%r12), %r15
	movq	16(%r12), %r13
.L112:
	movq	-344(%rbp), %r14
	movl	$16, %edx
	movl	$1, %esi
	movl	$.LC12, %edi
	movq	%r14, %rcx
	call	fwrite
	movq	(%r12), %rdi
	call	finals_outs
	movl	$.LC13, %esi
	movl	%eax, %edx
	movq	%r14, %rdi
	xorl	%eax, %eax
	call	fprintf
	movq	(%r12), %rdx
	leaq	-304(%rbp), %rcx
	movl	$4, %r8d
	movl	$do_dump_outcome, %esi
	movq	%r14, %rdi
	call	dump_outs
	testq	%r15, %r15
	je	.L131
	movq	-344(%rbp), %r14
	movl	$.LC24, %edx
	movl	$.LC18, %esi
	xorl	%eax, %eax
	movq	%r14, %rdi
	call	fprintf
	movq	%r14, %rcx
	movl	$11, %edx
	movl	$1, %esi
	movl	$.LC19, %edi
	call	fwrite
	movq	%r13, %rcx
	movq	%r15, %rdx
	movl	$.LC20, %esi
	movq	%r14, %rdi
	xorl	%eax, %eax
	call	fprintf
	movl	$.LC25, %edx
	movl	$.LC22, %esi
	movq	%r14, %rdi
	xorl	%eax, %eax
	call	fprintf
	movl	$38, %edx
	movq	%r14, %rcx
	movl	$1, %esi
	movl	$.LC23, %edi
	call	fwrite
	movl	$.LC7, %edx
	testq	%r13, %r13
	movl	$.LC8, %eax
	cmove	%rax, %rdx
.L117:
	movq	-344(%rbp), %rdi
	xorl	%eax, %eax
	movq	%r13, %r8
	movq	%r15, %rcx
	movl	$.LC14, %esi
	call	fprintf
	testq	%rbx, %rbx
	js	.L115
	cvtsi2sdq	%rbx, %xmm0
.L116:
	divsd	.LC15(%rip), %xmm0
	movq	-344(%rbp), %rbx
	movl	$.LC16, %esi
	movl	$1, %eax
	movq	%rbx, %rdi
	call	fprintf
	movq	%rbx, %rdi
	call	fflush
	movq	(%r12), %rdi
	call	free_outs
	movq	%r12, %rdi
	call	free
	leaq	-40(%rbp), %rsp
	xorl	%eax, %eax
	popq	%rbx
	popq	%r12
	popq	%r13
	popq	%r14
	popq	%r15
	popq	%rbp
	.cfi_remember_state
	.cfi_def_cfa 7, 8
	ret
.L131:
	.cfi_restore_state
	movq	-344(%rbp), %r14
	movl	$.LC17, %edx
	movl	$.LC18, %esi
	xorl	%eax, %eax
	movq	%r14, %rdi
	call	fprintf
	movq	%r14, %rcx
	movl	$11, %edx
	movl	$1, %esi
	movl	$.LC19, %edi
	call	fwrite
	movq	%r13, %rcx
	xorl	%edx, %edx
	movl	$.LC20, %esi
	movq	%r14, %rdi
	xorl	%eax, %eax
	call	fprintf
	movl	$.LC21, %edx
	movl	$.LC22, %esi
	movq	%r14, %rdi
	xorl	%eax, %eax
	call	fprintf
	movl	$38, %edx
	movq	%r14, %rcx
	movl	$1, %esi
	movl	$.LC23, %edi
	call	fwrite
	movl	$.LC6, %edx
	jmp	.L117
.L130:
	movq	8(%r12), %r15
	movq	16(%r12), %r13
	leaq	0(%r13,%r15), %rax
	cmpq	%rax, %r14
	jne	.L106
	jmp	.L112
.L129:
	movl	%ebx, %esi
	movl	$.LC9, %edi
	xorl	%eax, %eax
	call	log_error
	movl	$.LC10, %edi
	xorl	%eax, %eax
	call	log_error
	jmp	.L100
.L128:
	cmpl	$1, %esi
	jle	.L119
	sarl	%esi
	movl	%esi, %ebx
	.p2align 4,,4
	jmp	.L99
.L115:
	movq	%rbx, %rax
	andl	$1, %ebx
	shrq	%rax
	orq	%rbx, %rax
	cvtsi2sdq	%rax, %xmm0
	addsd	%xmm0, %xmm0
	jmp	.L116
.L119:
	movl	$1, %ebx
	jmp	.L99
.L101:
	movq	%r13, %rdi
	call	zyva
	movq	%rax, -352(%rbp)
	jmp	.L102
	.cfi_endproc
.LFE47:
	.size	main, .-main
	.section	.rodata.cst8,"aM",@progbits,8
	.align 8
.LC15:
	.long	0
	.long	1093567616
	.ident	"GCC: (GNU) 4.8.5 20150623 (Red Hat 4.8.5-36)"
	.section	.note.GNU-stack,"",@progbits
