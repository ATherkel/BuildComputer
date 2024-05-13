
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
