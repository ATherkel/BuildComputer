## How program is supposed to be run:
# https://www.coursera.org/learn/nand2tetris2/lecture/qmJl3/unit-1-8-vm-translator-proposed-implementation





## Read lines

filename = '/nand2tetris/projects/7/StackArithmetic/SimpleAdd/SimpleAdd.vm'

file = open(filename, 'r')
Lines = file.readlines()





## ---- VM language: ----

## Arithmetic / Logical commands

# add
# sub
# neg
# eq
# gt
# lt
# and
# or
# not

## Memory access commands

# pop <segment> <i>
# push <segment> <i>