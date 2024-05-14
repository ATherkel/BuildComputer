
import importlib

dict_filepath = "nand2tetris/projects/7/VMTranslator/src/utils/dict/dict"
dict = importlib.import_module(dict_filepath.replace("/", "."))


class Parser:

    def __init__(self, filename : str = "") -> None:
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
        self.filename = filename
        self.file = open(self.filename, 'r')

    def instruction(self, line = None) -> None:
        line = line if line is not None else self.filename.readline().strip()
        self.instruction = line.split("//")[0].strip().split()



filename = 'nand2tetris/projects/7/StackArithmetic/SimpleAdd/SimpleAdd.vm'
parser = Parser(filename)

parser.filename[:2]

