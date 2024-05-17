// ---- push {segment} {index} ----

// addr = segment + i, *SP = *addr, SP++


// addr <- SegmentPointer + i
@{index}
D = A

// Not used if segment is 'constant'
//@{segmentPointer}
//A = D + M
//D = M

// RAM[SP] = RAM[addr]
@SP
A = M
M = D

// SP++
@SP
M = M + 1