section .text             ;section declaration
global _start             ;when ld creates the object file, it uses _start as the entry point

_start:

mov edx,len               ; third argument - message length
mov ecx,msg               ; second argument - pointer
mov ebx,1                 ; first argument: file handle (stdout)
mov eax,4                 ; system call number (sys_write)
int 0x80                  ; call the kernel

mov edx,len2               ; third argument - message length
mov ecx,msg2               ; second argument - pointer
mov ebx,1                 ; first argument: file handle (stdout)
mov eax,4                 ; system call number (sys_write)
int 0x80                  ; call the kernel

mov ebx,0                 ; these three
mov eax,1                 ; are the
int 0x80                  ; quite sequence

section .data               ;data section - presumably where we keep constant-like things

msg db "Hello World",0xa  ;our dear string - 0xa means \n
len equ $ - msg             ; length??

msg2 db "Strazdvoytye Mundo!",0xa  ;our dear string
len2 equ $ - msg2             ; length??


