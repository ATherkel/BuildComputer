// ---- add ----
// D = *SP
// SP--
// *SP = *SP + D
// SP++




// D = *SP
@SP
A = M
D = M

// SP--
@SP
M = M - 1

// *SP = *SP + D
A = M
M = D + M

// SP++
@SP
M = M + 1

