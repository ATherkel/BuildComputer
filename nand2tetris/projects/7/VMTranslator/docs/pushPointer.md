`push pointer i`
----

For `pointer` we get the _address_ pointed to by THIS/THAT.

We translate 
* `pointer 0` to `THIS` and
* `pointer 1` to `THAT`. 

Store it in `segmentPointer`. 

Output
----

```
addr <- segmentPointer      # D_eq_RAM_i.asm
D <- RAM[addr]              # ^--
RAM[SP] <- D                # RAM_SP_eq_D.asm
SP++                        # SPpp.asm
```