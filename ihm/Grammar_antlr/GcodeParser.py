# Generated from Gcode.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,87,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,4,0,30,8,0,11,0,12,0,31,1,0,1,0,1,1,1,1,1,1,5,1,39,8,1,10,1,
        12,1,42,9,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,
        1,6,1,6,1,6,1,6,3,6,61,8,6,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,
        10,1,10,1,10,1,11,1,11,1,11,3,11,78,8,11,1,12,1,12,1,13,3,13,83,
        8,13,1,13,1,13,1,13,0,0,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        0,0,79,0,29,1,0,0,0,2,35,1,0,0,0,4,45,1,0,0,0,6,48,1,0,0,0,8,51,
        1,0,0,0,10,54,1,0,0,0,12,60,1,0,0,0,14,62,1,0,0,0,16,65,1,0,0,0,
        18,68,1,0,0,0,20,71,1,0,0,0,22,74,1,0,0,0,24,79,1,0,0,0,26,82,1,
        0,0,0,28,30,3,2,1,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,
        32,1,0,0,0,32,33,1,0,0,0,33,34,3,4,2,0,34,1,1,0,0,0,35,36,3,6,3,
        0,36,40,3,8,4,0,37,39,3,12,6,0,38,37,1,0,0,0,39,42,1,0,0,0,40,38,
        1,0,0,0,40,41,1,0,0,0,41,43,1,0,0,0,42,40,1,0,0,0,43,44,3,24,12,
        0,44,3,1,0,0,0,45,46,3,6,3,0,46,47,3,10,5,0,47,5,1,0,0,0,48,49,5,
        1,0,0,49,50,5,11,0,0,50,7,1,0,0,0,51,52,5,2,0,0,52,53,5,11,0,0,53,
        9,1,0,0,0,54,55,5,3,0,0,55,11,1,0,0,0,56,61,3,14,7,0,57,61,3,16,
        8,0,58,61,3,18,9,0,59,61,3,20,10,0,60,56,1,0,0,0,60,57,1,0,0,0,60,
        58,1,0,0,0,60,59,1,0,0,0,61,13,1,0,0,0,62,63,5,4,0,0,63,64,3,22,
        11,0,64,15,1,0,0,0,65,66,5,5,0,0,66,67,3,22,11,0,67,17,1,0,0,0,68,
        69,5,6,0,0,69,70,3,22,11,0,70,19,1,0,0,0,71,72,5,7,0,0,72,73,3,22,
        11,0,73,21,1,0,0,0,74,77,3,26,13,0,75,76,5,8,0,0,76,78,5,11,0,0,
        77,75,1,0,0,0,77,78,1,0,0,0,78,23,1,0,0,0,79,80,5,9,0,0,80,25,1,
        0,0,0,81,83,5,10,0,0,82,81,1,0,0,0,82,83,1,0,0,0,83,84,1,0,0,0,84,
        85,5,11,0,0,85,27,1,0,0,0,5,31,40,60,77,82
    ]

