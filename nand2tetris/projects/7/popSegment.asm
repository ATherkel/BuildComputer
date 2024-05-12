//-- pop {segment} {index} ----
// addr = segment + i, SP--, *addr = *SP

// addr <- segmentPointer + i
@{index}
D = A
@{segmentPointer}
D = D + M // D = segment + i

// SP--
@SP
M = M - 1

// RAM[addr] <- RAM[SP]
// Store D in R13
// i.e. *R13 = addr
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