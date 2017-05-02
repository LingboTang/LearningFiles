	.file	"BFS.cpp"
	.text
	.align 2
	.globl	_ZN5GraphC2Ei
	.type	_ZN5GraphC2Ei, @function
_ZN5GraphC2Ei:
.LFB1081:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	subq	$8, %rsp
	.cfi_def_cfa_offset 32
	movq	%rdi, %rbp
	movl	%esi, (%rdi)
	movslq	%esi, %rbx
	movq	$-1, %rdi
	movabsq	$571957152676052992, %rax
	cmpq	%rax, %rbx
	ja	.L2
	movq	%rbx, %rdi
	salq	$4, %rdi
	addq	$8, %rdi
.L2:
	call	_Znam
	movq	%rbx, (%rax)
	leaq	8(%rax), %rdx
	testq	%rbx, %rbx
	je	.L3
	leaq	-2(%rbx), %rsi
.L4:
	movq	%rdx, (%rdx)
	movq	%rdx, 8(%rdx)
	subq	$1, %rsi
	addq	$16, %rdx
	cmpq	$-2, %rsi
	jne	.L4
.L3:
	addq	$8, %rax
	movq	%rax, 8(%rbp)
	addq	$8, %rsp
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE1081:
	.size	_ZN5GraphC2Ei, .-_ZN5GraphC2Ei
	.globl	_ZN5GraphC1Ei
	.set	_ZN5GraphC1Ei,_ZN5GraphC2Ei
	.align 2
	.globl	_ZN5Graph7addEdgeEii
	.type	_ZN5Graph7addEdgeEii, @function
_ZN5Graph7addEdgeEii:
.LFB1083:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	subq	$8, %rsp
	.cfi_def_cfa_offset 32
	movl	%edx, %ebp
	movslq	%esi, %rbx
	salq	$4, %rbx
	addq	8(%rdi), %rbx
	movl	$24, %edi
	call	_Znwm
	cmpq	$-16, %rax
	je	.L8
	movl	%ebp, 16(%rax)
.L8:
	movq	%rbx, %rsi
	movq	%rax, %rdi
	call	_ZNSt8__detail15_List_node_base7_M_hookEPS0_
	addq	$8, %rsp
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE1083:
	.size	_ZN5Graph7addEdgeEii, .-_ZN5Graph7addEdgeEii
	.section	.text._ZNSt10_List_baseIiSaIiEE8_M_clearEv,"axG",@progbits,_ZNSt10_List_baseIiSaIiEE8_M_clearEv,comdat
	.align 2
	.weak	_ZNSt10_List_baseIiSaIiEE8_M_clearEv
	.type	_ZNSt10_List_baseIiSaIiEE8_M_clearEv, @function
_ZNSt10_List_baseIiSaIiEE8_M_clearEv:
.LFB1114:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	subq	$8, %rsp
	.cfi_def_cfa_offset 32
	movq	%rdi, %rax
	movq	(%rdi), %rdi
	movq	%rax, %rbp
	cmpq	%rax, %rdi
	je	.L10
.L12:
	movq	(%rdi), %rbx
	call	_ZdlPv
	cmpq	%rbp, %rbx
	je	.L10
	movq	%rbx, %rdi
	jmp	.L12
.L10:
	addq	$8, %rsp
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE1114:
	.size	_ZNSt10_List_baseIiSaIiEE8_M_clearEv, .-_ZNSt10_List_baseIiSaIiEE8_M_clearEv
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	" "
	.text
	.align 2
	.globl	_ZN5Graph3BFSEi
	.type	_ZN5Graph3BFSEi, @function
_ZN5Graph3BFSEi:
.LFB1084:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA1084
	pushq	%r14
	.cfi_def_cfa_offset 16
	.cfi_offset 14, -16
	pushq	%r13
	.cfi_def_cfa_offset 24
	.cfi_offset 13, -24
	pushq	%r12
	.cfi_def_cfa_offset 32
	.cfi_offset 12, -32
	pushq	%rbp
	.cfi_def_cfa_offset 40
	.cfi_offset 6, -40
	pushq	%rbx
	.cfi_def_cfa_offset 48
	.cfi_offset 3, -48
	subq	$16, %rsp
	.cfi_def_cfa_offset 64
	movq	%rdi, %r12
	movl	%esi, %ebx
	movslq	(%rdi), %rdi
.LEHB0:
	call	_Znam
.LEHE0:
	movq	%rax, %r13
	cmpl	$0, (%r12)
	jle	.L15
	movl	$0, %eax
.L16:
	movslq	%eax, %rdx
	movb	$0, 0(%r13,%rdx)
	addl	$1, %eax
	cmpl	%eax, (%r12)
	jg	.L16
.L15:
	movq	%rsp, (%rsp)
	movq	%rsp, 8(%rsp)
	movslq	%ebx, %rax
	movb	$1, 0(%r13,%rax)
	movl	$24, %edi
.LEHB1:
	call	_Znwm
	cmpq	$-16, %rax
	je	.L17
	movl	%ebx, 16(%rax)
.L17:
	movq	%rsp, %rsi
	movq	%rax, %rdi
	call	_ZNSt8__detail15_List_node_base7_M_hookEPS0_
	movq	%rsp, %r14
	jmp	.L18
