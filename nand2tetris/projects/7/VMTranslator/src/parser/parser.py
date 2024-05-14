
import importlib

dicts_filepath = "nand2tetris/projects/7/VMTranslator/src/utils/dict/dict"
dicts = importlib.import_module(dicts_filepath.replace("/", "."))


class parser:
    """
    - Handles the parsing of a single .vm file.
    
    - Reads a VM command, parses the command into its lexical
    components, and provides convenient access to these components.

    - Ignores all white space and comments.
    """

    def __init__(self, file) -> None:
        self.line = None        ## Initialize line.
        self.lineNo = 0         ## Initialize line number.
        self.instruction = None ## Initialize instruction.
        self.file = file        ## functions need to be able to grab file. 


    def peek(self) -> str:
        """
        Peeks at the next line in a filestream without advancing the pointer.

        Parameters
        ----
        file - A file object. Should be opened in read mode ('r').

        If the file is at the end, an empty string is returned. Empty lines return carriage return (e.g. \\n)
        """
        pos = self.file.tell()      # Get current position in the filestream
        line = self.file.readline() # Read line
        self.file.seek(pos)         # Return to previous line
        return line
    

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
        Are there more commands in the input?
        """
        return bool(self.peek())
    
    def advance(self) -> None:
        """
        Arguments
        ----
        None

        Returns
        ----
        None
        Function
        ----
        Reads the next command from the input and makes it the current command. 
        Should be called only if hasMoreCommands() is true.
        Initially there is no current command.
        """
        self.line = self.file.readline()
        self.lineNo += 1

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
        command = self.instruction[0]
        try:
            return dicts.commandType[command]
        except:
            raise KeyError(f"Current command invalid: Cannot parse '{self.line.strip()}' on line {self.lineNo}.")

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
            out = self.instruction[0]
        elif self.commandType() == "C_RETURN":
            return ValueError(f"arg1() called on invalid command type: '{self.commandType()}'")
        else:
            out = self.instruction[1]
        
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
            return int(self.instruction[2])
        else:
            return ValueError(f"arg2() called on invalid command type: '{self.commandType()}'")
    
    def getinstruction(self):
        self.instruction = self.line.split("//")[0].strip().split()






