grammar Expr;

CHAR_TYPE: 'char';
INT_TYPE: 'int';
FLOAT_TYPE: 'float';
IdentVarSimples: [a-zA-Z_][a-zA-Z_0-9]*;
SEMICOLON: ';';
COMMA: ',';
WS: [ \t\r\n]+ -> skip;
NUMBER: [0-9]+;
NUMBER_NOT_ZERO: [1-9][0-9]*; // char a[0];

ADD_OP: '+';
SUB_OP: '-';
MUL_OP: '*';
DIV_OP: '/';
OPERADOR_ATRIBUICAO: '=' | '+=' | '-=' | '*=' | '/=';
OPERADOR_RELACIONAL: '==' | '!=' | '<' | '<=' | '>' | '>=';
INCREMENTO: '++';
DECREMENTO: '--';
ARRAY_DECLARATION: '[' NUMBER_NOT_ZERO+ ']';

declaration: ( char_declaration | declaracao_simples);

TipoSimples: INT_TYPE | FLOAT_TYPE;

char_declaration:
	CHAR_TYPE IdentVarSimples (ARRAY_DECLARATION)? (
		COMMA IdentVarSimples (ARRAY_DECLARATION)?
	)*;

declaracao_simples: int_declaration | float_declaration;

int_declaration:
	INT_TYPE IdentVarSimples (COMMA IdentVarSimples)*;

float_declaration:
	FLOAT_TYPE IdentVarSimples (COMMA IdentVarSimples)*;

comando: ( operacao_matematica | operacao_simples) SEMICOLON;

if_statement:
	'if' '(' condicao ')' '{' comando* '}' (
		'else' '{' comando* '}'
	)?;

while_statement: 'while' '(' condicao ')' '{' comando* '}';

elemento: IdentVarSimples | NUMBER; // a | 0+

elemento_nao_zero: IdentVarSimples | NUMBER_NOT_ZERO; // a | 1+

operacao_matematica:
	IdentVarSimples OPERADOR_ATRIBUICAO operacao_composta; // a = a + 1;

operacao_simples:
	IdentVarSimples (INCREMENTO | DECREMENTO); //a++

condicao: elemento OPERADOR_RELACIONAL elemento;

operacao_composta:
	elemento (
		(
			(ADD_OP | SUB_OP | MUL_OP) elemento
			| DIV_OP elemento_nao_zero
		)
	)*;

program: (
		(declaration | if_statement | while_statement) SEMICOLON
	)*;