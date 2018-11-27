section .data
	a dd 10
	b dd 20
	msg db "%d",10,0
section .text
	extern printf
	global main
main:
	xor eax,eax
	xor ebx,ebx
	mov eax,dword[a]
	mov ebx,dword[b]
	add eax,ebx
	push eax
	push msg
	call printf
	add esp,8
