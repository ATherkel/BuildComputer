// RAM[D] <- RAM[SP]
// Store D in R13
// i.e. *R13 = D


@R13
M = D
// D = RAM[SP]
@SP
A = M
D = M
// *R13 
@R13
A = M
M = D