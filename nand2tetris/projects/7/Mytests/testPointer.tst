
load testPointer.asm,

set RAM[0] 256,   // initializes the stack pointer

repeat 450 {      // enough cycles to complete the execution
  ticktock;
}
