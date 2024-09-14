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
        4,1,23,129,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,3,0,30,8,0,1,1,1,1,1,1,3,1,35,8,1,1,1,1,1,1,1,3,1,40,8,1,5,1,
        42,8,1,10,1,12,1,45,9,1,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,
        3,4,57,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,67,8,5,10,5,12,5,
        70,9,5,1,5,1,5,1,5,1,5,5,5,76,8,5,10,5,12,5,79,9,5,1,5,3,5,82,8,
        5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,90,8,6,10,6,12,6,93,9,6,1,6,1,6,1,
        7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,5,9,108,8,9,10,9,12,9,
        111,9,9,1,10,1,10,1,10,5,10,116,8,10,10,10,12,10,119,9,10,1,11,1,
        11,1,12,5,12,124,8,12,10,12,12,12,127,9,12,1,12,0,0,13,0,2,4,6,8,
        10,12,14,16,18,20,22,24,0,3,1,0,16,17,1,0,18,19,2,0,11,11,15,15,
        130,0,29,1,0,0,0,2,31,1,0,0,0,4,46,1,0,0,0,6,49,1,0,0,0,8,56,1,0,
        0,0,10,60,1,0,0,0,12,83,1,0,0,0,14,96,1,0,0,0,16,100,1,0,0,0,18,
        104,1,0,0,0,20,112,1,0,0,0,22,120,1,0,0,0,24,125,1,0,0,0,26,30,3,
        2,1,0,27,30,3,4,2,0,28,30,3,6,3,0,29,26,1,0,0,0,29,27,1,0,0,0,29,
        28,1,0,0,0,30,1,1,0,0,0,31,32,5,8,0,0,32,34,5,11,0,0,33,35,5,23,
        0,0,34,33,1,0,0,0,34,35,1,0,0,0,35,43,1,0,0,0,36,37,5,13,0,0,37,
        39,5,11,0,0,38,40,5,23,0,0,39,38,1,0,0,0,39,40,1,0,0,0,40,42,1,0,
        0,0,41,36,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,3,
        1,0,0,0,45,43,1,0,0,0,46,47,5,9,0,0,47,48,5,22,0,0,48,5,1,0,0,0,
        49,50,5,10,0,0,50,51,5,22,0,0,51,7,1,0,0,0,52,57,3,0,0,0,53,57,3,
        10,5,0,54,57,3,12,6,0,55,57,3,14,7,0,56,52,1,0,0,0,56,53,1,0,0,0,
        56,54,1,0,0,0,56,55,1,0,0,0,57,58,1,0,0,0,58,59,5,12,0,0,59,9,1,
        0,0,0,60,61,5,1,0,0,61,62,5,2,0,0,62,63,3,16,8,0,63,64,5,3,0,0,64,
        68,5,4,0,0,65,67,3,8,4,0,66,65,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,
        0,68,69,1,0,0,0,69,71,1,0,0,0,70,68,1,0,0,0,71,81,5,5,0,0,72,73,
        5,6,0,0,73,77,5,4,0,0,74,76,3,8,4,0,75,74,1,0,0,0,76,79,1,0,0,0,
        77,75,1,0,0,0,77,78,1,0,0,0,78,80,1,0,0,0,79,77,1,0,0,0,80,82,5,
        5,0,0,81,72,1,0,0,0,81,82,1,0,0,0,82,11,1,0,0,0,83,84,5,7,0,0,84,
        85,5,2,0,0,85,86,3,16,8,0,86,87,5,3,0,0,87,91,5,4,0,0,88,90,3,8,
        4,0,89,88,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,94,
        1,0,0,0,93,91,1,0,0,0,94,95,5,5,0,0,95,13,1,0,0,0,96,97,5,11,0,0,
        97,98,5,20,0,0,98,99,3,18,9,0,99,15,1,0,0,0,100,101,3,18,9,0,101,
        102,5,21,0,0,102,103,3,18,9,0,103,17,1,0,0,0,104,109,3,20,10,0,105,
        106,7,0,0,0,106,108,3,20,10,0,107,105,1,0,0,0,108,111,1,0,0,0,109,
        107,1,0,0,0,109,110,1,0,0,0,110,19,1,0,0,0,111,109,1,0,0,0,112,117,
        3,22,11,0,113,114,7,1,0,0,114,116,3,22,11,0,115,113,1,0,0,0,116,
        119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,21,1,0,0,0,119,117,
        1,0,0,0,120,121,7,2,0,0,121,23,1,0,0,0,122,124,3,8,4,0,123,122,1,
        0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,25,1,0,
        0,0,127,125,1,0,0,0,12,29,34,39,43,56,68,77,81,91,109,117,125
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'('", "')'", "'{'", "'}'", "'else'", 
                     "'while'", "'char'", "'int'", "'float'", "<INVALID>", 
                     "';'", "','", "<INVALID>", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "CHAR_TYPE", "INT_TYPE", "FLOAT_TYPE", "IDENTIFIER", 
                      "SEMICOLON", "COMMA", "WS", "NUMBER", "ADD_OP", "SUB_OP", 
                      "MUL_OP", "DIV_OP", "ASSIGN_OP", "REL_OP", "IDENTIFIER_LIST", 
                      "ARRAY_DECLARATION" ]

    RULE_declaration = 0
    RULE_char_declaration = 1
    RULE_int_declaration = 2
    RULE_float_declaration = 3
    RULE_statement = 4
    RULE_if_statement = 5
    RULE_while_statement = 6
    RULE_assignment = 7
    RULE_condition = 8
    RULE_expression = 9
    RULE_term = 10
    RULE_factor = 11
    RULE_program = 12

    ruleNames =  [ "declaration", "char_declaration", "int_declaration", 
                   "float_declaration", "statement", "if_statement", "while_statement", 
                   "assignment", "condition", "expression", "term", "factor", 
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
    IDENTIFIER=11
    SEMICOLON=12
    COMMA=13
    WS=14
    NUMBER=15
    ADD_OP=16
    SUB_OP=17
    MUL_OP=18
    DIV_OP=19
    ASSIGN_OP=20
    REL_OP=21
    IDENTIFIER_LIST=22
    ARRAY_DECLARATION=23

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
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.state = 26
                self.char_declaration()
                pass
            elif token in [9]:
                self.state = 27
                self.int_declaration()
                pass
            elif token in [10]:
                self.state = 28
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
            self.state = 31
            self.match(ExprParser.CHAR_TYPE)
            self.state = 32
            self.match(ExprParser.IDENTIFIER)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 33
                self.match(ExprParser.ARRAY_DECLARATION)


            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 36
                self.match(ExprParser.COMMA)
                self.state = 37
                self.match(ExprParser.IDENTIFIER)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 38
                    self.match(ExprParser.ARRAY_DECLARATION)


                self.state = 45
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
            self.state = 46
            self.match(ExprParser.INT_TYPE)
            self.state = 47
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
            self.state = 49
            self.match(ExprParser.FLOAT_TYPE)
            self.state = 50
            self.match(ExprParser.IDENTIFIER_LIST)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)

        def declaration(self):
            return self.getTypedRuleContext(ExprParser.DeclarationContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(ExprParser.If_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(ExprParser.While_statementContext,0)


        def assignment(self):
            return self.getTypedRuleContext(ExprParser.AssignmentContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10]:
                self.state = 52
                self.declaration()
                pass
            elif token in [1]:
                self.state = 53
                self.if_statement()
                pass
            elif token in [7]:
                self.state = 54
                self.while_statement()
                pass
            elif token in [11]:
                self.state = 55
                self.assignment()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 58
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

        def condition(self):
            return self.getTypedRuleContext(ExprParser.ConditionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


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
        self.enterRule(localctx, 10, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(ExprParser.T__0)
            self.state = 61
            self.match(ExprParser.T__1)
            self.state = 62
            self.condition()
            self.state = 63
            self.match(ExprParser.T__2)
            self.state = 64
            self.match(ExprParser.T__3)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3970) != 0):
                self.state = 65
                self.statement()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self.match(ExprParser.T__4)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 72
                self.match(ExprParser.T__5)
                self.state = 73
                self.match(ExprParser.T__3)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3970) != 0):
                    self.state = 74
                    self.statement()
                    self.state = 79
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 80
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

        def condition(self):
            return self.getTypedRuleContext(ExprParser.ConditionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


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
        self.enterRule(localctx, 12, self.RULE_while_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(ExprParser.T__6)
            self.state = 84
            self.match(ExprParser.T__1)
            self.state = 85
            self.condition()
            self.state = 86
            self.match(ExprParser.T__2)
            self.state = 87
            self.match(ExprParser.T__3)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3970) != 0):
                self.state = 88
                self.statement()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
            self.match(ExprParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)

        def ASSIGN_OP(self):
            return self.getToken(ExprParser.ASSIGN_OP, 0)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = ExprParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(ExprParser.IDENTIFIER)
            self.state = 97
            self.match(ExprParser.ASSIGN_OP)
            self.state = 98
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)


        def REL_OP(self):
            return self.getToken(ExprParser.REL_OP, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = ExprParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.expression()
            self.state = 101
            self.match(ExprParser.REL_OP)
            self.state = 102
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.TermContext)
            else:
                return self.getTypedRuleContext(ExprParser.TermContext,i)


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

        def getRuleIndex(self):
            return ExprParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = ExprParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.term()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16 or _la==17:
                self.state = 105
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 106
                self.term()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.FactorContext)
            else:
                return self.getTypedRuleContext(ExprParser.FactorContext,i)


        def MUL_OP(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.MUL_OP)
            else:
                return self.getToken(ExprParser.MUL_OP, i)

        def DIV_OP(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.DIV_OP)
            else:
                return self.getToken(ExprParser.DIV_OP, i)

        def getRuleIndex(self):
            return ExprParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = ExprParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.factor()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 113
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 114
                self.factor()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(ExprParser.NUMBER, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = ExprParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
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


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


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
        self.enterRule(localctx, 24, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3970) != 0):
                self.state = 122
                self.statement()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





