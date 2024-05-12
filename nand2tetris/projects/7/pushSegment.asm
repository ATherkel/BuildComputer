// ---- push segment i
// addr = segment + i, *SP = *addr, SP++



// addr <- SegmentPointer + i
@i
D = A
@segment
D = D + M

// RAM[SP] = RAM[addr]
@SP
A = M
M = D

// SP++
@SP
M = M + 1