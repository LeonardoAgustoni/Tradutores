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


    # Enter a parse tree produced by ExprParser#char_declaration.
    def enterChar_declaration(self, ctx:ExprParser.Char_declarationContext):
        pass

    # Exit a parse tree produced by ExprParser#char_declaration.
    def exitChar_declaration(self, ctx:ExprParser.Char_declarationContext):
        pass


    # Enter a parse tree produced by ExprParser#int_declaration.
    def enterInt_declaration(self, ctx:ExprParser.Int_declarationContext):
        pass

    # Exit a parse tree produced by ExprParser#int_declaration.
    def exitInt_declaration(self, ctx:ExprParser.Int_declarationContext):
        pass


    # Enter a parse tree produced by ExprParser#float_declaration.
    def enterFloat_declaration(self, ctx:ExprParser.Float_declarationContext):
        pass

    # Exit a parse tree produced by ExprParser#float_declaration.
    def exitFloat_declaration(self, ctx:ExprParser.Float_declarationContext):
        pass



del ExprParser