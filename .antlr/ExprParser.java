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
		CHAR_TYPE=1, INT_TYPE=2, FLOAT_TYPE=3, IDENTIFIER=4, SEMICOLON=5, COMMA=6, 
		WS=7, IDENTIFIER_LIST=8, ARRAY_DECLARATION=9;
	public static final int
		RULE_declaration = 0, RULE_char_declaration = 1, RULE_int_declaration = 2, 
		RULE_float_declaration = 3;
	private static String[] makeRuleNames() {
		return new String[] {
			"declaration", "char_declaration", "int_declaration", "float_declaration"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'char'", "'int'", "'float'", null, "';'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "CHAR_TYPE", "INT_TYPE", "FLOAT_TYPE", "IDENTIFIER", "SEMICOLON", 
			"COMMA", "WS", "IDENTIFIER_LIST", "ARRAY_DECLARATION"
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
		public TerminalNode SEMICOLON() { return getToken(ExprParser.SEMICOLON, 0); }
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
			setState(11);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CHAR_TYPE:
				{
				setState(8);
				char_declaration();
				}
				break;
			case INT_TYPE:
				{
				setState(9);
				int_declaration();
				}
				break;
			case FLOAT_TYPE:
				{
				setState(10);
				float_declaration();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(13);
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
	public static class Char_declarationContext extends ParserRuleContext {
		public TerminalNode CHAR_TYPE() { return getToken(ExprParser.CHAR_TYPE, 0); }
		public List<TerminalNode> IDENTIFIER() { return getTokens(ExprParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(ExprParser.IDENTIFIER, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(ExprParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ExprParser.COMMA, i);
		}
		public List<TerminalNode> ARRAY_DECLARATION() { return getTokens(ExprParser.ARRAY_DECLARATION); }
		public TerminalNode ARRAY_DECLARATION(int i) {
			return getToken(ExprParser.ARRAY_DECLARATION, i);
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
			setState(15);
			match(CHAR_TYPE);
			setState(32);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==IDENTIFIER) {
				{
				{
				setState(16);
				match(IDENTIFIER);
				setState(21);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(17);
					match(COMMA);
					setState(18);
					match(IDENTIFIER);
					}
					}
					setState(23);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(28);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ARRAY_DECLARATION) {
					{
					setState(24);
					match(ARRAY_DECLARATION);
					setState(26);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==COMMA) {
						{
						setState(25);
						match(COMMA);
						}
					}

					}
				}

				}
				}
				setState(34);
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
			setState(35);
			match(INT_TYPE);
			setState(36);
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
			setState(38);
			match(FLOAT_TYPE);
			setState(39);
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

	public static final String _serializedATN =
		"\u0004\u0001\t*\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0003\u0000\f\b\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0005\u0001\u0014\b\u0001\n\u0001\f\u0001"+
		"\u0017\t\u0001\u0001\u0001\u0001\u0001\u0003\u0001\u001b\b\u0001\u0003"+
		"\u0001\u001d\b\u0001\u0005\u0001\u001f\b\u0001\n\u0001\f\u0001\"\t\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0000\u0000\u0004\u0000\u0002\u0004\u0006\u0000\u0000+\u0000"+
		"\u000b\u0001\u0000\u0000\u0000\u0002\u000f\u0001\u0000\u0000\u0000\u0004"+
		"#\u0001\u0000\u0000\u0000\u0006&\u0001\u0000\u0000\u0000\b\f\u0003\u0002"+
		"\u0001\u0000\t\f\u0003\u0004\u0002\u0000\n\f\u0003\u0006\u0003\u0000\u000b"+
		"\b\u0001\u0000\u0000\u0000\u000b\t\u0001\u0000\u0000\u0000\u000b\n\u0001"+
		"\u0000\u0000\u0000\f\r\u0001\u0000\u0000\u0000\r\u000e\u0005\u0005\u0000"+
		"\u0000\u000e\u0001\u0001\u0000\u0000\u0000\u000f \u0005\u0001\u0000\u0000"+
		"\u0010\u0015\u0005\u0004\u0000\u0000\u0011\u0012\u0005\u0006\u0000\u0000"+
		"\u0012\u0014\u0005\u0004\u0000\u0000\u0013\u0011\u0001\u0000\u0000\u0000"+
		"\u0014\u0017\u0001\u0000\u0000\u0000\u0015\u0013\u0001\u0000\u0000\u0000"+
		"\u0015\u0016\u0001\u0000\u0000\u0000\u0016\u001c\u0001\u0000\u0000\u0000"+
		"\u0017\u0015\u0001\u0000\u0000\u0000\u0018\u001a\u0005\t\u0000\u0000\u0019"+
		"\u001b\u0005\u0006\u0000\u0000\u001a\u0019\u0001\u0000\u0000\u0000\u001a"+
		"\u001b\u0001\u0000\u0000\u0000\u001b\u001d\u0001\u0000\u0000\u0000\u001c"+
		"\u0018\u0001\u0000\u0000\u0000\u001c\u001d\u0001\u0000\u0000\u0000\u001d"+
		"\u001f\u0001\u0000\u0000\u0000\u001e\u0010\u0001\u0000\u0000\u0000\u001f"+
		"\"\u0001\u0000\u0000\u0000 \u001e\u0001\u0000\u0000\u0000 !\u0001\u0000"+
		"\u0000\u0000!\u0003\u0001\u0000\u0000\u0000\" \u0001\u0000\u0000\u0000"+
		"#$\u0005\u0002\u0000\u0000$%\u0005\b\u0000\u0000%\u0005\u0001\u0000\u0000"+
		"\u0000&\'\u0005\u0003\u0000\u0000\'(\u0005\b\u0000\u0000(\u0007\u0001"+
		"\u0000\u0000\u0000\u0005\u000b\u0015\u001a\u001c ";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}