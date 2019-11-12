	.file	"sb.c"
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"%-6lu%c>0:EAX=%i; 1:EAX=%i;\n"
	.text
	.p2align 4,,15
	.type	do_dump_outcome, @function
do_dump_outcome:
.LFB35:
	.cfi_startproc
	cmpl	$1, %ecx
	movl	8(%rsi), %r9d
	movl	(%rsi), %r8d
	sbbl	%ecx, %ecx
	movl	$.LC0, %esi
	xorl	%eax, %eax
	andl	$16, %ecx
	addl	$42, %ecx
	jmp	fprintf
	.cfi_endproc
.LFE35:
	.size	do_dump_outcome, .-do_dump_outcome
	.section	.rodata.str1.8,"aMS",@progbits,1
	.align 8
.LC1:
	.string	"sb-iwp2.3.a-amd4, check_globals failed"
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
	movq	56(%rdi), %rax
	movq	(%rdi), %r14
	movq	8(%rdi), %r13
	movl	4(%rax), %eax
	testl	%eax, %eax
	jle	.L8
	subl	$1, %eax
	leaq	48(%rdi), %rbp
	xorl	%ebx, %ebx
	movl	%eax, %r12d
	cltq
	salq	$2, %rax
	notq	%r12
	salq	$2, %r12
	addq	%rax, %r14
	addq	%rax, %r13
	jmp	.L9
	.p2align 4,,10
	.p2align 3
.L6:
	movq	%rbp, %rdi
	call	rand_bit
	testl	%eax, %eax
	je	.L7
	movl	0(%r13,%rbx), %eax
	testl	%eax, %eax
	jne	.L18
.L7:
	subq	$4, %rbx
	cmpq	%r12, %rbx
	je	.L8
.L9:
	movq	%rbp, %rdi
	call	rand_bit
	testl	%eax, %eax
	je	.L6
	movl	(%r14,%rbx), %edx
	testl	%edx, %edx
	je	.L6
	movl	$.LC1, %edi
	call	fatal
	jmp	.L6
	.p2align 4,,10
	.p2align 3
.L18:
	movl	$.LC1, %edi
	subq	$4, %rbx
	call	fatal
	cmpq	%r12, %rbx
	jne	.L9
	.p2align 4,,10
	.p2align 3
.L8:
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
	.p2align 4,,15
	.type	P1, @function
P1:
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
# 40 "sb.c" 1
	mfence
# 0 "" 2
#NO_APP
	movq	8(%rdi), %rbx
	movq	%rbx, %rdi
	call	check_globals
	movq	56(%rbx), %rax
	movl	0(%rbp), %r10d
	movq	40(%rbx), %r9
	movq	24(%rbx), %r8
	movl	4(%rax), %esi
	subl	$1, %esi
	movslq	%esi, %rcx
	salq	$2, %rcx
	testl	%esi, %esi
	js	.L24
	.p2align 4,,10
	.p2align 3
.L28:
	movl	%esi, %eax
	leaq	(%r9,%rcx), %rdx
	andl	$1, %eax
	cmpl	%r10d, %eax
	je	.L33
	.p2align 4,,10
	.p2align 3
.L29:
	movl	(%rdx), %eax
	testl	%eax, %eax
	je	.L29
.L22:
	movq	8(%rbx), %rdx
	movq	(%rbx), %rdi
#APP
# 250 "sb.c" 1
	
#START _litmus_P1
#_litmus_P1_0
	movl $1,(%rdi,%rcx)
#_litmus_P1_1
	movl (%rdx,%rcx),%eax
#END _litmus_P1
	
# 0 "" 2
#NO_APP
	subl	$1, %esi
	movl	%eax, (%r8,%rcx)
	subq	$4, %rcx
	cmpl	$-1, %esi
	jne	.L28
.L24:
#APP
# 40 "sb.c" 1
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
.L33:
	.cfi_restore_state
	movl	$1, (%rdx)
	jmp	.L22
	.cfi_endproc
.LFE42:
	.size	P1, .-P1
	.section	.rodata.str1.1
.LC4:
	.string	"%lf %lf\n"
	.text
	.p2align 4,,15
	.type	P0, @function
P0:
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
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	movq	%rdi, %rbx
	subq	$72, %rsp
	.cfi_def_cfa_offset 128
#APP
# 40 "sb.c" 1
	mfence
