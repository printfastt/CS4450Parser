# Generated from python_pd1.g4 by ANTLR 4.13.2
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
        4,1,19,77,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,3,2,33,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,
        3,44,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,5,3,61,8,3,10,3,12,3,64,9,3,1,4,1,4,1,4,1,4,5,4,70,8,4,10,4,
        12,4,73,9,4,1,4,1,4,1,4,0,1,6,5,0,2,4,6,8,0,0,86,0,11,1,0,0,0,2,
        15,1,0,0,0,4,32,1,0,0,0,6,43,1,0,0,0,8,65,1,0,0,0,10,12,3,2,1,0,
        11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,1,1,0,
        0,0,15,16,3,4,2,0,16,3,1,0,0,0,17,18,5,15,0,0,18,19,5,5,0,0,19,33,
        3,6,3,0,20,21,5,15,0,0,21,22,5,6,0,0,22,33,3,6,3,0,23,24,5,15,0,
        0,24,25,5,7,0,0,25,33,3,6,3,0,26,27,5,15,0,0,27,28,5,8,0,0,28,33,
        3,6,3,0,29,30,5,15,0,0,30,31,5,9,0,0,31,33,3,6,3,0,32,17,1,0,0,0,
        32,20,1,0,0,0,32,23,1,0,0,0,32,26,1,0,0,0,32,29,1,0,0,0,33,5,1,0,
        0,0,34,35,6,3,-1,0,35,36,5,1,0,0,36,37,3,6,3,0,37,38,5,2,0,0,38,
        44,1,0,0,0,39,44,3,8,4,0,40,44,5,17,0,0,41,44,5,16,0,0,42,44,5,15,
        0,0,43,34,1,0,0,0,43,39,1,0,0,0,43,40,1,0,0,0,43,41,1,0,0,0,43,42,
        1,0,0,0,44,62,1,0,0,0,45,46,10,10,0,0,46,47,5,10,0,0,47,61,3,6,3,
        11,48,49,10,9,0,0,49,50,5,11,0,0,50,61,3,6,3,10,51,52,10,8,0,0,52,
        53,5,12,0,0,53,61,3,6,3,9,54,55,10,7,0,0,55,56,5,13,0,0,56,61,3,
        6,3,8,57,58,10,6,0,0,58,59,5,14,0,0,59,61,3,6,3,7,60,45,1,0,0,0,
        60,48,1,0,0,0,60,51,1,0,0,0,60,54,1,0,0,0,60,57,1,0,0,0,61,64,1,
        0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,7,1,0,0,0,64,62,1,0,0,0,65,
        66,5,3,0,0,66,71,3,6,3,0,67,68,5,18,0,0,68,70,3,6,3,0,69,67,1,0,
        0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,71,
        1,0,0,0,74,75,5,4,0,0,75,9,1,0,0,0,6,13,32,43,60,62,71
    ]

