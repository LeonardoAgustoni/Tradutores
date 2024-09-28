// Generated from /Users/I557924/Library/CloudStorage/OneDrive-Personal/Estudos/UNISINOS/antlr/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ExprParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, CHAR_TYPE=8, INT_TYPE=9, 
		FLOAT_TYPE=10, IdentVarSimples=11, SEMICOLON=12, COMMA=13, WS=14, NUMBER=15, 
		NUMBER_NOT_ZERO=16, ADD_OP=17, SUB_OP=18, MUL_OP=19, DIV_OP=20, OPERADOR_ATRIBUICAO=21, 
		OPERADOR_RELACIONAL=22, INCREMENTO=23, DECREMENTO=24, ARRAY_DECLARATION=25, 
		TipoSimples=26;
	public static final int
		RULE_declaration = 0, RULE_char_declaration = 1, RULE_declaracao_simples = 2, 
		RULE_int_declaration = 3, RULE_float_declaration = 4, RULE_comando = 5, 
		RULE_if_statement = 6, RULE_while_statement = 7, RULE_elemento = 8, RULE_operacao_matematica = 9, 
		RULE_operacao_simples = 10, RULE_condicao = 11, RULE_operacao_composta = 12, 
		RULE_program = 13;
	private static String[] makeRuleNames() {
		return new String[] {
			"declaration", "char_declaration", "declaracao_simples", "int_declaration", 
			"float_declaration", "comando", "if_statement", "while_statement", "elemento", 
			"operacao_matematica", "operacao_simples", "condicao", "operacao_composta", 
			"program"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'if'", "'('", "')'", "'{'", "'}'", "'else'", "'while'", "'char'", 
			"'int'", "'float'", null, "';'", "','", null, null, null, "'+'", "'-'", 
			"'*'", "'/'", null, null, "'++'", "'--'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, "CHAR_TYPE", "INT_TYPE", 
			"FLOAT_TYPE", "IdentVarSimples", "SEMICOLON", "COMMA", "WS", "NUMBER", 
			"NUMBER_NOT_ZERO", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "OPERADOR_ATRIBUICAO", 
			"OPERADOR_RELACIONAL", "INCREMENTO", "DECREMENTO", "ARRAY_DECLARATION", 
			"TipoSimples"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Expr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ExprParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarationContext extends ParserRuleContext {
		public Char_declarationContext char_declaration() {
			return getRuleContext(Char_declarationContext.class,0);
		}
		public Declaracao_simplesContext declaracao_simples() {
			return getRuleContext(Declaracao_simplesContext.class,0);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CHAR_TYPE:
				{
				setState(28);
				char_declaration();
				}
				break;
			case INT_TYPE:
			case FLOAT_TYPE:
				{
				setState(29);
				declaracao_simples();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Char_declarationContext extends ParserRuleContext {
		public TerminalNode CHAR_TYPE() { return getToken(ExprParser.CHAR_TYPE, 0); }
		public List<TerminalNode> IdentVarSimples() { return getTokens(ExprParser.IdentVarSimples); }
		public TerminalNode IdentVarSimples(int i) {
			return getToken(ExprParser.IdentVarSimples, i);
		}
		public List<TerminalNode> ARRAY_DECLARATION() { return getTokens(ExprParser.ARRAY_DECLARATION); }
		public TerminalNode ARRAY_DECLARATION(int i) {
			return getToken(ExprParser.ARRAY_DECLARATION, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(ExprParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ExprParser.COMMA, i);
		}
		public Char_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_char_declaration; }
	}

	public final Char_declarationContext char_declaration() throws RecognitionException {
		Char_declarationContext _localctx = new Char_declarationContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_char_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			match(CHAR_TYPE);
			setState(33);
			match(IdentVarSimples);
			setState(35);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ARRAY_DECLARATION) {
				{
				setState(34);
				match(ARRAY_DECLARATION);
				}
			}

			setState(44);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(37);
				match(COMMA);
				setState(38);
				match(IdentVarSimples);
				setState(40);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ARRAY_DECLARATION) {
					{
					setState(39);
					match(ARRAY_DECLARATION);
					}
				}

				}
				}
				setState(46);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Declaracao_simplesContext extends ParserRuleContext {
		public Int_declarationContext int_declaration() {
			return getRuleContext(Int_declarationContext.class,0);
		}
		public Float_declarationContext float_declaration() {
			return getRuleContext(Float_declarationContext.class,0);
		}
		public Declaracao_simplesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracao_simples; }
	}

	public final Declaracao_simplesContext declaracao_simples() throws RecognitionException {
		Declaracao_simplesContext _localctx = new Declaracao_simplesContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_declaracao_simples);
		try {
			setState(49);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT_TYPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(47);
				int_declaration();
				}
				break;
			case FLOAT_TYPE:
				enterOuterAlt(_localctx, 2);
				{
				setState(48);
				float_declaration();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Int_declarationContext extends ParserRuleContext {
		public TerminalNode INT_TYPE() { return getToken(ExprParser.INT_TYPE, 0); }
		public List<TerminalNode> IdentVarSimples() { return getTokens(ExprParser.IdentVarSimples); }
		public TerminalNode IdentVarSimples(int i) {
			return getToken(ExprParser.IdentVarSimples, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(ExprParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ExprParser.COMMA, i);
		}
		public Int_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_int_declaration; }
	}

	public final Int_declarationContext int_declaration() throws RecognitionException {
		Int_declarationContext _localctx = new Int_declarationContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_int_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			match(INT_TYPE);
			setState(52);
			match(IdentVarSimples);
			setState(57);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(53);
				match(COMMA);
				setState(54);
				match(IdentVarSimples);
				}
				}
				setState(59);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Float_declarationContext extends ParserRuleContext {
		public TerminalNode FLOAT_TYPE() { return getToken(ExprParser.FLOAT_TYPE, 0); }
		public List<TerminalNode> IdentVarSimples() { return getTokens(ExprParser.IdentVarSimples); }
		public TerminalNode IdentVarSimples(int i) {
			return getToken(ExprParser.IdentVarSimples, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(ExprParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ExprParser.COMMA, i);
		}
		public Float_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_float_declaration; }
	}

	public final Float_declarationContext float_declaration() throws RecognitionException {
		Float_declarationContext _localctx = new Float_declarationContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_float_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			match(FLOAT_TYPE);
			setState(61);
			match(IdentVarSimples);
			setState(66);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(62);
				match(COMMA);
				setState(63);
				match(IdentVarSimples);
				}
				}
				setState(68);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ComandoContext extends ParserRuleContext {
		public TerminalNode SEMICOLON() { return getToken(ExprParser.SEMICOLON, 0); }
		public Operacao_matematicaContext operacao_matematica() {
			return getRuleContext(Operacao_matematicaContext.class,0);
		}
		public Operacao_simplesContext operacao_simples() {
			return getRuleContext(Operacao_simplesContext.class,0);
		}
		public ComandoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando; }
	}

	public final ComandoContext comando() throws RecognitionException {
		ComandoContext _localctx = new ComandoContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_comando);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				{
				setState(69);
				operacao_matematica();
				}
				break;
			case 2:
				{
				setState(70);
				operacao_simples();
				}
				break;
			}
			setState(73);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class If_statementContext extends ParserRuleContext {
		public CondicaoContext condicao() {
			return getRuleContext(CondicaoContext.class,0);
		}
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public If_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_statement; }
	}

	public final If_statementContext if_statement() throws RecognitionException {
		If_statementContext _localctx = new If_statementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_if_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(T__0);
			setState(76);
			match(T__1);
			setState(77);
			condicao();
			setState(78);
			match(T__2);
			setState(79);
			match(T__3);
			setState(83);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==IdentVarSimples) {
				{
				{
				setState(80);
				comando();
				}
				}
				setState(85);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(86);
			match(T__4);
			setState(96);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__5) {
				{
				setState(87);
				match(T__5);
				setState(88);
				match(T__3);
				setState(92);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==IdentVarSimples) {
					{
					{
					setState(89);
					comando();
					}
					}
					setState(94);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(95);
				match(T__4);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class While_statementContext extends ParserRuleContext {
		public CondicaoContext condicao() {
			return getRuleContext(CondicaoContext.class,0);
		}
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public While_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_statement; }
	}

	public final While_statementContext while_statement() throws RecognitionException {
		While_statementContext _localctx = new While_statementContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_while_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(98);
			match(T__6);
			setState(99);
			match(T__1);
			setState(100);
			condicao();
			setState(101);
			match(T__2);
			setState(102);
			match(T__3);
			setState(106);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==IdentVarSimples) {
				{
				{
				setState(103);
				comando();
				}
				}
				setState(108);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(109);
			match(T__4);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ElementoContext extends ParserRuleContext {
		public TerminalNode IdentVarSimples() { return getToken(ExprParser.IdentVarSimples, 0); }
		public TerminalNode NUMBER() { return getToken(ExprParser.NUMBER, 0); }
		public ElementoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elemento; }
	}

	public final ElementoContext elemento() throws RecognitionException {
		ElementoContext _localctx = new ElementoContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_elemento);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			_la = _input.LA(1);
			if ( !(_la==IdentVarSimples || _la==NUMBER) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Operacao_matematicaContext extends ParserRuleContext {
		public TerminalNode IdentVarSimples() { return getToken(ExprParser.IdentVarSimples, 0); }
		public TerminalNode OPERADOR_ATRIBUICAO() { return getToken(ExprParser.OPERADOR_ATRIBUICAO, 0); }
		public Operacao_compostaContext operacao_composta() {
			return getRuleContext(Operacao_compostaContext.class,0);
		}
		public Operacao_matematicaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operacao_matematica; }
	}

	public final Operacao_matematicaContext operacao_matematica() throws RecognitionException {
		Operacao_matematicaContext _localctx = new Operacao_matematicaContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_operacao_matematica);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(113);
			match(IdentVarSimples);
			setState(114);
			match(OPERADOR_ATRIBUICAO);
			setState(115);
			operacao_composta();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Operacao_simplesContext extends ParserRuleContext {
		public TerminalNode IdentVarSimples() { return getToken(ExprParser.IdentVarSimples, 0); }
		public TerminalNode INCREMENTO() { return getToken(ExprParser.INCREMENTO, 0); }
		public TerminalNode DECREMENTO() { return getToken(ExprParser.DECREMENTO, 0); }
		public Operacao_simplesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operacao_simples; }
	}

	public final Operacao_simplesContext operacao_simples() throws RecognitionException {
		Operacao_simplesContext _localctx = new Operacao_simplesContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_operacao_simples);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			match(IdentVarSimples);
			setState(118);
			_la = _input.LA(1);
			if ( !(_la==INCREMENTO || _la==DECREMENTO) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondicaoContext extends ParserRuleContext {
		public List<ElementoContext> elemento() {
			return getRuleContexts(ElementoContext.class);
		}
		public ElementoContext elemento(int i) {
			return getRuleContext(ElementoContext.class,i);
		}
		public TerminalNode OPERADOR_RELACIONAL() { return getToken(ExprParser.OPERADOR_RELACIONAL, 0); }
		public CondicaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicao; }
	}

	public final CondicaoContext condicao() throws RecognitionException {
		CondicaoContext _localctx = new CondicaoContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_condicao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			elemento();
			setState(121);
			match(OPERADOR_RELACIONAL);
			setState(122);
			elemento();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Operacao_compostaContext extends ParserRuleContext {
		public List<ElementoContext> elemento() {
			return getRuleContexts(ElementoContext.class);
		}
		public ElementoContext elemento(int i) {
			return getRuleContext(ElementoContext.class,i);
		}
		public List<TerminalNode> ADD_OP() { return getTokens(ExprParser.ADD_OP); }
		public TerminalNode ADD_OP(int i) {
			return getToken(ExprParser.ADD_OP, i);
		}
		public List<TerminalNode> SUB_OP() { return getTokens(ExprParser.SUB_OP); }
		public TerminalNode SUB_OP(int i) {
			return getToken(ExprParser.SUB_OP, i);
		}
		public List<TerminalNode> MUL_OP() { return getTokens(ExprParser.MUL_OP); }
		public TerminalNode MUL_OP(int i) {
			return getToken(ExprParser.MUL_OP, i);
		}
		public List<TerminalNode> DIV_OP() { return getTokens(ExprParser.DIV_OP); }
		public TerminalNode DIV_OP(int i) {
			return getToken(ExprParser.DIV_OP, i);
		}
		public Operacao_compostaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operacao_composta; }
	}

	public final Operacao_compostaContext operacao_composta() throws RecognitionException {
		Operacao_compostaContext _localctx = new Operacao_compostaContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_operacao_composta);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(124);
			elemento();
			setState(129);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1966080L) != 0)) {
				{
				{
				setState(125);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1966080L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(126);
				elemento();
				}
				}
				setState(131);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public List<TerminalNode> SEMICOLON() { return getTokens(ExprParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(ExprParser.SEMICOLON, i);
		}
		public List<DeclarationContext> declaration() {
			return getRuleContexts(DeclarationContext.class);
		}
		public DeclarationContext declaration(int i) {
			return getRuleContext(DeclarationContext.class,i);
		}
		public List<If_statementContext> if_statement() {
			return getRuleContexts(If_statementContext.class);
		}
		public If_statementContext if_statement(int i) {
			return getRuleContext(If_statementContext.class,i);
		}
		public List<While_statementContext> while_statement() {
			return getRuleContexts(While_statementContext.class);
		}
		public While_statementContext while_statement(int i) {
			return getRuleContext(While_statementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(141);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1922L) != 0)) {
				{
				{
				setState(135);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case CHAR_TYPE:
				case INT_TYPE:
				case FLOAT_TYPE:
					{
					setState(132);
					declaration();
					}
					break;
				case T__0:
					{
					setState(133);
					if_statement();
					}
					break;
				case T__6:
					{
					setState(134);
					while_statement();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(137);
				match(SEMICOLON);
				}
				}
				setState(143);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001a\u0091\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0001\u0000\u0001\u0000\u0003\u0000\u001f"+
		"\b\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001$\b\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0003\u0001)\b\u0001\u0005\u0001+\b\u0001"+
		"\n\u0001\f\u0001.\t\u0001\u0001\u0002\u0001\u0002\u0003\u00022\b\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0005\u00038\b\u0003"+
		"\n\u0003\f\u0003;\t\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0005\u0004A\b\u0004\n\u0004\f\u0004D\t\u0004\u0001\u0005\u0001\u0005"+
		"\u0003\u0005H\b\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0005\u0006R\b\u0006"+
		"\n\u0006\f\u0006U\t\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0005\u0006[\b\u0006\n\u0006\f\u0006^\t\u0006\u0001\u0006\u0003\u0006"+
		"a\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0005\u0007i\b\u0007\n\u0007\f\u0007l\t\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001"+
		"\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001"+
		"\f\u0001\f\u0005\f\u0080\b\f\n\f\f\f\u0083\t\f\u0001\r\u0001\r\u0001\r"+
		"\u0003\r\u0088\b\r\u0001\r\u0001\r\u0005\r\u008c\b\r\n\r\f\r\u008f\t\r"+
		"\u0001\r\u0000\u0000\u000e\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012"+
		"\u0014\u0016\u0018\u001a\u0000\u0003\u0002\u0000\u000b\u000b\u000f\u000f"+
		"\u0001\u0000\u0017\u0018\u0001\u0000\u0011\u0014\u0092\u0000\u001e\u0001"+
		"\u0000\u0000\u0000\u0002 \u0001\u0000\u0000\u0000\u00041\u0001\u0000\u0000"+
		"\u0000\u00063\u0001\u0000\u0000\u0000\b<\u0001\u0000\u0000\u0000\nG\u0001"+
		"\u0000\u0000\u0000\fK\u0001\u0000\u0000\u0000\u000eb\u0001\u0000\u0000"+
		"\u0000\u0010o\u0001\u0000\u0000\u0000\u0012q\u0001\u0000\u0000\u0000\u0014"+
		"u\u0001\u0000\u0000\u0000\u0016x\u0001\u0000\u0000\u0000\u0018|\u0001"+
		"\u0000\u0000\u0000\u001a\u008d\u0001\u0000\u0000\u0000\u001c\u001f\u0003"+
		"\u0002\u0001\u0000\u001d\u001f\u0003\u0004\u0002\u0000\u001e\u001c\u0001"+
		"\u0000\u0000\u0000\u001e\u001d\u0001\u0000\u0000\u0000\u001f\u0001\u0001"+
		"\u0000\u0000\u0000 !\u0005\b\u0000\u0000!#\u0005\u000b\u0000\u0000\"$"+
		"\u0005\u0019\u0000\u0000#\"\u0001\u0000\u0000\u0000#$\u0001\u0000\u0000"+
		"\u0000$,\u0001\u0000\u0000\u0000%&\u0005\r\u0000\u0000&(\u0005\u000b\u0000"+
		"\u0000\')\u0005\u0019\u0000\u0000(\'\u0001\u0000\u0000\u0000()\u0001\u0000"+
		"\u0000\u0000)+\u0001\u0000\u0000\u0000*%\u0001\u0000\u0000\u0000+.\u0001"+
		"\u0000\u0000\u0000,*\u0001\u0000\u0000\u0000,-\u0001\u0000\u0000\u0000"+
		"-\u0003\u0001\u0000\u0000\u0000.,\u0001\u0000\u0000\u0000/2\u0003\u0006"+
		"\u0003\u000002\u0003\b\u0004\u00001/\u0001\u0000\u0000\u000010\u0001\u0000"+
		"\u0000\u00002\u0005\u0001\u0000\u0000\u000034\u0005\t\u0000\u000049\u0005"+
		"\u000b\u0000\u000056\u0005\r\u0000\u000068\u0005\u000b\u0000\u000075\u0001"+
		"\u0000\u0000\u00008;\u0001\u0000\u0000\u000097\u0001\u0000\u0000\u0000"+
		"9:\u0001\u0000\u0000\u0000:\u0007\u0001\u0000\u0000\u0000;9\u0001\u0000"+
		"\u0000\u0000<=\u0005\n\u0000\u0000=B\u0005\u000b\u0000\u0000>?\u0005\r"+
		"\u0000\u0000?A\u0005\u000b\u0000\u0000@>\u0001\u0000\u0000\u0000AD\u0001"+
		"\u0000\u0000\u0000B@\u0001\u0000\u0000\u0000BC\u0001\u0000\u0000\u0000"+
		"C\t\u0001\u0000\u0000\u0000DB\u0001\u0000\u0000\u0000EH\u0003\u0012\t"+
		"\u0000FH\u0003\u0014\n\u0000GE\u0001\u0000\u0000\u0000GF\u0001\u0000\u0000"+
		"\u0000HI\u0001\u0000\u0000\u0000IJ\u0005\f\u0000\u0000J\u000b\u0001\u0000"+
		"\u0000\u0000KL\u0005\u0001\u0000\u0000LM\u0005\u0002\u0000\u0000MN\u0003"+
		"\u0016\u000b\u0000NO\u0005\u0003\u0000\u0000OS\u0005\u0004\u0000\u0000"+
		"PR\u0003\n\u0005\u0000QP\u0001\u0000\u0000\u0000RU\u0001\u0000\u0000\u0000"+
		"SQ\u0001\u0000\u0000\u0000ST\u0001\u0000\u0000\u0000TV\u0001\u0000\u0000"+
		"\u0000US\u0001\u0000\u0000\u0000V`\u0005\u0005\u0000\u0000WX\u0005\u0006"+
		"\u0000\u0000X\\\u0005\u0004\u0000\u0000Y[\u0003\n\u0005\u0000ZY\u0001"+
		"\u0000\u0000\u0000[^\u0001\u0000\u0000\u0000\\Z\u0001\u0000\u0000\u0000"+
		"\\]\u0001\u0000\u0000\u0000]_\u0001\u0000\u0000\u0000^\\\u0001\u0000\u0000"+
		"\u0000_a\u0005\u0005\u0000\u0000`W\u0001\u0000\u0000\u0000`a\u0001\u0000"+
		"\u0000\u0000a\r\u0001\u0000\u0000\u0000bc\u0005\u0007\u0000\u0000cd\u0005"+
		"\u0002\u0000\u0000de\u0003\u0016\u000b\u0000ef\u0005\u0003\u0000\u0000"+
		"fj\u0005\u0004\u0000\u0000gi\u0003\n\u0005\u0000hg\u0001\u0000\u0000\u0000"+
		"il\u0001\u0000\u0000\u0000jh\u0001\u0000\u0000\u0000jk\u0001\u0000\u0000"+
		"\u0000km\u0001\u0000\u0000\u0000lj\u0001\u0000\u0000\u0000mn\u0005\u0005"+
		"\u0000\u0000n\u000f\u0001\u0000\u0000\u0000op\u0007\u0000\u0000\u0000"+
		"p\u0011\u0001\u0000\u0000\u0000qr\u0005\u000b\u0000\u0000rs\u0005\u0015"+
		"\u0000\u0000st\u0003\u0018\f\u0000t\u0013\u0001\u0000\u0000\u0000uv\u0005"+
		"\u000b\u0000\u0000vw\u0007\u0001\u0000\u0000w\u0015\u0001\u0000\u0000"+
		"\u0000xy\u0003\u0010\b\u0000yz\u0005\u0016\u0000\u0000z{\u0003\u0010\b"+
		"\u0000{\u0017\u0001\u0000\u0000\u0000|\u0081\u0003\u0010\b\u0000}~\u0007"+
		"\u0002\u0000\u0000~\u0080\u0003\u0010\b\u0000\u007f}\u0001\u0000\u0000"+
		"\u0000\u0080\u0083\u0001\u0000\u0000\u0000\u0081\u007f\u0001\u0000\u0000"+
		"\u0000\u0081\u0082\u0001\u0000\u0000\u0000\u0082\u0019\u0001\u0000\u0000"+
		"\u0000\u0083\u0081\u0001\u0000\u0000\u0000\u0084\u0088\u0003\u0000\u0000"+
		"\u0000\u0085\u0088\u0003\f\u0006\u0000\u0086\u0088\u0003\u000e\u0007\u0000"+
		"\u0087\u0084\u0001\u0000\u0000\u0000\u0087\u0085\u0001\u0000\u0000\u0000"+
		"\u0087\u0086\u0001\u0000\u0000\u0000\u0088\u0089\u0001\u0000\u0000\u0000"+
		"\u0089\u008a\u0005\f\u0000\u0000\u008a\u008c\u0001\u0000\u0000\u0000\u008b"+
		"\u0087\u0001\u0000\u0000\u0000\u008c\u008f\u0001\u0000\u0000\u0000\u008d"+
		"\u008b\u0001\u0000\u0000\u0000\u008d\u008e\u0001\u0000\u0000\u0000\u008e"+
		"\u001b\u0001\u0000\u0000\u0000\u008f\u008d\u0001\u0000\u0000\u0000\u000f"+
		"\u001e#(,19BGS\\`j\u0081\u0087\u008d";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}