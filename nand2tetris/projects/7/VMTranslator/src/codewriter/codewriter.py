
class codewriter:
    """ writes the assembly code that implements the parsed command. """

    
    def __init__(self, file) -> None:
        self.file = file        ## functions need to be able to grab file. 


    def writeArithmetic(command : str) -> None:
        """
        Arguments
            command (string)
        Function
            Writes to the output file the assembly code that implements the given arithmetic command.
            """
        
    def writePushPop(command : str, segment : str, index : int):
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
        # Write push and pop commands from push.asm and pop.asm
        if parser.arg1().lower() == "constant":
            print("constant.")
        elif parser.arg1().lower == "static":
            print("static.")
        else:
            print(parser.arg1())  

    
    def close():
        """
        Function
        ----
        Closes the output file.

        Likely redundant for my method.
        """
