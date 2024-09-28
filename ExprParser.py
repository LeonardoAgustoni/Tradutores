# Generated from Expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,26,153,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,3,0,33,8,0,1,1,1,1,1,1,3,1,38,8,1,1,1,1,1,1,1,
        3,1,43,8,1,5,1,45,8,1,10,1,12,1,48,9,1,1,2,1,2,3,2,52,8,2,1,3,1,
        3,1,3,1,3,5,3,58,8,3,10,3,12,3,61,9,3,1,4,1,4,1,4,1,4,5,4,67,8,4,
        10,4,12,4,70,9,4,1,5,1,5,3,5,74,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,
        1,6,5,6,84,8,6,10,6,12,6,87,9,6,1,6,1,6,1,6,1,6,5,6,93,8,6,10,6,
        12,6,96,9,6,1,6,3,6,99,8,6,1,7,1,7,1,7,1,7,1,7,1,7,5,7,107,8,7,10,
        7,12,7,110,9,7,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,10,1,10,1,11,
        1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,3,13,134,
        8,13,5,13,136,8,13,10,13,12,13,139,9,13,1,14,1,14,1,14,3,14,144,
        8,14,1,14,1,14,5,14,148,8,14,10,14,12,14,151,9,14,1,14,0,0,15,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,4,2,0,11,11,15,15,2,0,11,
        11,16,16,1,0,23,24,1,0,17,19,154,0,32,1,0,0,0,2,34,1,0,0,0,4,51,
        1,0,0,0,6,53,1,0,0,0,8,62,1,0,0,0,10,73,1,0,0,0,12,77,1,0,0,0,14,
        100,1,0,0,0,16,113,1,0,0,0,18,115,1,0,0,0,20,117,1,0,0,0,22,121,
        1,0,0,0,24,124,1,0,0,0,26,128,1,0,0,0,28,149,1,0,0,0,30,33,3,2,1,
        0,31,33,3,4,2,0,32,30,1,0,0,0,32,31,1,0,0,0,33,1,1,0,0,0,34,35,5,
        8,0,0,35,37,5,11,0,0,36,38,5,25,0,0,37,36,1,0,0,0,37,38,1,0,0,0,
        38,46,1,0,0,0,39,40,5,13,0,0,40,42,5,11,0,0,41,43,5,25,0,0,42,41,
        1,0,0,0,42,43,1,0,0,0,43,45,1,0,0,0,44,39,1,0,0,0,45,48,1,0,0,0,
        46,44,1,0,0,0,46,47,1,0,0,0,47,3,1,0,0,0,48,46,1,0,0,0,49,52,3,6,
        3,0,50,52,3,8,4,0,51,49,1,0,0,0,51,50,1,0,0,0,52,5,1,0,0,0,53,54,
        5,9,0,0,54,59,5,11,0,0,55,56,5,13,0,0,56,58,5,11,0,0,57,55,1,0,0,
        0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,7,1,0,0,0,61,59,1,
        0,0,0,62,63,5,10,0,0,63,68,5,11,0,0,64,65,5,13,0,0,65,67,5,11,0,
        0,66,64,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,9,1,
        0,0,0,70,68,1,0,0,0,71,74,3,20,10,0,72,74,3,22,11,0,73,71,1,0,0,
        0,73,72,1,0,0,0,74,75,1,0,0,0,75,76,5,12,0,0,76,11,1,0,0,0,77,78,
        5,1,0,0,78,79,5,2,0,0,79,80,3,24,12,0,80,81,5,3,0,0,81,85,5,4,0,
        0,82,84,3,10,5,0,83,82,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,
        1,0,0,0,86,88,1,0,0,0,87,85,1,0,0,0,88,98,5,5,0,0,89,90,5,6,0,0,
        90,94,5,4,0,0,91,93,3,10,5,0,92,91,1,0,0,0,93,96,1,0,0,0,94,92,1,
        0,0,0,94,95,1,0,0,0,95,97,1,0,0,0,96,94,1,0,0,0,97,99,5,5,0,0,98,
        89,1,0,0,0,98,99,1,0,0,0,99,13,1,0,0,0,100,101,5,7,0,0,101,102,5,
        2,0,0,102,103,3,24,12,0,103,104,5,3,0,0,104,108,5,4,0,0,105,107,
        3,10,5,0,106,105,1,0,0,0,107,110,1,0,0,0,108,106,1,0,0,0,108,109,
        1,0,0,0,109,111,1,0,0,0,110,108,1,0,0,0,111,112,5,5,0,0,112,15,1,
        0,0,0,113,114,7,0,0,0,114,17,1,0,0,0,115,116,7,1,0,0,116,19,1,0,
        0,0,117,118,5,11,0,0,118,119,5,21,0,0,119,120,3,26,13,0,120,21,1,
        0,0,0,121,122,5,11,0,0,122,123,7,2,0,0,123,23,1,0,0,0,124,125,3,
        16,8,0,125,126,5,22,0,0,126,127,3,16,8,0,127,25,1,0,0,0,128,137,
        3,16,8,0,129,130,7,3,0,0,130,134,3,16,8,0,131,132,5,20,0,0,132,134,
        3,18,9,0,133,129,1,0,0,0,133,131,1,0,0,0,134,136,1,0,0,0,135,133,
        1,0,0,0,136,139,1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,27,1,
        0,0,0,139,137,1,0,0,0,140,144,3,0,0,0,141,144,3,12,6,0,142,144,3,
        14,7,0,143,140,1,0,0,0,143,141,1,0,0,0,143,142,1,0,0,0,144,145,1,
        0,0,0,145,146,5,12,0,0,146,148,1,0,0,0,147,143,1,0,0,0,148,151,1,
        0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,29,1,0,0,0,151,149,1,0,
        0,0,16,32,37,42,46,51,59,68,73,85,94,98,108,133,137,143,149
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'('", "')'", "'{'", "'}'", "'else'", 
                     "'while'", "'char'", "'int'", "'float'", "<INVALID>", 
                     "';'", "','", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "<INVALID>", "<INVALID>", 
                     "'++'", "'--'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "CHAR_TYPE", "INT_TYPE", "FLOAT_TYPE", "IdentVarSimples", 
                      "SEMICOLON", "COMMA", "WS", "NUMBER", "NUMBER_NOT_ZERO", 
                      "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "OPERADOR_ATRIBUICAO", 
                      "OPERADOR_RELACIONAL", "INCREMENTO", "DECREMENTO", 
                      "ARRAY_DECLARATION", "TipoSimples" ]

    RULE_declaration = 0
    RULE_char_declaration = 1
    RULE_declaracao_simples = 2
    RULE_int_declaration = 3
    RULE_float_declaration = 4
    RULE_comando = 5
    RULE_if_statement = 6
    RULE_while_statement = 7
    RULE_elemento = 8
    RULE_elemento_nao_zero = 9
    RULE_operacao_matematica = 10
    RULE_operacao_simples = 11
    RULE_condicao = 12
    RULE_operacao_composta = 13
    RULE_program = 14

    ruleNames =  [ "declaration", "char_declaration", "declaracao_simples", 
                   "int_declaration", "float_declaration", "comando", "if_statement", 
                   "while_statement", "elemento", "elemento_nao_zero", "operacao_matematica", 
                   "operacao_simples", "condicao", "operacao_composta", 
                   "program" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    CHAR_TYPE=8
    INT_TYPE=9
    FLOAT_TYPE=10
    IdentVarSimples=11
    SEMICOLON=12
    COMMA=13
    WS=14
    NUMBER=15
    NUMBER_NOT_ZERO=16
    ADD_OP=17
    SUB_OP=18
    MUL_OP=19
    DIV_OP=20
    OPERADOR_ATRIBUICAO=21
    OPERADOR_RELACIONAL=22
    INCREMENTO=23
    DECREMENTO=24
    ARRAY_DECLARATION=25
    TipoSimples=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def char_declaration(self):
            return self.getTypedRuleContext(ExprParser.Char_declarationContext,0)


        def declaracao_simples(self):
            return self.getTypedRuleContext(ExprParser.Declaracao_simplesContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = ExprParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.state = 30
                self.char_declaration()
                pass
            elif token in [9, 10]:
                self.state = 31
                self.declaracao_simples()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Char_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR_TYPE(self):
            return self.getToken(ExprParser.CHAR_TYPE, 0)

        def IdentVarSimples(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.IdentVarSimples)
            else:
                return self.getToken(ExprParser.IdentVarSimples, i)

        def ARRAY_DECLARATION(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ARRAY_DECLARATION)
            else:
                return self.getToken(ExprParser.ARRAY_DECLARATION, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_char_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChar_declaration" ):
                listener.enterChar_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChar_declaration" ):
                listener.exitChar_declaration(self)




    def char_declaration(self):

        localctx = ExprParser.Char_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_char_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(ExprParser.CHAR_TYPE)
            self.state = 35
            self.match(ExprParser.IdentVarSimples)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 36
                self.match(ExprParser.ARRAY_DECLARATION)


            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 39
                self.match(ExprParser.COMMA)
                self.state = 40
                self.match(ExprParser.IdentVarSimples)
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==25:
                    self.state = 41
                    self.match(ExprParser.ARRAY_DECLARATION)


                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracao_simplesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_declaration(self):
            return self.getTypedRuleContext(ExprParser.Int_declarationContext,0)


        def float_declaration(self):
            return self.getTypedRuleContext(ExprParser.Float_declarationContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_declaracao_simples

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao_simples" ):
                listener.enterDeclaracao_simples(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao_simples" ):
                listener.exitDeclaracao_simples(self)




    def declaracao_simples(self):

        localctx = ExprParser.Declaracao_simplesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracao_simples)
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.int_declaration()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.float_declaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(ExprParser.INT_TYPE, 0)

        def IdentVarSimples(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.IdentVarSimples)
            else:
                return self.getToken(ExprParser.IdentVarSimples, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_int_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_declaration" ):
                listener.enterInt_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_declaration" ):
                listener.exitInt_declaration(self)




    def int_declaration(self):

        localctx = ExprParser.Int_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_int_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(ExprParser.INT_TYPE)
            self.state = 54
            self.match(ExprParser.IdentVarSimples)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 55
                self.match(ExprParser.COMMA)
                self.state = 56
                self.match(ExprParser.IdentVarSimples)
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT_TYPE(self):
            return self.getToken(ExprParser.FLOAT_TYPE, 0)

        def IdentVarSimples(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.IdentVarSimples)
            else:
                return self.getToken(ExprParser.IdentVarSimples, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_float_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat_declaration" ):
                listener.enterFloat_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat_declaration" ):
                listener.exitFloat_declaration(self)




    def float_declaration(self):

        localctx = ExprParser.Float_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_float_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(ExprParser.FLOAT_TYPE)
            self.state = 63
            self.match(ExprParser.IdentVarSimples)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 64
                self.match(ExprParser.COMMA)
                self.state = 65
                self.match(ExprParser.IdentVarSimples)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)

        def operacao_matematica(self):
            return self.getTypedRuleContext(ExprParser.Operacao_matematicaContext,0)


        def operacao_simples(self):
            return self.getTypedRuleContext(ExprParser.Operacao_simplesContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)




    def comando(self):

        localctx = ExprParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comando)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 71
                self.operacao_matematica()
                pass

            elif la_ == 2:
                self.state = 72
                self.operacao_simples()
                pass


            self.state = 75
            self.match(ExprParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condicao(self):
            return self.getTypedRuleContext(ExprParser.CondicaoContext,0)


        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ComandoContext)
            else:
                return self.getTypedRuleContext(ExprParser.ComandoContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = ExprParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(ExprParser.T__0)
            self.state = 78
            self.match(ExprParser.T__1)
            self.state = 79
            self.condicao()
            self.state = 80
            self.match(ExprParser.T__2)
            self.state = 81
            self.match(ExprParser.T__3)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 82
                self.comando()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self.match(ExprParser.T__4)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 89
                self.match(ExprParser.T__5)
                self.state = 90
                self.match(ExprParser.T__3)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==11:
                    self.state = 91
                    self.comando()
                    self.state = 96
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 97
                self.match(ExprParser.T__4)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condicao(self):
            return self.getTypedRuleContext(ExprParser.CondicaoContext,0)


        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ComandoContext)
            else:
                return self.getTypedRuleContext(ExprParser.ComandoContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_while_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_statement" ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_statement" ):
                listener.exitWhile_statement(self)




    def while_statement(self):

        localctx = ExprParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_while_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(ExprParser.T__6)
            self.state = 101
            self.match(ExprParser.T__1)
            self.state = 102
            self.condicao()
            self.state = 103
            self.match(ExprParser.T__2)
            self.state = 104
            self.match(ExprParser.T__3)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 105
                self.comando()
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 111
            self.match(ExprParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IdentVarSimples(self):
            return self.getToken(ExprParser.IdentVarSimples, 0)

        def NUMBER(self):
            return self.getToken(ExprParser.NUMBER, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_elemento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElemento" ):
                listener.enterElemento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElemento" ):
                listener.exitElemento(self)




    def elemento(self):

        localctx = ExprParser.ElementoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_elemento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            _la = self._input.LA(1)
            if not(_la==11 or _la==15):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elemento_nao_zeroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IdentVarSimples(self):
            return self.getToken(ExprParser.IdentVarSimples, 0)

        def NUMBER_NOT_ZERO(self):
            return self.getToken(ExprParser.NUMBER_NOT_ZERO, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_elemento_nao_zero

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElemento_nao_zero" ):
                listener.enterElemento_nao_zero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElemento_nao_zero" ):
                listener.exitElemento_nao_zero(self)




    def elemento_nao_zero(self):

        localctx = ExprParser.Elemento_nao_zeroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_elemento_nao_zero)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            _la = self._input.LA(1)
            if not(_la==11 or _la==16):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operacao_matematicaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IdentVarSimples(self):
            return self.getToken(ExprParser.IdentVarSimples, 0)

        def OPERADOR_ATRIBUICAO(self):
            return self.getToken(ExprParser.OPERADOR_ATRIBUICAO, 0)

        def operacao_composta(self):
            return self.getTypedRuleContext(ExprParser.Operacao_compostaContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_operacao_matematica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacao_matematica" ):
                listener.enterOperacao_matematica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacao_matematica" ):
                listener.exitOperacao_matematica(self)




    def operacao_matematica(self):

        localctx = ExprParser.Operacao_matematicaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_operacao_matematica)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(ExprParser.IdentVarSimples)
            self.state = 118
            self.match(ExprParser.OPERADOR_ATRIBUICAO)
            self.state = 119
            self.operacao_composta()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operacao_simplesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IdentVarSimples(self):
            return self.getToken(ExprParser.IdentVarSimples, 0)

        def INCREMENTO(self):
            return self.getToken(ExprParser.INCREMENTO, 0)

        def DECREMENTO(self):
            return self.getToken(ExprParser.DECREMENTO, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_operacao_simples

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacao_simples" ):
                listener.enterOperacao_simples(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacao_simples" ):
                listener.exitOperacao_simples(self)




    def operacao_simples(self):

        localctx = ExprParser.Operacao_simplesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_operacao_simples)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(ExprParser.IdentVarSimples)
            self.state = 122
            _la = self._input.LA(1)
            if not(_la==23 or _la==24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elemento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ElementoContext)
            else:
                return self.getTypedRuleContext(ExprParser.ElementoContext,i)


        def OPERADOR_RELACIONAL(self):
            return self.getToken(ExprParser.OPERADOR_RELACIONAL, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_condicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicao" ):
                listener.enterCondicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicao" ):
                listener.exitCondicao(self)




    def condicao(self):

        localctx = ExprParser.CondicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_condicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.elemento()
            self.state = 125
            self.match(ExprParser.OPERADOR_RELACIONAL)
            self.state = 126
            self.elemento()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operacao_compostaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elemento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ElementoContext)
            else:
                return self.getTypedRuleContext(ExprParser.ElementoContext,i)


        def DIV_OP(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.DIV_OP)
            else:
                return self.getToken(ExprParser.DIV_OP, i)

        def elemento_nao_zero(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Elemento_nao_zeroContext)
            else:
                return self.getTypedRuleContext(ExprParser.Elemento_nao_zeroContext,i)


        def ADD_OP(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ADD_OP)
            else:
                return self.getToken(ExprParser.ADD_OP, i)

        def SUB_OP(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.SUB_OP)
            else:
                return self.getToken(ExprParser.SUB_OP, i)

        def MUL_OP(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.MUL_OP)
            else:
                return self.getToken(ExprParser.MUL_OP, i)

        def getRuleIndex(self):
            return ExprParser.RULE_operacao_composta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacao_composta" ):
                listener.enterOperacao_composta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacao_composta" ):
                listener.exitOperacao_composta(self)




    def operacao_composta(self):

        localctx = ExprParser.Operacao_compostaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_operacao_composta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.elemento()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1966080) != 0):
                self.state = 133
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [17, 18, 19]:
                    self.state = 129
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 130
                    self.elemento()
                    pass
                elif token in [20]:
                    self.state = 131
                    self.match(ExprParser.DIV_OP)
                    self.state = 132
                    self.elemento_nao_zero()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.SEMICOLON)
            else:
                return self.getToken(ExprParser.SEMICOLON, i)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(ExprParser.DeclarationContext,i)


        def if_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.If_statementContext)
            else:
                return self.getTypedRuleContext(ExprParser.If_statementContext,i)


        def while_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.While_statementContext)
            else:
                return self.getTypedRuleContext(ExprParser.While_statementContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1922) != 0):
                self.state = 143
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8, 9, 10]:
                    self.state = 140
                    self.declaration()
                    pass
                elif token in [1]:
                    self.state = 141
                    self.if_statement()
                    pass
                elif token in [7]:
                    self.state = 142
                    self.while_statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 145
                self.match(ExprParser.SEMICOLON)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





