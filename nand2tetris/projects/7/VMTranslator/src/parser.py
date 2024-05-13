import re

from dict import dict


def parser(filename : str):
    """
    Parses each VM command into its lexical elements. 
    
    Arguments
    ----
    filename : str  - A string containing the path to the VM file. """

    ## ---- Constructor ----
    # Read file
    lines = readlines(filename)
    # Remove comments
    lines_nocomment = removeComments(lines)


    def Constructor(filename : str) -> None:
        """
        Arguments
        ----
        Input file / stream

        Returns
        ----
        N/A

        Function
        ----
        Opens the input file/stream and gets ready to parse it.
        """
        ...


    def hasMoreCommands() -> bool:
        """
        Arguments
        ----
        N/A

        Returns
        ----
        bool
        
        Function
        ----
        Reads the next command from the input and makes it the current command. 
        Should be called only if hasMoreCommands() is true.
        Initially there is no current command.
        """


    def commandType() -> str:
        """
        Arguments
        ----
        N/A

        Returns
        ----
        C_ARITHMETIC, C_PUSH, C_POP, C_LABEL, C_GOTO, C_IF, 
        C_FUNCTION, C_RETURN, C_CALL

        Function
        ----
        Returns a constant representing the type of the current command. 
        C_ARITHMETIC is returned for all the arithmetic/logical commands.

        """
        ...

    def arg1() -> str:
        """
        Arguments
        ----
        N/A

        Returns
        ----
        Str

        Function
        ----
        Returns the first argument of the current command. 
        In the case of C_ARITHMETIC, the command itself (add, sub, etc.)
        is returned.
        Should not be called if the current command is C_RETURN.
        """
        ...
        
    def arg2() -> int:
        """
        Arguments
        ----
        N/A

        Returns
        ----
        int

        Function
        ----
        Returns the second argument of the current command.
        Should be called only if the current command is
            C_PUSH, C_POP, C_FUNCTION or C_CALL.
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



## ---- readlines ----

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




## ---- removeComments ----

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