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
        4,1,9,37,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,3,0,12,8,0,
        1,0,1,0,1,1,1,1,1,1,3,1,19,8,1,1,1,1,1,1,1,3,1,24,8,1,5,1,26,8,1,
        10,1,12,1,29,9,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,0,0,4,0,2,4,6,0,0,37,
        0,11,1,0,0,0,2,15,1,0,0,0,4,30,1,0,0,0,6,33,1,0,0,0,8,12,3,2,1,0,
        9,12,3,4,2,0,10,12,3,6,3,0,11,8,1,0,0,0,11,9,1,0,0,0,11,10,1,0,0,
        0,12,13,1,0,0,0,13,14,5,5,0,0,14,1,1,0,0,0,15,16,5,1,0,0,16,18,5,
        4,0,0,17,19,5,9,0,0,18,17,1,0,0,0,18,19,1,0,0,0,19,27,1,0,0,0,20,
        21,5,6,0,0,21,23,5,4,0,0,22,24,5,9,0,0,23,22,1,0,0,0,23,24,1,0,0,
        0,24,26,1,0,0,0,25,20,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,
        1,0,0,0,28,3,1,0,0,0,29,27,1,0,0,0,30,31,5,2,0,0,31,32,5,8,0,0,32,
        5,1,0,0,0,33,34,5,3,0,0,34,35,5,8,0,0,35,7,1,0,0,0,4,11,18,23,27
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'char'", "'int'", "'float'", "<INVALID>", 
                     "';'", "','" ]

    symbolicNames = [ "<INVALID>", "CHAR_TYPE", "INT_TYPE", "FLOAT_TYPE", 
                      "IDENTIFIER", "SEMICOLON", "COMMA", "WS", "IDENTIFIER_LIST", 
                      "ARRAY_DECLARATION" ]

    RULE_declaration = 0
    RULE_char_declaration = 1
    RULE_int_declaration = 2
    RULE_float_declaration = 3

    ruleNames =  [ "declaration", "char_declaration", "int_declaration", 
                   "float_declaration" ]

    EOF = Token.EOF
    CHAR_TYPE=1
    INT_TYPE=2
    FLOAT_TYPE=3
    IDENTIFIER=4
    SEMICOLON=5
    COMMA=6
    WS=7
    IDENTIFIER_LIST=8
    ARRAY_DECLARATION=9

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

        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)

        def char_declaration(self):
            return self.getTypedRuleContext(ExprParser.Char_declarationContext,0)


        def int_declaration(self):
            return self.getTypedRuleContext(ExprParser.Int_declarationContext,0)


        def float_declaration(self):
            return self.getTypedRuleContext(ExprParser.Float_declarationContext,0)


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
            self.state = 11
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 8
                self.char_declaration()
                pass
            elif token in [2]:
                self.state = 9
                self.int_declaration()
                pass
            elif token in [3]:
                self.state = 10
                self.float_declaration()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 13
            self.match(ExprParser.SEMICOLON)
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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.IDENTIFIER)
            else:
                return self.getToken(ExprParser.IDENTIFIER, i)

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
            self.state = 15
            self.match(ExprParser.CHAR_TYPE)
            self.state = 16
            self.match(ExprParser.IDENTIFIER)
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 17
                self.match(ExprParser.ARRAY_DECLARATION)


            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 20
                self.match(ExprParser.COMMA)
                self.state = 21
                self.match(ExprParser.IDENTIFIER)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 22
                    self.match(ExprParser.ARRAY_DECLARATION)


                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def IDENTIFIER_LIST(self):
            return self.getToken(ExprParser.IDENTIFIER_LIST, 0)

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
        self.enterRule(localctx, 4, self.RULE_int_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(ExprParser.INT_TYPE)
            self.state = 31
            self.match(ExprParser.IDENTIFIER_LIST)
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

        def IDENTIFIER_LIST(self):
            return self.getToken(ExprParser.IDENTIFIER_LIST, 0)

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
        self.enterRule(localctx, 6, self.RULE_float_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(ExprParser.FLOAT_TYPE)
            self.state = 34
            self.match(ExprParser.IDENTIFIER_LIST)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





