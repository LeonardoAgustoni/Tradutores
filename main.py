from antlr4 import CommonTokenStream, InputStream
from ExprLexer import ExprLexer
from ExprParser import ExprParser


input_text = input("> ")
lexer = ExprLexer(InputStream(input_text))
stream = CommonTokenStream(lexer)
parser = ExprParser(stream)

tree = parser.program()

print(tree.toStringTree(recog=parser))
