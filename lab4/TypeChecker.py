#!/usr/bin/python
from _ast import AST


class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node): # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)

    # simpler version of generic_visit, not so general
    #def generic_visit(self, node):
    #    for child in node.children:
    #        self.visit(child)


class TypeChecker(NodeVisitor):

    def visit_BinaryExpression(self, node):
                                          # alternative usage, requires definition of accept method in class Node
        type1 = self.visit(node.left)     # type1 = node.left.accept(self) 
        type2 = self.visit(node.right)    # type2 = node.right.accept(self)
        op = node.op

    def visit_UnaryExpression(self, node):
        pass

    def visit_Negation(self, node):
        pass

    def visit_Transposition(self, node):
        pass

    def visit_Assignment(self, node):
        pass

    def visit_Function(self, node):
        pass

    def visit_Variable(self, node):
        pass

    def visit_If(self, node):
        pass

    def visit_While(self, node):
        pass

    def visit_Range(self, node):
        pass

    def visit_For(self, node):
        pass

    def visit_Break(self, node):
        pass

    def visit_Continue(self, node):
        pass

    def visit_Return(self, node):
        pass

    def visit_Print(self, node):
        pass

    def visit_VariableAttribute(self, node):
        pass

    def visit_Error(self, node):
        pass

    def visit_CodeBlock(self, node):
        pass

    def visit_Program(self, node):
        pass

    def visit_Instruction(self, node):
        pass

    def visit_Matrix(self, node):
        pass

    def visit_Rows(self, node):
        pass

    def visit_Sequence(self, node):
        pass