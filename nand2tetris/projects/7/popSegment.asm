// ---- pop segment i
// addr = segment + i, SP--, *addr = *SP
// addr <- segmentPointer + i
@i
D = A
@segment
D = D + M // D = segment + i

// SP--
@SP
M = M - 1

// RAM[addr] <- RAM[SP]
// Store D in THIS
// i.e. *THIS = addr
@THIS
M = D
// D = RAM[SP]
@SP
A = M
D = M
// *THIS 
@THIS
A = M
M = D