class python_pd1Parser ( Parser ):

    grammarFileName = "python_pd1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'['", "']'", "'='", "'+='", 
                     "'-='", "'*='", "'/='", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "<INVALID>", "<INVALID>", "<INVALID>", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
                      "MUL_ASSIGN", "DIV_ASSIGN", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "VARIABLE", "NUMBER", "STRING", "COMMA", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_expression = 3
    RULE_list = 4

    ruleNames =  [ "program", "statement", "assignment", "expression", "list" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    ASSIGN=5
    ADD_ASSIGN=6
    SUB_ASSIGN=7
    MUL_ASSIGN=8
    DIV_ASSIGN=9
    ADD=10
    SUB=11
    MUL=12
    DIV=13
    MOD=14
    VARIABLE=15
    NUMBER=16
    STRING=17
    COMMA=18
    WS=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_pd1Parser.StatementContext)
            else:
                return self.getTypedRuleContext(python_pd1Parser.StatementContext,i)


        def getRuleIndex(self):
            return python_pd1Parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = python_pd1Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.statement()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==15):
                    break

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

        def assignment(self):
            return self.getTypedRuleContext(python_pd1Parser.AssignmentContext,0)


        def getRuleIndex(self):
            return python_pd1Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = python_pd1Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.assignment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return python_pd1Parser.RULE_assignment

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SubAssignContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.AssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(python_pd1Parser.VARIABLE, 0)
        def SUB_ASSIGN(self):
            return self.getToken(python_pd1Parser.SUB_ASSIGN, 0)
        def expression(self):
            return self.getTypedRuleContext(python_pd1Parser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubAssign" ):
                listener.enterSubAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubAssign" ):
                listener.exitSubAssign(self)


    class MulAssignContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.AssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(python_pd1Parser.VARIABLE, 0)
        def MUL_ASSIGN(self):
            return self.getToken(python_pd1Parser.MUL_ASSIGN, 0)
        def expression(self):
            return self.getTypedRuleContext(python_pd1Parser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulAssign" ):
                listener.enterMulAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulAssign" ):
                listener.exitMulAssign(self)


    class AddAssignContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.AssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(python_pd1Parser.VARIABLE, 0)
        def ADD_ASSIGN(self):
            return self.getToken(python_pd1Parser.ADD_ASSIGN, 0)
        def expression(self):
            return self.getTypedRuleContext(python_pd1Parser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddAssign" ):
                listener.enterAddAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddAssign" ):
                listener.exitAddAssign(self)


    class SimpleAssignContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.AssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(python_pd1Parser.VARIABLE, 0)
        def ASSIGN(self):
            return self.getToken(python_pd1Parser.ASSIGN, 0)
        def expression(self):
            return self.getTypedRuleContext(python_pd1Parser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleAssign" ):
                listener.enterSimpleAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleAssign" ):
                listener.exitSimpleAssign(self)


    class DivAssignContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.AssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(python_pd1Parser.VARIABLE, 0)
        def DIV_ASSIGN(self):
            return self.getToken(python_pd1Parser.DIV_ASSIGN, 0)
        def expression(self):
            return self.getTypedRuleContext(python_pd1Parser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivAssign" ):
                listener.enterDivAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivAssign" ):
                listener.exitDivAssign(self)



    def assignment(self):

        localctx = python_pd1Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = python_pd1Parser.SimpleAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(python_pd1Parser.VARIABLE)
                self.state = 18
                self.match(python_pd1Parser.ASSIGN)
                self.state = 19
                self.expression(0)
                pass

            elif la_ == 2:
                localctx = python_pd1Parser.AddAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.match(python_pd1Parser.VARIABLE)
                self.state = 21
                self.match(python_pd1Parser.ADD_ASSIGN)
                self.state = 22
                self.expression(0)
                pass

            elif la_ == 3:
                localctx = python_pd1Parser.SubAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.match(python_pd1Parser.VARIABLE)
                self.state = 24
                self.match(python_pd1Parser.SUB_ASSIGN)
                self.state = 25
                self.expression(0)
                pass

            elif la_ == 4:
                localctx = python_pd1Parser.MulAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.match(python_pd1Parser.VARIABLE)
                self.state = 27
                self.match(python_pd1Parser.MUL_ASSIGN)
                self.state = 28
                self.expression(0)
                pass

            elif la_ == 5:
                localctx = python_pd1Parser.DivAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 29
                self.match(python_pd1Parser.VARIABLE)
                self.state = 30
                self.match(python_pd1Parser.DIV_ASSIGN)
                self.state = 31
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return python_pd1Parser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumberContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(python_pd1Parser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)


    class ParensContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(python_pd1Parser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class ModuloExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_pd1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(python_pd1Parser.ExpressionContext,i)

        def MOD(self):
            return self.getToken(python_pd1Parser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModuloExpr" ):
                listener.enterModuloExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModuloExpr" ):
                listener.exitModuloExpr(self)


    class StringContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(python_pd1Parser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)


    class AdditionExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_pd1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(python_pd1Parser.ExpressionContext,i)

        def ADD(self):
            return self.getToken(python_pd1Parser.ADD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditionExpr" ):
                listener.enterAdditionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditionExpr" ):
                listener.exitAdditionExpr(self)


    class VariableContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(python_pd1Parser.VARIABLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)


    class MultiplicationExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_pd1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(python_pd1Parser.ExpressionContext,i)

        def MUL(self):
            return self.getToken(python_pd1Parser.MUL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicationExpr" ):
                listener.enterMultiplicationExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicationExpr" ):
                listener.exitMultiplicationExpr(self)


    class ListExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def list_(self):
            return self.getTypedRuleContext(python_pd1Parser.ListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListExpr" ):
                listener.enterListExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListExpr" ):
                listener.exitListExpr(self)


    class SubtractionExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_pd1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(python_pd1Parser.ExpressionContext,i)

        def SUB(self):
            return self.getToken(python_pd1Parser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubtractionExpr" ):
                listener.enterSubtractionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubtractionExpr" ):
                listener.exitSubtractionExpr(self)


    class DivisionExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_pd1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(python_pd1Parser.ExpressionContext,i)

        def DIV(self):
            return self.getToken(python_pd1Parser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivisionExpr" ):
                listener.enterDivisionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivisionExpr" ):
                listener.exitDivisionExpr(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = python_pd1Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = python_pd1Parser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 35
                self.match(python_pd1Parser.T__0)
                self.state = 36
                self.expression(0)
                self.state = 37
                self.match(python_pd1Parser.T__1)
                pass
            elif token in [3]:
                localctx = python_pd1Parser.ListExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 39
                self.list_()
                pass
            elif token in [17]:
                localctx = python_pd1Parser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 40
                self.match(python_pd1Parser.STRING)
                pass
            elif token in [16]:
                localctx = python_pd1Parser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 41
                self.match(python_pd1Parser.NUMBER)
                pass
            elif token in [15]:
                localctx = python_pd1Parser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 42
                self.match(python_pd1Parser.VARIABLE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 62
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 60
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = python_pd1Parser.AdditionExprContext(self, python_pd1Parser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 45
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 46
                        self.match(python_pd1Parser.ADD)
                        self.state = 47
                        self.expression(11)
                        pass

                    elif la_ == 2:
                        localctx = python_pd1Parser.SubtractionExprContext(self, python_pd1Parser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 48
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 49
                        self.match(python_pd1Parser.SUB)
                        self.state = 50
                        self.expression(10)
                        pass

                    elif la_ == 3:
                        localctx = python_pd1Parser.MultiplicationExprContext(self, python_pd1Parser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 51
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 52
                        self.match(python_pd1Parser.MUL)
                        self.state = 53
                        self.expression(9)
                        pass

                    elif la_ == 4:
                        localctx = python_pd1Parser.DivisionExprContext(self, python_pd1Parser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 54
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 55
                        self.match(python_pd1Parser.DIV)
                        self.state = 56
                        self.expression(8)
                        pass

                    elif la_ == 5:
                        localctx = python_pd1Parser.ModuloExprContext(self, python_pd1Parser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 57
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 58
                        self.match(python_pd1Parser.MOD)
                        self.state = 59
                        self.expression(7)
                        pass

             
                self.state = 64
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_pd1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(python_pd1Parser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(python_pd1Parser.COMMA)
            else:
                return self.getToken(python_pd1Parser.COMMA, i)

        def getRuleIndex(self):
            return python_pd1Parser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)




    def list_(self):

        localctx = python_pd1Parser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(python_pd1Parser.T__2)
            self.state = 66
            self.expression(0)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 67
                self.match(python_pd1Parser.COMMA)
                self.state = 68
                self.expression(0)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.match(python_pd1Parser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         




