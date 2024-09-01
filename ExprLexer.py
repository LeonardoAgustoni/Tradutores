# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,9,69,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,
        2,1,2,1,2,1,2,1,2,1,3,1,3,5,3,37,8,3,10,3,12,3,40,9,3,1,4,1,4,1,
        5,1,5,1,6,4,6,47,8,6,11,6,12,6,48,1,6,1,6,1,7,1,7,1,7,1,7,5,7,57,
        8,7,10,7,12,7,60,9,7,1,8,1,8,4,8,64,8,8,11,8,12,8,65,1,8,1,8,0,0,
        9,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,1,0,4,3,0,65,90,95,95,
        97,122,4,0,48,57,65,90,95,95,97,122,3,0,9,10,13,13,32,32,1,0,48,
        57,72,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,
        0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,1,19,1,0,0,
        0,3,24,1,0,0,0,5,28,1,0,0,0,7,34,1,0,0,0,9,41,1,0,0,0,11,43,1,0,
        0,0,13,46,1,0,0,0,15,52,1,0,0,0,17,61,1,0,0,0,19,20,5,99,0,0,20,
        21,5,104,0,0,21,22,5,97,0,0,22,23,5,114,0,0,23,2,1,0,0,0,24,25,5,
        105,0,0,25,26,5,110,0,0,26,27,5,116,0,0,27,4,1,0,0,0,28,29,5,102,
        0,0,29,30,5,108,0,0,30,31,5,111,0,0,31,32,5,97,0,0,32,33,5,116,0,
        0,33,6,1,0,0,0,34,38,7,0,0,0,35,37,7,1,0,0,36,35,1,0,0,0,37,40,1,
        0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,8,1,0,0,0,40,38,1,0,0,0,41,
        42,5,59,0,0,42,10,1,0,0,0,43,44,5,44,0,0,44,12,1,0,0,0,45,47,7,2,
        0,0,46,45,1,0,0,0,47,48,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,50,
        1,0,0,0,50,51,6,6,0,0,51,14,1,0,0,0,52,58,3,7,3,0,53,54,3,11,5,0,
        54,55,3,7,3,0,55,57,1,0,0,0,56,53,1,0,0,0,57,60,1,0,0,0,58,56,1,
        0,0,0,58,59,1,0,0,0,59,16,1,0,0,0,60,58,1,0,0,0,61,63,5,91,0,0,62,
        64,7,3,0,0,63,62,1,0,0,0,64,65,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,
        0,66,67,1,0,0,0,67,68,5,93,0,0,68,18,1,0,0,0,5,0,38,48,58,65,1,6,
        0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CHAR_TYPE = 1
    INT_TYPE = 2
    FLOAT_TYPE = 3
    IDENTIFIER = 4
    SEMICOLON = 5
    COMMA = 6
    WS = 7
    IDENTIFIER_LIST = 8
    ARRAY_DECLARATION = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'char'", "'int'", "'float'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "CHAR_TYPE", "INT_TYPE", "FLOAT_TYPE", "IDENTIFIER", "SEMICOLON", 
            "COMMA", "WS", "IDENTIFIER_LIST", "ARRAY_DECLARATION" ]

    ruleNames = [ "CHAR_TYPE", "INT_TYPE", "FLOAT_TYPE", "IDENTIFIER", "SEMICOLON", 
                  "COMMA", "WS", "IDENTIFIER_LIST", "ARRAY_DECLARATION" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


