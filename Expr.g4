grammar Expr;

CHAR_TYPE: 'char';
INT_TYPE: 'int';
FLOAT_TYPE: 'float';
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
SEMICOLON: ';';
COMMA: ',';
WS: [ \t\r\n]+ -> skip;
NUMBER: [0-9]+;

ADD_OP: '+';
SUB_OP: '-';
MUL_OP: '*';
DIV_OP: '/';
ASSIGN_OP: '=';
REL_OP: '==' | '!=' | '<' | '<=' | '>' | '>=';

declaration: (
		char_declaration
		| int_declaration
		| float_declaration
	);

IDENTIFIER_LIST: IDENTIFIER (COMMA IDENTIFIER)*;

ARRAY_DECLARATION: '[' [0-9]+ ']';

char_declaration:
	CHAR_TYPE IDENTIFIER (ARRAY_DECLARATION)? (
		COMMA IDENTIFIER (ARRAY_DECLARATION)?
	)*;

int_declaration: INT_TYPE IDENTIFIER_LIST;

float_declaration: FLOAT_TYPE IDENTIFIER_LIST;

statement: (
		declaration
		| if_statement
		| while_statement
		| assignment
	) SEMICOLON;

if_statement:
	'if' '(' condition ')' '{' statement* '}' (
		'else' '{' statement* '}'
	)?;

while_statement: 'while' '(' condition ')' '{' statement* '}';

assignment: IDENTIFIER ASSIGN_OP expression;

condition: expression REL_OP expression;

expression: term ((ADD_OP | SUB_OP) term)*;

term: factor ((MUL_OP | DIV_OP) factor)*;

factor: IDENTIFIER | NUMBER;

program: statement*;