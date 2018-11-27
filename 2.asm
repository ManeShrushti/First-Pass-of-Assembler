;; print from first space to end of string

section .data
	First db "This is the string",0
	Second db "This is another string",0,10
	a dd 10,20
section .bss
	n resd 3
section .text
	global main
main:
	xor ecx,ecx
	mov eax,First
pqr:
	cmp byte[eax],0
	jz xyz
	inc ecx
	inc eax
	jmp pqr
xyz: 
	xor edx,edx
	inc eax
	push eax
abc:
	cmp byte[eax],0
	jz tst
	inc edx
	inc eax
	jmp abc
	
tst:
	pop eax
	mov esi,eax
	mov eax,4
	mov ebx,1
	mov ecx,esi
	int 0x80
