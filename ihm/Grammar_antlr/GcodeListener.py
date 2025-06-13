# Generated from Gcode.g4 by ANTLR 4.13.2
from antlr4 import *
import struct
if "." in __name__:
    from .GcodeParser import GcodeParser
else:
    from GcodeParser import GcodeParser

# This class defines a complete listener for a parse tree produced by GcodeParser.
class GcodeListener(ParseTreeListener):
    def __init__(self):
        self.line_registers = []

    def float_to_int(self, f):
        """Converte float para representação hexadecimal (IEEE 754)"""
        return int (10*float(f)) 

    def int_sequence_to_registers(self, int_seq):
        registers = []
        for item in int_seq:
            registers.append(item)
        return registers

    # Enter a parse tree produced by GcodeParser#gcode.
    def enterGcode(self, ctx:GcodeParser.GcodeContext):
        pass

    # Exit a parse tree produced by GcodeParser#gcode.
    def exitGcode(self, ctx:GcodeParser.GcodeContext):
        pass


    # Enter a parse tree produced by GcodeParser#statement.
    def enterStatement(self, ctx:GcodeParser.StatementContext):
       # int_values = []

        # G-code inteiro
        gcode_val = ctx.codFunc().INT().getText()
        self.line_registers.append((int(gcode_val)))

        # Coordenadas: X, Y, I, J
        for coord_ctx in ctx.coord():
            if coord_ctx.coordX():
                val = coord_ctx.coordX().coordValue().getText()
            elif coord_ctx.coordY():
                val = coord_ctx.coordY().coordValue().getText()
            elif coord_ctx.coordI():
                val = coord_ctx.coordI().coordValue().getText()
            elif coord_ctx.coordJ():
                val = coord_ctx.coordJ().coordValue().getText()
            else:
                continue

            int_val = self.float_to_int(val)
            self.line_registers.append(int_val)

    # Exit a parse tree produced by GcodeParser#statement.
    def exitStatement(self, ctx:GcodeParser.StatementContext):
        pass


    # Enter a parse tree produced by GcodeParser#programEnd.
    def enterProgramEnd(self, ctx:GcodeParser.ProgramEndContext):
        pass

    # Exit a parse tree produced by GcodeParser#programEnd.
    def exitProgramEnd(self, ctx:GcodeParser.ProgramEndContext):
        pass


    # Enter a parse tree produced by GcodeParser#lineNumber.
    def enterLineNumber(self, ctx:GcodeParser.LineNumberContext):
        pass

    # Exit a parse tree produced by GcodeParser#lineNumber.
    def exitLineNumber(self, ctx:GcodeParser.LineNumberContext):
        pass


    # Enter a parse tree produced by GcodeParser#codFunc.
    def enterCodFunc(self, ctx:GcodeParser.CodFuncContext):
        pass

    # Exit a parse tree produced by GcodeParser#codFunc.
    def exitCodFunc(self, ctx:GcodeParser.CodFuncContext):
        pass


    # Enter a parse tree produced by GcodeParser#mEnd.
    def enterMEnd(self, ctx:GcodeParser.MEndContext):
        pass

    # Exit a parse tree produced by GcodeParser#mEnd.
    def exitMEnd(self, ctx:GcodeParser.MEndContext):
        pass


    # Enter a parse tree produced by GcodeParser#coord.
    def enterCoord(self, ctx:GcodeParser.CoordContext):
        pass

    # Exit a parse tree produced by GcodeParser#coord.
    def exitCoord(self, ctx:GcodeParser.CoordContext):
        pass


    # Enter a parse tree produced by GcodeParser#coordX.
    def enterCoordX(self, ctx:GcodeParser.CoordXContext):
        pass

    # Exit a parse tree produced by GcodeParser#coordX.
    def exitCoordX(self, ctx:GcodeParser.CoordXContext):
        pass


    # Enter a parse tree produced by GcodeParser#coordY.
    def enterCoordY(self, ctx:GcodeParser.CoordYContext):
        pass

    # Exit a parse tree produced by GcodeParser#coordY.
    def exitCoordY(self, ctx:GcodeParser.CoordYContext):
        pass


    # Enter a parse tree produced by GcodeParser#coordI.
    def enterCoordI(self, ctx:GcodeParser.CoordIContext):
        pass

    # Exit a parse tree produced by GcodeParser#coordI.
    def exitCoordI(self, ctx:GcodeParser.CoordIContext):
        pass


    # Enter a parse tree produced by GcodeParser#coordJ.
    def enterCoordJ(self, ctx:GcodeParser.CoordJContext):
        pass

    # Exit a parse tree produced by GcodeParser#coordJ.
    def exitCoordJ(self, ctx:GcodeParser.CoordJContext):
        pass


    # Enter a parse tree produced by GcodeParser#coordValue.
    def enterCoordValue(self, ctx:GcodeParser.CoordValueContext):
        pass

    # Exit a parse tree produced by GcodeParser#coordValue.
    def exitCoordValue(self, ctx:GcodeParser.CoordValueContext):
        pass


    # Enter a parse tree produced by GcodeParser#lineEnd.
    def enterLineEnd(self, ctx:GcodeParser.LineEndContext):
        pass

    # Exit a parse tree produced by GcodeParser#lineEnd.
    def exitLineEnd(self, ctx:GcodeParser.LineEndContext):
        pass


    # Enter a parse tree produced by GcodeParser#signedInt.
    def enterSignedInt(self, ctx:GcodeParser.SignedIntContext):
        pass

    # Exit a parse tree produced by GcodeParser#signedInt.
    def exitSignedInt(self, ctx:GcodeParser.SignedIntContext):
        pass



del GcodeParser