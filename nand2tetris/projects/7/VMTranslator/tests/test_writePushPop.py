



# import importlib

# writer_module = importlib.import_module("src.codewriter.codewriter")
from src.codewriter import codewriter as cw
# importlib.reload(cw)


testwriter = cw.codewriter("")

print("---- push local 7 ----")
print(testwriter.writePushPop("C_PUSH", "static", 7))