# 0 "" 2
#NO_APP
	movq	8(%rdi), %r12
	movq	%r12, %rdi
	call	check_globals
	movq	56(%r12), %rax
	movl	(%rbx), %r13d
	movq	40(%r12), %r14
	movq	16(%r12), %r15
	movl	4(%rax), %ebp
	subl	$1, %ebp
	js	.L40
	xorpd	%xmm4, %xmm4
	movslq	%ebp, %rbx
	salq	$2, %rbx
	movsd	%xmm4, 8(%rsp)
	movsd	%xmm4, (%rsp)
	.p2align 4,,10
	.p2align 3
.L39:
	leaq	16(%rsp), %rsi
	movl	$4, %edi
	call	clock_gettime
	movl	%ebp, %eax
	leaq	(%r14,%rbx), %rdx
	andl	$1, %eax
	cmpl	%r13d, %eax
	je	.L46
	.p2align 4,,10
	.p2align 3
.L43:
	movl	(%rdx), %eax
	testl	%eax, %eax
	je	.L43
.L37:
	leaq	32(%rsp), %rsi
	movl	$4, %edi
	call	clock_gettime
	movq	8(%r12), %rdx
	movq	(%r12), %rcx
#APP
# 218 "sb.c" 1
	
#START _litmus_P0
#_litmus_P0_0
	movl $1,(%rdx,%rbx)
#_litmus_P0_1
	movl (%rcx,%rbx),%eax
#END _litmus_P0
	
# 0 "" 2
#NO_APP
	leaq	48(%rsp), %rsi
	movl	%eax, (%r15,%rbx)
	movl	$4, %edi
	subl	$1, %ebp
	subq	$4, %rbx
	call	clock_gettime
	cvtsi2sdq	40(%rsp), %xmm0
	cvtsi2sdq	24(%rsp), %xmm2
	divsd	.LC3(%rip), %xmm0
	cvtsi2sdq	32(%rsp), %xmm1
	cmpl	$-1, %ebp
	divsd	.LC3(%rip), %xmm2
	addsd	%xmm0, %xmm1
	cvtsi2sdq	16(%rsp), %xmm0
	movapd	%xmm1, %xmm3
	addsd	%xmm2, %xmm0
	cvtsi2sdq	56(%rsp), %xmm2
	divsd	.LC3(%rip), %xmm2
	subsd	%xmm0, %xmm3
	movsd	(%rsp), %xmm0
	addsd	%xmm3, %xmm0
	movsd	%xmm0, (%rsp)
	cvtsi2sdq	48(%rsp), %xmm0
	addsd	%xmm2, %xmm0
	subsd	%xmm1, %xmm0
	addsd	8(%rsp), %xmm0
	movsd	%xmm0, 8(%rsp)
	jne	.L39
.L35:
#APP
# 40 "sb.c" 1
	mfence
# 0 "" 2
#NO_APP
	movsd	8(%rsp), %xmm1
	movl	$.LC4, %edi
	movsd	(%rsp), %xmm0
	movl	$2, %eax
	call	printf
	addq	$72, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	xorl	%eax, %eax
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
.L46:
	.cfi_restore_state
	movl	$1, (%rdx)
	jmp	.L37
.L40:
	xorpd	%xmm5, %xmm5
	movsd	%xmm5, 8(%rsp)
	movsd	%xmm5, (%rsp)
	jmp	.L35
	.cfi_endproc
.LFE41:
	.size	P0, .-P0
	.section	.rodata.str1.1
.LC5:
	.string	"Run %i of %i\r"
	.text
	.p2align 4,,15
	.type	zyva, @function
