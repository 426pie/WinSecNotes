Goal

Simple Token Impersonation. User provides a PID and a EXE filepath. This program duplicates the tokens from the PID process, and starts the EXE program using those duplcated tokens. 

Note that these are POC and do not have robust error checking. Failures could be caused if this program doesn't have permissions to OpenProcess the given PID or execute the EXE filepath.

Build

cl ImpersonateToken.c
