// ---- unary action ----
// SP--
// *SP = {action}*SP
// SP++
@SP
M = M - 1

A = M
M = {action}M

@SP
M = M + 1