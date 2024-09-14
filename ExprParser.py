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
        4,1,25,144,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,0,3,0,34,8,0,1,1,1,1,1,1,3,1,39,8,1,1,1,1,1,
        1,1,3,1,44,8,1,5,1,46,8,1,10,1,12,1,49,9,1,1,2,1,2,1,2,1,3,1,3,1,
        3,1,4,1,4,1,4,3,4,60,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,70,
        8,5,10,5,12,5,73,9,5,1,5,1,5,1,5,1,5,5,5,79,8,5,10,5,12,5,82,9,5,
        1,5,3,5,85,8,5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,93,8,6,10,6,12,6,96,9,
        6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,
        1,10,1,11,1,11,1,11,5,11,117,8,11,10,11,12,11,120,9,11,1,12,1,12,
        1,12,5,12,125,8,12,10,12,12,12,128,9,12,1,13,1,13,1,14,1,14,1,14,
        3,14,135,8,14,1,14,1,14,5,14,139,8,14,10,14,12,14,142,9,14,1,14,
        0,0,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,3,1,0,16,17,1,0,
        18,19,2,0,11,11,15,15,144,0,33,1,0,0,0,2,35,1,0,0,0,4,50,1,0,0,0,
        6,53,1,0,0,0,8,59,1,0,0,0,10,63,1,0,0,0,12,86,1,0,0,0,14,99,1,0,
        0,0,16,103,1,0,0,0,18,106,1,0,0,0,20,109,1,0,0,0,22,113,1,0,0,0,
        24,121,1,0,0,0,26,129,1,0,0,0,28,140,1,0,0,0,30,34,3,2,1,0,31,34,
        3,4,2,0,32,34,3,6,3,0,33,30,1,0,0,0,33,31,1,0,0,0,33,32,1,0,0,0,
        34,1,1,0,0,0,35,36,5,8,0,0,36,38,5,11,0,0,37,39,5,25,0,0,38,37,1,
        0,0,0,38,39,1,0,0,0,39,47,1,0,0,0,40,41,5,13,0,0,41,43,5,11,0,0,
        42,44,5,25,0,0,43,42,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,40,1,
        0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,3,1,0,0,0,49,
        47,1,0,0,0,50,51,5,9,0,0,51,52,5,24,0,0,52,5,1,0,0,0,53,54,5,10,
        0,0,54,55,5,24,0,0,55,7,1,0,0,0,56,60,3,14,7,0,57,60,3,16,8,0,58,
        60,3,18,9,0,59,56,1,0,0,0,59,57,1,0,0,0,59,58,1,0,0,0,60,61,1,0,
        0,0,61,62,5,12,0,0,62,9,1,0,0,0,63,64,5,1,0,0,64,65,5,2,0,0,65,66,
        3,20,10,0,66,67,5,3,0,0,67,71,5,4,0,0,68,70,3,8,4,0,69,68,1,0,0,
        0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,71,
        1,0,0,0,74,84,5,5,0,0,75,76,5,6,0,0,76,80,5,4,0,0,77,79,3,8,4,0,
        78,77,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,83,1,
        0,0,0,82,80,1,0,0,0,83,85,5,5,0,0,84,75,1,0,0,0,84,85,1,0,0,0,85,
        11,1,0,0,0,86,87,5,7,0,0,87,88,5,2,0,0,88,89,3,20,10,0,89,90,5,3,
        0,0,90,94,5,4,0,0,91,93,3,8,4,0,92,91,1,0,0,0,93,96,1,0,0,0,94,92,
        1,0,0,0,94,95,1,0,0,0,95,97,1,0,0,0,96,94,1,0,0,0,97,98,5,5,0,0,
        98,13,1,0,0,0,99,100,5,11,0,0,100,101,5,20,0,0,101,102,3,22,11,0,
        102,15,1,0,0,0,103,104,5,11,0,0,104,105,5,22,0,0,105,17,1,0,0,0,
        106,107,5,11,0,0,107,108,5,23,0,0,108,19,1,0,0,0,109,110,3,22,11,
        0,110,111,5,21,0,0,111,112,3,22,11,0,112,21,1,0,0,0,113,118,3,24,
        12,0,114,115,7,0,0,0,115,117,3,24,12,0,116,114,1,0,0,0,117,120,1,
        0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,23,1,0,0,0,120,118,1,0,
        0,0,121,126,3,26,13,0,122,123,7,1,0,0,123,125,3,26,13,0,124,122,
        1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,25,1,
        0,0,0,128,126,1,0,0,0,129,130,7,2,0,0,130,27,1,0,0,0,131,135,3,0,
        0,0,132,135,3,10,5,0,133,135,3,12,6,0,134,131,1,0,0,0,134,132,1,
        0,0,0,134,133,1,0,0,0,135,136,1,0,0,0,136,137,5,12,0,0,137,139,1,
        0,0,0,138,134,1,0,0,0,139,142,1,0,0,0,140,138,1,0,0,0,140,141,1,
        0,0,0,141,29,1,0,0,0,142,140,1,0,0,0,13,33,38,43,47,59,71,80,84,
        94,118,126,134,140
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'('", "')'", "'{'", "'}'", "'else'", 
                     "'while'", "'char'", "'int'", "'float'", "<INVALID>", 
                     "';'", "','", "<INVALID>", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'='", "<INVALID>", "'++'", "'--'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "CHAR_TYPE", "INT_TYPE", "FLOAT_TYPE", "IDENTIFIER", 
                      "SEMICOLON", "COMMA", "WS", "NUMBER", "ADD_OP", "SUB_OP", 
                      "MUL_OP", "DIV_OP", "ASSIGN_OP", "REL_OP", "INCREMENT", 
                      "DECREMENT", "IDENTIFIER_LIST", "ARRAY_DECLARATION" ]

    RULE_declaration = 0
    RULE_char_declaration = 1
    RULE_int_declaration = 2
    RULE_float_declaration = 3
    RULE_statement = 4
    RULE_if_statement = 5
    RULE_while_statement = 6
    RULE_assignment = 7
    RULE_increment = 8
    RULE_decrement = 9
    RULE_condition = 10
    RULE_expression = 11
    RULE_term = 12
    RULE_factor = 13
    RULE_program = 14

    ruleNames =  [ "declaration", "char_declaration", "int_declaration", 
                   "float_declaration", "statement", "if_statement", "while_statement", 
                   "assignment", "increment", "decrement", "condition", 
                   "expression", "term", "factor", "program" ]

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
    INCREMENT=22
    DECREMENT=23
    IDENTIFIER_LIST=24
    ARRAY_DECLARATION=25

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
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.state = 30
                self.char_declaration()
                pass
            elif token in [9]:
                self.state = 31
                self.int_declaration()
                pass
            elif token in [10]:
                self.state = 32
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
            self.state = 35
            self.match(ExprParser.CHAR_TYPE)
            self.state = 36
            self.match(ExprParser.IDENTIFIER)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 37
                self.match(ExprParser.ARRAY_DECLARATION)


            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 40
                self.match(ExprParser.COMMA)
                self.state = 41
                self.match(ExprParser.IDENTIFIER)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==25:
                    self.state = 42
                    self.match(ExprParser.ARRAY_DECLARATION)


                self.state = 49
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
            self.state = 50
            self.match(ExprParser.INT_TYPE)
            self.state = 51
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
            self.state = 53
            self.match(ExprParser.FLOAT_TYPE)
            self.state = 54
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

        def assignment(self):
            return self.getTypedRuleContext(ExprParser.AssignmentContext,0)


        def increment(self):
            return self.getTypedRuleContext(ExprParser.IncrementContext,0)


        def decrement(self):
            return self.getTypedRuleContext(ExprParser.DecrementContext,0)


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
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 56
                self.assignment()
                pass

            elif la_ == 2:
                self.state = 57
                self.increment()
                pass

            elif la_ == 3:
                self.state = 58
                self.decrement()
                pass


            self.state = 61
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
            self.state = 63
            self.match(ExprParser.T__0)
            self.state = 64
            self.match(ExprParser.T__1)
            self.state = 65
            self.condition()
            self.state = 66
            self.match(ExprParser.T__2)
            self.state = 67
            self.match(ExprParser.T__3)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 68
                self.statement()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.match(ExprParser.T__4)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 75
                self.match(ExprParser.T__5)
                self.state = 76
                self.match(ExprParser.T__3)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==11:
                    self.state = 77
                    self.statement()
                    self.state = 82
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 83
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
            self.state = 86
            self.match(ExprParser.T__6)
            self.state = 87
            self.match(ExprParser.T__1)
            self.state = 88
            self.condition()
            self.state = 89
            self.match(ExprParser.T__2)
            self.state = 90
            self.match(ExprParser.T__3)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 91
                self.statement()
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
            self.state = 99
            self.match(ExprParser.IDENTIFIER)
            self.state = 100
            self.match(ExprParser.ASSIGN_OP)
            self.state = 101
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncrementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)

        def INCREMENT(self):
            return self.getToken(ExprParser.INCREMENT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_increment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncrement" ):
                listener.enterIncrement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncrement" ):
                listener.exitIncrement(self)




    def increment(self):

        localctx = ExprParser.IncrementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_increment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(ExprParser.IDENTIFIER)
            self.state = 104
            self.match(ExprParser.INCREMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecrementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)

        def DECREMENT(self):
            return self.getToken(ExprParser.DECREMENT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_decrement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecrement" ):
                listener.enterDecrement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecrement" ):
                listener.exitDecrement(self)




    def decrement(self):

        localctx = ExprParser.DecrementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_decrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(ExprParser.IDENTIFIER)
            self.state = 107
            self.match(ExprParser.DECREMENT)
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
        self.enterRule(localctx, 20, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.expression()
            self.state = 110
            self.match(ExprParser.REL_OP)
            self.state = 111
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
        self.enterRule(localctx, 22, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.term()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16 or _la==17:
                self.state = 114
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 115
                self.term()
                self.state = 120
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
        self.enterRule(localctx, 24, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.factor()
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 122
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 123
                self.factor()
                self.state = 128
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
        self.enterRule(localctx, 26, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
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
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1922) != 0):
                self.state = 134
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8, 9, 10]:
                    self.state = 131
                    self.declaration()
                    pass
                elif token in [1]:
                    self.state = 132
                    self.if_statement()
                    pass
                elif token in [7]:
                    self.state = 133
                    self.while_statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 136
                self.match(ExprParser.SEMICOLON)
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





