import ply.yacc as yacc
import scanner
import numpy

tokens = scanner.tokens

precedence = (
    # to fill ...
    ("nonassoc", 'LESSER', 'GREATER', 'LESSER_EQUALS', 'GREATER_EQUALS', 'NOT_EQUALS', 'EQUALS'),
    ("right", 'ASSIGN', 'ADD_ASSIGN', 'SUBSTRACT_ASSIGN', 'MULTIPLY_ASSIGN', 'DIVIDE_ASSIGN'),
    ("left", 'PLUS', 'MINUS', 'MPLUS', 'MMINUS'),
    ("left", 'TIMES', 'DIVIDE', 'MTIMES', 'MDIVIDE'),
    ("noassoc", 'ZEROS', 'ONES', 'EYE'),
    ("noassoc", 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET'),
    ("right", 'UMINUS'),
    ("nonassoc", 'TRANSPOSITION')
    # to fill ...
)

symbols_dict = {}

def p_program(p):
    """PROGRAM : EXPRESSION"""
    print("RESULT =", p[1])


def p_expression_number(p):
    """EXPRESSION : INT
                  | FLOAT"""
    p[0] = p[1]


def p_expression_id(p):
    """EXPRESSION : ID"""
    p[0] = p[1]
    value = symbols_dict.get(p[1])
    if value:
        p[0] = value
    else:
        p[0] = 0
        print("'%s' not used\n" % p[1])


def p_expression_sum(p):
    """EXPRESSION : EXPRESSION PLUS EXPRESSION
                  | EXPRESSION MINUS EXPRESSION
                  | EXPRESSION MPLUS EXPRESSION
                  | EXPRESSION MMINUS EXPRESSION"""
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '.+':
        p[0] = p[1] - p[3]
    elif p[2] == '.-':
        p[0] = p[1] - p[3]


def p_expression_mul(p):
    """EXPRESSION : EXPRESSION TIMES EXPRESSION
                  | EXPRESSION DIVIDE EXPRESSION
                  | EXPRESSION MTIMES EXPRESSION
                  | EXPRESSION MDIVIDE EXPRESSION"""
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == '.*':
        pass
    elif p[2] == './':
        pass


def p_expression_assignment(p):
    """EXPRESSION : EXPRESSION ASSIGN EXPRESSION
                  | EXPRESSION ADD_ASSIGN EXPRESSION
                  | EXPRESSION SUBSTRACT_ASSIGN EXPRESSION
                  | EXPRESSION MULTIPLY_ASSIGN EXPRESSION
                  | EXPRESSION DIVIDE_ASSIGN EXPRESSION"""
    if p[2] == '=':
        p[0] = p[3]
    elif p[2] == '+=':
        p[0] += p[3]
    elif p[2] == '-=':
        p[0] -= p[3]
    elif p[2] == '*=':
        p[0] *= p[3]
    elif p[2] == '/=':
        p[0] /= p[3]

    symbols_dict[p[1]] = p[0]


def p_expression_relational(p):
    """ EXPRESSION : LESSER
                   | GREATER
                   | LESSER_EQUALS
                   | GREATER_EQUALS
                   | NOT_EQUALS
                   | EQUALS"""
    p[0] = p[1]


def p_unary_negation(p):
    """EXPRESSION : MINUS EXPRESSION %prec UMINUS"""
    p[0] = -p[2]

def p_matrix_transpose(p):
    """ EXPRESSION : EXPRESSION TRANSPOSITION """
    p[0] = p[2].transpose(1, 0)

def p_error(p):
    if p:
        print("Syntax error at line %d: LexToken(%s, '%s')" % (p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")

def p_expression_function(p):
    """EXPRESSION : ZEROS EXPRESSION
                  | ONES EXPRESSION
                  | EYE EXPRESSION"""
    if p[1] == 'zeros':
        pass
        # p[0] = zeros(p[2])
    elif p[1] == 'ones':
        pass
        # p[0] = ones(p[2])
    elif p[1] == 'eye':
        pass
        # p[0] = eye(p[2])


def p_expression_brackets(p):
    """EXPRESSION : LBRACKET EXPRESSION RBRACKET
                  | EXPRESSION"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


# def p_instructions_1(p):
#     """instructions : instructions instruction """
#
#
# def p_instructions_2(p):
#     """instructions : instruction """


# to finish the grammar
# ....


parser = yacc.yacc()
