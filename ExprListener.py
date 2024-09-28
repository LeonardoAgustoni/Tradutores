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


    # Enter a parse tree produced by ExprParser#declaracao_simples.
    def enterDeclaracao_simples(self, ctx:ExprParser.Declaracao_simplesContext):
        pass

    # Exit a parse tree produced by ExprParser#declaracao_simples.
    def exitDeclaracao_simples(self, ctx:ExprParser.Declaracao_simplesContext):
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


    # Enter a parse tree produced by ExprParser#comando.
    def enterComando(self, ctx:ExprParser.ComandoContext):
        pass

    # Exit a parse tree produced by ExprParser#comando.
    def exitComando(self, ctx:ExprParser.ComandoContext):
        pass


    # Enter a parse tree produced by ExprParser#if_statement.
    def enterIf_statement(self, ctx:ExprParser.If_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#if_statement.
    def exitIf_statement(self, ctx:ExprParser.If_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#while_statement.
    def enterWhile_statement(self, ctx:ExprParser.While_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#while_statement.
    def exitWhile_statement(self, ctx:ExprParser.While_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#elemento.
    def enterElemento(self, ctx:ExprParser.ElementoContext):
        pass

    # Exit a parse tree produced by ExprParser#elemento.
    def exitElemento(self, ctx:ExprParser.ElementoContext):
        pass


    # Enter a parse tree produced by ExprParser#elemento_nao_zero.
    def enterElemento_nao_zero(self, ctx:ExprParser.Elemento_nao_zeroContext):
        pass

    # Exit a parse tree produced by ExprParser#elemento_nao_zero.
    def exitElemento_nao_zero(self, ctx:ExprParser.Elemento_nao_zeroContext):
        pass


    # Enter a parse tree produced by ExprParser#operacao_matematica.
    def enterOperacao_matematica(self, ctx:ExprParser.Operacao_matematicaContext):
        pass

    # Exit a parse tree produced by ExprParser#operacao_matematica.
    def exitOperacao_matematica(self, ctx:ExprParser.Operacao_matematicaContext):
        pass


    # Enter a parse tree produced by ExprParser#operacao_simples.
    def enterOperacao_simples(self, ctx:ExprParser.Operacao_simplesContext):
        pass

    # Exit a parse tree produced by ExprParser#operacao_simples.
    def exitOperacao_simples(self, ctx:ExprParser.Operacao_simplesContext):
        pass


    # Enter a parse tree produced by ExprParser#condicao.
    def enterCondicao(self, ctx:ExprParser.CondicaoContext):
        pass

    # Exit a parse tree produced by ExprParser#condicao.
    def exitCondicao(self, ctx:ExprParser.CondicaoContext):
        pass


    # Enter a parse tree produced by ExprParser#operacao_composta.
    def enterOperacao_composta(self, ctx:ExprParser.Operacao_compostaContext):
        pass

    # Exit a parse tree produced by ExprParser#operacao_composta.
    def exitOperacao_composta(self, ctx:ExprParser.Operacao_compostaContext):
        pass


    # Enter a parse tree produced by ExprParser#program.
    def enterProgram(self, ctx:ExprParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExprParser#program.
    def exitProgram(self, ctx:ExprParser.ProgramContext):
        pass



del ExprParser