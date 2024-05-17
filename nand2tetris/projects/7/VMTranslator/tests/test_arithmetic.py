



# import importlib

# writer_module = importlib.import_module("src.codewriter.codewriter")
from src.codewriter import codewriter as cw
# importlib.reload(cw)

# importlib.reload(cw)

testwriter = cw.codewriter("")

print("---- eq ----")
print(testwriter.writeArithmetic("lt"))

# print("---- push local 7 ----")
# testwriter.writePushPop("C_PUSH", "constant", 7)


