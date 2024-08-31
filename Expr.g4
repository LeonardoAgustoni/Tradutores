grammar Expr;

CHAR_TYPE: 'char';
INT_TYPE: 'int';
FLOAT_TYPE: 'float';
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
SEMICOLON: ';';
COMMA: ',';
WS: [ \t\r\n]+ -> skip;

declaration: (
		char_declaration
		| int_declaration
		| float_declaration
	) SEMICOLON;

char_declaration:
	CHAR_TYPE (
		IDENTIFIER (COMMA IDENTIFIER)* (
			ARRAY_DECLARATION (COMMA)?
		)?
	)*; // char a, b[10], c, d[20];

int_declaration: INT_TYPE IDENTIFIER_LIST; // int a2, b3, c4;

float_declaration: FLOAT_TYPE IDENTIFIER_LIST; // float a1, b2;

IDENTIFIER_LIST: IDENTIFIER (COMMA IDENTIFIER)*; // a, b, c;

ARRAY_DECLARATION: '[' [0-9]+ ']'; // [1123];