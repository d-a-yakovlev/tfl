# Generated from mus.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .musParser import musParser
else:
    from musParser import musParser

# This class defines a complete generic visitor for a parse tree produced by musParser.

class musVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by musParser#ChordExpr.
    def visitChordExpr(self, ctx:musParser.ChordExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musParser#NumberExpr.
    def visitNumberExpr(self, ctx:musParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musParser#StaveExpr.
    def visitStaveExpr(self, ctx:musParser.StaveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musParser#ByeExpr.
    def visitByeExpr(self, ctx:musParser.ByeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musParser#HelloExpr.
    def visitHelloExpr(self, ctx:musParser.HelloExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musParser#NotaExpr.
    def visitNotaExpr(self, ctx:musParser.NotaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musParser#SongsExpr.
    def visitSongsExpr(self, ctx:musParser.SongsExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musParser#ListExpr.
    def visitListExpr(self, ctx:musParser.ListExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musParser#ParenExpr.
    def visitParenExpr(self, ctx:musParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musParser#InfixExpr.
    def visitInfixExpr(self, ctx:musParser.InfixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musParser#RealExpr.
    def visitRealExpr(self, ctx:musParser.RealExprContext):
        return self.visitChildren(ctx)



del musParser