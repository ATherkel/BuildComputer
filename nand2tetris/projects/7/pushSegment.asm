// ---- push {segment} {index} ----

// addr = segment + i, *SP = *addr, SP++


// addr <- SegmentPointer + i
@{index}
D = A
@{segmentPointer}
D = D + M

// RAM[SP] = RAM[addr]
@SP
A = M
M = D

// SP++
@SP
M = M + 1