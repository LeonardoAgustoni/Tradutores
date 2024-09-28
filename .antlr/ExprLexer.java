// Generated from /Users/I557924/Library/CloudStorage/OneDrive-Personal/Estudos/UNISINOS/antlr/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class ExprLexer extends Lexer {
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
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "CHAR_TYPE", 
			"INT_TYPE", "FLOAT_TYPE", "IdentVarSimples", "SEMICOLON", "COMMA", "WS", 
			"NUMBER", "NUMBER_NOT_ZERO", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", 
			"OPERADOR_ATRIBUICAO", "OPERADOR_RELACIONAL", "INCREMENTO", "DECREMENTO", 
			"ARRAY_DECLARATION", "TipoSimples"
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


	public ExprLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Expr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u001a\u00a9\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017"+
		"\u0002\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\n\u0001\n\u0005\n]\b\n\n\n\f\n`\t\n\u0001\u000b"+
		"\u0001\u000b\u0001\f\u0001\f\u0001\r\u0004\rg\b\r\u000b\r\f\rh\u0001\r"+
		"\u0001\r\u0001\u000e\u0004\u000en\b\u000e\u000b\u000e\f\u000eo\u0001\u000f"+
		"\u0001\u000f\u0005\u000ft\b\u000f\n\u000f\f\u000fw\t\u000f\u0001\u0010"+
		"\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0013"+
		"\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0003\u0014\u008a\b\u0014"+
		"\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0003\u0015\u0096\b\u0015"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0018\u0001\u0018\u0004\u0018\u00a0\b\u0018\u000b\u0018\f\u0018"+
		"\u00a1\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0003\u0019\u00a8"+
		"\b\u0019\u0000\u0000\u001a\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004"+
		"\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017"+
		"\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'"+
		"\u0014)\u0015+\u0016-\u0017/\u00181\u00193\u001a\u0001\u0000\u0005\u0003"+
		"\u0000AZ__az\u0004\u000009AZ__az\u0003\u0000\t\n\r\r  \u0001\u000009\u0001"+
		"\u000019\u00b7\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000"+
		"\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000"+
		"\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000"+
		"\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000"+
		"\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000"+
		"\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000"+
		"\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000"+
		"\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000"+
		"\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%"+
		"\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001"+
		"\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000"+
		"\u0000\u0000/\u0001\u0000\u0000\u0000\u00001\u0001\u0000\u0000\u0000\u0000"+
		"3\u0001\u0000\u0000\u0000\u00015\u0001\u0000\u0000\u0000\u00038\u0001"+
		"\u0000\u0000\u0000\u0005:\u0001\u0000\u0000\u0000\u0007<\u0001\u0000\u0000"+
		"\u0000\t>\u0001\u0000\u0000\u0000\u000b@\u0001\u0000\u0000\u0000\rE\u0001"+
		"\u0000\u0000\u0000\u000fK\u0001\u0000\u0000\u0000\u0011P\u0001\u0000\u0000"+
		"\u0000\u0013T\u0001\u0000\u0000\u0000\u0015Z\u0001\u0000\u0000\u0000\u0017"+
		"a\u0001\u0000\u0000\u0000\u0019c\u0001\u0000\u0000\u0000\u001bf\u0001"+
		"\u0000\u0000\u0000\u001dm\u0001\u0000\u0000\u0000\u001fq\u0001\u0000\u0000"+
		"\u0000!x\u0001\u0000\u0000\u0000#z\u0001\u0000\u0000\u0000%|\u0001\u0000"+
		"\u0000\u0000\'~\u0001\u0000\u0000\u0000)\u0089\u0001\u0000\u0000\u0000"+
		"+\u0095\u0001\u0000\u0000\u0000-\u0097\u0001\u0000\u0000\u0000/\u009a"+
		"\u0001\u0000\u0000\u00001\u009d\u0001\u0000\u0000\u00003\u00a7\u0001\u0000"+
		"\u0000\u000056\u0005i\u0000\u000067\u0005f\u0000\u00007\u0002\u0001\u0000"+
		"\u0000\u000089\u0005(\u0000\u00009\u0004\u0001\u0000\u0000\u0000:;\u0005"+
		")\u0000\u0000;\u0006\u0001\u0000\u0000\u0000<=\u0005{\u0000\u0000=\b\u0001"+
		"\u0000\u0000\u0000>?\u0005}\u0000\u0000?\n\u0001\u0000\u0000\u0000@A\u0005"+
		"e\u0000\u0000AB\u0005l\u0000\u0000BC\u0005s\u0000\u0000CD\u0005e\u0000"+
		"\u0000D\f\u0001\u0000\u0000\u0000EF\u0005w\u0000\u0000FG\u0005h\u0000"+
		"\u0000GH\u0005i\u0000\u0000HI\u0005l\u0000\u0000IJ\u0005e\u0000\u0000"+
		"J\u000e\u0001\u0000\u0000\u0000KL\u0005c\u0000\u0000LM\u0005h\u0000\u0000"+
		"MN\u0005a\u0000\u0000NO\u0005r\u0000\u0000O\u0010\u0001\u0000\u0000\u0000"+
		"PQ\u0005i\u0000\u0000QR\u0005n\u0000\u0000RS\u0005t\u0000\u0000S\u0012"+
		"\u0001\u0000\u0000\u0000TU\u0005f\u0000\u0000UV\u0005l\u0000\u0000VW\u0005"+
		"o\u0000\u0000WX\u0005a\u0000\u0000XY\u0005t\u0000\u0000Y\u0014\u0001\u0000"+
		"\u0000\u0000Z^\u0007\u0000\u0000\u0000[]\u0007\u0001\u0000\u0000\\[\u0001"+
		"\u0000\u0000\u0000]`\u0001\u0000\u0000\u0000^\\\u0001\u0000\u0000\u0000"+
		"^_\u0001\u0000\u0000\u0000_\u0016\u0001\u0000\u0000\u0000`^\u0001\u0000"+
		"\u0000\u0000ab\u0005;\u0000\u0000b\u0018\u0001\u0000\u0000\u0000cd\u0005"+
		",\u0000\u0000d\u001a\u0001\u0000\u0000\u0000eg\u0007\u0002\u0000\u0000"+
		"fe\u0001\u0000\u0000\u0000gh\u0001\u0000\u0000\u0000hf\u0001\u0000\u0000"+
		"\u0000hi\u0001\u0000\u0000\u0000ij\u0001\u0000\u0000\u0000jk\u0006\r\u0000"+
		"\u0000k\u001c\u0001\u0000\u0000\u0000ln\u0007\u0003\u0000\u0000ml\u0001"+
		"\u0000\u0000\u0000no\u0001\u0000\u0000\u0000om\u0001\u0000\u0000\u0000"+
		"op\u0001\u0000\u0000\u0000p\u001e\u0001\u0000\u0000\u0000qu\u0007\u0004"+
		"\u0000\u0000rt\u0007\u0003\u0000\u0000sr\u0001\u0000\u0000\u0000tw\u0001"+
		"\u0000\u0000\u0000us\u0001\u0000\u0000\u0000uv\u0001\u0000\u0000\u0000"+
		"v \u0001\u0000\u0000\u0000wu\u0001\u0000\u0000\u0000xy\u0005+\u0000\u0000"+
		"y\"\u0001\u0000\u0000\u0000z{\u0005-\u0000\u0000{$\u0001\u0000\u0000\u0000"+
		"|}\u0005*\u0000\u0000}&\u0001\u0000\u0000\u0000~\u007f\u0005/\u0000\u0000"+
		"\u007f(\u0001\u0000\u0000\u0000\u0080\u008a\u0005=\u0000\u0000\u0081\u0082"+
		"\u0005+\u0000\u0000\u0082\u008a\u0005=\u0000\u0000\u0083\u0084\u0005-"+
		"\u0000\u0000\u0084\u008a\u0005=\u0000\u0000\u0085\u0086\u0005*\u0000\u0000"+
		"\u0086\u008a\u0005=\u0000\u0000\u0087\u0088\u0005/\u0000\u0000\u0088\u008a"+
		"\u0005=\u0000\u0000\u0089\u0080\u0001\u0000\u0000\u0000\u0089\u0081\u0001"+
		"\u0000\u0000\u0000\u0089\u0083\u0001\u0000\u0000\u0000\u0089\u0085\u0001"+
		"\u0000\u0000\u0000\u0089\u0087\u0001\u0000\u0000\u0000\u008a*\u0001\u0000"+
		"\u0000\u0000\u008b\u008c\u0005=\u0000\u0000\u008c\u0096\u0005=\u0000\u0000"+
		"\u008d\u008e\u0005!\u0000\u0000\u008e\u0096\u0005=\u0000\u0000\u008f\u0096"+
		"\u0005<\u0000\u0000\u0090\u0091\u0005<\u0000\u0000\u0091\u0096\u0005="+
		"\u0000\u0000\u0092\u0096\u0005>\u0000\u0000\u0093\u0094\u0005>\u0000\u0000"+
		"\u0094\u0096\u0005=\u0000\u0000\u0095\u008b\u0001\u0000\u0000\u0000\u0095"+
		"\u008d\u0001\u0000\u0000\u0000\u0095\u008f\u0001\u0000\u0000\u0000\u0095"+
		"\u0090\u0001\u0000\u0000\u0000\u0095\u0092\u0001\u0000\u0000\u0000\u0095"+
		"\u0093\u0001\u0000\u0000\u0000\u0096,\u0001\u0000\u0000\u0000\u0097\u0098"+
		"\u0005+\u0000\u0000\u0098\u0099\u0005+\u0000\u0000\u0099.\u0001\u0000"+
		"\u0000\u0000\u009a\u009b\u0005-\u0000\u0000\u009b\u009c\u0005-\u0000\u0000"+
		"\u009c0\u0001\u0000\u0000\u0000\u009d\u009f\u0005[\u0000\u0000\u009e\u00a0"+
		"\u0003\u001f\u000f\u0000\u009f\u009e\u0001\u0000\u0000\u0000\u00a0\u00a1"+
		"\u0001\u0000\u0000\u0000\u00a1\u009f\u0001\u0000\u0000\u0000\u00a1\u00a2"+
		"\u0001\u0000\u0000\u0000\u00a2\u00a3\u0001\u0000\u0000\u0000\u00a3\u00a4"+
		"\u0005]\u0000\u0000\u00a42\u0001\u0000\u0000\u0000\u00a5\u00a8\u0003\u0011"+
		"\b\u0000\u00a6\u00a8\u0003\u0013\t\u0000\u00a7\u00a5\u0001\u0000\u0000"+
		"\u0000\u00a7\u00a6\u0001\u0000\u0000\u0000\u00a84\u0001\u0000\u0000\u0000"+
		"\t\u0000^hou\u0089\u0095\u00a1\u00a7\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}