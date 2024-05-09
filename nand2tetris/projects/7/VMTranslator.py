## How the program is supposed to be run:
# https://www.coursera.org/learn/nand2tetris2/lecture/qmJl3/unit-1-8-vm-translator-proposed-implementation

#### ---- import ----
# https://stackoverflow.com/a/37867717/3560695

import re
import sys

# Test packages
import os ## Testing purposes


## Test stuff START

# os.getcwd()



## Test stuff END


## Read lines method
def readlines(filename : str):
    """
Returns a list of the lines from an input filename.

Parameters
----
filename : str
    File path and file name of file to be read.
    """
    file = open(filename, 'r')
    lines = file.readlines()
    # print(lines)
    return lines

def removeComments(input_data : str | list, comment : str = "//") -> str | list:
    """ Returns the input stripped for comments. 
    If the first argument is a list, iterate over all elements. 
    Does not handle multiline comments. 

    Parameters
    ----
    input_data : str or list of str
        Input string or list of strings.
    comment : str, optional
        Comment token. Defaults to "//". Everything after this token is removed.
    """
    # Compile the regular expression pattern
    re_comment = re.escape(comment)
    # https://regex101.com/r/BH3D67/1
    regex = r'\s*' + re_comment + '.*'

    # Initialize output variable
    output = None

    if isinstance(input_data, str):
        output = re.sub(regex, '', input_data)
    elif isinstance(input_data, list):
        data_nocomment = [re.sub(regex, '', line) for line in input_data]
        ## Remove empty lines
        output = [line for line in data_nocomment if line.strip()]
    else:
        raise ValueError("input_data must be a string or list of strings.") 
    return output

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




def parser(a):
    """ parses each VM command into its lexical elements. """

    ## ---- Constructor ----
    # Read file
    lines = readlines(filename)
    # Remove comments
    lines_nocomment = removeComments(lines)


    def commandType() -> str:
        """
        Returns a constant representing the type of the current command. 
        C_ARITHMETIC is returned for all the arithmetic/logical commands.

        Returns C_ARITHMETIC, C_PUSH, C_POP,
        C_LABEL, C_GOTO, C_IF, C_FUNCTION, 
        C_RETURN, C_CALL
        """
        ...

    def arg1() -> str:
        """

        Returns string
        """
        ...
    def arg2() -> int:
        """

        """
        ...
    
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


def codewriter(a):
    """ writes the assembly code that implements the parsed command. """
    def constructor():
        """
        Arguments
            Output file / stream
        Function
            Opens the output file / stream and gets ready to write into it.
        """
    def writeArithmetic():
        """
        Arguments
            command (string)
        Function
            Writes to the output file the assembly code that implements the given arithmetic command.
            """
    def writePushPop(command, segment : str, index : int):
        """
        Arguments
        ----
            command (C_PUSH or C_POP)
            segment : str
            index : int
        Function
        ----
        Writes to the output file the assembly code that implements the given command,
        where command is either C_PUSH or C_POP.
        """
    def close():
        """
        Function
        ----
        Closes the output file.

        Likely redundant for my method.
        """























def main(filename : str = None):
    """

"""
    # Check if the correct number of command-line arguments are provided
    if filename is None:
        if len(sys.argv) != 2:
            print("Usage: py VMTranslator.py <filename>")
            return
        filename = sys.argv[1]



    # Call functions from different modules to perform the main tasks
    parsed_data = parser(filename)
    translated_data = codewriter(parsed_data)

    translated_data = lines_nocomment
    # https://regex101.com/r/SkENd5/1

    out_filename = changeExtension(filename, "asm")
    writelines(input_data = translated_data, filename = out_filename)
    return translated_data



if __name__ == "__main__":
    main()


filename = 'nand2tetris/projects/7/StackArithmetic/SimpleAdd/SimpleAdd.vm'
main(filename)
