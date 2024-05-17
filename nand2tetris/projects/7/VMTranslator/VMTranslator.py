## How the program is supposed to be run:
# https://www.coursera.org/learn/nand2tetris2/lecture/qmJl3/unit-1-8-vm-translator-proposed-implementation


#### ---- import ----
# https://stackoverflow.com/a/37867717/3560695

import re
import sys

## Import parser
## We have to use import_module since the path contains an illegal directory name (7). 
# parser_module = importlib.import_module("src.parser.parser")
import src.parser.parser as p

# writer_module = importlib.import_module("src.codewriter.codewriter")
import src.codewriter.codewriter as cw


#### ---- main ----

#def main():


def main(filename = None):

    if filename is None:
        # Check if the correct number of command-line arguments are provided
        if len(sys.argv) != 2:
            print("Usage: py VMTranslator.py <filename>")
            return
        filename = sys.argv[1]
    
    ## https://regex101.com/r/x0v99o/3
    ## https://stackoverflow.com/a/59696768/3560695
    regex = r'^(?P<path>.*[\\\/])?(?P<name>\.*.*?)(?P<extension>\.[^.]+?|)$'

    filename_write = re.sub(regex, r"\1\2.asm", filename)


    Parser = p.parser
    codewriter = cw.codewriter

    with open(filename, 'r') as file, open(filename_write, "w") as file_write:
        parser = Parser(file)
        writer = codewriter(file_write)

        while parser.hasMoreCommands(): ## As long as file has more lines, do:
            parser.advance()            ## Go to the next line in the file.
            parser.getinstruction()
            if not parser.instruction:  ## If instruction is blank, skip. Line consisted only of a comment. 
                continue
            parser.getVMinstruction()   ## sets parser.VMinstruction to current instruction

            # print(f"---- Line {parser.lineNo} ----")
            # print(f"instruction = {parser.instruction}")
            # print(f"commandType() = {parser.commandType()}, type = {type(parser.commandType())}")
            # print(f"arg1() = {parser.arg1()}")
            # print(f"arg2() = {parser.arg2()}")


            commandType = parser.commandType()
            if parser.commandType() == "C_ARITHMETIC":
                # Write arithmetic from arithmetic.asm
                arg1 = parser.arg1()
                lines = writer.writeArithmetic(arg1)

            elif parser.commandType() in ["C_PUSH", "C_POP"]:
                arg1 = parser.arg1()
                arg2 = parser.arg2()
                lines = writer.writePushPop(commandType, arg1, arg2)
            else:
                ...
            
            ## lines is now the full .asm script. Write to output asm file.
            file_write.write(f'// {parser.instruction}\n')
            for line in lines:
                file_write.write(f'{line}\n')


        


import importlib

# ## Testing
# filename = '.../StackArithmetic/SimpleAdd/SimpleAdd.vm'
# filename = '.../StackArithmetic/Stacktest/Stacktest.vm'
# filename = '.../StackArithmetic/Stacktest/Stacktest.vm'

# importlib.reload(p)
# importlib.reload(cw)

# main(filename[1:])

if __name__ == "main":
    main()




















