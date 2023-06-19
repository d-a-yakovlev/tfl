# Generated from mus.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .musParser import musParser
else:
    from musParser import musParser

# This class defines a complete listener for a parse tree produced by musParser.
class musListener(ParseTreeListener):

    # Enter a parse tree produced by musParser#ChordExpr.
    def enterChordExpr(self, ctx:musParser.ChordExprContext):
        pass

    # Exit a parse tree produced by musParser#ChordExpr.
    def exitChordExpr(self, ctx:musParser.ChordExprContext):
        pass


    # Enter a parse tree produced by musParser#NumberExpr.
    def enterNumberExpr(self, ctx:musParser.NumberExprContext):
        pass

    # Exit a parse tree produced by musParser#NumberExpr.
    def exitNumberExpr(self, ctx:musParser.NumberExprContext):
        pass


    # Enter a parse tree produced by musParser#StaveExpr.
    def enterStaveExpr(self, ctx:musParser.StaveExprContext):
        pass

    # Exit a parse tree produced by musParser#StaveExpr.
    def exitStaveExpr(self, ctx:musParser.StaveExprContext):
        pass


    # Enter a parse tree produced by musParser#ByeExpr.
    def enterByeExpr(self, ctx:musParser.ByeExprContext):
        pass

    # Exit a parse tree produced by musParser#ByeExpr.
    def exitByeExpr(self, ctx:musParser.ByeExprContext):
        pass


    # Enter a parse tree produced by musParser#HelloExpr.
    def enterHelloExpr(self, ctx:musParser.HelloExprContext):
        pass

    # Exit a parse tree produced by musParser#HelloExpr.
    def exitHelloExpr(self, ctx:musParser.HelloExprContext):
        pass


    # Enter a parse tree produced by musParser#NotaExpr.
    def enterNotaExpr(self, ctx:musParser.NotaExprContext):
        pass

    # Exit a parse tree produced by musParser#NotaExpr.
    def exitNotaExpr(self, ctx:musParser.NotaExprContext):
        pass


    # Enter a parse tree produced by musParser#SongsExpr.
    def enterSongsExpr(self, ctx:musParser.SongsExprContext):
        pass

    # Exit a parse tree produced by musParser#SongsExpr.
    def exitSongsExpr(self, ctx:musParser.SongsExprContext):
        pass


    # Enter a parse tree produced by musParser#ListExpr.
    def enterListExpr(self, ctx:musParser.ListExprContext):
        pass

    # Exit a parse tree produced by musParser#ListExpr.
    def exitListExpr(self, ctx:musParser.ListExprContext):
        pass


    # Enter a parse tree produced by musParser#ParenExpr.
    def enterParenExpr(self, ctx:musParser.ParenExprContext):
        pass

    # Exit a parse tree produced by musParser#ParenExpr.
    def exitParenExpr(self, ctx:musParser.ParenExprContext):
        pass


    # Enter a parse tree produced by musParser#InfixExpr.
    def enterInfixExpr(self, ctx:musParser.InfixExprContext):
        pass

    # Exit a parse tree produced by musParser#InfixExpr.
    def exitInfixExpr(self, ctx:musParser.InfixExprContext):
        pass


    # Enter a parse tree produced by musParser#RealExpr.
    def enterRealExpr(self, ctx:musParser.RealExprContext):
        pass

    # Exit a parse tree produced by musParser#RealExpr.
    def exitRealExpr(self, ctx:musParser.RealExprContext):
        pass



del musParser