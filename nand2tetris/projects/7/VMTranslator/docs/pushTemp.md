`push temp i`
----

`RAM[SP] <- RAM[temp + i]`

temp is realized as 5 in the Hack language, so
`RAM[SP] <- RAM[5 + i]`

In the function `writePushPop` we do this by setting `i = temp + i`:
```
i += 5 + i
```

So the final version must be:

Output
----
```
D = i                    # D_eq_i.asm
RAM[SP] <- RAM[D]        # RAM_SP_eq_RAM_D.asm
SP++                     # SPpp.asm
```