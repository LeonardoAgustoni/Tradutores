// Generated from /Users/I557924/SAPDevelop/antlr/Expr.g4 by ANTLR 4.13.1
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
		CHAR_TYPE=1, INT_TYPE=2, FLOAT_TYPE=3, IDENTIFIER=4, SEMICOLON=5, COMMA=6, 
		WS=7, IDENTIFIER_LIST=8, ARRAY_DECLARATION=9;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"CHAR_TYPE", "INT_TYPE", "FLOAT_TYPE", "IDENTIFIER", "SEMICOLON", "COMMA", 
			"WS", "IDENTIFIER_LIST", "ARRAY_DECLARATION"
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
		"\u0004\u0000\tE\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0003\u0001\u0003\u0005\u0003%\b\u0003\n\u0003\f\u0003(\t\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0004\u0006/\b"+
		"\u0006\u000b\u0006\f\u00060\u0001\u0006\u0001\u0006\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0005\u00079\b\u0007\n\u0007\f\u0007<\t"+
		"\u0007\u0001\b\u0001\b\u0004\b@\b\b\u000b\b\f\bA\u0001\b\u0001\b\u0000"+
		"\u0000\t\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b"+
		"\u0006\r\u0007\u000f\b\u0011\t\u0001\u0000\u0004\u0003\u0000AZ__az\u0004"+
		"\u000009AZ__az\u0003\u0000\t\n\r\r  \u0001\u000009H\u0000\u0001\u0001"+
		"\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001"+
		"\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000"+
		"\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000"+
		"\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000"+
		"\u0000\u0001\u0013\u0001\u0000\u0000\u0000\u0003\u0018\u0001\u0000\u0000"+
		"\u0000\u0005\u001c\u0001\u0000\u0000\u0000\u0007\"\u0001\u0000\u0000\u0000"+
		"\t)\u0001\u0000\u0000\u0000\u000b+\u0001\u0000\u0000\u0000\r.\u0001\u0000"+
		"\u0000\u0000\u000f4\u0001\u0000\u0000\u0000\u0011=\u0001\u0000\u0000\u0000"+
		"\u0013\u0014\u0005c\u0000\u0000\u0014\u0015\u0005h\u0000\u0000\u0015\u0016"+
		"\u0005a\u0000\u0000\u0016\u0017\u0005r\u0000\u0000\u0017\u0002\u0001\u0000"+
		"\u0000\u0000\u0018\u0019\u0005i\u0000\u0000\u0019\u001a\u0005n\u0000\u0000"+
		"\u001a\u001b\u0005t\u0000\u0000\u001b\u0004\u0001\u0000\u0000\u0000\u001c"+
		"\u001d\u0005f\u0000\u0000\u001d\u001e\u0005l\u0000\u0000\u001e\u001f\u0005"+
		"o\u0000\u0000\u001f \u0005a\u0000\u0000 !\u0005t\u0000\u0000!\u0006\u0001"+
		"\u0000\u0000\u0000\"&\u0007\u0000\u0000\u0000#%\u0007\u0001\u0000\u0000"+
		"$#\u0001\u0000\u0000\u0000%(\u0001\u0000\u0000\u0000&$\u0001\u0000\u0000"+
		"\u0000&\'\u0001\u0000\u0000\u0000\'\b\u0001\u0000\u0000\u0000(&\u0001"+
		"\u0000\u0000\u0000)*\u0005;\u0000\u0000*\n\u0001\u0000\u0000\u0000+,\u0005"+
		",\u0000\u0000,\f\u0001\u0000\u0000\u0000-/\u0007\u0002\u0000\u0000.-\u0001"+
		"\u0000\u0000\u0000/0\u0001\u0000\u0000\u00000.\u0001\u0000\u0000\u0000"+
		"01\u0001\u0000\u0000\u000012\u0001\u0000\u0000\u000023\u0006\u0006\u0000"+
		"\u00003\u000e\u0001\u0000\u0000\u00004:\u0003\u0007\u0003\u000056\u0003"+
		"\u000b\u0005\u000067\u0003\u0007\u0003\u000079\u0001\u0000\u0000\u0000"+
		"85\u0001\u0000\u0000\u00009<\u0001\u0000\u0000\u0000:8\u0001\u0000\u0000"+
		"\u0000:;\u0001\u0000\u0000\u0000;\u0010\u0001\u0000\u0000\u0000<:\u0001"+
		"\u0000\u0000\u0000=?\u0005[\u0000\u0000>@\u0007\u0003\u0000\u0000?>\u0001"+
		"\u0000\u0000\u0000@A\u0001\u0000\u0000\u0000A?\u0001\u0000\u0000\u0000"+
		"AB\u0001\u0000\u0000\u0000BC\u0001\u0000\u0000\u0000CD\u0005]\u0000\u0000"+
		"D\u0012\u0001\u0000\u0000\u0000\u0005\u0000&0:A\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}