
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

        Parser = parser_module.parser

        ## Used in some of the .asm templates.
        ## Contains Hack name convention for segments, e.g. local is "LCL"
        segmentPointer = dicts.segment[segment]

        # Write push and pop commands from push.asm and pop.asm
        
        ## First handle 'pointer' logic translation to THIS/THAT
        if segment == "pointer":
            segment = ["THIS", "THAT"][index]

        if command == "C_PUSH":
            if segment == "constant":
                asm_location = "pushConstant.asm"
            elif segment in ["local", "argument", "this", "that"]:
                asm_location = "pushSegment.asm"
            elif segment == "static":
                asm_location = "pushStatic.asm"
            elif segment == "temp":
                ...
            elif segment == "pointer":
                ...
        
        with open("nand2tetris/projects/7/VMTranslator/src/utils/asm/pushSegment.asm", 'r') as asm:
            parser = Parser(asm)
            
            while parser.hasMoreCommands():
                parser.advance()
                parser.getinstruction()
                if not parser.instruction:  ## If instruction is blank, skip. Line consisted only of a comment. 
                    continue
        return lines

        
    