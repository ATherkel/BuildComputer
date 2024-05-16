

import importlib



writer_module = importlib.import_module("nand2tetris.projects.7.VMTranslator.src.codewriter.codewriter")

importlib.reload(writer_module)


testwriter = writer_module.codewriter("")


testwriter.writeArithmetic("add")
