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
        4,1,8,52,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,3,0,
        14,8,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,22,8,1,10,1,12,1,25,9,1,1,1,1,
        1,3,1,29,8,1,3,1,31,8,1,5,1,33,8,1,10,1,12,1,36,9,1,1,2,1,2,1,2,
        1,3,1,3,1,3,1,4,1,4,1,4,5,4,47,8,4,10,4,12,4,50,9,4,1,4,0,0,5,0,
        2,4,6,8,0,0,53,0,13,1,0,0,0,2,17,1,0,0,0,4,37,1,0,0,0,6,40,1,0,0,
        0,8,43,1,0,0,0,10,14,3,2,1,0,11,14,3,4,2,0,12,14,3,6,3,0,13,10,1,
        0,0,0,13,11,1,0,0,0,13,12,1,0,0,0,14,15,1,0,0,0,15,16,5,5,0,0,16,
        1,1,0,0,0,17,34,5,1,0,0,18,23,5,4,0,0,19,20,5,6,0,0,20,22,5,4,0,
        0,21,19,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,30,
        1,0,0,0,25,23,1,0,0,0,26,28,5,8,0,0,27,29,5,6,0,0,28,27,1,0,0,0,
        28,29,1,0,0,0,29,31,1,0,0,0,30,26,1,0,0,0,30,31,1,0,0,0,31,33,1,
        0,0,0,32,18,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,
        3,1,0,0,0,36,34,1,0,0,0,37,38,5,2,0,0,38,39,3,8,4,0,39,5,1,0,0,0,
        40,41,5,3,0,0,41,42,3,8,4,0,42,7,1,0,0,0,43,48,5,4,0,0,44,45,5,6,
        0,0,45,47,5,4,0,0,46,44,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,
        1,0,0,0,49,9,1,0,0,0,50,48,1,0,0,0,6,13,23,28,30,34,48
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'char'", "'int'", "'float'", "<INVALID>", 
                     "';'", "','" ]

    symbolicNames = [ "<INVALID>", "CHAR_TYPE", "INT_TYPE", "FLOAT_TYPE", 
                      "IDENTIFIER", "SEMICOLON", "COMMA", "WS", "ARRAY_DECLARATION" ]

    RULE_declaration = 0
    RULE_charDecl = 1
    RULE_intDecl = 2
    RULE_floatDecl = 3
    RULE_identifierList = 4

    ruleNames =  [ "declaration", "charDecl", "intDecl", "floatDecl", "identifierList" ]

    EOF = Token.EOF
    CHAR_TYPE=1
    INT_TYPE=2
    FLOAT_TYPE=3
    IDENTIFIER=4
    SEMICOLON=5
    COMMA=6
    WS=7
    ARRAY_DECLARATION=8

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

        def charDecl(self):
            return self.getTypedRuleContext(ExprParser.CharDeclContext,0)


        def intDecl(self):
            return self.getTypedRuleContext(ExprParser.IntDeclContext,0)


        def floatDecl(self):
            return self.getTypedRuleContext(ExprParser.FloatDeclContext,0)


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
            self.state = 13
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 10
                self.charDecl()
                pass
            elif token in [2]:
                self.state = 11
                self.intDecl()
                pass
            elif token in [3]:
                self.state = 12
                self.floatDecl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 15
            self.match(ExprParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharDeclContext(ParserRuleContext):
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

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def ARRAY_DECLARATION(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ARRAY_DECLARATION)
            else:
                return self.getToken(ExprParser.ARRAY_DECLARATION, i)

        def getRuleIndex(self):
            return ExprParser.RULE_charDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharDecl" ):
                listener.enterCharDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharDecl" ):
                listener.exitCharDecl(self)




    def charDecl(self):

        localctx = ExprParser.CharDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_charDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(ExprParser.CHAR_TYPE)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 18
                self.match(ExprParser.IDENTIFIER)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 19
                    self.match(ExprParser.COMMA)
                    self.state = 20
                    self.match(ExprParser.IDENTIFIER)
                    self.state = 25
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8:
                    self.state = 26
                    self.match(ExprParser.ARRAY_DECLARATION)
                    self.state = 28
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6:
                        self.state = 27
                        self.match(ExprParser.COMMA)




                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(ExprParser.INT_TYPE, 0)

        def identifierList(self):
            return self.getTypedRuleContext(ExprParser.IdentifierListContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_intDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntDecl" ):
                listener.enterIntDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntDecl" ):
                listener.exitIntDecl(self)




    def intDecl(self):

        localctx = ExprParser.IntDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_intDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(ExprParser.INT_TYPE)
            self.state = 38
            self.identifierList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT_TYPE(self):
            return self.getToken(ExprParser.FLOAT_TYPE, 0)

        def identifierList(self):
            return self.getTypedRuleContext(ExprParser.IdentifierListContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_floatDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatDecl" ):
                listener.enterFloatDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatDecl" ):
                listener.exitFloatDecl(self)




    def floatDecl(self):

        localctx = ExprParser.FloatDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_floatDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(ExprParser.FLOAT_TYPE)
            self.state = 41
            self.identifierList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.IDENTIFIER)
            else:
                return self.getToken(ExprParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_identifierList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierList" ):
                listener.enterIdentifierList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierList" ):
                listener.exitIdentifierList(self)




    def identifierList(self):

        localctx = ExprParser.IdentifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_identifierList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(ExprParser.IDENTIFIER)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 44
                self.match(ExprParser.COMMA)
                self.state = 45
                self.match(ExprParser.IDENTIFIER)
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





