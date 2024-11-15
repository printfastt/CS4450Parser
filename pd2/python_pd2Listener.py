# Generated from pd2/python_pd2.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .python_pd2Parser import python_pd2Parser
else:
    from python_pd2Parser import python_pd2Parser

# This class defines a complete listener for a parse tree produced by python_pd2Parser.
class python_pd2Listener(ParseTreeListener):

    # Enter a parse tree produced by python_pd2Parser#program.
    def enterProgram(self, ctx:python_pd2Parser.ProgramContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#program.
    def exitProgram(self, ctx:python_pd2Parser.ProgramContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#statement.
    def enterStatement(self, ctx:python_pd2Parser.StatementContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#statement.
    def exitStatement(self, ctx:python_pd2Parser.StatementContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#simpleAssign.
    def enterSimpleAssign(self, ctx:python_pd2Parser.SimpleAssignContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#simpleAssign.
    def exitSimpleAssign(self, ctx:python_pd2Parser.SimpleAssignContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#addAssign.
    def enterAddAssign(self, ctx:python_pd2Parser.AddAssignContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#addAssign.
    def exitAddAssign(self, ctx:python_pd2Parser.AddAssignContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#subAssign.
    def enterSubAssign(self, ctx:python_pd2Parser.SubAssignContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#subAssign.
    def exitSubAssign(self, ctx:python_pd2Parser.SubAssignContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#mulAssign.
    def enterMulAssign(self, ctx:python_pd2Parser.MulAssignContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#mulAssign.
    def exitMulAssign(self, ctx:python_pd2Parser.MulAssignContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#divAssign.
    def enterDivAssign(self, ctx:python_pd2Parser.DivAssignContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#divAssign.
    def exitDivAssign(self, ctx:python_pd2Parser.DivAssignContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#if_block.
    def enterIf_block(self, ctx:python_pd2Parser.If_blockContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#if_block.
    def exitIf_block(self, ctx:python_pd2Parser.If_blockContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#block.
    def enterBlock(self, ctx:python_pd2Parser.BlockContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#block.
    def exitBlock(self, ctx:python_pd2Parser.BlockContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#orCondition.
    def enterOrCondition(self, ctx:python_pd2Parser.OrConditionContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#orCondition.
    def exitOrCondition(self, ctx:python_pd2Parser.OrConditionContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#andCondition.
    def enterAndCondition(self, ctx:python_pd2Parser.AndConditionContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#andCondition.
    def exitAndCondition(self, ctx:python_pd2Parser.AndConditionContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#notCondition.
    def enterNotCondition(self, ctx:python_pd2Parser.NotConditionContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#notCondition.
    def exitNotCondition(self, ctx:python_pd2Parser.NotConditionContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#comparisonCondition.
    def enterComparisonCondition(self, ctx:python_pd2Parser.ComparisonConditionContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#comparisonCondition.
    def exitComparisonCondition(self, ctx:python_pd2Parser.ComparisonConditionContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#number.
    def enterNumber(self, ctx:python_pd2Parser.NumberContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#number.
    def exitNumber(self, ctx:python_pd2Parser.NumberContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#parens.
    def enterParens(self, ctx:python_pd2Parser.ParensContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#parens.
    def exitParens(self, ctx:python_pd2Parser.ParensContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#moduloExpr.
    def enterModuloExpr(self, ctx:python_pd2Parser.ModuloExprContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#moduloExpr.
    def exitModuloExpr(self, ctx:python_pd2Parser.ModuloExprContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#string.
    def enterString(self, ctx:python_pd2Parser.StringContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#string.
    def exitString(self, ctx:python_pd2Parser.StringContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#additionExpr.
    def enterAdditionExpr(self, ctx:python_pd2Parser.AdditionExprContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#additionExpr.
    def exitAdditionExpr(self, ctx:python_pd2Parser.AdditionExprContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#variable.
    def enterVariable(self, ctx:python_pd2Parser.VariableContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#variable.
    def exitVariable(self, ctx:python_pd2Parser.VariableContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#multiplicationExpr.
    def enterMultiplicationExpr(self, ctx:python_pd2Parser.MultiplicationExprContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#multiplicationExpr.
    def exitMultiplicationExpr(self, ctx:python_pd2Parser.MultiplicationExprContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#listExpr.
    def enterListExpr(self, ctx:python_pd2Parser.ListExprContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#listExpr.
    def exitListExpr(self, ctx:python_pd2Parser.ListExprContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#subtractionExpr.
    def enterSubtractionExpr(self, ctx:python_pd2Parser.SubtractionExprContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#subtractionExpr.
    def exitSubtractionExpr(self, ctx:python_pd2Parser.SubtractionExprContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#divisionExpr.
    def enterDivisionExpr(self, ctx:python_pd2Parser.DivisionExprContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#divisionExpr.
    def exitDivisionExpr(self, ctx:python_pd2Parser.DivisionExprContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#comparison.
    def enterComparison(self, ctx:python_pd2Parser.ComparisonContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#comparison.
    def exitComparison(self, ctx:python_pd2Parser.ComparisonContext):
        pass


    # Enter a parse tree produced by python_pd2Parser#list.
    def enterList(self, ctx:python_pd2Parser.ListContext):
        pass

    # Exit a parse tree produced by python_pd2Parser#list.
    def exitList(self, ctx:python_pd2Parser.ListContext):
        pass



del python_pd2Parser