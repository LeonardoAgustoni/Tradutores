# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#declaration.
    def enterDeclaration(self, ctx:ExprParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#declaration.
    def exitDeclaration(self, ctx:ExprParser.DeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#charDecl.
    def enterCharDecl(self, ctx:ExprParser.CharDeclContext):
        pass

    # Exit a parse tree produced by ExprParser#charDecl.
    def exitCharDecl(self, ctx:ExprParser.CharDeclContext):
        pass


    # Enter a parse tree produced by ExprParser#intDecl.
    def enterIntDecl(self, ctx:ExprParser.IntDeclContext):
        pass

    # Exit a parse tree produced by ExprParser#intDecl.
    def exitIntDecl(self, ctx:ExprParser.IntDeclContext):
        pass


    # Enter a parse tree produced by ExprParser#floatDecl.
    def enterFloatDecl(self, ctx:ExprParser.FloatDeclContext):
        pass

    # Exit a parse tree produced by ExprParser#floatDecl.
    def exitFloatDecl(self, ctx:ExprParser.FloatDeclContext):
        pass


    # Enter a parse tree produced by ExprParser#identifierList.
    def enterIdentifierList(self, ctx:ExprParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by ExprParser#identifierList.
    def exitIdentifierList(self, ctx:ExprParser.IdentifierListContext):
        pass



del ExprParser