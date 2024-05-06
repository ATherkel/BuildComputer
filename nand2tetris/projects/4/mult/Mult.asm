// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.


// max(R0, R1) + ... + MAX(R0,R1)
// min(R0, R1) times
// Store in R2

@R2
M = 0 // Initialize sum

// Find min
    @R0
    D = M
    @END
    D; JEQ // Stop script if R0 = 0
    @R1
    D = M
    @END
    D; JEQ // Stop if R1 = 0
    D = D - M
    @MINR0
    D ; JLT // D < 0 <=> R0 < R1
    
    @R1
    D = M
    @min
    M = 1 // set variable min = R1
    @max
    M = 0 // set var max = R0
    @INITI
    0; JMP
        

(MINR0)
    @R0
    D = M
    @min
    M = 0
    @max
    M = 1 // set variable min = R1 (min is a pointer)
    

(INITI)
@i
M = D // Initialize i = min(R0, R1) (call i = Rx)


(LOOP)
    @max
    A = M
    D = M
    @R2
    M = D + M // R2 = R2 + max(R0, R1)
    
    // i--
    @i
    M = M - 1
    D = M
    @LOOP
    D ; JGT


(END)
@END
    0 ; JMP
    