zyva:
.LFB43:
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
	subq	$168, %rsp
	.cfi_def_cfa_offset 224
	movq	16(%rdi), %rbp
	movq	8(%rdi), %rdi
	call	pb_wait
	movl	$24, %edi
	movq	$P0, 32(%rsp)
	movq	$P1, 40(%rsp)
	call	malloc_check
	movslq	4(%rbp), %rbx
	movq	$0, (%rax)
	movq	%rax, %r14
	movq	$0, 16(%rax)
	movq	$0, 8(%rax)
	movq	%rbp, 152(%rsp)
	call	rand
	salq	$2, %rbx
	movl	%eax, 144(%rsp)
	movq	%rbx, %rdi
	call	malloc_check
	movq	%rbx, %rdi
	movq	%rax, 112(%rsp)
	call	malloc_check
	movq	%rbx, %rdi
	movq	%rax, 120(%rsp)
	call	malloc_check
	movq	%rbx, %rdi
	movq	%rax, 96(%rsp)
	call	malloc_check
	movl	$2, %edi
	movq	%rax, 104(%rsp)
	call	pb_create
	movq	%rbx, %rdi
	movq	%rax, 128(%rsp)
	call	malloc_check
	movl	8(%rbp), %ecx
	movq	%rax, 136(%rsp)
	leaq	96(%rsp), %rax
	movl	$1, 80(%rsp)
	movl	$0, 64(%rsp)
	movq	%rax, 88(%rsp)
	movq	%rax, 72(%rsp)
	testl	%ecx, %ecx
	jle	.L58
	leaq	144(%rsp), %rax
	leaq	80(%rsp), %r13
	xorl	%r12d, %r12d
	movq	%rax, 8(%rsp)
	.p2align 4,,10
	.p2align 3
.L64:
	cmpl	$1, 0(%rbp)
	jle	.L49
	movq	stderr(%rip), %rdi
	movl	%r12d, %edx
	movl	$.LC5, %esi
	xorl	%eax, %eax
	call	fprintf
.L49:
	movq	152(%rsp), %rax
	movl	4(%rax), %edx
	subl	$1, %edx
	js	.L53
	movl	%edx, %r11d
	movslq	%edx, %rdx
	xorl	%ecx, %ecx
	salq	$2, %rdx
	notq	%r11
	movq	%rdx, %r10
	movq	%rdx, %r8
	movq	%rdx, %rdi
	movq	%rdx, %rsi
	addq	96(%rsp), %r10
	addq	104(%rsp), %r8
	addq	112(%rsp), %rdi
	addq	120(%rsp), %rsi
	salq	$2, %r11
	addq	136(%rsp), %rdx
	.p2align 4,,10
	.p2align 3
.L54:
	movl	$0, (%r10,%rcx)
	leaq	(%rcx,%rdx), %rax
	movl	$0, (%r8,%rcx)
	movl	$-239487, (%rdi,%rcx)
	movl	$-239487, (%rsi,%rcx)
	subq	$4, %rcx
	cmpq	%r11, %rcx
	movl	$0, (%rax)
	jne	.L54
.L53:
	movl	12(%rbp), %edx
	testl	%edx, %edx
	jne	.L68
.L52:
	movq	40(%rsp), %rsi
	leaq	24(%rsp), %rdi
	movq	%r13, %rdx
	call	launch
	movq	32(%rsp), %rsi
	leaq	64(%rsp), %rdx
	leaq	16(%rsp), %rdi
	call	launch
	movl	12(%rbp), %eax
	testl	%eax, %eax
	jne	.L69
.L55:
	leaq	24(%rsp), %rdi
	call	join
	leaq	16(%rsp), %rdi
	call	join
	movl	4(%rbp), %eax
	subl	$1, %eax
	js	.L62
	movslq	%eax, %rdx
	movl	%eax, %eax
	leaq	0(,%rdx,4), %rbx
	subq	%rax, %rdx
	leaq	-4(,%rdx,4), %r15
	jmp	.L63
	.p2align 4,,10
	.p2align 3
.L70:
	testl	%edx, %edx
	jne	.L59
	movq	(%r14), %rdi
	leaq	48(%rsp), %rsi
	movl	$1, %r8d
	movl	$1, %ecx
	movl	$2, %edx
	subq	$4, %rbx
	movq	$0, 48(%rsp)
	movq	$0, 56(%rsp)
	call	add_outcome_outs
	addq	$1, 8(%r14)
	cmpq	%r15, %rbx
	movq	%rax, (%r14)
	je	.L62
.L63:
	movq	112(%rsp), %rax
	movq	120(%rsp), %rdx
	movslq	(%rax,%rbx), %rax
	movslq	(%rdx,%rbx), %rdx
	testl	%eax, %eax
	je	.L70
.L59:
	movq	(%r14), %rdi
	leaq	48(%rsp), %rsi
	movq	%rdx, 56(%rsp)
	xorl	%r8d, %r8d
	movl	$1, %ecx
	movl	$2, %edx
	subq	$4, %rbx
	movq	%rax, 48(%rsp)
	call	add_outcome_outs
	addq	$1, 16(%r14)
	cmpq	%r15, %rbx
	movq	%rax, (%r14)
	jne	.L63
