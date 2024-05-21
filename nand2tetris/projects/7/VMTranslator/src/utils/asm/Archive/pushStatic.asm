// ---- push static {index} ----

// addr = Foo.i, *SP = *addr, SP++

@{index}
D = A

@{segmentPointer}
A = D + A
D = A


// addr <- SegmentPointer + i
@{index}
D = A

// Not used if segment is 'constant'
// @{segmentPointer}
// A = D + M
// D = M

// RAM[SP] = RAM[addr]
@SP
A = M
M = D

// SP++
@SP
M = M + 1