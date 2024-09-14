// Generated from /Users/I557924/SAPDevelop/antlr/Expr.g4 by ANTLR 4.13.1
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
		FLOAT_TYPE=10, IDENTIFIER=11, SEMICOLON=12, COMMA=13, WS=14, NUMBER=15, 
		ADD_OP=16, SUB_OP=17, MUL_OP=18, DIV_OP=19, ASSIGN_OP=20, REL_OP=21, IDENTIFIER_LIST=22, 
		ARRAY_DECLARATION=23;
	public static final int
		RULE_declaration = 0, RULE_char_declaration = 1, RULE_int_declaration = 2, 
		RULE_float_declaration = 3, RULE_statement = 4, RULE_if_statement = 5, 
		RULE_while_statement = 6, RULE_assignment = 7, RULE_condition = 8, RULE_expression = 9, 
		RULE_term = 10, RULE_factor = 11, RULE_program = 12;
	private static String[] makeRuleNames() {
		return new String[] {
			"declaration", "char_declaration", "int_declaration", "float_declaration", 
			"statement", "if_statement", "while_statement", "assignment", "condition", 
			"expression", "term", "factor", "program"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'if'", "'('", "')'", "'{'", "'}'", "'else'", "'while'", "'char'", 
			"'int'", "'float'", null, "';'", "','", null, null, "'+'", "'-'", "'*'", 
			"'/'", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, "CHAR_TYPE", "INT_TYPE", 
			"FLOAT_TYPE", "IDENTIFIER", "SEMICOLON", "COMMA", "WS", "NUMBER", "ADD_OP", 
			"SUB_OP", "MUL_OP", "DIV_OP", "ASSIGN_OP", "REL_OP", "IDENTIFIER_LIST", 
			"ARRAY_DECLARATION"
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
		public Int_declarationContext int_declaration() {
			return getRuleContext(Int_declarationContext.class,0);
		}
		public Float_declarationContext float_declaration() {
			return getRuleContext(Float_declarationContext.class,0);
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
			setState(29);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CHAR_TYPE:
				{
				setState(26);
				char_declaration();
				}
				break;
			case INT_TYPE:
				{
				setState(27);
				int_declaration();
				}
				break;
			case FLOAT_TYPE:
				{
				setState(28);
				float_declaration();
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
		public List<TerminalNode> IDENTIFIER() { return getTokens(ExprParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(ExprParser.IDENTIFIER, i);
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
			setState(31);
			match(CHAR_TYPE);
			setState(32);
			match(IDENTIFIER);
			setState(34);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ARRAY_DECLARATION) {
				{
				setState(33);
				match(ARRAY_DECLARATION);
				}
			}

			setState(43);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(36);
				match(COMMA);
				setState(37);
				match(IDENTIFIER);
				setState(39);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ARRAY_DECLARATION) {
					{
					setState(38);
					match(ARRAY_DECLARATION);
					}
				}

				}
				}
				setState(45);
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
	public static class Int_declarationContext extends ParserRuleContext {
		public TerminalNode INT_TYPE() { return getToken(ExprParser.INT_TYPE, 0); }
		public TerminalNode IDENTIFIER_LIST() { return getToken(ExprParser.IDENTIFIER_LIST, 0); }
		public Int_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_int_declaration; }
	}

	public final Int_declarationContext int_declaration() throws RecognitionException {
		Int_declarationContext _localctx = new Int_declarationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_int_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			match(INT_TYPE);
			setState(47);
			match(IDENTIFIER_LIST);
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
		public TerminalNode IDENTIFIER_LIST() { return getToken(ExprParser.IDENTIFIER_LIST, 0); }
		public Float_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_float_declaration; }
	}

	public final Float_declarationContext float_declaration() throws RecognitionException {
		Float_declarationContext _localctx = new Float_declarationContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_float_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(49);
			match(FLOAT_TYPE);
			setState(50);
			match(IDENTIFIER_LIST);
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
	public static class StatementContext extends ParserRuleContext {
		public TerminalNode SEMICOLON() { return getToken(ExprParser.SEMICOLON, 0); }
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public If_statementContext if_statement() {
			return getRuleContext(If_statementContext.class,0);
		}
		public While_statementContext while_statement() {
			return getRuleContext(While_statementContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(56);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CHAR_TYPE:
			case INT_TYPE:
			case FLOAT_TYPE:
				{
				setState(52);
				declaration();
				}
				break;
			case T__0:
				{
				setState(53);
				if_statement();
				}
				break;
			case T__6:
				{
				setState(54);
				while_statement();
				}
				break;
			case IDENTIFIER:
				{
				setState(55);
				assignment();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(58);
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
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public If_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_statement; }
	}

	public final If_statementContext if_statement() throws RecognitionException {
		If_statementContext _localctx = new If_statementContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_if_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			match(T__0);
			setState(61);
			match(T__1);
			setState(62);
			condition();
			setState(63);
			match(T__2);
			setState(64);
			match(T__3);
			setState(68);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3970L) != 0)) {
				{
				{
				setState(65);
				statement();
				}
				}
				setState(70);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(71);
			match(T__4);
			setState(81);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__5) {
				{
				setState(72);
				match(T__5);
				setState(73);
				match(T__3);
				setState(77);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3970L) != 0)) {
					{
					{
					setState(74);
					statement();
					}
					}
					setState(79);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(80);
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
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public While_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_statement; }
	}

	public final While_statementContext while_statement() throws RecognitionException {
		While_statementContext _localctx = new While_statementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_while_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			match(T__6);
			setState(84);
			match(T__1);
			setState(85);
			condition();
			setState(86);
			match(T__2);
			setState(87);
			match(T__3);
			setState(91);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3970L) != 0)) {
				{
				{
				setState(88);
				statement();
				}
				}
				setState(93);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(94);
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
	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(ExprParser.IDENTIFIER, 0); }
		public TerminalNode ASSIGN_OP() { return getToken(ExprParser.ASSIGN_OP, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(96);
			match(IDENTIFIER);
			setState(97);
			match(ASSIGN_OP);
			setState(98);
			expression();
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
	public static class ConditionContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode REL_OP() { return getToken(ExprParser.REL_OP, 0); }
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(100);
			expression();
			setState(101);
			match(REL_OP);
			setState(102);
			expression();
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
	public static class ExpressionContext extends ParserRuleContext {
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public List<TerminalNode> ADD_OP() { return getTokens(ExprParser.ADD_OP); }
		public TerminalNode ADD_OP(int i) {
			return getToken(ExprParser.ADD_OP, i);
		}
		public List<TerminalNode> SUB_OP() { return getTokens(ExprParser.SUB_OP); }
		public TerminalNode SUB_OP(int i) {
			return getToken(ExprParser.SUB_OP, i);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			term();
			setState(109);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ADD_OP || _la==SUB_OP) {
				{
				{
				setState(105);
				_la = _input.LA(1);
				if ( !(_la==ADD_OP || _la==SUB_OP) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(106);
				term();
				}
				}
				setState(111);
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
	public static class TermContext extends ParserRuleContext {
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public List<TerminalNode> MUL_OP() { return getTokens(ExprParser.MUL_OP); }
		public TerminalNode MUL_OP(int i) {
			return getToken(ExprParser.MUL_OP, i);
		}
		public List<TerminalNode> DIV_OP() { return getTokens(ExprParser.DIV_OP); }
		public TerminalNode DIV_OP(int i) {
			return getToken(ExprParser.DIV_OP, i);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			factor();
			setState(117);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==MUL_OP || _la==DIV_OP) {
				{
				{
				setState(113);
				_la = _input.LA(1);
				if ( !(_la==MUL_OP || _la==DIV_OP) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(114);
				factor();
				}
				}
				setState(119);
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
	public static class FactorContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(ExprParser.IDENTIFIER, 0); }
		public TerminalNode NUMBER() { return getToken(ExprParser.NUMBER, 0); }
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_factor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			_la = _input.LA(1);
			if ( !(_la==IDENTIFIER || _la==NUMBER) ) {
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
	public static class ProgramContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3970L) != 0)) {
				{
				{
				setState(122);
				statement();
				}
				}
				setState(127);
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
		"\u0004\u0001\u0017\u0081\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0001\u0000\u0001\u0000\u0001\u0000\u0003\u0000\u001e"+
		"\b\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001#\b\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0003\u0001(\b\u0001\u0005\u0001*\b\u0001"+
		"\n\u0001\f\u0001-\t\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0003\u00049\b\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0005\u0005C\b\u0005"+
		"\n\u0005\f\u0005F\t\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0005\u0005L\b\u0005\n\u0005\f\u0005O\t\u0005\u0001\u0005\u0003\u0005"+
		"R\b\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0005\u0006Z\b\u0006\n\u0006\f\u0006]\t\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0005\tl\b\t\n\t\f\to\t\t\u0001"+
		"\n\u0001\n\u0001\n\u0005\nt\b\n\n\n\f\nw\t\n\u0001\u000b\u0001\u000b\u0001"+
		"\f\u0005\f|\b\f\n\f\f\f\u007f\t\f\u0001\f\u0000\u0000\r\u0000\u0002\u0004"+
		"\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u0000\u0003\u0001\u0000"+
		"\u0010\u0011\u0001\u0000\u0012\u0013\u0002\u0000\u000b\u000b\u000f\u000f"+
		"\u0082\u0000\u001d\u0001\u0000\u0000\u0000\u0002\u001f\u0001\u0000\u0000"+
		"\u0000\u0004.\u0001\u0000\u0000\u0000\u00061\u0001\u0000\u0000\u0000\b"+
		"8\u0001\u0000\u0000\u0000\n<\u0001\u0000\u0000\u0000\fS\u0001\u0000\u0000"+
		"\u0000\u000e`\u0001\u0000\u0000\u0000\u0010d\u0001\u0000\u0000\u0000\u0012"+
		"h\u0001\u0000\u0000\u0000\u0014p\u0001\u0000\u0000\u0000\u0016x\u0001"+
		"\u0000\u0000\u0000\u0018}\u0001\u0000\u0000\u0000\u001a\u001e\u0003\u0002"+
		"\u0001\u0000\u001b\u001e\u0003\u0004\u0002\u0000\u001c\u001e\u0003\u0006"+
		"\u0003\u0000\u001d\u001a\u0001\u0000\u0000\u0000\u001d\u001b\u0001\u0000"+
		"\u0000\u0000\u001d\u001c\u0001\u0000\u0000\u0000\u001e\u0001\u0001\u0000"+
		"\u0000\u0000\u001f \u0005\b\u0000\u0000 \"\u0005\u000b\u0000\u0000!#\u0005"+
		"\u0017\u0000\u0000\"!\u0001\u0000\u0000\u0000\"#\u0001\u0000\u0000\u0000"+
		"#+\u0001\u0000\u0000\u0000$%\u0005\r\u0000\u0000%\'\u0005\u000b\u0000"+
		"\u0000&(\u0005\u0017\u0000\u0000\'&\u0001\u0000\u0000\u0000\'(\u0001\u0000"+
		"\u0000\u0000(*\u0001\u0000\u0000\u0000)$\u0001\u0000\u0000\u0000*-\u0001"+
		"\u0000\u0000\u0000+)\u0001\u0000\u0000\u0000+,\u0001\u0000\u0000\u0000"+
		",\u0003\u0001\u0000\u0000\u0000-+\u0001\u0000\u0000\u0000./\u0005\t\u0000"+
		"\u0000/0\u0005\u0016\u0000\u00000\u0005\u0001\u0000\u0000\u000012\u0005"+
		"\n\u0000\u000023\u0005\u0016\u0000\u00003\u0007\u0001\u0000\u0000\u0000"+
		"49\u0003\u0000\u0000\u000059\u0003\n\u0005\u000069\u0003\f\u0006\u0000"+
		"79\u0003\u000e\u0007\u000084\u0001\u0000\u0000\u000085\u0001\u0000\u0000"+
		"\u000086\u0001\u0000\u0000\u000087\u0001\u0000\u0000\u00009:\u0001\u0000"+
		"\u0000\u0000:;\u0005\f\u0000\u0000;\t\u0001\u0000\u0000\u0000<=\u0005"+
		"\u0001\u0000\u0000=>\u0005\u0002\u0000\u0000>?\u0003\u0010\b\u0000?@\u0005"+
		"\u0003\u0000\u0000@D\u0005\u0004\u0000\u0000AC\u0003\b\u0004\u0000BA\u0001"+
		"\u0000\u0000\u0000CF\u0001\u0000\u0000\u0000DB\u0001\u0000\u0000\u0000"+
		"DE\u0001\u0000\u0000\u0000EG\u0001\u0000\u0000\u0000FD\u0001\u0000\u0000"+
		"\u0000GQ\u0005\u0005\u0000\u0000HI\u0005\u0006\u0000\u0000IM\u0005\u0004"+
		"\u0000\u0000JL\u0003\b\u0004\u0000KJ\u0001\u0000\u0000\u0000LO\u0001\u0000"+
		"\u0000\u0000MK\u0001\u0000\u0000\u0000MN\u0001\u0000\u0000\u0000NP\u0001"+
		"\u0000\u0000\u0000OM\u0001\u0000\u0000\u0000PR\u0005\u0005\u0000\u0000"+
		"QH\u0001\u0000\u0000\u0000QR\u0001\u0000\u0000\u0000R\u000b\u0001\u0000"+
		"\u0000\u0000ST\u0005\u0007\u0000\u0000TU\u0005\u0002\u0000\u0000UV\u0003"+
		"\u0010\b\u0000VW\u0005\u0003\u0000\u0000W[\u0005\u0004\u0000\u0000XZ\u0003"+
		"\b\u0004\u0000YX\u0001\u0000\u0000\u0000Z]\u0001\u0000\u0000\u0000[Y\u0001"+
		"\u0000\u0000\u0000[\\\u0001\u0000\u0000\u0000\\^\u0001\u0000\u0000\u0000"+
		"][\u0001\u0000\u0000\u0000^_\u0005\u0005\u0000\u0000_\r\u0001\u0000\u0000"+
		"\u0000`a\u0005\u000b\u0000\u0000ab\u0005\u0014\u0000\u0000bc\u0003\u0012"+
		"\t\u0000c\u000f\u0001\u0000\u0000\u0000de\u0003\u0012\t\u0000ef\u0005"+
		"\u0015\u0000\u0000fg\u0003\u0012\t\u0000g\u0011\u0001\u0000\u0000\u0000"+
		"hm\u0003\u0014\n\u0000ij\u0007\u0000\u0000\u0000jl\u0003\u0014\n\u0000"+
		"ki\u0001\u0000\u0000\u0000lo\u0001\u0000\u0000\u0000mk\u0001\u0000\u0000"+
		"\u0000mn\u0001\u0000\u0000\u0000n\u0013\u0001\u0000\u0000\u0000om\u0001"+
		"\u0000\u0000\u0000pu\u0003\u0016\u000b\u0000qr\u0007\u0001\u0000\u0000"+
		"rt\u0003\u0016\u000b\u0000sq\u0001\u0000\u0000\u0000tw\u0001\u0000\u0000"+
		"\u0000us\u0001\u0000\u0000\u0000uv\u0001\u0000\u0000\u0000v\u0015\u0001"+
		"\u0000\u0000\u0000wu\u0001\u0000\u0000\u0000xy\u0007\u0002\u0000\u0000"+
		"y\u0017\u0001\u0000\u0000\u0000z|\u0003\b\u0004\u0000{z\u0001\u0000\u0000"+
		"\u0000|\u007f\u0001\u0000\u0000\u0000}{\u0001\u0000\u0000\u0000}~\u0001"+
		"\u0000\u0000\u0000~\u0019\u0001\u0000\u0000\u0000\u007f}\u0001\u0000\u0000"+
		"\u0000\f\u001d\"\'+8DMQ[mu}";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}