// push constant 2
@2
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push local 3
@3
D = A
@LCL
A = D + A
D = M
@SP
A = M
M = D
@SP
M = M + 1
// push argument 4
@4
D = A
@ARG
A = D + A
D = M
@SP
A = M
M = D
@SP
M = M + 1
// push this 0
@0
D = A
@THIS
A = D + A
D = M
@SP
A = M
M = D
@SP
M = M + 1
// push that 0
@0
D = A
@THAT
A = D + A
D = M
@SP
A = M
M = D
@SP
M = M + 1
// push pointer 0
@0
D = A
@None
A = D + A
D = M
@SP
A = M
M = D
@SP
M = M + 1
// push static 5
@testPush.5
D = A
@SP
A = M
M = D
@SP
M = M + 1
