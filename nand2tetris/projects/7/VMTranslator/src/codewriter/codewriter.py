
import os
# import importlib

# sys.path.append("C:/Users/Bruger/OneDrive/Dokumenter/GitHub/BuildComputer/nand2tetris/projects/7/VMTranslator")


# parser_module = importlib.import_module("src.parser.parser")
import src.parser.parser as parser_module
# importlib.reload(parser_module)

# dicts_filepath = "nand2tetris/projects/7/VMTranslator/src/utils/dict/dict"
# dicts = importlib.import_module(dicts_filepath.replace("/", "."))
import src.utils.dict.dict as dicts

class codewriter:
    """ writes the assembly code that implements the parsed command. """

    
    def __init__(self, file) -> None:
        self.file = file        ## functions need to be able to grab file. 
        self.newline = '\n'

        self.Parser = parser_module.parser
        
        ## Initialize number of times arithmetic has been called
        self.arithmeticNo = 0

        ## Used in some of the .asm templates.
        self.segment = None
        self.index = None

    def writeArithmetic(self, command : str) -> None:
        """
        Arguments
            command (string)
        Function
            Writes to the output file the assembly code that implements the given arithmetic command.
            """
        
        ## Unary or binary operation:
        arity = dicts.arithmetic[command]


        ## action is used in some of the .asm templates.
        ## Contains Hack code for the arithmetic operations
        action = dicts.arithmetic_action[command]
        if command in ["eq", "lt", "gt"]:
            action = dicts.compare_action.format(**locals())
        
        with open(f"src/utils/asm/arithmetic_{arity}.asm", 'r') as asm:
            parser = self.Parser(asm)
            
            lines = self.processCommands(parser, action = action)
        
        self.arithmeticNo += 1
        return lines


        
    def writePushPop(self, command : str, segment : str, index : int, filename : str = ""):
        """
        Arguments
        ----
            command : ('C_PUSH' or 'C_POP')
            segment : constant, local etc.
            index   : pointer number in the segment
            filename: Name of file - used for push/pop static i
        Function
        ----
        Writes to the output file the assembly code that implements the given command,
        where command is either C_PUSH or C_POP.

        If push/pop static i from filename.vm, convert to push/pop filename.i 
        """
        
        segmentPointer = None ## Initialize - passed to self.processCommands but not always used.
        lines = [] ## Initialize lines. 

        ## First handle 'pointer' logic translation to THIS/THAT
        if segment == "pointer":
            if index not in [0, 1]:
                raise ValueError(f"push/pop pointer only valid for value 0 or 1. Input: {index}")
            segment = ["this", "that"][index] ## e.g. 'push pointer 0' means 'push this'
            index = 0 ## Silently 'push THIS' means 'push THIS 0'
        elif segment == "temp" and (not 0 <= index < 7):
            raise ValueError(f"'temp' segment only valid for index values 0 to 7. Input: {index}.")
        
        elif segment == "static":
            if filename == "":
                raise ValueError(f"No filename supplied for push/pop static.")
            file = os.path.splitext(os.path.basename(filename))[0]
            index = file + "." + str(index)
        elif segment in dicts.segment.keys():
            ## Used in some of the .asm templates.
            ## Contains Hack name convention for segments, e.g. local is "LCL"
            segmentPointer = dicts.segment[segment]
        # elif segment == "temp":
        #     ...
        # elif segment == "pointer": ## Handled above
        #     ...

        if command == "C_PUSH":
            if segment in ["constant", "static"]:
                # D <- index
                lines.extend(self.processAsm("D_eq_i.asm", index = index))
            elif segment in dicts.segment.keys(): # local, argument, this, that, temp
                # addr <- segmentPointer + index
                # D <- RAM[addr]
                lines.extend(self.processAsm("D_eq_RAM_segmentPointer_p_i.asm",index = index, segmentPointer = segmentPointer))
            else:
                raise ValueError(f"Segment = '{segment}' not handled.")
            ## RAM[SP] <- D
            ## SP++ 
            lines.extend(self.processAsm("RAM_SP_eq_D.asm"))
            lines.extend(self.processAsm("SPpp.asm"))


        elif command == "C_POP":
            if segment == "constant":
                raise ValueError("Cannot pop constant.")
            elif segment in dicts.segment.keys():
                ...

            
        else:
            raise KeyError(f"Unexpected command '{command}' in writePushPop (should be 'C_PUSH' or 'C_POP')")
        
        

        return lines


    
    def processCommands(self, parser, **kwargs):
        """
        Arguments
        ----
            parser : parser object
        Function
        ----
        Process commands using the provided parser object until there are no more commands.
        """
        lines = []
        while parser.hasMoreCommands():
            parser.advance()
            parser.getinstruction()
            if not parser.instruction:  ## If instruction is blank, skip. Line consisted only of a comment. 
                continue
                
            ## Replace any {} in the input file with its value, sent to this function through **kwargs.
            ## Important that the arguments are named. E.g.
            ##  segment = 'local'
            ##  processCommands(..., segment = segment)
            ##  processCommands(..., segment = 'local')
            line = parser.instruction.format(**kwargs)
            
            lines.append(line)
        
        return lines

    def processAsm(self, asm_file : str, **kwargs):
        with open(f"src/utils/asm/{asm_file}", 'r') as asm:
            parser = self.Parser(asm)
            lines = self.processCommands(parser, **kwargs)
        return lines
        
    