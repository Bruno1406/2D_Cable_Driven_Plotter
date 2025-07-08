// Generated from c:/Users/delar/2D_Cable_Driven_Plotter/ihm/Grammar_antlr/Gcode.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link GcodeParser}.
 */
public interface GcodeListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link GcodeParser#gcode}.
	 * @param ctx the parse tree
	 */
	void enterGcode(GcodeParser.GcodeContext ctx);
	/**
	 * Exit a parse tree produced by {@link GcodeParser#gcode}.
	 * @param ctx the parse tree
	 */
	void exitGcode(GcodeParser.GcodeContext ctx);
	/**
	 * Enter a parse tree produced by {@link GcodeParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(GcodeParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link GcodeParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(GcodeParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link GcodeParser#programEnd}.
	 * @param ctx the parse tree
	 */
	void enterProgramEnd(GcodeParser.ProgramEndContext ctx);
	/**
	 * Exit a parse tree produced by {@link GcodeParser#programEnd}.
	 * @param ctx the parse tree
	 */
	void exitProgramEnd(GcodeParser.ProgramEndContext ctx);
	/**
	 * Enter a parse tree produced by {@link GcodeParser#lineNumber}.
	 * @param ctx the parse tree
	 */
	void enterLineNumber(GcodeParser.LineNumberContext ctx);
	/**
	 * Exit a parse tree produced by {@link GcodeParser#lineNumber}.
	 * @param ctx the parse tree
	 */
	void exitLineNumber(GcodeParser.LineNumberContext ctx);
	/**
	 * Enter a parse tree produced by {@link GcodeParser#codFunc}.
	 * @param ctx the parse tree
	 */
	void enterCodFunc(GcodeParser.CodFuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link GcodeParser#codFunc}.
	 * @param ctx the parse tree
	 */
	void exitCodFunc(GcodeParser.CodFuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link GcodeParser#mEnd}.
	 * @param ctx the parse tree
	 */
	void enterMEnd(GcodeParser.MEndContext ctx);
	/**
	 * Exit a parse tree produced by {@link GcodeParser#mEnd}.
	 * @param ctx the parse tree
	 */
	void exitMEnd(GcodeParser.MEndContext ctx);
	/**
	 * Enter a parse tree produced by {@link GcodeParser#coord}.
	 * @param ctx the parse tree
	 */
	void enterCoord(GcodeParser.CoordContext ctx);
	/**
	 * Exit a parse tree produced by {@link GcodeParser#coord}.
	 * @param ctx the parse tree
	 */
	void exitCoord(GcodeParser.CoordContext ctx);
	/**
	 * Enter a parse tree produced by {@link GcodeParser#coordX}.
	 * @param ctx the parse tree
	 */
	void enterCoordX(GcodeParser.CoordXContext ctx);
	/**
	 * Exit a parse tree produced by {@link GcodeParser#coordX}.
	 * @param ctx the parse tree
	 */
	void exitCoordX(GcodeParser.CoordXContext ctx);
	/**
	 * Enter a parse tree produced by {@link GcodeParser#coordY}.
	 * @param ctx the parse tree
	 */
	void enterCoordY(GcodeParser.CoordYContext ctx);
	/**
	 * Exit a parse tree produced by {@link GcodeParser#coordY}.
	 * @param ctx the parse tree
	 */
	void exitCoordY(GcodeParser.CoordYContext ctx);
	/**
	 * Enter a parse tree produced by {@link GcodeParser#coordI}.
	 * @param ctx the parse tree
	 */
	void enterCoordI(GcodeParser.CoordIContext ctx);
	/**
	 * Exit a parse tree produced by {@link GcodeParser#coordI}.
	 * @param ctx the parse tree
	 */
	void exitCoordI(GcodeParser.CoordIContext ctx);
	/**
	 * Enter a parse tree produced by {@link GcodeParser#coordJ}.
	 * @param ctx the parse tree
	 */
	void enterCoordJ(GcodeParser.CoordJContext ctx);
	/**
	 * Exit a parse tree produced by {@link GcodeParser#coordJ}.
	 * @param ctx the parse tree
	 */
	void exitCoordJ(GcodeParser.CoordJContext ctx);
	/**
	 * Enter a parse tree produced by {@link GcodeParser#coordValue}.
	 * @param ctx the parse tree
	 */
	void enterCoordValue(GcodeParser.CoordValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link GcodeParser#coordValue}.
	 * @param ctx the parse tree
	 */
	void exitCoordValue(GcodeParser.CoordValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link GcodeParser#lineEnd}.
	 * @param ctx the parse tree
	 */
	void enterLineEnd(GcodeParser.LineEndContext ctx);
	/**
	 * Exit a parse tree produced by {@link GcodeParser#lineEnd}.
	 * @param ctx the parse tree
	 */
	void exitLineEnd(GcodeParser.LineEndContext ctx);
	/**
	 * Enter a parse tree produced by {@link GcodeParser#signedInt}.
	 * @param ctx the parse tree
	 */
	void enterSignedInt(GcodeParser.SignedIntContext ctx);
	/**
	 * Exit a parse tree produced by {@link GcodeParser#signedInt}.
	 * @param ctx the parse tree
	 */
	void exitSignedInt(GcodeParser.SignedIntContext ctx);
}