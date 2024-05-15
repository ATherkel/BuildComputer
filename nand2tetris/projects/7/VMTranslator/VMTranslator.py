## How the program is supposed to be run:
# https://www.coursera.org/learn/nand2tetris2/lecture/qmJl3/unit-1-8-vm-translator-proposed-implementation


#### ---- import ----
# https://stackoverflow.com/a/37867717/3560695

import importlib
import re

## Import parser
## We have to use import_module since the path contains an illegal directory name (7). 
parser_module = importlib.import_module("nand2tetris.projects.7.VMTranslator.src.parser.parser")
importlib.reload(parser_module)
Parser = parser_module.parser

writer_module = importlib.import_module("nand2tetris.projects.7.VMTranslator.src.codewriter.codewriter")
importlib.reload(writer_module)
codewriter = writer_module.codewriter


#### ---- main ----

#def main():


def main(filename):
    
    ## https://regex101.com/r/x0v99o/3
    ## https://stackoverflow.com/a/59696768/3560695
    regex = r'^(?P<path>.*[\\\/])?(?P<name>\.*.*?)(?P<extension>\.[^.]+?|)$'

    filename_write = re.sub(regex, r"\1\2.asm", filename)


    with open(filename, 'r') as file, open(filename_write, "w") as file_write:
        parser = Parser(file)
        writer = codewriter(file_write)

        while parser.hasMoreCommands(): ## As long as file has more lines, do:
            parser.advance()            ## Go to the next line in the file.
            parser.getinstruction()     ## sets parser.instruction to current instruction
            if not parser.instruction:  ## If instruction is blank, skip. Line consisted only of a comment. 
                continue
            print(f"---- Line {parser.lineNo} ----")
            # print(f"instruction = {parser.instruction}")
            # print(f"commandType() = {parser.commandType()}, type = {type(parser.commandType())}")
            # print(f"arg1() = {parser.arg1()}")
            # print(f"arg2() = {parser.arg2()}")


            if parser.commandType() == "C_ARITHMETIC":
                # Write arithmetic from arithmetic.asm
                ...
            elif parser.commandType() in ["C_PUSH", "C_POP"]:
                commandType = parser.commandType()
                arg1 = parser.arg1()
                arg2 = parser.arg2()
                print(writer.writePushPop(commandType, arg1, arg2))
                ...
            else:
                ...




## Testing
filename = '/nand2tetris/projects/7/StackArithmetic/SimpleAdd/SimpleAdd.vm'
main(filename[1:])























