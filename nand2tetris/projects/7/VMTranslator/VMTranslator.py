## How the program is supposed to be run:
# https://www.coursera.org/learn/nand2tetris2/lecture/qmJl3/unit-1-8-vm-translator-proposed-implementation


#### ---- import ----
# https://stackoverflow.com/a/37867717/3560695

import importlib.util
import sys
import re

## Import parser
## We have to use import_module since the path contains an illegal directory name (7). 
parser_module = importlib.import_module("nand2tetris.projects.7.VMTranslator.src.parser.parser")
Parser = parser_module.parser




#### ---- main ----

#def main():


def main(filename):
    
    ## https://regex101.com/r/x0v99o/3
    ## https://stackoverflow.com/a/59696768/3560695
    regex = r'^(?P<path>.*[\\\/])?(?P<name>\.*.*?)(?P<extension>\.[^.]+?|)$'

    filename_write = re.sub(regex, r"\1\2.asm")


    with open(filename, 'r') as file, open(filename_write, "w"):
        parser = Parser(file)

        while parser.hasMoreCommands(): ## As long as file has more lines, do:
            parser.advance()            ## Go to the next line in the file.
            parser.getinstruction()     ## sets parser.instruction to current instruction
            if not parser.instruction:  ## If instruction is blank, skip. Line consisted only of a comment. 
                continue
            print(f"---- Line {parser.lineNo} ----")
            print(f"instruction = {parser.instruction}")
            print(f"commandType() = {parser.commandType()}")
            print(f"arg1() = {parser.arg1()}")
            print(f"arg2() = {parser.arg2()}")

            if parser.commandType() == "C_ARITHMETIC":
                # Write arithmetic from arithmetic.asm
                ...
            elif parser.commandType() in ["C_PUSH", "C_POP"]:
                # Write push and pop commands from push.asm and pop.asm
                ...
            else:
                ...




## Testing
filename = '/nand2tetris/projects/7/StackArithmetic/SimpleAdd/SimpleAdd.vm'

main(filename[1:])





## Below is probably redundant







# https://chat.openai.com/share/40c7964c-0f2f-44d2-81c7-e88d6a1868a1
def changeExtension(string : str, newExtension : str):
    """
    """
    if not isinstance(string, str):
        raise TypeError("Input <string> must be a string")
    if not isinstance(newExtension, str):
        raise TypeError("Input <newExtension> must be a string")
    
    # Regex pattern to capture the base name and extension
    # https://regex101.com/r/SkENd5/1
    regex = r"^(?P<base>[^.].*\.)(?P<extension>\w+)$|(?P<fullname>^.*$)"

    # Replace the extension with the new extension
    new_string = re.sub(
        regex, 
        lambda m: (
            m.group('base') + newExtension 
            if m.group('base') 
            else m.group('fullname')
        ), 
        string)
    
    return new_string


def writelines(input_data : str | list, filename) -> None:
    """
    Write the given string or list of strings to the specified file.

    Args:
        input_data (str | list): The string or list of strings to write to the file.
        filename (str): The name of the file to write to.

    Raises:
        TypeError: If input_data is neither a string nor a list, or if filename is not a string.
        ValueError: If filename is an empty string.
        IOError: If there is an issue writing to the file.

    Returns:
        None
    """
    # Check input types
    if not isinstance(input_data, (str, list)):
        raise TypeError("Input data must be a string or a list of strings")
    if not isinstance(filename, str):
        raise TypeError("Filename must be a string")
    
    # Check filename is not empty
    if not filename:
        raise ValueError("Filename cannot be an empty string")

    # Open the file in write mode
    try:
        with open(filename, 'w') as file:
            # Write data to the file
            if isinstance(input_data, str):
                file.write(input_data)
            else:
                file.writelines(input_data)
    except IOError as e:
        raise IOError("Error writing to file: " + str(e))
























