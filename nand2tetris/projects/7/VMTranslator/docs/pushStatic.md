`push static i`
----

<<<<<<< Updated upstream
For `static` we set `index = "Filename.i"`, hence all we have to do is `D <- Filename.i`. 

This also means `push static i` is equivalent to `push segment i` documented in [`pushSegment.md`](pushSegment.md). 
=======
For `static` we set `index = "filename.i"`, hence what we have to do is `D <- RAM[filename.i]`. 
>>>>>>> Stashed changes

Output
----

```
<<<<<<< Updated upstream
D <- i                   # D_eq_i.asm
RAM[SP] <- RAM[D]        # RAM_SP_eq_RAM_D.asm
SP++                     # SPpp.asm
=======
addr <- i                   # D_eq_RAM_i.asm
D <- RAM[addr]              # ^--
RAM[SP] <- D                # RAM_SP_eq_D.asm
SP++                        # SPpp.asm
>>>>>>> Stashed changes
```