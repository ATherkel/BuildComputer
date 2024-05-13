import re
import importlib.util

## Import segment dictionary
## We have to use import_module since the path contains an illegal directory name (7). 
segment_module = importlib.import_module("nand2tetris.projects.7.VMTranslator.src.parser.segment")
segment = segment_module.segment



class parser:
    """
    Parses each VM command into its lexical elements. 
    
    Arguments
    ----
    filename : str  - A string containing the path to the VM file. """

    def __init__(self, filename : str) -> None:
        """
        Arguments
        ----
        filename : str
            Input file / stream

        Returns
        ----
        None

        Function
        ----
        Opens the input file/stream and gets ready to parse it.

        Raises
        ----
        FileNotFoundError
            If the specified file does not exist.
        """
        try:
            file = open(filename, 'r')
            self.lines = file.readlines()
        except FileNotFoundError:
                raise FileNotFoundError(f"File does not exist. Input file string: '{filename}")
        self.current_command = None


    def hasMoreCommands(self) -> bool:
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
        return bool(self.file.peek())


    def commandType(self) -> str:
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
        if self.current_command.startswith("push"):
            return "C_PUSH"
        elif self.current_command.startswith("pop"):
            return "C_POP"
        elif self.current_command in [
            "add", "sub", "neg",
            "eq", "gt", "lt",
            "and", "or", "not"]:
            return "C_ARITHMETIC"
        
        else:
            raise ValueError(f"Current command invalid: Cannot parse '{self.current_command}'")

    def arg1(self) -> str:
        """
        Arguments
        ----
        None

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
        if self.commandType() == "C_ARITHMETIC":
            out = self.current_command
        else:
            out = self.current_command.split()[1]
        
        return out
        
    def arg2(self) -> int:
        """
        Arguments
        ----
        None

        Returns
        ----
        int

        Function
        ----
        Returns the second argument of the current command.
        Should be called only if the current command is
            C_PUSH, C_POP, C_FUNCTION or C_CALL.
        """
        if self.commandType() in ["C_PUSH", "C_POP", "C_FUNCTION", "C_CALL"]:
            return int(self.current_command.split()[2])
        else:
            return ValueError(f"arg2() called on invalid command type: '{self.current_command}'")
    
    def close(self) -> None:
        self.file.close()
        
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

    def removeComments(input_data : str | list, comment : str = "//") -> (str | list):
        """ Returns the input stripped for comments. 
        If the first argument is a list, iterate over all elements. 
        Does not handle multiline comments. 

        Arguments
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