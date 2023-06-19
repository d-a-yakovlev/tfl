# Generated from mus.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("\35\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\5\2\23\n\2\3\2\3\2\3\2\7\2\30\n\2\f\2\16")
        buf.write("\2\33\13\2\3\2\2\3\2\3\2\2\3\3\2\3\4\2%\2\22\3\2\2\2\4")
        buf.write("\5\b\2\1\2\5\6\7\5\2\2\6\7\5\2\2\2\7\b\7\6\2\2\b\23\3")
        buf.write("\2\2\2\t\23\7\7\2\2\n\23\7\b\2\2\13\23\7\t\2\2\f\23\7")
        buf.write("\n\2\2\r\23\7\r\2\2\16\23\7\17\2\2\17\23\7\21\2\2\20\23")
        buf.write("\7\22\2\2\21\23\7\23\2\2\22\4\3\2\2\2\22\t\3\2\2\2\22")
        buf.write("\n\3\2\2\2\22\13\3\2\2\2\22\f\3\2\2\2\22\r\3\2\2\2\22")
        buf.write("\16\3\2\2\2\22\17\3\2\2\2\22\20\3\2\2\2\22\21\3\2\2\2")
        buf.write("\23\31\3\2\2\2\24\25\f\r\2\2\25\26\t\2\2\2\26\30\5\2\2")
        buf.write("\16\27\24\3\2\2\2\30\33\3\2\2\2\31\27\3\2\2\2\31\32\3")
        buf.write("\2\2\2\32\3\3\2\2\2\33\31\3\2\2\2\4\22\31")
        return buf.getvalue()


class musParser ( Parser ):

    grammarFileName = "mus.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INT", "REAL", "NOTA", "CHORD", "WS", 
                      "FIRST_STAVE_ELEMENT", "STAVE", "FIRST_SONG", "SONGS", 
                      "FIRST_LIST_ELEMENT", "LIST", "HELLO", "BYE" ]

    RULE_expr = 0

    ruleNames =  [ "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    INT=5
    REAL=6
    NOTA=7
    CHORD=8
    WS=9
    FIRST_STAVE_ELEMENT=10
    STAVE=11
    FIRST_SONG=12
    SONGS=13
    FIRST_LIST_ELEMENT=14
    LIST=15
    HELLO=16
    BYE=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return musParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ChordExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def CHORD(self):
            return self.getToken(musParser.CHORD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChordExpr" ):
                listener.enterChordExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChordExpr" ):
                listener.exitChordExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChordExpr" ):
                return visitor.visitChordExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(musParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class StaveExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def STAVE(self):
            return self.getToken(musParser.STAVE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStaveExpr" ):
                listener.enterStaveExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStaveExpr" ):
                listener.exitStaveExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStaveExpr" ):
                return visitor.visitStaveExpr(self)
            else:
                return visitor.visitChildren(self)


    class ByeExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def BYE(self):
            return self.getToken(musParser.BYE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterByeExpr" ):
                listener.enterByeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitByeExpr" ):
                listener.exitByeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitByeExpr" ):
                return visitor.visitByeExpr(self)
            else:
                return visitor.visitChildren(self)


    class HelloExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def HELLO(self):
            return self.getToken(musParser.HELLO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHelloExpr" ):
                listener.enterHelloExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHelloExpr" ):
                listener.exitHelloExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHelloExpr" ):
                return visitor.visitHelloExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotaExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def NOTA(self):
            return self.getToken(musParser.NOTA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotaExpr" ):
                listener.enterNotaExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotaExpr" ):
                listener.exitNotaExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotaExpr" ):
                return visitor.visitNotaExpr(self)
            else:
                return visitor.visitChildren(self)


    class SongsExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def SONGS(self):
            return self.getToken(musParser.SONGS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSongsExpr" ):
                listener.enterSongsExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSongsExpr" ):
                listener.exitSongsExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSongsExpr" ):
                return visitor.visitSongsExpr(self)
            else:
                return visitor.visitChildren(self)


    class ListExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def LIST(self):
            return self.getToken(musParser.LIST, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListExpr" ):
                listener.enterListExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListExpr" ):
                listener.exitListExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListExpr" ):
                return visitor.visitListExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(musParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class InfixExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(musParser.ExprContext)
            else:
                return self.getTypedRuleContext(musParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfixExpr" ):
                listener.enterInfixExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfixExpr" ):
                listener.exitInfixExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfixExpr" ):
                return visitor.visitInfixExpr(self)
            else:
                return visitor.visitChildren(self)


    class RealExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def REAL(self):
            return self.getToken(musParser.REAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRealExpr" ):
                listener.enterRealExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRealExpr" ):
                listener.exitRealExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRealExpr" ):
                return visitor.visitRealExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = musParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [musParser.T__2]:
                localctx = musParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 3
                self.match(musParser.T__2)
                self.state = 4
                self.expr(0)
                self.state = 5
                self.match(musParser.T__3)
                pass
            elif token in [musParser.INT]:
                localctx = musParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 7
                localctx.atom = self.match(musParser.INT)
                pass
            elif token in [musParser.REAL]:
                localctx = musParser.RealExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 8
                localctx.atom = self.match(musParser.REAL)
                pass
            elif token in [musParser.NOTA]:
                localctx = musParser.NotaExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                localctx.atom = self.match(musParser.NOTA)
                pass
            elif token in [musParser.CHORD]:
                localctx = musParser.ChordExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 10
                localctx.atom = self.match(musParser.CHORD)
                pass
            elif token in [musParser.STAVE]:
                localctx = musParser.StaveExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                localctx.atom = self.match(musParser.STAVE)
                pass
            elif token in [musParser.SONGS]:
                localctx = musParser.SongsExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 12
                localctx.atom = self.match(musParser.SONGS)
                pass
            elif token in [musParser.LIST]:
                localctx = musParser.ListExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                localctx.atom = self.match(musParser.LIST)
                pass
            elif token in [musParser.HELLO]:
                localctx = musParser.HelloExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 14
                localctx.atom = self.match(musParser.HELLO)
                pass
            elif token in [musParser.BYE]:
                localctx = musParser.ByeExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 15
                localctx.atom = self.match(musParser.BYE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 23
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = musParser.InfixExprContext(self, musParser.ExprContext(self, _parentctx, _parentState))
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 18
                    if not self.precpred(self._ctx, 11):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                    self.state = 19
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==musParser.T__0 or _la==musParser.T__1):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 20
                    localctx.right = self.expr(12) 
                self.state = 25
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         