.L23:
	movl	16(%rax), %ebp
	movl	%ebp, %esi
	movl	$_ZSt4cout, %edi
	call	_ZNSolsEi
	movl	$1, %edx
	movl	$.LC0, %esi
	movq	%rax, %rdi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movq	(%rsp), %rbx
	movq	%rbx, %rdi
	call	_ZNSt8__detail15_List_node_base9_M_unhookEv
	movq	%rbx, %rdi
	call	_ZdlPv
	movslq	%ebp, %rbp
	salq	$4, %rbp
	movq	%rbp, %rax
	addq	8(%r12), %rax
	movq	(%rax), %rbx
	cmpq	%rbx, %rax
	je	.L18
.L22:
	movslq	16(%rbx), %rdx
	addq	%r13, %rdx
	cmpb	$0, (%rdx)
	jne	.L20
	movb	$1, (%rdx)
	movl	$24, %edi
	call	_Znwm
.LEHE1:
	cmpq	$-16, %rax
	je	.L21
	movl	16(%rbx), %edx
	movl	%edx, 16(%rax)
.L21:
	movq	%r14, %rsi
	movq	%rax, %rdi
	call	_ZNSt8__detail15_List_node_base7_M_hookEPS0_
.L20:
	movq	(%rbx), %rbx
	movq	%rbp, %rax
	addq	8(%r12), %rax
	cmpq	%rax, %rbx
	jne	.L22
.L18:
	movq	(%rsp), %rax
	cmpq	%r14, %rax
	jne	.L23
	movq	%rsp, %rdi
	call	_ZNSt10_List_baseIiSaIiEE8_M_clearEv
	jmp	.L26
.L25:
	movq	%rax, %rbx
	movq	%rsp, %rdi
	call	_ZNSt10_List_baseIiSaIiEE8_M_clearEv
	movq	%rbx, %rdi
.LEHB2:
	call	_Unwind_Resume
.LEHE2:
.L26:
	addq	$16, %rsp
	.cfi_def_cfa_offset 48
	popq	%rbx
	.cfi_def_cfa_offset 40
	popq	%rbp
	.cfi_def_cfa_offset 32
	popq	%r12
	.cfi_def_cfa_offset 24
	popq	%r13
	.cfi_def_cfa_offset 16
	popq	%r14
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE1084:
	.globl	__gxx_personality_v0
	.section	.gcc_except_table,"a",@progbits
.LLSDA1084:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE1084-.LLSDACSB1084
.LLSDACSB1084:
	.uleb128 .LEHB0-.LFB1084
	.uleb128 .LEHE0-.LEHB0
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB1-.LFB1084
	.uleb128 .LEHE1-.LEHB1
	.uleb128 .L25-.LFB1084
	.uleb128 0
	.uleb128 .LEHB2-.LFB1084
	.uleb128 .LEHE2-.LEHB2
	.uleb128 0
	.uleb128 0
.LLSDACSE1084:
	.text
	.size	_ZN5Graph3BFSEi, .-_ZN5Graph3BFSEi
	.section	.rodata.str1.8,"aMS",@progbits,1
	.align 8
.LC1:
	.string	"Following is Breadth First Traversal"
	.section	.rodata.str1.1
.LC2:
	.string	"(Starting from vertex 2) \n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB1085:
	.cfi_startproc
	subq	$24, %rsp
	.cfi_def_cfa_offset 32
	movl	$4, %esi
	movq	%rsp, %rdi
	call	_ZN5GraphC1Ei
	movl	$1, %edx
	movl	$0, %esi
	movq	%rsp, %rdi
	call	_ZN5Graph7addEdgeEii
	movl	$2, %edx
	movl	$0, %esi
	movq	%rsp, %rdi
	call	_ZN5Graph7addEdgeEii
	movl	$2, %edx
	movl	$1, %esi
	movq	%rsp, %rdi
	call	_ZN5Graph7addEdgeEii
	movl	$0, %edx
	movl	$2, %esi
	movq	%rsp, %rdi
	call	_ZN5Graph7addEdgeEii
	movl	$3, %edx
	movl	$2, %esi
	movq	%rsp, %rdi
	call	_ZN5Graph7addEdgeEii
	movl	$3, %edx
	movl	$3, %esi
	movq	%rsp, %rdi
	call	_ZN5Graph7addEdgeEii
	movl	$.LC1, %esi
	movl	$_ZSt4cout, %edi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movl	$.LC2, %esi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movl	$2, %esi
	movq	%rsp, %rdi
	call	_ZN5Graph3BFSEi
	movl	$0, %eax
	addq	$24, %rsp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE1085:
	.size	main, .-main
	.type	_GLOBAL__sub_I__ZN5GraphC2Ei, @function
_GLOBAL__sub_I__ZN5GraphC2Ei:
.LFB1165:
	.cfi_startproc
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	movl	$_ZStL8__ioinit, %edi
	call	_ZNSt8ios_base4InitC1Ev
	movl	$__dso_handle, %edx
	movl	$_ZStL8__ioinit, %esi
	movl	$_ZNSt8ios_base4InitD1Ev, %edi
	call	__cxa_atexit
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE1165:
	.size	_GLOBAL__sub_I__ZN5GraphC2Ei, .-_GLOBAL__sub_I__ZN5GraphC2Ei
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I__ZN5GraphC2Ei
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.hidden	__dso_handle
	.ident	"GCC: (GNU) 4.8.5 20150623 (Red Hat 4.8.5-11)"
	.section	.note.GNU-stack,"",@progbits
