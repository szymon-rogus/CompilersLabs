#!/usr/bin/python

import ply.yacc as yacc
import Types as types
from scanner import lexer, tokens


class Parser:
    tokens = tokens

    def __init__(self):
        self.parser = yacc.yacc(module=self)
        self.lexer = lexer
        self.error = False

    def parse(self, txt):
        return self.parser.parse(txt, lexer=self.lexer)

    precedence = (
        ('nonassoc', 'IF'),
        ('nonassoc', 'LESSER', 'GREATER', 'EQUALS', 'NOT_EQUALS', 'LESSER_EQUALS', 'GREATER_EQUALS', 'ELSE'),
        ('left', 'PLUS', 'MINUS', 'MPLUS', 'MMINUS'),
        ('left', 'TIMES', 'DIVIDE', 'MTIMES', 'MDIVIDE'),
        ('left', 'UMINUS'),
        ('nonassoc', 'TRANSPOSITION'),
    )

    def p_program(self, p):
        """PROGRAM : CODE_BLOCK"""
        p[0] = types.Program(p[1])

    def p_code_block_curly(self, p):
        """
        CODE_BLOCK : CODE_BLOCK LBRACE CODE_BLOCK RBRACE
              | LBRACE CODE_BLOCK RBRACE
        """
        if len(p) == 5:
            p[1].instructions.append(p[3])
            p[0] = p[1]
        else:
            p[0] = types.CodeBlock(p[2])

    def p_code_block(self, p):
        """
        CODE_BLOCK : CODE_BLOCK instruction
              | instruction
        """
        if len(p) == 3:
            p[1].instructions.append(p[2])
            p[0] = p[1]
        else:
            p[0] = types.CodeBlock(p[1])

    def p_instruction(self, p):
        """
        instruction : statement SEMICOLON
                    | if_statement
                    | while_statement
                    | for_statement
        """
        p[0] = p[1]

    def p_statement(self, p):
        """
        statement : assignment
                  | keyword
        """
        p[0] = types.Instruction(p[1])

    def p_assignment(self, p):
        """
        assignment : variable assignment_operator expression
        """
        p[0] = types.Assignment(p[1], p[2], p[3])

    def p_variable(self, p):
        """
        variable : ID
                 | variable_attribute
        """
        p[0] = types.Variable(p[1])

    def p_variable_attribute(self, p):
        """
        variable_attribute : ID LSQUARE sequence RSQUARE
        """
        p[0] = types.VariableAttribute(p[1], p[3])

    def p_sequence(self, p):
        """
        sequence : sequence COMMA expression
                 | expression
        """
        if len(p) == 4:
            p[1].expressions.append(p[3])
            p[0] = p[1]
        else:
            p[0] = types.Sequence(p[1])

    def p_value(self, p):
        """
        value : FLOAT
              | INT
              | STRING
              | matrix
              | variable_attribute
        """

        p[0] = types.Value(p[1])

    def p_matrix(self, p):
        """
        matrix : LSQUARE rows RSQUARE
        """
        p[0] = types.Matrix(p[2])

    def p_rows(self, p):
        """
        rows : rows SEMICOLON sequence
             | sequence
        """
        if len(p) == 2:
            p[0] = types.Rows(p[1])
        else:
            p[1].row_list.append(p[3])
            p[0] = p[1]

    def p_expression_value(self, p):
        """
        expression : value
        """
        p[0] = p[1]

    def p_expression_id(self, p):
        """expression : ID"""
        p[0] = types.Variable(p[1])

    def p_expression_negation(self, p):
        """
        expression : MINUS expression %prec UMINUS
        """
        p[0] = types.Negation(p[2])

    def p_id_transposition(self, p):
        """
        expression : ID TRANSPOSITION
        """
        p[0] = types.Transposition(types.Variable(p[1]))

    def p_expression_transposition(self, p):
        """
        expression : LBRACKET expression RBRACKET TRANSPOSITION
        """
        p[0] = types.Transposition(p[2])

    def p_expression_bracket(self, p):
        """
        expression : LBRACKET expression RBRACKET
        """
        p[0] = p[2]

    def p_bin_expressions(self, p):
        """
        expression : expression PLUS expression
                   | expression MINUS expression
                   | expression TIMES expression
                   | expression DIVIDE expression
                   | expression MPLUS expression
                   | expression MMINUS expression
                   | expression MTIMES expression
                   | expression MDIVIDE expression
        """
        p[0] = types.BinaryExpression(p[1], p[2], p[3])

    def p_expression_fun(self, p):
        """
        expression : function LBRACKET expression RBRACKET
                   | function LBRACKET sequence RBRACKET
        """
        p[0] = types.Function(p[1], p[3])

    def p_keyword_print(self, p):
        """
        keyword : PRINT sequence
        """
        p[0] = types.Print(p[2])

    def p_keyword_break(self, p):
        """
        keyword : BREAK
        """
        p[0] = types.Break()

    def p_keyword_continue(self, p):
        """
        keyword : CONTINUE
        """
        p[0] = types.Continue()

    def p_keyword_return(self, p):
        """
        keyword : RETURN expression
        """
        p[0] = types.Return(p[2])

    def p_relation(self, p):
        """relation : expression logic_operator expression"""
        p[0] = types.BinaryExpression(p[1], p[2], p[3])

    def p_body(self, p):
        """body : LBRACE CODE_BLOCK RBRACE
                | instruction"""
        if len(p) == 2:
            p[0] = types.Instruction(p[1])
        else:
            p[0] = types.Instruction(p[2])

    def p_if_statement(self, p):
        """
        if_statement : IF LBRACKET relation RBRACKET body %prec IF
        """
        p[0] = types.If(p[3], p[5])

    def p_if_else_statement(self, p):
        """
        if_statement : IF LBRACKET relation RBRACKET body ELSE body
        """
        p[0] = types.If(p[3], p[5], p[7])

    def p_while_statement(self, p):
        """while_statement : WHILE LBRACKET relation RBRACKET body"""
        p[0] = types.While(p[3], p[5])

    def p_for_statement(self, p):
        """for_statement : FOR ID ASSIGN range body"""
        p[0] = types.For(p[2], p[4], p[5])

    def p_range(self, p):
        """range : expression RANGE expression RANGE expression
                 | expression RANGE expression"""
        if len(p) == 4:
            p[0] = types.Range(p[1], p[3])
        else:
            p[0] = types.Range(p[1], p[3], p[5])

    def p_assignment_operator(self, p):
        """
        assignment_operator : ASSIGN
                            | ADD_ASSIGN
                            | SUBSTRACT_ASSIGN
                            | MULTIPLY_ASSIGN
                            | DIVIDE_ASSIGN
        """
        p[0] = p[1]

    def p_comparision_operator(self, p):
        """
        logic_operator : LESSER
                       | GREATER
                       | EQUALS
                       | NOT_EQUALS
                       | LESSER_EQUALS
                       | GREATER_EQUALS
        """
        p[0] = p[1]

    def p_function(self, p):
        """
        function : EYE
                 | ZEROS
                 | ONES
        """
        p[0] = p[1]

    def p_error(self, p):
        self.error = True
        err_sign = "***********************"
        if p:
            line = p.lexer.lineno if hasattr(p.lexer, 'lineno') else p.lexer.lexer.lineno
            value = p.value
        else:
            line = 'last'
            value = ''
        print('{}\nERROR\nIllegal symbol {} at line {}\n'.format(err_sign, value, line))
