// addr <- segmentPointer + i
@{index}
D = A
@{segmentPointer}
A = M
A = D + A
// D <- RAM[addr]
D = M