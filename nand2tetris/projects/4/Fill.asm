// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.


// Set nscr to number of addresses on screen
@8192
D = A
@nscr
M = D


// Set pSCREEN to address of SCREEN
@SCREEN
D = A
@pSCREEN
M = D


(CHECKKBD)
//  if (KBD != 0) then do
//      col = -1
//      lastkbd = 1
//      goto COLSCREEN
//  end
//  else // (KBD = 0) do
//      if lastkbd = 0 then
//          goto CHECKKBD
//      else // (lastkbd != 0) do
//          lastkbd = 0
//          col = 0
//          i = 0
//          goto COLSCREEN
//      end
//  end


//  if (KBD != 0) then do
//      col = -1
//      lastkbd = 1
//      goto COLSCREEN
    @KBD
    D = M
    @KBDINACTIVE
    D ; JEQ
// If KBD = 0 then go to KBDINACTIVE

// Here KBD != 0

    @col
    M = -1
    @lastkbd
    M = -1
    @i
    M = 0
    
        // if first address same 
        // color as coloring, 
        // assume we have already colored.
        // Then exit loop.
        // if col = SCREEN then goto CHECKKBD
        @col
        D = M
        @SCREEN
        D = D - M
        @CHECKKBD
        D ; JEQ
        
    @COLSCREEN
    0 ; JMP


(KBDINACTIVE)
    @lastkbd
    D = M
    @CHECKKBD
    D; JEQ
    // Else (lastkbd != 0)
    @lastkbd
    M = 0
    @col
    M = 0
    @i
    M = 0
    @COLSCREEN
    0 ; JMP






(initi)
    // Initialize i = 0
    @i
    M = 0
    @COLSCREEN
    0; JMP

(COLSCREEN)
    //  if (i = nscr) goto CHECKKBD
    @i
    D = M
    @nscr
    D = D - M
    @CHECKKBD
    D ; JEQ
    // endif (i = nscr)
    
    // (i < nscr)
    // Do instruction
    // RAM[pSCREEN + i] = col
    @pSCREEN
    D = M
    @i
    D = D + M
    // Store current location
    @curloc
    M = D
    // Get pixel color to D register
    @col
    D = M
    @curloc
    A = M
    // Actually color pixel
    M = D
    
    
    // i++
    @i
    M = M + 1
    
    @COLSCREEN
    0; JMP
// End colscreen loop



(END)
    @END
    0;JMP