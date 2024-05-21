// push constant 10
@10
D = A
@SP
A = M
M = D
@SP
M = M + 1
// pop local 2
@2
D = A
@LCL
D = D + A
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
