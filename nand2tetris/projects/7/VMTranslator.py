## How program is supposed to be run:
# https://www.coursera.org/learn/nand2tetris2/lecture/qmJl3/unit-1-8-vm-translator-proposed-implementation

#### ---- import ----
# https://stackoverflow.com/a/37867717/3560695

import re

# Test packages
import os ## Testing purposes


## Test stuff START

# os.getcwd()


# filename = 'nand2tetris/projects/7/StackArithmetic/SimpleAdd/SimpleAdd.vm'


## Test stuff END




## Read lines method
def readlines(filename : str, comment = "//"):
    """
Returns a list of the lines from an input filename. Removes comments and blank lines.

Parameters
----
filename : str
    File path and file name of file to be read.
comment : str
    Comment identifier.
    """
    import re
    file = open(filename, 'r')
    lines = file.readlines()
    
    ## Remove comments
    re_comment = re.escape(comment)
    # print(re_comment)
    lines_nocomment = [re.sub(r'(\s*'+re_comment+'.*)','',line) for line in lines]
    # print(lines_nocomment)
    ## Remove empty lines
    lines_filtered = [line for line in lines_nocomment if line.strip()]
    # print(lines_filtered)
    return lines_filtered





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