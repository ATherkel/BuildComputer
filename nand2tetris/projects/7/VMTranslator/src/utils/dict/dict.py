commandType = {
    "push" : "C_PUSH",
    "pop" : "C_POP",
    
    "" : "C_LABEL",
    "" : "C_GOTO",
    "" : "C_IF",
    "" : "C_FUNCTION",
    "" : "C_RETURN",
    "" : "C_CALL",

    "add" : "C_ARITHMETIC",
    "sub" : "C_ARITHMETIC",
    "neg" : "C_ARITHMETIC",
    "eq" : "C_ARITHMETIC",
    "gt" : "C_ARITHMETIC",
    "lt" : "C_ARITHMETIC",
    "and" : "C_ARITHMETIC",
    "or" : "C_ARITHMETIC",
    "not" : "C_ARITHMETIC"
}
    
segment = {
    "local" : "LCL",
    "argument" : "ARG",
    "this" : "THIS",
    "that" : "THAT",

    "temp" : 5,
}

arithmetic = {
    "neg" : 1,
    "not" : 1,

    "add" : 2,
    "sub" : 2,
    "eq"  : 2,
    "gt"  : 2,
    "lt"  : 2,
    "and" : 2,
    "or"  : 2,
}

arithmetic_action = {
    "neg" : "-", # M = -M
    "not" : "!", # M = !M

    "add" : "M = M + D",
    "sub" : "M = M - D",
    "eq"  : "JEQ",
    "gt"  : "JGT",
    "lt"  : "JLT",
    "and" : "M = M & D",
    "or"  : "M = M | D",
}

compare_action = """
D = M - D
@TRUE{self.arithmeticNo}
D; {action}
D = 0
@SP
A = M
M = D
@CONTINUE{self.arithmeticNo}
0; JMP
(TRUE{self.arithmeticNo})
D = -1
@SP
A = M
M = D
(CONTINUE{self.arithmeticNo})
""".strip()



"""
    "R13" : 13,
    "R14" : 14,
    "constant" : "CONST",
"""