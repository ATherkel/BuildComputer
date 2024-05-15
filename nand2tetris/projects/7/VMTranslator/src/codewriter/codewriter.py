
import importlib

parser_module = importlib.import_module("nand2tetris.projects.7.VMTranslator.src.parser.parser")
importlib.reload(parser_module)

dicts_filepath = "nand2tetris/projects/7/VMTranslator/src/utils/dict/dict"
dicts = importlib.import_module(dicts_filepath.replace("/", "."))



class codewriter:
    """ writes the assembly code that implements the parsed command. """

    
    def __init__(self, file) -> None:
        self.file = file        ## functions need to be able to grab file. 

    @staticmethod
    def writeArithmetic(command : str) -> None:
        """
        Arguments
            command (string)
        Function
            Writes to the output file the assembly code that implements the given arithmetic command.
            """
        print(command)
        
    @staticmethod
    def writePushPop(command : str, segment : str, index : int):
        """
        Arguments
        ----
            command : ('C_PUSH' or 'C_POP')
            segment : constant, local etc.
            index   : pointer number in the segment
        Function
        ----
        Writes to the output file the assembly code that implements the given command,
        where command is either C_PUSH or C_POP.
        """
        newline = '\n'

        segmentPointer = dicts.segment[segment]

        # Write push and pop commands from push.asm and pop.asm

        if command == "C_PUSH":
            with open("nand2tetris/projects/7/VMTranslator/src/utils/asm/pushSegment.asm", 'r') as asm:
                lines = f"{asm.read().replace(newline, '')}".format(**locals())
        print(lines)

        

    