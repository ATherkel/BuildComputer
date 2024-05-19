load testPush.vm,

set sp 256,        // stack pointer
set local 300,     // base address of the local segment
set argument 400,  // base address of the argument segment
set this 3000,     // base address of the this segment
set that 3010,     // base address of the that segment

repeat 7 {        // testPush.vm has 25 VM commands
  vmstep;
}
