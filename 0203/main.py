import sys
from antlr4 import *
from dist.musLexer import musLexer
from dist.musParser import musParser
from dist.musVisitor import musVisitor

from parsers.Nota import Nota
from parsers.Chord import Chord
from parsers.Stave import Stave
from parsers.Songs import Songs
from parsers.List import List


def get_username():
    from pwd import getpwuid
    from os import getuid
    return getpwuid(getuid())[ 0 ]


class MyVisitor(musVisitor):
    def visitNumberExpr(self, ctx):
        value = ctx.getText()
        return int(value)
    
    def visitRealExpr(self, ctx):
        value = ctx.getText()
        return float(value)
    
    def visitNotaExpr(self, ctx):
        value = ctx.getText()
        try:
            return Nota(value)
        except Exception as e:
            return str(e)
    
    def visitChordExpr(self, ctx):
        value = ctx.getText()
        return Chord(value)
    
    def visitStaveExpr(self, ctx):
        value = ctx.getText()
        return Stave(value)
    
    def visitSongsExpr(self, ctx):
        value = ctx.getText()
        return Songs(value)
    
    def visitListExpr(self, ctx):
        value = ctx.getText()
        return List(value)

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitInfixExpr(self, ctx):
        l, r = None, None
        try:
            l = self.visit(ctx.left)
            r = self.visit(ctx.right)
        except Exception as e:
            return str(e)

        if not (isinstance(l, int) 
                or isinstance(l, float) 
                or isinstance(l, Nota)
                or isinstance(l, Chord)
                or isinstance(l, Stave)):
            return f"Left operand : {type(l)} can't support operations"
        
        if not (isinstance(r, int) 
                or isinstance(r, float)
                or isinstance(r, Nota)
                or isinstance(r, Chord)
                or isinstance(r, Stave)):
            return f"Right operand : {type(r)} can't support operations"

        op = ctx.op.text
        if op == '/' and (l is Nota or r is Nota):
            return f"Nota cant't handle with division"
        
        operation =  {
        '+': lambda: l + r,
        '-': lambda: l - r,
        }

        return operation.get(op, lambda: None)()

    def visitByeExpr(self, ctx):
        print(f"goodbye {get_username()}")
        sys.exit(0)

    def visitHelloExpr(self, ctx):
        return (f"{ctx.getText()} {get_username()}")


def main():
    while True:
        data =  InputStream(input(">>> "))
        lexer = musLexer(data)
        stream = CommonTokenStream(lexer)
        parser = musParser(stream)
        tree = parser.expr()
        visitor = MyVisitor()
        output = visitor.visit(tree)
        print(output)


if __name__ == "__main__":
    exit(main())