class GcodeParser ( Parser ):

    grammarFileName = "Gcode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'N'", "'G'", "'M30'", "'X'", "'Y'", "'I'", 
                     "'J'", "'.'", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SIGN", "INT", "WS" ]

    RULE_gcode = 0
    RULE_statement = 1
    RULE_programEnd = 2
    RULE_lineNumber = 3
    RULE_codFunc = 4
    RULE_mEnd = 5
    RULE_coord = 6
    RULE_coordX = 7
    RULE_coordY = 8
    RULE_coordI = 9
    RULE_coordJ = 10
    RULE_coordValue = 11
    RULE_lineEnd = 12
    RULE_signedInt = 13

    ruleNames =  [ "gcode", "statement", "programEnd", "lineNumber", "codFunc", 
                   "mEnd", "coord", "coordX", "coordY", "coordI", "coordJ", 
                   "coordValue", "lineEnd", "signedInt" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    SIGN=10
    INT=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class GcodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def programEnd(self):
            return self.getTypedRuleContext(GcodeParser.ProgramEndContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GcodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(GcodeParser.StatementContext,i)


        def getRuleIndex(self):
            return GcodeParser.RULE_gcode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGcode" ):
                listener.enterGcode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGcode" ):
                listener.exitGcode(self)




    def gcode(self):

        localctx = GcodeParser.GcodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_gcode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 28
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 31 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 33
            self.programEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lineNumber(self):
            return self.getTypedRuleContext(GcodeParser.LineNumberContext,0)


        def codFunc(self):
            return self.getTypedRuleContext(GcodeParser.CodFuncContext,0)


        def lineEnd(self):
            return self.getTypedRuleContext(GcodeParser.LineEndContext,0)


        def coord(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GcodeParser.CoordContext)
            else:
                return self.getTypedRuleContext(GcodeParser.CoordContext,i)


        def getRuleIndex(self):
            return GcodeParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = GcodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.lineNumber()
            self.state = 36
            self.codFunc()
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 240) != 0):
                self.state = 37
                self.coord()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
            self.lineEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramEndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lineNumber(self):
            return self.getTypedRuleContext(GcodeParser.LineNumberContext,0)


        def mEnd(self):
            return self.getTypedRuleContext(GcodeParser.MEndContext,0)


        def getRuleIndex(self):
            return GcodeParser.RULE_programEnd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgramEnd" ):
                listener.enterProgramEnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgramEnd" ):
                listener.exitProgramEnd(self)




    def programEnd(self):

        localctx = GcodeParser.ProgramEndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_programEnd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.lineNumber()
            self.state = 46
            self.mEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(GcodeParser.INT, 0)

        def getRuleIndex(self):
            return GcodeParser.RULE_lineNumber

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLineNumber" ):
                listener.enterLineNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLineNumber" ):
                listener.exitLineNumber(self)




    def lineNumber(self):

        localctx = GcodeParser.LineNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_lineNumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(GcodeParser.T__0)
            self.state = 49
            self.match(GcodeParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CodFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(GcodeParser.INT, 0)

        def getRuleIndex(self):
            return GcodeParser.RULE_codFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCodFunc" ):
                listener.enterCodFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCodFunc" ):
                listener.exitCodFunc(self)




    def codFunc(self):

        localctx = GcodeParser.CodFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_codFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(GcodeParser.T__1)
            self.state = 52
            self.match(GcodeParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MEndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GcodeParser.RULE_mEnd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMEnd" ):
                listener.enterMEnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMEnd" ):
                listener.exitMEnd(self)




    def mEnd(self):

        localctx = GcodeParser.MEndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_mEnd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(GcodeParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coordX(self):
            return self.getTypedRuleContext(GcodeParser.CoordXContext,0)


        def coordY(self):
            return self.getTypedRuleContext(GcodeParser.CoordYContext,0)


        def coordI(self):
            return self.getTypedRuleContext(GcodeParser.CoordIContext,0)


        def coordJ(self):
            return self.getTypedRuleContext(GcodeParser.CoordJContext,0)


        def getRuleIndex(self):
            return GcodeParser.RULE_coord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoord" ):
                listener.enterCoord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoord" ):
                listener.exitCoord(self)




    def coord(self):

        localctx = GcodeParser.CoordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_coord)
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.coordX()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.coordY()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.coordI()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self.coordJ()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordXContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coordValue(self):
            return self.getTypedRuleContext(GcodeParser.CoordValueContext,0)


        def getRuleIndex(self):
            return GcodeParser.RULE_coordX

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoordX" ):
                listener.enterCoordX(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoordX" ):
                listener.exitCoordX(self)




    def coordX(self):

        localctx = GcodeParser.CoordXContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_coordX)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(GcodeParser.T__3)
            self.state = 63
            self.coordValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordYContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coordValue(self):
            return self.getTypedRuleContext(GcodeParser.CoordValueContext,0)


        def getRuleIndex(self):
            return GcodeParser.RULE_coordY

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoordY" ):
                listener.enterCoordY(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoordY" ):
                listener.exitCoordY(self)




    def coordY(self):

        localctx = GcodeParser.CoordYContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_coordY)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(GcodeParser.T__4)
            self.state = 66
            self.coordValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordIContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coordValue(self):
            return self.getTypedRuleContext(GcodeParser.CoordValueContext,0)


        def getRuleIndex(self):
            return GcodeParser.RULE_coordI

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoordI" ):
                listener.enterCoordI(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoordI" ):
                listener.exitCoordI(self)




    def coordI(self):

        localctx = GcodeParser.CoordIContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_coordI)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(GcodeParser.T__5)
            self.state = 69
            self.coordValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordJContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coordValue(self):
            return self.getTypedRuleContext(GcodeParser.CoordValueContext,0)


        def getRuleIndex(self):
            return GcodeParser.RULE_coordJ

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoordJ" ):
                listener.enterCoordJ(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoordJ" ):
                listener.exitCoordJ(self)




    def coordJ(self):

        localctx = GcodeParser.CoordJContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_coordJ)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(GcodeParser.T__6)
            self.state = 72
            self.coordValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signedInt(self):
            return self.getTypedRuleContext(GcodeParser.SignedIntContext,0)


        def INT(self):
            return self.getToken(GcodeParser.INT, 0)

        def getRuleIndex(self):
            return GcodeParser.RULE_coordValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoordValue" ):
                listener.enterCoordValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoordValue" ):
                listener.exitCoordValue(self)




    def coordValue(self):

        localctx = GcodeParser.CoordValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_coordValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.signedInt()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 75
                self.match(GcodeParser.T__7)
                self.state = 76
                self.match(GcodeParser.INT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineEndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GcodeParser.RULE_lineEnd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLineEnd" ):
                listener.enterLineEnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLineEnd" ):
                listener.exitLineEnd(self)




    def lineEnd(self):

        localctx = GcodeParser.LineEndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_lineEnd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(GcodeParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignedIntContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(GcodeParser.INT, 0)

        def SIGN(self):
            return self.getToken(GcodeParser.SIGN, 0)

        def getRuleIndex(self):
            return GcodeParser.RULE_signedInt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignedInt" ):
                listener.enterSignedInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignedInt" ):
                listener.exitSignedInt(self)




    def signedInt(self):

        localctx = GcodeParser.SignedIntContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_signedInt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 81
                self.match(GcodeParser.SIGN)


            self.state = 84
            self.match(GcodeParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





