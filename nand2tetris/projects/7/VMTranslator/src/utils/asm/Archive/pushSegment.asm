// ---- push {segment} {index} ----

// addr = segment + i, *SP = *addr, SP++

// If segment is constant: 
//  addr <- i
// If segment is static:
//  addr <- i
// Else:
//  addr <- segmentPointer + i


// i or file.i
@{index}


// if segment not in ["constant", "static"]:
// D = A
// @{segmentPointer}
// A = D + A

// if segment == "constant":
//  D = A
// else:
// D = RAM[addr]
// D = M


// RAM[SP] = RAM[addr]
@SP
A = M
M = D

// SP++
@SP
M = M + 1