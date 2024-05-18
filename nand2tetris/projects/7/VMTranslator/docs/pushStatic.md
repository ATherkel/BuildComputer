`push static i`
----

For `static` we set `index = "Filename.i"`, hence all we have to do is `D <- Filename.i`. 

This also means `push static i` is equivalent to `push segment i` documented in [`pushSegment.md`](pushSegment.md). 

Output
----

```
D <- i                   # D_eq_i.asm
RAM[SP] <- RAM[D]        # RAM_SP_eq_RAM_D.asm
SP++                     # SPpp.asm
```