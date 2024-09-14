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
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, CHAR_TYPE=8, INT_TYPE=9, 
		FLOAT_TYPE=10, IDENTIFIER=11, SEMICOLON=12, COMMA=13, WS=14, NUMBER=15, 
		ADD_OP=16, SUB_OP=17, MUL_OP=18, DIV_OP=19, ASSIGN_OP=20, REL_OP=21, IDENTIFIER_LIST=22, 
		ARRAY_DECLARATION=23;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "CHAR_TYPE", 
			"INT_TYPE", "FLOAT_TYPE", "IDENTIFIER", "SEMICOLON", "COMMA", "WS", "NUMBER", 
			"ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "ASSIGN_OP", "REL_OP", "IDENTIFIER_LIST", 
			"ARRAY_DECLARATION"
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
		"\u0004\u0000\u0017\u0092\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\n\u0001\n\u0005\nW\b\n\n\n\f\nZ\t\n\u0001\u000b"+
		"\u0001\u000b\u0001\f\u0001\f\u0001\r\u0004\ra\b\r\u000b\r\f\rb\u0001\r"+
		"\u0001\r\u0001\u000e\u0004\u000eh\b\u000e\u000b\u000e\f\u000ei\u0001\u000f"+
		"\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012"+
		"\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0003\u0014\u0080\b\u0014\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0005\u0015\u0086\b\u0015\n\u0015\f\u0015\u0089\t\u0015\u0001"+
		"\u0016\u0001\u0016\u0004\u0016\u008d\b\u0016\u000b\u0016\f\u0016\u008e"+
		"\u0001\u0016\u0001\u0016\u0000\u0000\u0017\u0001\u0001\u0003\u0002\u0005"+
		"\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n"+
		"\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011"+
		"#\u0012%\u0013\'\u0014)\u0015+\u0016-\u0017\u0001\u0000\u0004\u0003\u0000"+
		"AZ__az\u0004\u000009AZ__az\u0003\u0000\t\n\r\r  \u0001\u000009\u009b\u0000"+
		"\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000"+
		"\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000"+
		"\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r"+
		"\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011"+
		"\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015"+
		"\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019"+
		"\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d"+
		"\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001"+
		"\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000"+
		"\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000"+
		"\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000\u0000\u0001/"+
		"\u0001\u0000\u0000\u0000\u00032\u0001\u0000\u0000\u0000\u00054\u0001\u0000"+
		"\u0000\u0000\u00076\u0001\u0000\u0000\u0000\t8\u0001\u0000\u0000\u0000"+
		"\u000b:\u0001\u0000\u0000\u0000\r?\u0001\u0000\u0000\u0000\u000fE\u0001"+
		"\u0000\u0000\u0000\u0011J\u0001\u0000\u0000\u0000\u0013N\u0001\u0000\u0000"+
		"\u0000\u0015T\u0001\u0000\u0000\u0000\u0017[\u0001\u0000\u0000\u0000\u0019"+
		"]\u0001\u0000\u0000\u0000\u001b`\u0001\u0000\u0000\u0000\u001dg\u0001"+
		"\u0000\u0000\u0000\u001fk\u0001\u0000\u0000\u0000!m\u0001\u0000\u0000"+
		"\u0000#o\u0001\u0000\u0000\u0000%q\u0001\u0000\u0000\u0000\'s\u0001\u0000"+
		"\u0000\u0000)\u007f\u0001\u0000\u0000\u0000+\u0081\u0001\u0000\u0000\u0000"+
		"-\u008a\u0001\u0000\u0000\u0000/0\u0005i\u0000\u000001\u0005f\u0000\u0000"+
		"1\u0002\u0001\u0000\u0000\u000023\u0005(\u0000\u00003\u0004\u0001\u0000"+
		"\u0000\u000045\u0005)\u0000\u00005\u0006\u0001\u0000\u0000\u000067\u0005"+
		"{\u0000\u00007\b\u0001\u0000\u0000\u000089\u0005}\u0000\u00009\n\u0001"+
		"\u0000\u0000\u0000:;\u0005e\u0000\u0000;<\u0005l\u0000\u0000<=\u0005s"+
		"\u0000\u0000=>\u0005e\u0000\u0000>\f\u0001\u0000\u0000\u0000?@\u0005w"+
		"\u0000\u0000@A\u0005h\u0000\u0000AB\u0005i\u0000\u0000BC\u0005l\u0000"+
		"\u0000CD\u0005e\u0000\u0000D\u000e\u0001\u0000\u0000\u0000EF\u0005c\u0000"+
		"\u0000FG\u0005h\u0000\u0000GH\u0005a\u0000\u0000HI\u0005r\u0000\u0000"+
		"I\u0010\u0001\u0000\u0000\u0000JK\u0005i\u0000\u0000KL\u0005n\u0000\u0000"+
		"LM\u0005t\u0000\u0000M\u0012\u0001\u0000\u0000\u0000NO\u0005f\u0000\u0000"+
		"OP\u0005l\u0000\u0000PQ\u0005o\u0000\u0000QR\u0005a\u0000\u0000RS\u0005"+
		"t\u0000\u0000S\u0014\u0001\u0000\u0000\u0000TX\u0007\u0000\u0000\u0000"+
		"UW\u0007\u0001\u0000\u0000VU\u0001\u0000\u0000\u0000WZ\u0001\u0000\u0000"+
		"\u0000XV\u0001\u0000\u0000\u0000XY\u0001\u0000\u0000\u0000Y\u0016\u0001"+
		"\u0000\u0000\u0000ZX\u0001\u0000\u0000\u0000[\\\u0005;\u0000\u0000\\\u0018"+
		"\u0001\u0000\u0000\u0000]^\u0005,\u0000\u0000^\u001a\u0001\u0000\u0000"+
		"\u0000_a\u0007\u0002\u0000\u0000`_\u0001\u0000\u0000\u0000ab\u0001\u0000"+
		"\u0000\u0000b`\u0001\u0000\u0000\u0000bc\u0001\u0000\u0000\u0000cd\u0001"+
		"\u0000\u0000\u0000de\u0006\r\u0000\u0000e\u001c\u0001\u0000\u0000\u0000"+
		"fh\u0007\u0003\u0000\u0000gf\u0001\u0000\u0000\u0000hi\u0001\u0000\u0000"+
		"\u0000ig\u0001\u0000\u0000\u0000ij\u0001\u0000\u0000\u0000j\u001e\u0001"+
		"\u0000\u0000\u0000kl\u0005+\u0000\u0000l \u0001\u0000\u0000\u0000mn\u0005"+
		"-\u0000\u0000n\"\u0001\u0000\u0000\u0000op\u0005*\u0000\u0000p$\u0001"+
		"\u0000\u0000\u0000qr\u0005/\u0000\u0000r&\u0001\u0000\u0000\u0000st\u0005"+
		"=\u0000\u0000t(\u0001\u0000\u0000\u0000uv\u0005=\u0000\u0000v\u0080\u0005"+
		"=\u0000\u0000wx\u0005!\u0000\u0000x\u0080\u0005=\u0000\u0000y\u0080\u0005"+
		"<\u0000\u0000z{\u0005<\u0000\u0000{\u0080\u0005=\u0000\u0000|\u0080\u0005"+
		">\u0000\u0000}~\u0005>\u0000\u0000~\u0080\u0005=\u0000\u0000\u007fu\u0001"+
		"\u0000\u0000\u0000\u007fw\u0001\u0000\u0000\u0000\u007fy\u0001\u0000\u0000"+
		"\u0000\u007fz\u0001\u0000\u0000\u0000\u007f|\u0001\u0000\u0000\u0000\u007f"+
		"}\u0001\u0000\u0000\u0000\u0080*\u0001\u0000\u0000\u0000\u0081\u0087\u0003"+
		"\u0015\n\u0000\u0082\u0083\u0003\u0019\f\u0000\u0083\u0084\u0003\u0015"+
		"\n\u0000\u0084\u0086\u0001\u0000\u0000\u0000\u0085\u0082\u0001\u0000\u0000"+
		"\u0000\u0086\u0089\u0001\u0000\u0000\u0000\u0087\u0085\u0001\u0000\u0000"+
		"\u0000\u0087\u0088\u0001\u0000\u0000\u0000\u0088,\u0001\u0000\u0000\u0000"+
		"\u0089\u0087\u0001\u0000\u0000\u0000\u008a\u008c\u0005[\u0000\u0000\u008b"+
		"\u008d\u0007\u0003\u0000\u0000\u008c\u008b\u0001\u0000\u0000\u0000\u008d"+
		"\u008e\u0001\u0000\u0000\u0000\u008e\u008c\u0001\u0000\u0000\u0000\u008e"+
		"\u008f\u0001\u0000\u0000\u0000\u008f\u0090\u0001\u0000\u0000\u0000\u0090"+
		"\u0091\u0005]\u0000\u0000\u0091.\u0001\u0000\u0000\u0000\u0007\u0000X"+
		"bi\u007f\u0087\u008e\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}