.L62:
	movl	8(%rbp), %ecx
	addl	$1, %r12d
	cmpl	%r12d, %ecx
	jg	.L64
.L58:
	movq	96(%rsp), %rdi
	call	free
	movq	104(%rsp), %rdi
	call	free
	movq	112(%rsp), %rdi
	call	free
	movq	120(%rsp), %rdi
	call	free
	movq	128(%rsp), %rdi
	call	pb_free
	movq	136(%rsp), %rdi
	call	free
	addq	$168, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	movq	%r14, %rax
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
.L68:
	.cfi_restore_state
	movq	8(%rsp), %rdi
	leaq	32(%rsp), %rsi
	movl	$2, %edx
	call	perm_funs
	jmp	.L52
	.p2align 4,,10
	.p2align 3
.L69:
	movq	8(%rsp), %rdi
	leaq	16(%rsp), %rsi
	movl	$2, %edx
	call	perm_threads
	jmp	.L55
	.cfi_endproc
.LFE43:
	.size	zyva, .-zyva
	.section	.rodata.str1.1
.LC6:
	.string	"Never"
.LC7:
	.string	"Sometimes"
.LC8:
	.string	"Always"
	.section	.rodata.str1.8
	.align 8
.LC9:
	.string	"sb-iwp2.3.a-amd4: n=%i, r=%i, s=%i"
	.section	.rodata.str1.1
.LC10:
	.string	"\n"
.LC11:
	.string	"sb-iwp2.3.a-amd4, sum_hist"
	.section	.rodata.str1.8
	.align 8
.LC12:
	.string	"Test sb-iwp2.3.a-amd4 Allowed\n"
	.section	.rodata.str1.1
.LC13:
	.string	"Histogram (%i states)\n"
	.section	.rodata.str1.8
	.align 8
.LC14:
	.string	"Observation sb-iwp2.3.a-amd4 %s %lu %lu\n"
	.section	.rodata.str1.1
.LC16:
	.string	"Time sb-iwp2.3.a-amd4 %.2f\n"
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
	.string	"Hash=edd4722437d708675ed921e7607e77f0\n"
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
.LFB46:
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
	subq	$328, %rsp
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
	movq	%rax, -328(%rbp)
	call	timeofday
	movl	-60(%rbp), %esi
	movq	%rax, -344(%rbp)
	movl	-152(%rbp), %ecx
	movl	-160(%rbp), %eax
	movl	-156(%rbp), %edx
	movl	$1, -292(%rbp)
	testl	%esi, %esi
	movl	%eax, -304(%rbp)
	movl	%ecx, -300(%rbp)
	movl	%edx, -296(%rbp)
	je	.L72
	movl	$0, -292(%rbp)
.L72:
	movl	-140(%rbp), %ebx
	movl	-144(%rbp), %esi
	testl	%ebx, %ebx
	jle	.L102
.L73:
	testl	%eax, %eax
	jne	.L103
.L74:
	leal	-1(%rbx), %eax
	xorl	%r12d, %r12d
	xorl	%r15d, %r15d
	movl	%eax, -312(%rbp)
	cltq
	leaq	22(,%rax,8), %rax
	andq	$-16, %rax
	subq	%rax, %rsp
	movslq	%ebx, %rax
	movq	%rax, -352(%rbp)
	leaq	(%rax,%rax,2), %rax
	movq	%rsp, %r13
	movq	%rsp, -368(%rbp)
	leaq	22(,%rax,8), %rax
	andq	$-16, %rax
	subq	%rax, %rsp
	call	pm_create
	movl	%ebx, %edi
	movq	%rax, -320(%rbp)
	call	pb_create
	movq	%r12, -336(%rbp)
	movq	%rax, -360(%rbp)
	movl	%r15d, %r12d
	movq	%rax, %r15
	movq	%r13, %rax
	movq	%rsp, %r13
	movq	%rax, %r14
	.p2align 4,,10
	.p2align 3
.L78:
	leaq	-304(%rbp), %rax
	cmpl	%r12d, -312(%rbp)
	movq	%r15, 8(%r13)
	movq	%rax, 16(%r13)
	movq	-320(%rbp), %rax
	movq	%rax, 0(%r13)
	jle	.L75
	movq	%r13, %rdx
	movl	$zyva, %esi
	movq	%r14, %rdi
	call	launch
