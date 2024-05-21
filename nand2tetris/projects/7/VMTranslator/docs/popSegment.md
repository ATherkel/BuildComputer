`pop segment i`
----

where `segment in ["local", "argument", "this", "that"]`.

We cannot actually directly store `RAM[SP]` in `RAM[D]`, since we have to store `RAM[SP]` in `D`. 
So, intermediately, we store `RAM[D]` in `R13`, then retrieve `RAM[SP]` in `D` and finish.

Output
----

```
D <- segmentPointer + i  # D_eq_segmentPointer_p_i.asm
SP--                     # SPmm.asm
R13 <- D                 # R13_eq_D.asm
RAM[R13] <- RAM[SP]      # RAM_R13_eq_RAM_SP.asm
```