.data
	ssn DWORD 000h
	syscallAddr QWORD 000h

.code
	StageSyscall PROC
		mov ssn, ecx
		ret
	StageSyscall ENDP

	PerformSyscall PROC
		mov r10, rcx
		mov eax, ssn
		syscall
		ret
	PerformSyscall ENDP
End
