// push constant 3000
@3000
D = A
@SP
A = M
M = D
@SP
M = M + 1
// pop pointer 0
@THIS
D = A
@SP
M = M - 1
@R13
M = D
@SP
A = M
D = M
@R13
A = M
M = D
// push constant 5
@5
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push pointer 0
@THIS
D = M
@SP
A = M
M = D
@SP
M = M + 1
