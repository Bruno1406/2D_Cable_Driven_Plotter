// Generated from c:/Users/delar/2D_Cable_Driven_Plotter/ihm/Grammar_antlr/Gcode.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class GcodeParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		SIGN=10, INT=11, WS=12;
	public static final int
		RULE_gcode = 0, RULE_statement = 1, RULE_programEnd = 2, RULE_lineNumber = 3, 
		RULE_codFunc = 4, RULE_mEnd = 5, RULE_coord = 6, RULE_coordX = 7, RULE_coordY = 8, 
		RULE_coordI = 9, RULE_coordJ = 10, RULE_coordValue = 11, RULE_lineEnd = 12, 
		RULE_signedInt = 13;
	private static String[] makeRuleNames() {
		return new String[] {
			"gcode", "statement", "programEnd", "lineNumber", "codFunc", "mEnd", 
			"coord", "coordX", "coordY", "coordI", "coordJ", "coordValue", "lineEnd", 
			"signedInt"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'N'", "'G'", "'M30'", "'X'", "'Y'", "'I'", "'J'", "'.'", "'\\n'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, "SIGN", "INT", 
			"WS"
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
	public String getGrammarFileName() { return "Gcode.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public GcodeParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GcodeContext extends ParserRuleContext {
		public ProgramEndContext programEnd() {
			return getRuleContext(ProgramEndContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public GcodeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_gcode; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).enterGcode(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).exitGcode(this);
		}
	}

	public final GcodeContext gcode() throws RecognitionException {
		GcodeContext _localctx = new GcodeContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_gcode);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(29); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(28);
					statement();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(31); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(33);
			programEnd();
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
		public LineNumberContext lineNumber() {
			return getRuleContext(LineNumberContext.class,0);
		}
		public CodFuncContext codFunc() {
			return getRuleContext(CodFuncContext.class,0);
		}
		public LineEndContext lineEnd() {
			return getRuleContext(LineEndContext.class,0);
		}
		public List<CoordContext> coord() {
			return getRuleContexts(CoordContext.class);
		}
		public CoordContext coord(int i) {
			return getRuleContext(CoordContext.class,i);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).exitStatement(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(35);
			lineNumber();
			setState(36);
			codFunc();
			setState(40);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 240L) != 0)) {
				{
				{
				setState(37);
				coord();
				}
				}
				setState(42);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(43);
			lineEnd();
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
	public static class ProgramEndContext extends ParserRuleContext {
		public LineNumberContext lineNumber() {
			return getRuleContext(LineNumberContext.class,0);
		}
		public MEndContext mEnd() {
			return getRuleContext(MEndContext.class,0);
		}
		public ProgramEndContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programEnd; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).enterProgramEnd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).exitProgramEnd(this);
		}
	}

	public final ProgramEndContext programEnd() throws RecognitionException {
		ProgramEndContext _localctx = new ProgramEndContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_programEnd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			lineNumber();
			setState(46);
			mEnd();
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
	public static class LineNumberContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(GcodeParser.INT, 0); }
		public LineNumberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lineNumber; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).enterLineNumber(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).exitLineNumber(this);
		}
	}

	public final LineNumberContext lineNumber() throws RecognitionException {
		LineNumberContext _localctx = new LineNumberContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_lineNumber);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			match(T__0);
			setState(49);
			match(INT);
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
	public static class CodFuncContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(GcodeParser.INT, 0); }
		public CodFuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_codFunc; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).enterCodFunc(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).exitCodFunc(this);
		}
	}

	public final CodFuncContext codFunc() throws RecognitionException {
		CodFuncContext _localctx = new CodFuncContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_codFunc);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			match(T__1);
			setState(52);
			match(INT);
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
	public static class MEndContext extends ParserRuleContext {
		public MEndContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mEnd; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).enterMEnd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).exitMEnd(this);
		}
	}

	public final MEndContext mEnd() throws RecognitionException {
		MEndContext _localctx = new MEndContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_mEnd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			match(T__2);
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
	public static class CoordContext extends ParserRuleContext {
		public CoordXContext coordX() {
			return getRuleContext(CoordXContext.class,0);
		}
		public CoordYContext coordY() {
			return getRuleContext(CoordYContext.class,0);
		}
		public CoordIContext coordI() {
			return getRuleContext(CoordIContext.class,0);
		}
		public CoordJContext coordJ() {
			return getRuleContext(CoordJContext.class,0);
		}
		public CoordContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_coord; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).enterCoord(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).exitCoord(this);
		}
	}

	public final CoordContext coord() throws RecognitionException {
		CoordContext _localctx = new CoordContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_coord);
		try {
			setState(60);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
				enterOuterAlt(_localctx, 1);
				{
				setState(56);
				coordX();
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 2);
				{
				setState(57);
				coordY();
				}
				break;
			case T__5:
				enterOuterAlt(_localctx, 3);
				{
				setState(58);
				coordI();
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 4);
				{
				setState(59);
				coordJ();
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
	public static class CoordXContext extends ParserRuleContext {
		public CoordValueContext coordValue() {
			return getRuleContext(CoordValueContext.class,0);
		}
		public CoordXContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_coordX; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).enterCoordX(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).exitCoordX(this);
		}
	}

	public final CoordXContext coordX() throws RecognitionException {
		CoordXContext _localctx = new CoordXContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_coordX);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(62);
			match(T__3);
			setState(63);
			coordValue();
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
	public static class CoordYContext extends ParserRuleContext {
		public CoordValueContext coordValue() {
			return getRuleContext(CoordValueContext.class,0);
		}
		public CoordYContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_coordY; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).enterCoordY(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).exitCoordY(this);
		}
	}

	public final CoordYContext coordY() throws RecognitionException {
		CoordYContext _localctx = new CoordYContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_coordY);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(65);
			match(T__4);
			setState(66);
			coordValue();
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
	public static class CoordIContext extends ParserRuleContext {
		public CoordValueContext coordValue() {
			return getRuleContext(CoordValueContext.class,0);
		}
		public CoordIContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_coordI; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).enterCoordI(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).exitCoordI(this);
		}
	}

	public final CoordIContext coordI() throws RecognitionException {
		CoordIContext _localctx = new CoordIContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_coordI);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			match(T__5);
			setState(69);
			coordValue();
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
	public static class CoordJContext extends ParserRuleContext {
		public CoordValueContext coordValue() {
			return getRuleContext(CoordValueContext.class,0);
		}
		public CoordJContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_coordJ; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).enterCoordJ(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).exitCoordJ(this);
		}
	}

	public final CoordJContext coordJ() throws RecognitionException {
		CoordJContext _localctx = new CoordJContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_coordJ);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			match(T__6);
			setState(72);
			coordValue();
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
	public static class CoordValueContext extends ParserRuleContext {
		public SignedIntContext signedInt() {
			return getRuleContext(SignedIntContext.class,0);
		}
		public TerminalNode INT() { return getToken(GcodeParser.INT, 0); }
		public CoordValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_coordValue; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).enterCoordValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).exitCoordValue(this);
		}
	}

	public final CoordValueContext coordValue() throws RecognitionException {
		CoordValueContext _localctx = new CoordValueContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_coordValue);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			signedInt();
			setState(77);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__7) {
				{
				setState(75);
				match(T__7);
				setState(76);
				match(INT);
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
	public static class LineEndContext extends ParserRuleContext {
		public LineEndContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lineEnd; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).enterLineEnd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).exitLineEnd(this);
		}
	}

	public final LineEndContext lineEnd() throws RecognitionException {
		LineEndContext _localctx = new LineEndContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_lineEnd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			match(T__8);
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
	public static class SignedIntContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(GcodeParser.INT, 0); }
		public TerminalNode SIGN() { return getToken(GcodeParser.SIGN, 0); }
		public SignedIntContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_signedInt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).enterSignedInt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GcodeListener ) ((GcodeListener)listener).exitSignedInt(this);
		}
	}

	public final SignedIntContext signedInt() throws RecognitionException {
		SignedIntContext _localctx = new SignedIntContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_signedInt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SIGN) {
				{
				setState(81);
				match(SIGN);
				}
			}

			setState(84);
			match(INT);
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
		"\u0004\u0001\fW\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0001\u0000\u0004\u0000\u001e\b\u0000\u000b"+
		"\u0000\f\u0000\u001f\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0005\u0001\'\b\u0001\n\u0001\f\u0001*\t\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006=\b\u0006\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t"+
		"\u0001\t\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0003"+
		"\u000bN\b\u000b\u0001\f\u0001\f\u0001\r\u0003\rS\b\r\u0001\r\u0001\r\u0001"+
		"\r\u0000\u0000\u000e\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0016\u0018\u001a\u0000\u0000O\u0000\u001d\u0001\u0000\u0000\u0000\u0002"+
		"#\u0001\u0000\u0000\u0000\u0004-\u0001\u0000\u0000\u0000\u00060\u0001"+
		"\u0000\u0000\u0000\b3\u0001\u0000\u0000\u0000\n6\u0001\u0000\u0000\u0000"+
		"\f<\u0001\u0000\u0000\u0000\u000e>\u0001\u0000\u0000\u0000\u0010A\u0001"+
		"\u0000\u0000\u0000\u0012D\u0001\u0000\u0000\u0000\u0014G\u0001\u0000\u0000"+
		"\u0000\u0016J\u0001\u0000\u0000\u0000\u0018O\u0001\u0000\u0000\u0000\u001a"+
		"R\u0001\u0000\u0000\u0000\u001c\u001e\u0003\u0002\u0001\u0000\u001d\u001c"+
		"\u0001\u0000\u0000\u0000\u001e\u001f\u0001\u0000\u0000\u0000\u001f\u001d"+
		"\u0001\u0000\u0000\u0000\u001f \u0001\u0000\u0000\u0000 !\u0001\u0000"+
		"\u0000\u0000!\"\u0003\u0004\u0002\u0000\"\u0001\u0001\u0000\u0000\u0000"+
		"#$\u0003\u0006\u0003\u0000$(\u0003\b\u0004\u0000%\'\u0003\f\u0006\u0000"+
		"&%\u0001\u0000\u0000\u0000\'*\u0001\u0000\u0000\u0000(&\u0001\u0000\u0000"+
		"\u0000()\u0001\u0000\u0000\u0000)+\u0001\u0000\u0000\u0000*(\u0001\u0000"+
		"\u0000\u0000+,\u0003\u0018\f\u0000,\u0003\u0001\u0000\u0000\u0000-.\u0003"+
		"\u0006\u0003\u0000./\u0003\n\u0005\u0000/\u0005\u0001\u0000\u0000\u0000"+
		"01\u0005\u0001\u0000\u000012\u0005\u000b\u0000\u00002\u0007\u0001\u0000"+
		"\u0000\u000034\u0005\u0002\u0000\u000045\u0005\u000b\u0000\u00005\t\u0001"+
		"\u0000\u0000\u000067\u0005\u0003\u0000\u00007\u000b\u0001\u0000\u0000"+
		"\u00008=\u0003\u000e\u0007\u00009=\u0003\u0010\b\u0000:=\u0003\u0012\t"+
		"\u0000;=\u0003\u0014\n\u0000<8\u0001\u0000\u0000\u0000<9\u0001\u0000\u0000"+
		"\u0000<:\u0001\u0000\u0000\u0000<;\u0001\u0000\u0000\u0000=\r\u0001\u0000"+
		"\u0000\u0000>?\u0005\u0004\u0000\u0000?@\u0003\u0016\u000b\u0000@\u000f"+
		"\u0001\u0000\u0000\u0000AB\u0005\u0005\u0000\u0000BC\u0003\u0016\u000b"+
		"\u0000C\u0011\u0001\u0000\u0000\u0000DE\u0005\u0006\u0000\u0000EF\u0003"+
		"\u0016\u000b\u0000F\u0013\u0001\u0000\u0000\u0000GH\u0005\u0007\u0000"+
		"\u0000HI\u0003\u0016\u000b\u0000I\u0015\u0001\u0000\u0000\u0000JM\u0003"+
		"\u001a\r\u0000KL\u0005\b\u0000\u0000LN\u0005\u000b\u0000\u0000MK\u0001"+
		"\u0000\u0000\u0000MN\u0001\u0000\u0000\u0000N\u0017\u0001\u0000\u0000"+
		"\u0000OP\u0005\t\u0000\u0000P\u0019\u0001\u0000\u0000\u0000QS\u0005\n"+
		"\u0000\u0000RQ\u0001\u0000\u0000\u0000RS\u0001\u0000\u0000\u0000ST\u0001"+
		"\u0000\u0000\u0000TU\u0005\u000b\u0000\u0000U\u001b\u0001\u0000\u0000"+
		"\u0000\u0005\u001f(<MR";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}