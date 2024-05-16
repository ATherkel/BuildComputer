// ---- x {action} y ----
// D = *SP
// SP--
// *SP = *SP {action} D
// SP++




// D = *SP
@SP
A = M
D = M

// SP--
@SP
M = M - 1

// Arithmetic operation
// E.g. add: *SP = *SP + D
// E.g. eq: D = *SP - D, D; JEQ
A = M
{action}

// SP++
@SP
M = M + 1

