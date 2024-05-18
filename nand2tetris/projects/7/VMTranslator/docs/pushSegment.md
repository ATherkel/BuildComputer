`push segment i`
----

where `segment in ["local", "argument", "this", "that"]`

Output
----

```
addr <- segmentPointer + i  # D_eq_RAM_segmentPointer_p_i.asm
D <- RAM[addr]              # ^--
RAM[SP] <- D                # RAM_SP_eq_D.asm
SP++                        # SPpp.asm
```