.L76:
	addl	$1, %r12d
	addq	$24, %r13
	addq	$8, %r14
	cmpl	%r12d, %ebx
	jg	.L78
	movslq	-300(%rbp), %rax
	movslq	-296(%rbp), %r14
	movq	-336(%rbp), %r12
	imulq	%rax, %r14
	movl	-312(%rbp), %eax
	testl	%eax, %eax
	je	.L84
	leal	-2(%rbx), %eax
	xorl	%r13d, %r13d
	leaq	8(,%rax,8), %r15
	movq	%r15, -312(%rbp)
	movq	-368(%rbp), %r15
	.p2align 4,,10
	.p2align 3
.L85:
	leaq	(%r15,%r13), %rdi
	call	join
	movq	(%rax), %rdi
	movq	%rax, %rbx
	call	sum_outs
	cmpq	%rax, %r14
	jne	.L82
	movq	8(%rbx), %rdx
	movq	16(%rbx), %rax
	leaq	(%rax,%rdx), %rcx
	cmpq	%rcx, %r14
	je	.L83
.L82:
	movl	$.LC11, %edi
	call	fatal
	movq	8(%rbx), %rdx
	movq	16(%rbx), %rax
.L83:
	addq	%rdx, 8(%r12)
	addq	%rax, 16(%r12)
	movl	$2, %edx
	movq	(%rbx), %rsi
	movq	(%r12), %rdi
	addq	$8, %r13
	call	merge_outs
	movq	%rax, (%r12)
	movq	(%rbx), %rdi
	call	free_outs
	movq	%rbx, %rdi
	call	free
	cmpq	-312(%rbp), %r13
	jne	.L85
.L84:
	call	timeofday
	movq	-320(%rbp), %rdi
	movq	%rax, %rbx
	subq	-344(%rbp), %rbx
	call	pm_free
	movq	-360(%rbp), %rdi
	call	pb_free
	imulq	-352(%rbp), %r14
	movq	(%r12), %rdi
	call	sum_outs
	cmpq	%rax, %r14
	je	.L104
.L80:
	movl	$.LC11, %edi
	call	fatal
	movq	8(%r12), %r15
	movq	16(%r12), %r13
.L86:
	movq	-328(%rbp), %r14
	movl	$30, %edx
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
	leaq	-288(%rbp), %rcx
	movl	$2, %r8d
	movl	$do_dump_outcome, %esi
	movq	%r14, %rdi
	call	dump_outs
	testq	%r15, %r15
	je	.L105
	movq	-328(%rbp), %r14
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
.L91:
	movq	-328(%rbp), %rdi
	xorl	%eax, %eax
	movq	%r13, %r8
	movq	%r15, %rcx
	movl	$.LC14, %esi
	call	fprintf
	testq	%rbx, %rbx
	js	.L89
	cvtsi2sdq	%rbx, %xmm0
.L90:
	divsd	.LC15(%rip), %xmm0
	movq	-328(%rbp), %rbx
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
.L105:
	.cfi_restore_state
	movq	-328(%rbp), %r14
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
	jmp	.L91
.L104:
	movq	8(%r12), %r15
	movq	16(%r12), %r13
	leaq	0(%r13,%r15), %rax
	cmpq	%rax, %r14
	jne	.L80
	jmp	.L86
.L103:
	movl	%ebx, %esi
	movl	$.LC9, %edi
	xorl	%eax, %eax
	call	log_error
	movl	$.LC10, %edi
	xorl	%eax, %eax
	call	log_error
	jmp	.L74
.L102:
	cmpl	$1, %esi
	jle	.L93
	sarl	%esi
	movl	%esi, %ebx
	.p2align 4,,4
	jmp	.L73
.L89:
	movq	%rbx, %rax
	andl	$1, %ebx
	shrq	%rax
	orq	%rbx, %rax
	cvtsi2sdq	%rax, %xmm0
	addsd	%xmm0, %xmm0
	jmp	.L90
.L93:
	movl	$1, %ebx
	jmp	.L73
.L75:
	movq	%r13, %rdi
	call	zyva
	movq	%rax, -336(%rbp)
	jmp	.L76
	.cfi_endproc
.LFE46:
	.size	main, .-main
	.section	.rodata.cst8,"aM",@progbits,8
	.align 8
.LC3:
	.long	0
	.long	1104006501
	.align 8
.LC15:
	.long	0
	.long	1093567616
	.ident	"GCC: (GNU) 4.8.5 20150623 (Red Hat 4.8.5-36)"
	.section	.note.GNU-stack,"",@progbits
