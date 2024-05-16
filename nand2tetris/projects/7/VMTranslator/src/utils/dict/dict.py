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
    "THIS" : "THIS",
    "THAT" : "THAT",
    "constant" : "CONST",
}
