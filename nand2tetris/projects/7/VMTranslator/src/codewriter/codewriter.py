
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
        print(command)
        
    def writePushPop(command : str, segment : str, index : int, wtf):
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
        print(f"command = '{command}', segment = {segment}, index = {index}, wtf = {wtf}")

    
    def close():
        """
        Function
        ----
        Closes the output file.

        Likely redundant for my method.
        """
