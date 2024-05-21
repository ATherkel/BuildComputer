// RAM[R13] <- RAM[SP]

// D = RAM[SP]
@SP
A = M
D = M

// RAM[13] <- D
@R13
A = M
M = D