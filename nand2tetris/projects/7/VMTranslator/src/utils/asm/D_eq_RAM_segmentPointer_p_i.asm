// addr <- segmentPointer + i
@{index}
D = A
@{segmentPointer}
A = D + A
// D <- RAM[addr]
D = M