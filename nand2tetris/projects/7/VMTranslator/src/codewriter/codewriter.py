
import importlib

parser_module = importlib.import_module("nand2tetris.projects.7.VMTranslator.src.parser.parser")
importlib.reload(parser_module)

dicts_filepath = "nand2tetris/projects/7/VMTranslator/src/utils/dict/dict"
dicts = importlib.import_module(dicts_filepath.replace("/", "."))



class codewriter:
    """ writes the assembly code that implements the parsed command. """

    
    def __init__(self, file) -> None:
        self.file = file        ## functions need to be able to grab file. 
        self.newline = '\n'

        self.Parser = parser_module.parser

    @staticmethod
    def writeArithmetic(command : str, ) -> None:
        """
        Arguments
            command (string)
        Function
            Writes to the output file the assembly code that implements the given arithmetic command.
            """
        
        ## Unary or binary operation:
        arity = dicts.arithmetic[command]
        
        with open(f"nand2tetris/projects/7/VMTranslator/src/utils/asm/arithmetic_{arity}", 'r') as asm:
            ...



        
        
    def writePushPop(self, command : str, segment : str, index : int):
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
        
        ## First handle 'pointer' logic translation to THIS/THAT
        if segment == "pointer":
            segment = ["this", "that"][index] ## e.g. 'push pointer 0' means 'push this'
            index = 0 ## Silently 'push THIS' means 'push THIS 0'

        if command == "C_PUSH":
            if segment == "constant":
                asm_location = "pushConstant.asm"
            elif segment in ["local", "argument", "this", "that", "temp"]:
                ## Used in some of the .asm templates.
                ## Contains Hack name convention for segments, e.g. local is "LCL"
                segmentPointer = dicts.segment[segment]

                asm_location = "pushSegment.asm"
            elif segment == "static":
                asm_location = "pushStatic.asm"
            # elif segment == "temp":
            #     ...
            # elif segment == "pointer": ## Handled above
            #     ...
        
        lines = [] ## Initialize lines. 
        

        with open(f"nand2tetris/projects/7/VMTranslator/src/utils/asm/{asm_location}", 'r') as asm:
            parser = self.Parser(asm)
            
            while parser.hasMoreCommands():
                parser.advance()
                parser.getinstruction()
                if not parser.instruction:  ## If instruction is blank, skip. Line consisted only of a comment. 
                    continue
                
                line = parser.instruction.format(**locals())
                lines.append(line)
                # if not parser.hasMoreCommands():
                #     lines.append(self.newline)
        return lines
    

        
    